import random

from typing import Any, Dict, Set, Tuple


def select_random(dictionary: Dict[Any, float]) -> Any:
    """
    Selects a random key from the dictionary. The random choice is weighted by the integer
    values that the key corresponds to
    Parameters:
        dictionary (OrderedDict[Any, int]): Dictionary mapping item to its weighting
    Returns:
        Any: Random key from the dictionary weighted by the integer they correspond to
    """
    return random.choices(list(dictionary.keys()), weights=list(dictionary.values()))[0]


def generate(transition_probabilities: Dict[Tuple[str], float],
             vocabulary: Set[Tuple[str]],
             order: int) -> str:
    """
    Generates a random fantasy name for a given set of transition_probabilities, vocabulary, and order

    Parameters:
        transition_probabilities (Dict[Tuple[str], float]): A dictionary of transition probabilities, from state to
                                                            next state, alongside a (perhaps log) probability
        vocabulary (Set[Tuple[str]]): A vocabulary of states
        order (int): Markov order used

    Returns:
          str: A generated fantasy name
    """
    def make_next_probability_dict(current_state):
        """
        Helper function that generates the dictionary for select_random
        """
        next_dict = {}
        for v in vocabulary:
            potential_state = (current_state, v)
            if transition_probabilities.get(potential_state):
                next_dict[v] = transition_probabilities[potential_state]
        return next_dict

    generated_states = [tuple(0 for i in range(order))]
    while generated_states[-1][-1] != 1:
        generated_states.append(
            select_random(
                make_next_probability_dict(generated_states[-1])
            )
        )
    generated_states = generated_states[order:-1]
    fantasy_name = [*generated_states[0]]
    for state in generated_states[1:]:
        fantasy_name.append(state[-1])

    return "".join(fantasy_name)
