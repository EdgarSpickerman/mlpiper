# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mcenter_server_api.models.base_model_ import Model
from mcenter_server_api import util


class DashboardIonHealthInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pipeline=None, ion_node_id=None, host=None, location=None, error=None):  # noqa: E501
        """DashboardIonHealthInfo - a model defined in OpenAPI

        :param pipeline: The pipeline of this DashboardIonHealthInfo.  # noqa: E501
        :type pipeline: str
        :param ion_node_id: The ion_node_id of this DashboardIonHealthInfo.  # noqa: E501
        :type ion_node_id: str
        :param host: The host of this DashboardIonHealthInfo.  # noqa: E501
        :type host: str
        :param location: The location of this DashboardIonHealthInfo.  # noqa: E501
        :type location: str
        :param error: The error of this DashboardIonHealthInfo.  # noqa: E501
        :type error: str
        """
        self.openapi_types = {
            'pipeline': 'str',
            'ion_node_id': 'str',
            'host': 'str',
            'location': 'str',
            'error': 'str'
        }

        self.attribute_map = {
            'pipeline': 'pipeline',
            'ion_node_id': 'ionNodeId',
            'host': 'host',
            'location': 'location',
            'error': 'error'
        }

        self._pipeline = pipeline
        self._ion_node_id = ion_node_id
        self._host = host
        self._location = location
        self._error = error

    @classmethod
    def from_dict(cls, dikt) -> 'DashboardIonHealthInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Dashboard_ionHealthInfo of this DashboardIonHealthInfo.  # noqa: E501
        :rtype: DashboardIonHealthInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pipeline(self):
        """Gets the pipeline of this DashboardIonHealthInfo.


        :return: The pipeline of this DashboardIonHealthInfo.
        :rtype: str
        """
        return self._pipeline

    @pipeline.setter
    def pipeline(self, pipeline):
        """Sets the pipeline of this DashboardIonHealthInfo.


        :param pipeline: The pipeline of this DashboardIonHealthInfo.
        :type pipeline: str
        """

        self._pipeline = pipeline

    @property
    def ion_node_id(self):
        """Gets the ion_node_id of this DashboardIonHealthInfo.


        :return: The ion_node_id of this DashboardIonHealthInfo.
        :rtype: str
        """
        return self._ion_node_id

    @ion_node_id.setter
    def ion_node_id(self, ion_node_id):
        """Sets the ion_node_id of this DashboardIonHealthInfo.


        :param ion_node_id: The ion_node_id of this DashboardIonHealthInfo.
        :type ion_node_id: str
        """

        self._ion_node_id = ion_node_id

    @property
    def host(self):
        """Gets the host of this DashboardIonHealthInfo.


        :return: The host of this DashboardIonHealthInfo.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this DashboardIonHealthInfo.


        :param host: The host of this DashboardIonHealthInfo.
        :type host: str
        """

        self._host = host

    @property
    def location(self):
        """Gets the location of this DashboardIonHealthInfo.


        :return: The location of this DashboardIonHealthInfo.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this DashboardIonHealthInfo.


        :param location: The location of this DashboardIonHealthInfo.
        :type location: str
        """

        self._location = location

    @property
    def error(self):
        """Gets the error of this DashboardIonHealthInfo.


        :return: The error of this DashboardIonHealthInfo.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this DashboardIonHealthInfo.


        :param error: The error of this DashboardIonHealthInfo.
        :type error: str
        """

        self._error = error
