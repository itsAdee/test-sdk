# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.anomaly_trigger_request import AnomalyTriggerRequest
from verizon.models.trigger_notification import TriggerNotification


class TriggerType1(object):

    """Implementation of the 'TriggerType1' model.

    Trigger details.

    Attributes:
        name (str): Trigger name.
        trigger_category (str): This is the value to use in the request body
            to detect anomalous behaivior. The values in this table will only
            be relevant when this parameter is set to this value.
        account_name (str): Account name.
        anomaly_trigger_request (AnomalyTriggerRequest): The details of the
            UsageAnomaly trigger.
        notification (TriggerNotification): The notification details of the
            trigger.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "trigger_category": 'triggerCategory',
        "account_name": 'accountName',
        "anomaly_trigger_request": 'anomalyTriggerRequest',
        "notification": 'notification'
    }

    _optionals = [
        'name',
        'trigger_category',
        'account_name',
        'anomaly_trigger_request',
        'notification',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 trigger_category=APIHelper.SKIP,
                 account_name=APIHelper.SKIP,
                 anomaly_trigger_request=APIHelper.SKIP,
                 notification=APIHelper.SKIP):
        """Constructor for the TriggerType1 class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if trigger_category is not APIHelper.SKIP:
            self.trigger_category = trigger_category 
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if anomaly_trigger_request is not APIHelper.SKIP:
            self.anomaly_trigger_request = anomaly_trigger_request 
        if notification is not APIHelper.SKIP:
            self.notification = notification 

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
        trigger_category = dictionary.get("triggerCategory") if dictionary.get("triggerCategory") else APIHelper.SKIP
        account_name = dictionary.get("accountName") if dictionary.get("accountName") else APIHelper.SKIP
        anomaly_trigger_request = AnomalyTriggerRequest.from_dictionary(dictionary.get('anomalyTriggerRequest')) if 'anomalyTriggerRequest' in dictionary.keys() else APIHelper.SKIP
        notification = TriggerNotification.from_dictionary(dictionary.get('notification')) if 'notification' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   trigger_category,
                   account_name,
                   anomaly_trigger_request,
                   notification)
