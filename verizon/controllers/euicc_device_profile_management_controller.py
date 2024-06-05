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
from verizon.models.device_management_result import DeviceManagementResult
from verizon.models.request_response import RequestResponse
from verizon.exceptions.connectivity_management_result_exception import ConnectivityManagementResultException
from verizon.exceptions.rest_error_response_exception import RestErrorResponseException


class EUICCDeviceProfileManagementController(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(EUICCDeviceProfileManagementController, self).__init__(config)

    def download_local_profile_to_enable(self,
                                         body):
        """Does a POST request to /m2m/v1/devices/profile/actions/download_enable.

        Downloads an eUICC local profile to devices and enables the profile.

        Args:
            body (ProfileChangeStateRequest): Device Profile Query

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Request
                ID received on a successful response.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/devices/profile/actions/download_enable')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DeviceManagementResult.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Error response.', ConnectivityManagementResultException)
        ).execute()

    def download_local_profile_to_disable(self,
                                          body):
        """Does a POST request to /m2m/v1/devices/profile/actions/download_disable.

        Downloads an eUICC local profile to devices and leaves the profile
        disabled.

        Args:
            body (ProfileChangeStateRequest): Device Profile Query

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Request
                ID received on a successful response.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/devices/profile/actions/download_disable')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DeviceManagementResult.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Error response.', ConnectivityManagementResultException)
        ).execute()

    def enable_local_profile(self,
                             body):
        """Does a POST request to /m2m/v1/devices/profile/actions/enable.

        Enable a local profile that has been downloaded to eUICC devices.

        Args:
            body (ProfileChangeStateRequest): Update state

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Request
                ID

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/devices/profile/actions/enable')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(RequestResponse.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Error Response', RestErrorResponseException)
        ).execute()

    def disable_local_profile(self,
                              body):
        """Does a POST request to /m2m/v1/devices/profile/actions/disable.

        Disable a local profile on eUICC devices. The default or boot profile
        will become the enabled profile.

        Args:
            body (ProfileChangeStateRequest): Update state

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Request
                ID

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/devices/profile/actions/disable')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(RequestResponse.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Error Response', RestErrorResponseException)
        ).execute()

    def delete_local_profile(self,
                             body):
        """Does a POST request to /m2m/v1/devices/profile/actions/delete.

        Delete a local profile from eUICC devices. If the local profile is
        enabled, it will first be disabled and the boot or default profile
        will be enabled.

        Args:
            body (ProfileChangeStateRequest): Update state

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Request
                ID

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/devices/profile/actions/delete')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(RequestResponse.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Error Response', RestErrorResponseException)
        ).execute()
