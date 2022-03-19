import math

from typing import Any, Dict, List, Set, Tuple, Union

from fantasy_name_generator.data_processing.format_data import CARD_TYPE_TO_TRAINING_TYPE


def safelog(value: Union[int, float]) -> float:
    """
    Performs the log operation on the inputted value, return float("-inf") for values that are 0

    Parameters:
        value (Union[int, float]): Non-negative integer to take log of

    Returns:
        float: Log of the number if > 0, else float("-inf")
    """

    return float("-inf") if value == 0 else math.log(value)


def partition(partitionable: List[Any], size: int) -> List[Tuple[Any]]:
    """
    Partitions a list into a list of adjacent elements, such that each set of `size` consecutive elements are present
    in the array.

    E.g.
    >>> partition(['a','b','c','d'], size=2)
    [('a', 'b'), ('b', 'c'), ('c', 'd')]

    Parameters:
        partitionable (List[Any]): List to partition
        size (int): Size of partitions to make

    Returns:
        List[Tuple[Any]]: Adjacent partitions in the list
    """
    return_list = []
    for i in range(len(partitionable) - size + 1):
        return_list.append(tuple(partitionable[i + j] for j in range(size)))
    return return_list


def calculate_transition_probabilities(training_data: List[Dict[str, str]],
                                       order: int) -> Tuple[Dict[str, Dict[Tuple[str], float]], Set[Tuple[str]]]:
    """
    Calculates the transition probabilities for a given order of Markov chain and a given set of data

    Parameters:
        training_data (List[Dict[str, Dict[str, str]]]): A list of dictionaries. Each dictionary contains
                                         two fields:
                                         'name' -> fantasy name
                                         'type' -> e.g. creature, spell, enchantment, character
        order (int): Order of Markov chain to use

    Returns:
        Tuple[Dict[str, Dict[Tuple[str], float]], Set[Tuple[str]]]:
                                           Transition probabilities between states
                                           (for a given Markov order). Maps the type from the training data to
                                           the transition probabilities for states of that name.
                                           START STATE: 0, END STATE: 1.
                                           And: the observed vocabulary
    """
    transition_probabilities = {
        training_type: {} for training_type in CARD_TYPE_TO_TRAINING_TYPE.values()
    }
    total = 0
    states = set()
    for entry in training_data:

        name = [0] * order + list(entry['name']) + [1] * order
        name = partition(name, order)

        category_dictionary = transition_probabilities[entry['type']]
        states.add(name[0])

        for i in range(1, len(name)):
            category_dictionary[(name[i-1], name[i])] = category_dictionary.get((name[i-1], name[i]), 0) + 1
            states.add(name[i])

        total += len(name) - 1

    return transition_probabilities, states
