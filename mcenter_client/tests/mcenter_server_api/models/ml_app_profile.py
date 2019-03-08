# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mcenter_server_api.models.base_model_ import Model
from mcenter_server_api import util


class MLAppProfile(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, is_profile=None, ml_app_pattern_id=None, ml_app_pattern_name=None, version=None, workflow=None):  # noqa: E501
        """MLAppProfile - a model defined in OpenAPI

        :param is_profile: The is_profile of this MLAppProfile.  # noqa: E501
        :type is_profile: bool
        :param ml_app_pattern_id: The ml_app_pattern_id of this MLAppProfile.  # noqa: E501
        :type ml_app_pattern_id: str
        :param ml_app_pattern_name: The ml_app_pattern_name of this MLAppProfile.  # noqa: E501
        :type ml_app_pattern_name: str
        :param version: The version of this MLAppProfile.  # noqa: E501
        :type version: str
        :param workflow: The workflow of this MLAppProfile.  # noqa: E501
        :type workflow: List[MLAppProfileWorkflow]
        """
        self.openapi_types = {
            'is_profile': 'bool',
            'ml_app_pattern_id': 'str',
            'ml_app_pattern_name': 'str',
            'version': 'str',
            'workflow': 'List[MLAppProfileWorkflow]'
        }

        self.attribute_map = {
            'is_profile': 'isProfile',
            'ml_app_pattern_id': 'mlAppPatternId',
            'ml_app_pattern_name': 'mlAppPatternName',
            'version': 'version',
            'workflow': 'workflow'
        }

        self._is_profile = is_profile
        self._ml_app_pattern_id = ml_app_pattern_id
        self._ml_app_pattern_name = ml_app_pattern_name
        self._version = version
        self._workflow = workflow

    @classmethod
    def from_dict(cls, dikt) -> 'MLAppProfile':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MLAppProfile of this MLAppProfile.  # noqa: E501
        :rtype: MLAppProfile
        """
        return util.deserialize_model(dikt, cls)

    @property
    def is_profile(self):
        """Gets the is_profile of this MLAppProfile.


        :return: The is_profile of this MLAppProfile.
        :rtype: bool
        """
        return self._is_profile

    @is_profile.setter
    def is_profile(self, is_profile):
        """Sets the is_profile of this MLAppProfile.


        :param is_profile: The is_profile of this MLAppProfile.
        :type is_profile: bool
        """

        self._is_profile = is_profile

    @property
    def ml_app_pattern_id(self):
        """Gets the ml_app_pattern_id of this MLAppProfile.


        :return: The ml_app_pattern_id of this MLAppProfile.
        :rtype: str
        """
        return self._ml_app_pattern_id

    @ml_app_pattern_id.setter
    def ml_app_pattern_id(self, ml_app_pattern_id):
        """Sets the ml_app_pattern_id of this MLAppProfile.


        :param ml_app_pattern_id: The ml_app_pattern_id of this MLAppProfile.
        :type ml_app_pattern_id: str
        """

        self._ml_app_pattern_id = ml_app_pattern_id

    @property
    def ml_app_pattern_name(self):
        """Gets the ml_app_pattern_name of this MLAppProfile.


        :return: The ml_app_pattern_name of this MLAppProfile.
        :rtype: str
        """
        return self._ml_app_pattern_name

    @ml_app_pattern_name.setter
    def ml_app_pattern_name(self, ml_app_pattern_name):
        """Sets the ml_app_pattern_name of this MLAppProfile.


        :param ml_app_pattern_name: The ml_app_pattern_name of this MLAppProfile.
        :type ml_app_pattern_name: str
        """

        self._ml_app_pattern_name = ml_app_pattern_name

    @property
    def version(self):
        """Gets the version of this MLAppProfile.


        :return: The version of this MLAppProfile.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this MLAppProfile.


        :param version: The version of this MLAppProfile.
        :type version: str
        """

        self._version = version

    @property
    def workflow(self):
        """Gets the workflow of this MLAppProfile.


        :return: The workflow of this MLAppProfile.
        :rtype: List[MLAppProfileWorkflow]
        """
        return self._workflow

    @workflow.setter
    def workflow(self, workflow):
        """Sets the workflow of this MLAppProfile.


        :param workflow: The workflow of this MLAppProfile.
        :type workflow: List[MLAppProfileWorkflow]
        """

        self._workflow = workflow