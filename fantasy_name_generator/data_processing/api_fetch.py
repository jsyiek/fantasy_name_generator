import logging
import os
import pickle
import requests

from typing import Any, Dict, List

from fantasy_name_generator import REPOSITORY_PATH

__CARDS_CACHE_PATH = os.path.join(REPOSITORY_PATH, "fantasy_name_generator", ".cards_data.dat")
WEBSITE_URL = "https://api.magicthegathering.io/v1/cards"

this_logger = logging.getLogger()


def get_cards(**get_arguments) -> List[Dict]:
    """
    Makes a GET request to the Magic: the Gathering cards API. Returns a list of dictionary of cards.
    See the API website for information on the return format.
    Parameters:
        **get_arguments (Any): Any get arguments you want to pass.
    Returns:
        List[Dict]: List of dictionaries (which represent individual cards). This will be a maximum of 100 cards
                    due to API limitations.
    """
    return requests.get(WEBSITE_URL, get_arguments).json()["cards"]


def download_dataset(refresh_cache=False) -> List[Dict[str, Any]]:
    """
    Downloads all MTG cards in existence, caching the results to avoid having to perform the lookup multiple times
    over.

    Parameters:
        refresh_cache (bool): Whether or not to flush the cache (i.e. force it to redownload all cards). Defaults to
                              False

    Returns:
        List[Dict[str, Any]]: A list of cards, represented as dictionaries. See the documentation on
                              https://magicthegathering.io for information.
    """
    if refresh_cache or not os.path.exists(__CARDS_CACHE_PATH):
        this_logger.warning("Reloading cached data! Either this was requested or the cache could not be found.")
        cards = []
        next_cards = get_cards(page=0)
        i = 1
        while len(next_cards) == 100:
            this_logger.info(f"Calling API, page: {i}")
            next_cards = get_cards(page=i)
            cards.extend(next_cards)
            i += 1

        this_logger.info("API calls complete. Caching...")

        with open(__CARDS_CACHE_PATH, "wb+") as F:
            pickle.dump(cards, F)

        this_logger.info("Caching succeeded.")

    else:
        this_logger.info("Loading cached files...")
        with open(__CARDS_CACHE_PATH, "rb") as F:
            cards = pickle.load(F)

    return cards
