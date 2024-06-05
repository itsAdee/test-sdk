# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.gio_device_id import GIODeviceId


class Subrequest(object):

    """Implementation of the 'Subrequest' model.

    TODO: type model description here.

    Attributes:
        ids (GIODeviceId): TODO: type description here.
        status (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ids": 'ids',
        "status": 'status'
    }

    _optionals = [
        'ids',
        'status',
    ]

    def __init__(self,
                 ids=APIHelper.SKIP,
                 status=APIHelper.SKIP):
        """Constructor for the Subrequest class"""

        # Initialize members of the class
        if ids is not APIHelper.SKIP:
            self.ids = ids 
        if status is not APIHelper.SKIP:
            self.status = status 

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
        ids = GIODeviceId.from_dictionary(dictionary.get('ids')) if 'ids' in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        # Return an object of this model
        return cls(ids,
                   status)