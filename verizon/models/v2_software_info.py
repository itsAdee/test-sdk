# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class V2SoftwareInfo(object):

    """Implementation of the 'V2SoftwareInfo' model.

    Software information.

    Attributes:
        name (str): Software name.
        version (str): Software version.
        upgrade_time (str): Upgrade time.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "version": 'version',
        "upgrade_time": 'upgradeTime'
    }

    def __init__(self,
                 name=None,
                 version=None,
                 upgrade_time=None):
        """Constructor for the V2SoftwareInfo class"""

        # Initialize members of the class
        self.name = name 
        self.version = version 
        self.upgrade_time = upgrade_time 

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
        name = dictionary.get("name") if dictionary.get("name") else None
        version = dictionary.get("version") if dictionary.get("version") else None
        upgrade_time = dictionary.get("upgradeTime") if dictionary.get("upgradeTime") else None
        # Return an object of this model
        return cls(name,
                   version,
                   upgrade_time)
