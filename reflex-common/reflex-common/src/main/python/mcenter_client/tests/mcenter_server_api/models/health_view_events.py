# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mcenter_server_api.models.base_model_ import Model
from mcenter_server_api import util


class HealthViewEvents(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, db_name=None, query=None, name=None, type=None):  # noqa: E501
        """HealthViewEvents - a model defined in OpenAPI

        :param db_name: The db_name of this HealthViewEvents.  # noqa: E501
        :type db_name: str
        :param query: The query of this HealthViewEvents.  # noqa: E501
        :type query: str
        :param name: The name of this HealthViewEvents.  # noqa: E501
        :type name: str
        :param type: The type of this HealthViewEvents.  # noqa: E501
        :type type: str
        """
        self.openapi_types = {
            'db_name': 'str',
            'query': 'str',
            'name': 'str',
            'type': 'str'
        }

        self.attribute_map = {
            'db_name': 'dbName',
            'query': 'query',
            'name': 'name',
            'type': 'type'
        }

        self._db_name = db_name
        self._query = query
        self._name = name
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'HealthViewEvents':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The HealthView_events of this HealthViewEvents.  # noqa: E501
        :rtype: HealthViewEvents
        """
        return util.deserialize_model(dikt, cls)

    @property
    def db_name(self):
        """Gets the db_name of this HealthViewEvents.


        :return: The db_name of this HealthViewEvents.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this HealthViewEvents.


        :param db_name: The db_name of this HealthViewEvents.
        :type db_name: str
        """

        self._db_name = db_name

    @property
    def query(self):
        """Gets the query of this HealthViewEvents.


        :return: The query of this HealthViewEvents.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this HealthViewEvents.


        :param query: The query of this HealthViewEvents.
        :type query: str
        """

        self._query = query

    @property
    def name(self):
        """Gets the name of this HealthViewEvents.


        :return: The name of this HealthViewEvents.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HealthViewEvents.


        :param name: The name of this HealthViewEvents.
        :type name: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this HealthViewEvents.


        :return: The type of this HealthViewEvents.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HealthViewEvents.


        :param type: The type of this HealthViewEvents.
        :type type: str
        """

        self._type = type
