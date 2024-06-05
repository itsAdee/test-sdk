# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.v3_license_device import V3LicenseDevice


class V3LicenseSummary(object):

    """Implementation of the 'V3LicenseSummary' model.

    Information for FOTA licenses assigned to devices.

    Attributes:
        account_name (str): Account identifier.
        total_licenses (int): Total FOTA license count.
        assigned_licenses (int): Assigned FOTA license count.
        has_more_data (bool): True if there are more devices to retrieve.
        last_seen_device_id (str): Last seen device identifier.
        max_page_size (int): Maximum page size.
        device_list (List[V3LicenseDevice]): Device IMEI list.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "assigned_licenses": 'assignedLicenses',
        "has_more_data": 'hasMoreData',
        "max_page_size": 'maxPageSize',
        "total_licenses": 'totalLicenses',
        "last_seen_device_id": 'lastSeenDeviceId',
        "device_list": 'deviceList'
    }

    _optionals = [
        'total_licenses',
        'last_seen_device_id',
        'device_list',
    ]

    def __init__(self,
                 account_name=None,
                 assigned_licenses=None,
                 has_more_data=None,
                 max_page_size=None,
                 total_licenses=APIHelper.SKIP,
                 last_seen_device_id=APIHelper.SKIP,
                 device_list=APIHelper.SKIP):
        """Constructor for the V3LicenseSummary class"""

        # Initialize members of the class
        self.account_name = account_name 
        if total_licenses is not APIHelper.SKIP:
            self.total_licenses = total_licenses 
        self.assigned_licenses = assigned_licenses 
        self.has_more_data = has_more_data 
        if last_seen_device_id is not APIHelper.SKIP:
            self.last_seen_device_id = last_seen_device_id 
        self.max_page_size = max_page_size 
        if device_list is not APIHelper.SKIP:
            self.device_list = device_list 

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
        account_name = dictionary.get("accountName") if dictionary.get("accountName") else None
        assigned_licenses = dictionary.get("assignedLicenses") if dictionary.get("assignedLicenses") else None
        has_more_data = dictionary.get("hasMoreData") if "hasMoreData" in dictionary.keys() else None
        max_page_size = dictionary.get("maxPageSize") if dictionary.get("maxPageSize") else None
        total_licenses = dictionary.get("totalLicenses") if dictionary.get("totalLicenses") else APIHelper.SKIP
        last_seen_device_id = dictionary.get("lastSeenDeviceId") if dictionary.get("lastSeenDeviceId") else APIHelper.SKIP
        device_list = None
        if dictionary.get('deviceList') is not None:
            device_list = [V3LicenseDevice.from_dictionary(x) for x in dictionary.get('deviceList')]
        else:
            device_list = APIHelper.SKIP
        # Return an object of this model
        return cls(account_name,
                   assigned_licenses,
                   has_more_data,
                   max_page_size,
                   total_licenses,
                   last_seen_device_id,
                   device_list)
