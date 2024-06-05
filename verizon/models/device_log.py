# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class DeviceLog(object):

    """Implementation of the 'DeviceLog' model.

    Device logging information.

    Attributes:
        device_id (str): Device IMEI.
        log_time (datetime): Time of log.
        log_type (str): Log type (one of SoftwareUpdate, Event,
            UserNotification, AgentService, Wireless, WirelessWeb,
            MobileBroadbandModem, WindowsMDM).
        event_log (str): Event log.
        binary_log_file_base_64 (str): Base64-encoded contents of binary log
            file.
        binary_log_filename (str): File name of binary log file.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "device_id": 'deviceId',
        "log_time": 'logTime',
        "log_type": 'logType',
        "event_log": 'eventLog',
        "binary_log_file_base_64": 'binaryLogFileBase64',
        "binary_log_filename": 'binaryLogFilename'
    }

    def __init__(self,
                 device_id=None,
                 log_time=None,
                 log_type=None,
                 event_log=None,
                 binary_log_file_base_64=None,
                 binary_log_filename=None):
        """Constructor for the DeviceLog class"""

        # Initialize members of the class
        self.device_id = device_id 
        self.log_time = APIHelper.apply_datetime_converter(log_time, APIHelper.RFC3339DateTime) if log_time else None 
        self.log_type = log_type 
        self.event_log = event_log 
        self.binary_log_file_base_64 = binary_log_file_base_64 
        self.binary_log_filename = binary_log_filename 

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
        device_id = dictionary.get("deviceId") if dictionary.get("deviceId") else None
        log_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("logTime")).datetime if dictionary.get("logTime") else None
        log_type = dictionary.get("logType") if dictionary.get("logType") else None
        event_log = dictionary.get("eventLog") if dictionary.get("eventLog") else None
        binary_log_file_base_64 = dictionary.get("binaryLogFileBase64") if dictionary.get("binaryLogFileBase64") else None
        binary_log_filename = dictionary.get("binaryLogFilename") if dictionary.get("binaryLogFilename") else None
        # Return an object of this model
        return cls(device_id,
                   log_time,
                   log_type,
                   event_log,
                   binary_log_file_base_64,
                   binary_log_filename)
