# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.device_id import DeviceId
from verizon.models.label import Label


class DeviceUsageListRequest(object):

    """Implementation of the 'DeviceUsageListRequest' model.

    Request to return the daily network data usage of a single device during a
    specified time period.

    Attributes:
        earliest (str): The earliest date for which you want usage data.
        latest (str): The last date for which you want usage data.
        device_id (DeviceId): An identifier for a single device.
        label (Label): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "earliest": 'earliest',
        "latest": 'latest',
        "device_id": 'deviceId',
        "label": 'label'
    }

    _optionals = [
        'device_id',
        'label',
    ]

    def __init__(self,
                 earliest=None,
                 latest=None,
                 device_id=APIHelper.SKIP,
                 label=APIHelper.SKIP):
        """Constructor for the DeviceUsageListRequest class"""

        # Initialize members of the class
        self.earliest = earliest 
        self.latest = latest 
        if device_id is not APIHelper.SKIP:
            self.device_id = device_id 
        if label is not APIHelper.SKIP:
            self.label = label 

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
        earliest = dictionary.get("earliest") if dictionary.get("earliest") else None
        latest = dictionary.get("latest") if dictionary.get("latest") else None
        device_id = DeviceId.from_dictionary(dictionary.get('deviceId')) if 'deviceId' in dictionary.keys() else APIHelper.SKIP
        label = Label.from_dictionary(dictionary.get('label')) if 'label' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(earliest,
                   latest,
                   device_id,
                   label)