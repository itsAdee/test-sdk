# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class LocationReportStatus(object):

    """Implementation of the 'LocationReportStatus' model.

    Status of the report.

    Attributes:
        txid (str): The transaction ID of the report.
        status (ReportStatusEnum): Status of the report.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "txid": 'txid',
        "status": 'status'
    }

    _optionals = [
        'txid',
        'status',
    ]

    def __init__(self,
                 txid=APIHelper.SKIP,
                 status=APIHelper.SKIP):
        """Constructor for the LocationReportStatus class"""

        # Initialize members of the class
        if txid is not APIHelper.SKIP:
            self.txid = txid 
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
        txid = dictionary.get("txid") if dictionary.get("txid") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        # Return an object of this model
        return cls(txid,
                   status)