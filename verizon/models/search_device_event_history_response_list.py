# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.search_device_response import SearchDeviceResponse


class SearchDeviceEventHistoryResponseList(object):

    """Implementation of the 'SearchDeviceEventHistoryResponseList' model.

    A success response includes an array of all matching events.

    Attributes:
        search_device_event_history (List[SearchDeviceResponse]): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "search_device_event_history": 'SearchDeviceEventHistory'
    }

    _optionals = [
        'search_device_event_history',
    ]

    def __init__(self,
                 search_device_event_history=APIHelper.SKIP):
        """Constructor for the SearchDeviceEventHistoryResponseList class"""

        # Initialize members of the class
        if search_device_event_history is not APIHelper.SKIP:
            self.search_device_event_history = search_device_event_history 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        search_device_event_history = None
        if dictionary.get('SearchDeviceEventHistory') is not None:
            search_device_event_history = [SearchDeviceResponse.from_dictionary(x) for x in dictionary.get('SearchDeviceEventHistory')]
        else:
            search_device_event_history = APIHelper.SKIP
        # Return an object of this model
        return cls(search_device_event_history)
