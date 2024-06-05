# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.account_device_list import AccountDeviceList
from verizon.models.custom_fields import CustomFields


class CustomFieldsUpdateRequest(object):

    """Implementation of the 'CustomFieldsUpdateRequest' model.

    Request to assign or change custom field values for one or more devices.

    Attributes:
        account_name (str): The name of a billing account.This parameter is
            only required if the UWS account used for the current API session
            has access to multiple billing accounts.An account name is usually
            numeric, and must include any leading zeros.
        custom_fields (List[CustomFields]): Custom field names and values, if
            you want to only include devices that have matching values.
        custom_fields_to_update (List[CustomFields]): The names and new values
            of any custom fields that you want to change.
        devices (List[AccountDeviceList]): The devices that you want to
            change.
        group_name (str): The name of a device group, if you want to only
            include devices in that group.
        service_plan (str): The name of a service plan, if you want to only
            include devices that have that service plan.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "custom_fields": 'customFields',
        "custom_fields_to_update": 'customFieldsToUpdate',
        "devices": 'devices',
        "group_name": 'groupName',
        "service_plan": 'servicePlan'
    }

    _optionals = [
        'account_name',
        'custom_fields',
        'custom_fields_to_update',
        'devices',
        'group_name',
        'service_plan',
    ]

    def __init__(self,
                 account_name=APIHelper.SKIP,
                 custom_fields=APIHelper.SKIP,
                 custom_fields_to_update=APIHelper.SKIP,
                 devices=APIHelper.SKIP,
                 group_name=APIHelper.SKIP,
                 service_plan=APIHelper.SKIP):
        """Constructor for the CustomFieldsUpdateRequest class"""

        # Initialize members of the class
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if custom_fields is not APIHelper.SKIP:
            self.custom_fields = custom_fields 
        if custom_fields_to_update is not APIHelper.SKIP:
            self.custom_fields_to_update = custom_fields_to_update 
        if devices is not APIHelper.SKIP:
            self.devices = devices 
        if group_name is not APIHelper.SKIP:
            self.group_name = group_name 
        if service_plan is not APIHelper.SKIP:
            self.service_plan = service_plan 

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
        account_name = dictionary.get("accountName") if dictionary.get("accountName") else APIHelper.SKIP
        custom_fields = None
        if dictionary.get('customFields') is not None:
            custom_fields = [CustomFields.from_dictionary(x) for x in dictionary.get('customFields')]
        else:
            custom_fields = APIHelper.SKIP
        custom_fields_to_update = None
        if dictionary.get('customFieldsToUpdate') is not None:
            custom_fields_to_update = [CustomFields.from_dictionary(x) for x in dictionary.get('customFieldsToUpdate')]
        else:
            custom_fields_to_update = APIHelper.SKIP
        devices = None
        if dictionary.get('devices') is not None:
            devices = [AccountDeviceList.from_dictionary(x) for x in dictionary.get('devices')]
        else:
            devices = APIHelper.SKIP
        group_name = dictionary.get("groupName") if dictionary.get("groupName") else APIHelper.SKIP
        service_plan = dictionary.get("servicePlan") if dictionary.get("servicePlan") else APIHelper.SKIP
        # Return an object of this model
        return cls(account_name,
                   custom_fields,
                   custom_fields_to_update,
                   devices,
                   group_name,
                   service_plan)
