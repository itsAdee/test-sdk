# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.notification import Notification
from verizon.models.price_plan_trigger import PricePlanTrigger


class CreateTriggerV2Request(object):

    """Implementation of the 'CreateTriggerV2Request' model.

    Create Trigger Request

    Attributes:
        trigger_name (str): TODO: type description here.
        ecpd_id (str): TODO: type description here.
        device_group_name (str): TODO: type description here.
        trigger_category (str): TODO: type description here.
        price_plan_trigger (PricePlanTrigger): TODO: type description here.
        notification (Notification): TODO: type description here.
        active (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "trigger_name": 'triggerName',
        "ecpd_id": 'ecpdId',
        "device_group_name": 'deviceGroupName',
        "trigger_category": 'triggerCategory',
        "price_plan_trigger": 'pricePlanTrigger',
        "notification": 'notification',
        "active": 'active'
    }

    _optionals = [
        'trigger_name',
        'ecpd_id',
        'device_group_name',
        'trigger_category',
        'price_plan_trigger',
        'notification',
        'active',
    ]

    def __init__(self,
                 trigger_name=APIHelper.SKIP,
                 ecpd_id=APIHelper.SKIP,
                 device_group_name=APIHelper.SKIP,
                 trigger_category=APIHelper.SKIP,
                 price_plan_trigger=APIHelper.SKIP,
                 notification=APIHelper.SKIP,
                 active=APIHelper.SKIP):
        """Constructor for the CreateTriggerV2Request class"""

        # Initialize members of the class
        if trigger_name is not APIHelper.SKIP:
            self.trigger_name = trigger_name 
        if ecpd_id is not APIHelper.SKIP:
            self.ecpd_id = ecpd_id 
        if device_group_name is not APIHelper.SKIP:
            self.device_group_name = device_group_name 
        if trigger_category is not APIHelper.SKIP:
            self.trigger_category = trigger_category 
        if price_plan_trigger is not APIHelper.SKIP:
            self.price_plan_trigger = price_plan_trigger 
        if notification is not APIHelper.SKIP:
            self.notification = notification 
        if active is not APIHelper.SKIP:
            self.active = active 

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
        trigger_name = dictionary.get("triggerName") if dictionary.get("triggerName") else APIHelper.SKIP
        ecpd_id = dictionary.get("ecpdId") if dictionary.get("ecpdId") else APIHelper.SKIP
        device_group_name = dictionary.get("deviceGroupName") if dictionary.get("deviceGroupName") else APIHelper.SKIP
        trigger_category = dictionary.get("triggerCategory") if dictionary.get("triggerCategory") else APIHelper.SKIP
        price_plan_trigger = PricePlanTrigger.from_dictionary(dictionary.get('pricePlanTrigger')) if 'pricePlanTrigger' in dictionary.keys() else APIHelper.SKIP
        notification = Notification.from_dictionary(dictionary.get('notification')) if 'notification' in dictionary.keys() else APIHelper.SKIP
        active = dictionary.get("active") if "active" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(trigger_name,
                   ecpd_id,
                   device_group_name,
                   trigger_category,
                   price_plan_trigger,
                   notification,
                   active)
