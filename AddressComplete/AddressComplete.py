import urllib.parse
from typing import Tuple

import requests


class AddressComplete:
    """A client module for the Canada Post AddressComplete API."""

    DEFAULT_RETRIEVE_ENDPOINT = (
        "https://ws1.postescanada-canadapost.ca/addresscomplete/"
        "interactive/retrieve/v2.11/json.ws"
        "?provider=AddressComplete&package=Interactive"
        "&service=Retrieve&version=2.11&endpoint=json.ws"
    )
    
    DEFAULT_FIND_ENDPOINT = (
        "http://ws1.postescanada-canadapost.ca/addresscomplete/interactive/find"
        "/v2.10/json3.ws?provider=AddressComplete&package=Interactive&service="
        "Find&version=2.1&endpoint=json3.ws"
        )
    
    def __init__(self, api_key):
        """Initializes an AddressComplete client.
        
        Args:
            api_key (str): Your AddressComplete API key.
        """
        self.api_key = api_key
        

    def find(self, search_term, country="CAN", max_suggestions=10,
             language_preference="en"):
        """Finds address suggestions based on the search term.
        
        Args:
            search_term (str): The address search term.
            country (str): The country code (default is "CAN").
            max_suggestions (int): Maximum number of suggestions to 
            return.
            language_preference (str): Language preference (2 or 4 
            digit language code).
        """
        params = {
            "Key": self.api_key,
            "SearchTerm": search_term,
            "Country": country,
            "MaxSuggestions": max_suggestions,
            "LanguagePreference": language_preference,
        }
        
        url = f"{self.DEFAULT_FIND_ENDPOINT}&{urllib.parse.urlencode(params)}"
        
        response = requests.get(url)
        response.raise_for_status()
        
        return response.json()
    
    def retrieve(self, id):
        """Retrieves detailed address information based on the ID.
        
        Args:
            id (str): The unique identifier for the address.
        """
        url = (
            f"{self.DEFAULT_RETRIEVE_ENDPOINT}&Key={self.api_key}"
            f"&Id={urllib.parse.quote(id)}"
        )
        
        response = requests.get(url)
        response.raise_for_status()
        return response.json()