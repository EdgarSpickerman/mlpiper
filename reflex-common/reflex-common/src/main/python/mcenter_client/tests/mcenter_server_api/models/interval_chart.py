# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mcenter_server_api.models.base_model_ import Model
from mcenter_server_api import util


class IntervalChart(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, creation_times=None, graph_type=None, legend=None):  # noqa: E501
        """IntervalChart - a model defined in OpenAPI

        :param creation_times: The creation_times of this IntervalChart.  # noqa: E501
        :type creation_times: List[Dict[str, int]]
        :param graph_type: The graph_type of this IntervalChart.  # noqa: E501
        :type graph_type: str
        :param legend: The legend of this IntervalChart.  # noqa: E501
        :type legend: str
        """
        self.openapi_types = {
            'creation_times': 'List[Dict[str, int]]',
            'graph_type': 'str',
            'legend': 'str'
        }

        self.attribute_map = {
            'creation_times': 'creationTimes',
            'graph_type': 'graphType',
            'legend': 'legend'
        }

        self._creation_times = creation_times
        self._graph_type = graph_type
        self._legend = legend

    @classmethod
    def from_dict(cls, dikt) -> 'IntervalChart':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The IntervalChart of this IntervalChart.  # noqa: E501
        :rtype: IntervalChart
        """
        return util.deserialize_model(dikt, cls)

    @property
    def creation_times(self):
        """Gets the creation_times of this IntervalChart.


        :return: The creation_times of this IntervalChart.
        :rtype: List[Dict[str, int]]
        """
        return self._creation_times

    @creation_times.setter
    def creation_times(self, creation_times):
        """Sets the creation_times of this IntervalChart.


        :param creation_times: The creation_times of this IntervalChart.
        :type creation_times: List[Dict[str, int]]
        """

        self._creation_times = creation_times

    @property
    def graph_type(self):
        """Gets the graph_type of this IntervalChart.


        :return: The graph_type of this IntervalChart.
        :rtype: str
        """
        return self._graph_type

    @graph_type.setter
    def graph_type(self, graph_type):
        """Sets the graph_type of this IntervalChart.


        :param graph_type: The graph_type of this IntervalChart.
        :type graph_type: str
        """

        self._graph_type = graph_type

    @property
    def legend(self):
        """Gets the legend of this IntervalChart.


        :return: The legend of this IntervalChart.
        :rtype: str
        """
        return self._legend

    @legend.setter
    def legend(self, legend):
        """Sets the legend of this IntervalChart.


        :param legend: The legend of this IntervalChart.
        :type legend: str
        """

        self._legend = legend
