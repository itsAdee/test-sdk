# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.share_plan import SharePlan


class ChangePlan(object):

    """Implementation of the 'ChangePlan' model.

    TODO: type model description here.

    Attributes:
        trigger_date (str): TODO: type description here.
        share_plan (List[SharePlan]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "trigger_date": 'triggerDate',
        "share_plan": 'sharePlan'
    }

    _optionals = [
        'trigger_date',
        'share_plan',
    ]

    def __init__(self,
                 trigger_date=APIHelper.SKIP,
                 share_plan=APIHelper.SKIP):
        """Constructor for the ChangePlan class"""

        # Initialize members of the class
        if trigger_date is not APIHelper.SKIP:
            self.trigger_date = trigger_date 
        if share_plan is not APIHelper.SKIP:
            self.share_plan = share_plan 

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
        trigger_date = dictionary.get("triggerDate") if dictionary.get("triggerDate") else APIHelper.SKIP
        share_plan = None
        if dictionary.get('sharePlan') is not None:
            share_plan = [SharePlan.from_dictionary(x) for x in dictionary.get('sharePlan')]
        else:
            share_plan = APIHelper.SKIP
        # Return an object of this model
        return cls(trigger_date,
                   share_plan)
