# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.status_list import StatusList


class ManagedAccountsAddResponse(object):

    """Implementation of the 'ManagedAccountsAddResponse' model.

    TODO: type model description here.

    Attributes:
        tx_id (str): Transaction identifier
        status_list (List[StatusList]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "tx_id": 'TxId',
        "status_list": 'statusList'
    }

    _optionals = [
        'tx_id',
        'status_list',
    ]

    def __init__(self,
                 tx_id=APIHelper.SKIP,
                 status_list=APIHelper.SKIP):
        """Constructor for the ManagedAccountsAddResponse class"""

        # Initialize members of the class
        if tx_id is not APIHelper.SKIP:
            self.tx_id = tx_id 
        if status_list is not APIHelper.SKIP:
            self.status_list = status_list 

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
        tx_id = dictionary.get("TxId") if dictionary.get("TxId") else APIHelper.SKIP
        status_list = None
        if dictionary.get('statusList') is not None:
            status_list = [StatusList.from_dictionary(x) for x in dictionary.get('statusList')]
        else:
            status_list = APIHelper.SKIP
        # Return an object of this model
        return cls(tx_id,
                   status_list)
