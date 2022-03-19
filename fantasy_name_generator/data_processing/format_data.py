from typing import Any, Dict, List


CARD_TYPE_TO_TRAINING_TYPE = {
    'Creature': 'creature',
    'Instant': 'spell',
    'Sorcery': 'spell',
    'Enchantment': 'enchantment',
    'Legendary Creature': 'character',
    'Artifact': 'artifact',
    'Planeswalker': 'character',
    'Land': 'land'
}


def format_data(cards: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    """
    Formats a list of cards from the API to be in a format usable by the training module

    Parameters:
        cards (List[Dict[str, Any]]): Cards to format. Taken from the API (see api_fetch.get_cards)

    Returns:
        List[Dict[str, str]]: A list of dictionaries, where each dictionary represents a card. The fields are:
                              'type' -> either 'creature', 'spell', 'enchantment', 'character', 'artifact', or 'land'
                              'name' -> the fantasy name to train on
    """
    def format(name: str, card_types: List[str]):
        """
        Helper function standardize formatting the card data
        """
        if '//' in name:
            name = name.split(' // ')
        else:
            name = []
        for n in name:
            for t in card_types:
                card_standardized = {'type': CARD_TYPE_TO_TRAINING_TYPE[t], 'name': n.lower()}
                formatted_data.append(card_standardized)

    formatted_data = []
    for c in cards:
        if 'Legendary' in c.get('supertypes', []) and 'Creature' in c['types']:
            format(c['name'], ['Legendary Creature'])
        else:
            for t in c['types']:
                if CARD_TYPE_TO_TRAINING_TYPE.get(t):
                    format(c['name'], c['types'])
    return formatted_data
