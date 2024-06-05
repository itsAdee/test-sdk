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
from verizon.models.anomaly_detection_trigger import AnomalyDetectionTrigger
from verizon.models.intelligence_success_result import IntelligenceSuccessResult
from verizon.models.anomaly_trigger_result import AnomalyTriggerResult
from verizon.exceptions.intelligence_result_exception import IntelligenceResultException


class AnomalyTriggersV2Controller(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(AnomalyTriggersV2Controller, self).__init__(config)

    def create_anomaly_detection_trigger_v2(self,
                                            body):
        """Does a POST request to /m2m/v2/triggers.

        Creates the trigger to identify an anomaly.

        Args:
            body (List[CreateTriggerRequestOptions]): Request to create an
                anomaly trigger.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Result of
                request to create a trigger for anomaly detection.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v2/triggers')
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
            .deserialize_into(AnomalyDetectionTrigger.from_dictionary)
            .is_api_response(True)
            .local_error('default', 'An error occurred.', IntelligenceResultException)
        ).execute()

    def update_anomaly_detection_trigger_v2(self,
                                            body):
        """Does a PUT request to /m2m/v2/triggers.

        Updates an existing trigger using the account name.

        Args:
            body (List[UpdateTriggerRequestOptions]): Request to update
                existing trigger.

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
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v2/triggers')
            .http_method(HttpMethodEnum.PUT)
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
            .deserialize_into(IntelligenceSuccessResult.from_dictionary)
            .is_api_response(True)
            .local_error('default', 'An error occurred.', IntelligenceResultException)
        ).execute()

    def list_anomaly_detection_trigger_settings_v2(self,
                                                   trigger_id):
        """Does a GET request to /m2m/v2/triggers/{triggerId}.

        Retrieves the values for a specific trigger ID.

        Args:
            trigger_id (str): The trigger ID of a specific trigger.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Anomaly
                detection trigger details.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v2/triggers/{triggerId}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('triggerId')
                            .value(trigger_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(AnomalyTriggerResult.from_dictionary)
            .is_api_response(True)
            .local_error('default', 'An error occurred.', IntelligenceResultException)
        ).execute()
