# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class PromoAlertTriggerRequest(object):

    """Implementation of the 'PromoAlertTriggerRequest' model.

    TODO: type model description here.

    Attributes:
        data_percentage_50 (bool): TODO: type description here.
        data_percentage_75 (bool): TODO: type description here.
        data_percentage_90 (bool): TODO: type description here.
        no_of_days_b_4_promo_exp (int): TODO: type description here.
        sms_percentage_50 (bool): TODO: type description here.
        sms_percentage_75 (bool): TODO: type description here.
        sms_percentage_90 (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data_percentage_50": 'dataPercentage50',
        "data_percentage_75": 'dataPercentage75',
        "data_percentage_90": 'dataPercentage90',
        "no_of_days_b_4_promo_exp": 'noOfDaysB4PromoExp',
        "sms_percentage_50": 'smsPercentage50',
        "sms_percentage_75": 'smsPercentage75',
        "sms_percentage_90": 'smsPercentage90'
    }

    _optionals = [
        'data_percentage_50',
        'data_percentage_75',
        'data_percentage_90',
        'no_of_days_b_4_promo_exp',
        'sms_percentage_50',
        'sms_percentage_75',
        'sms_percentage_90',
    ]

    def __init__(self,
                 data_percentage_50=APIHelper.SKIP,
                 data_percentage_75=APIHelper.SKIP,
                 data_percentage_90=APIHelper.SKIP,
                 no_of_days_b_4_promo_exp=APIHelper.SKIP,
                 sms_percentage_50=APIHelper.SKIP,
                 sms_percentage_75=APIHelper.SKIP,
                 sms_percentage_90=APIHelper.SKIP):
        """Constructor for the PromoAlertTriggerRequest class"""

        # Initialize members of the class
        if data_percentage_50 is not APIHelper.SKIP:
            self.data_percentage_50 = data_percentage_50 
        if data_percentage_75 is not APIHelper.SKIP:
            self.data_percentage_75 = data_percentage_75 
        if data_percentage_90 is not APIHelper.SKIP:
            self.data_percentage_90 = data_percentage_90 
        if no_of_days_b_4_promo_exp is not APIHelper.SKIP:
            self.no_of_days_b_4_promo_exp = no_of_days_b_4_promo_exp 
        if sms_percentage_50 is not APIHelper.SKIP:
            self.sms_percentage_50 = sms_percentage_50 
        if sms_percentage_75 is not APIHelper.SKIP:
            self.sms_percentage_75 = sms_percentage_75 
        if sms_percentage_90 is not APIHelper.SKIP:
            self.sms_percentage_90 = sms_percentage_90 

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
        data_percentage_50 = dictionary.get("dataPercentage50") if "dataPercentage50" in dictionary.keys() else APIHelper.SKIP
        data_percentage_75 = dictionary.get("dataPercentage75") if "dataPercentage75" in dictionary.keys() else APIHelper.SKIP
        data_percentage_90 = dictionary.get("dataPercentage90") if "dataPercentage90" in dictionary.keys() else APIHelper.SKIP
        no_of_days_b_4_promo_exp = dictionary.get("noOfDaysB4PromoExp") if dictionary.get("noOfDaysB4PromoExp") else APIHelper.SKIP
        sms_percentage_50 = dictionary.get("smsPercentage50") if "smsPercentage50" in dictionary.keys() else APIHelper.SKIP
        sms_percentage_75 = dictionary.get("smsPercentage75") if "smsPercentage75" in dictionary.keys() else APIHelper.SKIP
        sms_percentage_90 = dictionary.get("smsPercentage90") if "smsPercentage90" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(data_percentage_50,
                   data_percentage_75,
                   data_percentage_90,
                   no_of_days_b_4_promo_exp,
                   sms_percentage_50,
                   sms_percentage_75,
                   sms_percentage_90)