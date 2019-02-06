# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mcenter_server_api.models.base_model_ import Model
from mcenter_server_api import util


class ReportIonMetrics(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, qo_q=None, mo_m=None, wo_w=None):  # noqa: E501
        """ReportIonMetrics - a model defined in OpenAPI

        :param qo_q: The qo_q of this ReportIonMetrics.  # noqa: E501
        :type qo_q: IntervalChart
        :param mo_m: The mo_m of this ReportIonMetrics.  # noqa: E501
        :type mo_m: IntervalChart
        :param wo_w: The wo_w of this ReportIonMetrics.  # noqa: E501
        :type wo_w: IntervalChart
        """
        self.openapi_types = {
            'qo_q': 'IntervalChart',
            'mo_m': 'IntervalChart',
            'wo_w': 'IntervalChart'
        }

        self.attribute_map = {
            'qo_q': 'QoQ',
            'mo_m': 'MoM',
            'wo_w': 'WoW'
        }

        self._qo_q = qo_q
        self._mo_m = mo_m
        self._wo_w = wo_w

    @classmethod
    def from_dict(cls, dikt) -> 'ReportIonMetrics':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Report_ionMetrics of this ReportIonMetrics.  # noqa: E501
        :rtype: ReportIonMetrics
        """
        return util.deserialize_model(dikt, cls)

    @property
    def qo_q(self):
        """Gets the qo_q of this ReportIonMetrics.


        :return: The qo_q of this ReportIonMetrics.
        :rtype: IntervalChart
        """
        return self._qo_q

    @qo_q.setter
    def qo_q(self, qo_q):
        """Sets the qo_q of this ReportIonMetrics.


        :param qo_q: The qo_q of this ReportIonMetrics.
        :type qo_q: IntervalChart
        """

        self._qo_q = qo_q

    @property
    def mo_m(self):
        """Gets the mo_m of this ReportIonMetrics.


        :return: The mo_m of this ReportIonMetrics.
        :rtype: IntervalChart
        """
        return self._mo_m

    @mo_m.setter
    def mo_m(self, mo_m):
        """Sets the mo_m of this ReportIonMetrics.


        :param mo_m: The mo_m of this ReportIonMetrics.
        :type mo_m: IntervalChart
        """

        self._mo_m = mo_m

    @property
    def wo_w(self):
        """Gets the wo_w of this ReportIonMetrics.


        :return: The wo_w of this ReportIonMetrics.
        :rtype: IntervalChart
        """
        return self._wo_w

    @wo_w.setter
    def wo_w(self, wo_w):
        """Sets the wo_w of this ReportIonMetrics.


        :param wo_w: The wo_w of this ReportIonMetrics.
        :type wo_w: IntervalChart
        """

        self._wo_w = wo_w
