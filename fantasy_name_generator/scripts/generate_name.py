import argparse
import logging

import fantasy_name_generator.data_processing.api_fetch as api_fetch
import fantasy_name_generator.data_processing.format_data as format_data
import fantasy_name_generator.markov_chain.training as training
import fantasy_name_generator.markov_chain.generation as generation


this_logger = logging.getLogger()


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-t', '--type', help="The type of name to generate",
                        choices=['creature', 'character', 'spell', 'enchantment', 'artifact', 'land'],
                        default=['creature'], nargs="+")
    parser.add_argument('-n', '--number', help="Number of fantasy names to generate", type=int,
                        default=10)
    parser.add_argument('--markov-order', help="Order of Markov Model to use. Higher orders increase coherence but "
                                               "reduce creativity.",
                        type=int, default=2)
    parser.add_argument('--reset-cache', help="Resets the cached dataset. This may take some time.",
                        action='store_true')

    return parser.parse_args()


def main():

    args = parse_args()

    cards = api_fetch.download_dataset()

    this_logger.info("Formatting dataset...")
    training_data = format_data.format_data(cards)

    this_logger.info("Estimating Markov transition probabilities...")
    transition_probabilities, vocabulary = training.calculate_transition_probabilities(training_data,
                                                                                       args.markov_order)

    this_logger.info("Beginning generation...")
    for t in args.type:
        for n in range(args.number):
            print(generation.generate(transition_probabilities[t], vocabulary, args.markov_order).title())


if __name__ == "__main__":
    main()
