# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.authentication.header_auth import HeaderAuth


class VZM2mToken(HeaderAuth):

    @property
    def error_message(self):
        """Display error message on occurrence of authentication failure
        in VZM2mToken

        """
        return "VZM2mToken: VZ-M2M-Token is undefined."

    def __init__(self, vz_m2m_token_credentials):
        auth_params = {}
        if vz_m2m_token_credentials is not None \
                and vz_m2m_token_credentials.vz_m2m_token is not None:
            auth_params["VZ-M2M-Token"] = vz_m2m_token_credentials.vz_m2m_token
        super().__init__(auth_params=auth_params)


class VZM2mTokenCredentials:

    @property
    def vz_m2m_token(self):
        return self._vz_m2m_token

    def __init__(self, vz_m2m_token):
        if vz_m2m_token is None:
            raise ValueError('vz_m2m_token cannot be None')
        self._vz_m2m_token = vz_m2m_token

    def clone_with(self, vz_m2m_token=None):
        return VZM2mTokenCredentials(vz_m2m_token or self.vz_m2m_token)
