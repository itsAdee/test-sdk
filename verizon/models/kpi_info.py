# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class KPIInfo(object):

    """Implementation of the 'KPIInfo' model.

    KPI Info Object

    Attributes:
        name (str): TODO: type description here.
        value (str): TODO: type description here.
        node_name (str): TODO: type description here.
        node_type (str): TODO: type description here.
        description (str): TODO: type description here.
        unit (str): TODO: type description here.
        category (str): TODO: type description here.
        time_of_last_update (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "value": 'value',
        "node_name": 'nodeName',
        "node_type": 'nodeType',
        "description": 'description',
        "unit": 'unit',
        "category": 'category',
        "time_of_last_update": 'timeOfLastUpdate'
    }

    _optionals = [
        'name',
        'value',
        'node_name',
        'node_type',
        'description',
        'unit',
        'category',
        'time_of_last_update',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 value=APIHelper.SKIP,
                 node_name=APIHelper.SKIP,
                 node_type=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 unit=APIHelper.SKIP,
                 category=APIHelper.SKIP,
                 time_of_last_update=APIHelper.SKIP):
        """Constructor for the KPIInfo class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if value is not APIHelper.SKIP:
            self.value = value 
        if node_name is not APIHelper.SKIP:
            self.node_name = node_name 
        if node_type is not APIHelper.SKIP:
            self.node_type = node_type 
        if description is not APIHelper.SKIP:
            self.description = description 
        if unit is not APIHelper.SKIP:
            self.unit = unit 
        if category is not APIHelper.SKIP:
            self.category = category 
        if time_of_last_update is not APIHelper.SKIP:
            self.time_of_last_update = time_of_last_update 

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
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        value = dictionary.get("value") if dictionary.get("value") else APIHelper.SKIP
        node_name = dictionary.get("nodeName") if dictionary.get("nodeName") else APIHelper.SKIP
        node_type = dictionary.get("nodeType") if dictionary.get("nodeType") else APIHelper.SKIP
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        unit = dictionary.get("unit") if dictionary.get("unit") else APIHelper.SKIP
        category = dictionary.get("category") if dictionary.get("category") else APIHelper.SKIP
        time_of_last_update = dictionary.get("timeOfLastUpdate") if dictionary.get("timeOfLastUpdate") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   value,
                   node_name,
                   node_type,
                   description,
                   unit,
                   category,
                   time_of_last_update)
