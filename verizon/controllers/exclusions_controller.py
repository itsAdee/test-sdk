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
from verizon.models.device_location_success_result import DeviceLocationSuccessResult
from verizon.models.devices_consent_result import DevicesConsentResult
from verizon.exceptions.device_location_result_exception import DeviceLocationResultException


class ExclusionsController(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(ExclusionsController, self).__init__(config)

    def exclude_devices(self,
                        body):
        """Does a POST request to /consents.

        This consents endpoint sets a new exclusion list.

        Args:
            body (ConsentRequest): Request to update account consent exclusion
                list.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success
                response.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEVICE_LOCATION)
            .path('/consents')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('*/*'))
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
            .deserialize_into(DeviceLocationSuccessResult.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Unexpected error.', DeviceLocationResultException)
        ).execute()

    def remove_devices_from_exclusion_list(self,
                                           account_name,
                                           device_list):
        """Does a DELETE request to /consents.

        Removes devices from the exclusion list so that they can be located
        with Device Location Services requests.

        Args:
            account_name (str): The numeric name of the account.
            device_list (str): A list of the device IDs to remove from the
                exclusion list.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Devices
                successfully removed from list.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEVICE_LOCATION)
            .path('/consents')
            .http_method(HttpMethodEnum.DELETE)
            .query_param(Parameter()
                         .key('accountName')
                         .value(account_name))
            .query_param(Parameter()
                         .key('deviceList')
                         .value(device_list))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DeviceLocationSuccessResult.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Unexpected error.', DeviceLocationResultException)
        ).execute()

    def list_excluded_devices(self,
                              account,
                              start_index):
        """Does a GET request to /consents/{account}/index/{startIndex}.

        This consents endpoint retrieves a list of excluded devices in an
        account.

        Args:
            account (str): Account identifier in "##########-#####".
            start_index (str): Zero-based number of the first record to
                return.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Excluded
                devices result.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEVICE_LOCATION)
            .path('/consents/{account}/index/{startIndex}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('account')
                            .value(account)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('startIndex')
                            .value(start_index)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DevicesConsentResult.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Unexpected error.', DeviceLocationResultException)
        ).execute()
