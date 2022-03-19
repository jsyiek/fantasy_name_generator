import pprint

import fantasy_name_generator.data_processing.api_fetch as api_fetch
import fantasy_name_generator.data_processing.format_data as format_data
import fantasy_name_generator.markov_chain.training as training
import fantasy_name_generator.markov_chain.generation as generation


if __name__ == "__main__":
    order = 2

    cards = api_fetch.download_dataset()
    formatted = format_data.format_data(cards)
    transitions_probabilities, vocabulary = training.calculate_transition_probabilities(formatted, order)
    print(generation.generate(transitions_probabilities['creature'], vocabulary, order))
