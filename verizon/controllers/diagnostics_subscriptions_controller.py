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
from apimatic_core.authentication.multiple.and_auth_group import And
from verizon.models.diagnostics_subscription import DiagnosticsSubscription
from verizon.exceptions.device_diagnostics_result_exception import DeviceDiagnosticsResultException


class DiagnosticsSubscriptionsController(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(DiagnosticsSubscriptionsController, self).__init__(config)

    def get_diagnostics_subscription(self,
                                     account_name):
        """Does a GET request to /subscriptions.

        This endpoint retrieves a diagnostics subscription by account.

        Args:
            account_name (str): Account identifier.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers.
                Diagnostics subscription response.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEVICE_DIAGNOSTICS)
            .path('/subscriptions')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('accountName')
                         .value(account_name))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(And(Single('thingspace_oauth'), Single('VZ-M2M-Token')))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DiagnosticsSubscription.from_dictionary)
            .is_api_response(True)
            .local_error('default', 'Error response.', DeviceDiagnosticsResultException)
        ).execute()
