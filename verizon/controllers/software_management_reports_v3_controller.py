# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from verizon.api_helper import APIHelper
from verizon.configuration import Server
from verizon.http.api_response import ApiResponse
from verizon.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from verizon.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from verizon.models.v3_campaign_history import V3CampaignHistory
from verizon.models.device_firmware_upgrade import DeviceFirmwareUpgrade
from verizon.models.v3_campaign_device import V3CampaignDevice
from verizon.exceptions.fota_v3_result_exception import FotaV3ResultException


class SoftwareManagementReportsV3Controller(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(SoftwareManagementReportsV3Controller, self).__init__(config)

    def get_campaign_history_by_status(self,
                                       acc,
                                       campaign_status,
                                       last_seen_campaign_id=None):
        """Does a GET request to /reports/{acc}/firmware/campaigns.

        Retrieve a list of campaigns for an account that have a specified
        campaign status.

        Args:
            acc (str): Account identifier.
            campaign_status (CampaignStatusEnum): Campaign status.
            last_seen_campaign_id (str, optional): Last seen campaign Id.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Return
                array of campaign history.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SOFTWARE_MANAGEMENT_V3)
            .path('/reports/{acc}/firmware/campaigns')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('acc')
                            .value(acc)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('campaignStatus')
                         .value(campaign_status))
            .query_param(Parameter()
                         .key('lastSeenCampaignId')
                         .value(last_seen_campaign_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(V3CampaignHistory.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Unexpected error.', FotaV3ResultException)
        ).execute()

    def get_device_firmware_upgrade_history(self,
                                            acc,
                                            device_id):
        """Does a GET request to /reports/{acc}/devices/{deviceId}.

        Retrieve campaign history for a specific device.

        Args:
            acc (str): Account identifier.
            device_id (str): Device IMEI identifier.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Returns a
                list of firmware upgrades.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SOFTWARE_MANAGEMENT_V3)
            .path('/reports/{acc}/devices/{deviceId}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('acc')
                            .value(acc)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('deviceId')
                            .value(device_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DeviceFirmwareUpgrade.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Unexpected error.', FotaV3ResultException)
        ).execute()

    def get_campaign_device_status(self,
                                   acc,
                                   campaign_id,
                                   last_seen_device_id=None):
        """Does a GET request to /reports/{acc}/campaigns/{campaignId}/devices.

        Retrieve a list of all devices in a campaign and the status of each
        device.

        Args:
            acc (str): Account identifier.
            campaign_id (str): Campaign identifier.
            last_seen_device_id (str, optional): Last seen device identifier.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Returns
                an array of campaign history.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SOFTWARE_MANAGEMENT_V3)
            .path('/reports/{acc}/campaigns/{campaignId}/devices')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('acc')
                            .value(acc)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('campaignId')
                            .value(campaign_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('lastSeenDeviceId')
                         .value(last_seen_device_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(V3CampaignDevice.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Unexpected error.', FotaV3ResultException)
        ).execute()
