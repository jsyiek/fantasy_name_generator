from typing import Dict, List


def calculate_transition_probabilities(training_data: List[Dict[str, Dict[str, str]]],
                                       order: int) -> Dict[str, Dict[List[str], float]]:
    """
    Calculates the transition probabilities for a given order of Markov chain and a given set of data

    Parameters:
        training_data (List[Dict[str, Dict[str, str]]]): A list of dictionaries. Each dictionary contains
                                         two fields:
                                         'name' -> fantasy name
                                         'type' -> e.g. creature, spell, enchantment, character
        order (int): Order of Markov chain to use

    Returns:
        Dict[str, Dict[List[str], float]]: Transition probabilities between states (for a given Markov order).
                                           Probabilities are in log form. Maps the type from the training data to
                                           the transition probabilities for states of that name.
    """
    pass
