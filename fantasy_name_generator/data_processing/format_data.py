from typing import Any, Dict, List

import fantasy_name_generator.data_processing.api_fetch as api_fetch


def format_data(cards: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    """
    Formats a list of cards from the API to be in a format usable by the training module

    Parameters:
        cards (List[Dict[str, Any]]): Cards to format. Taken from the API (see api_fetch.get_cards)

    Returns:
        List[Dict[str, str]]: A list of dictionaries, where each dictionary represents a card. The fields are:
                              'type' -> either 'creature', 'spell', 'enchantment', or 'character'
                              'name' -> the fantasy name to train on
    """
    pass
