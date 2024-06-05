# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class Fields2(object):

    """Implementation of the 'Fields2' model.

    List of fields affected by the event.

    Attributes:
        temperature (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "temperature": 'temperature'
    }

    _optionals = [
        'temperature',
    ]

    def __init__(self,
                 temperature=APIHelper.SKIP):
        """Constructor for the Fields2 class"""

        # Initialize members of the class
        if temperature is not APIHelper.SKIP:
            self.temperature = temperature 

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
        temperature = dictionary.get("temperature") if dictionary.get("temperature") else APIHelper.SKIP
        # Return an object of this model
        return cls(temperature)
