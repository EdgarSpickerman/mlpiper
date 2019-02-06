# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from mcenter_server_api.models.base_model_ import Model
from mcenter_server_api import util


class MLAppProfileWorkflow(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, parent=None, children=None, workflow_node_type=None, rest_server_port=None, parallelism=None, pipeline_mode=None, id=None, is_visible=None, pipeline_type=None, pipeline_agent_set=None, pipeline_pattern_id=None, cron_schedule=None):  # noqa: E501
        """MLAppProfileWorkflow - a model defined in OpenAPI

        :param parent: The parent of this MLAppProfileWorkflow.  # noqa: E501
        :type parent: str
        :param children: The children of this MLAppProfileWorkflow.  # noqa: E501
        :type children: str
        :param workflow_node_type: The workflow_node_type of this MLAppProfileWorkflow.  # noqa: E501
        :type workflow_node_type: str
        :param rest_server_port: The rest_server_port of this MLAppProfileWorkflow.  # noqa: E501
        :type rest_server_port: int
        :param parallelism: The parallelism of this MLAppProfileWorkflow.  # noqa: E501
        :type parallelism: int
        :param pipeline_mode: The pipeline_mode of this MLAppProfileWorkflow.  # noqa: E501
        :type pipeline_mode: str
        :param id: The id of this MLAppProfileWorkflow.  # noqa: E501
        :type id: str
        :param is_visible: The is_visible of this MLAppProfileWorkflow.  # noqa: E501
        :type is_visible: bool
        :param pipeline_type: The pipeline_type of this MLAppProfileWorkflow.  # noqa: E501
        :type pipeline_type: str
        :param pipeline_agent_set: The pipeline_agent_set of this MLAppProfileWorkflow.  # noqa: E501
        :type pipeline_agent_set: MLAppProfilePipelineAgentSet
        :param pipeline_pattern_id: The pipeline_pattern_id of this MLAppProfileWorkflow.  # noqa: E501
        :type pipeline_pattern_id: str
        :param cron_schedule: The cron_schedule of this MLAppProfileWorkflow.  # noqa: E501
        :type cron_schedule: str
        """
        self.openapi_types = {
            'parent': 'str',
            'children': 'str',
            'workflow_node_type': 'str',
            'rest_server_port': 'int',
            'parallelism': 'int',
            'pipeline_mode': 'str',
            'id': 'str',
            'is_visible': 'bool',
            'pipeline_type': 'str',
            'pipeline_agent_set': 'MLAppProfilePipelineAgentSet',
            'pipeline_pattern_id': 'str',
            'cron_schedule': 'str'
        }

        self.attribute_map = {
            'parent': 'parent',
            'children': 'children',
            'workflow_node_type': 'workflowNodeType',
            'rest_server_port': 'restServerPort',
            'parallelism': 'parallelism',
            'pipeline_mode': 'pipelineMode',
            'id': 'id',
            'is_visible': 'isVisible',
            'pipeline_type': 'pipelineType',
            'pipeline_agent_set': 'pipelineAgentSet',
            'pipeline_pattern_id': 'pipelinePatternId',
            'cron_schedule': 'cronSchedule'
        }

        self._parent = parent
        self._children = children
        self._workflow_node_type = workflow_node_type
        self._rest_server_port = rest_server_port
        self._parallelism = parallelism
        self._pipeline_mode = pipeline_mode
        self._id = id
        self._is_visible = is_visible
        self._pipeline_type = pipeline_type
        self._pipeline_agent_set = pipeline_agent_set
        self._pipeline_pattern_id = pipeline_pattern_id
        self._cron_schedule = cron_schedule

    @classmethod
    def from_dict(cls, dikt) -> 'MLAppProfileWorkflow':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MLAppProfile_workflow of this MLAppProfileWorkflow.  # noqa: E501
        :rtype: MLAppProfileWorkflow
        """
        return util.deserialize_model(dikt, cls)

    @property
    def parent(self):
        """Gets the parent of this MLAppProfileWorkflow.


        :return: The parent of this MLAppProfileWorkflow.
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this MLAppProfileWorkflow.


        :param parent: The parent of this MLAppProfileWorkflow.
        :type parent: str
        """

        self._parent = parent

    @property
    def children(self):
        """Gets the children of this MLAppProfileWorkflow.


        :return: The children of this MLAppProfileWorkflow.
        :rtype: str
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this MLAppProfileWorkflow.


        :param children: The children of this MLAppProfileWorkflow.
        :type children: str
        """

        self._children = children

    @property
    def workflow_node_type(self):
        """Gets the workflow_node_type of this MLAppProfileWorkflow.


        :return: The workflow_node_type of this MLAppProfileWorkflow.
        :rtype: str
        """
        return self._workflow_node_type

    @workflow_node_type.setter
    def workflow_node_type(self, workflow_node_type):
        """Sets the workflow_node_type of this MLAppProfileWorkflow.


        :param workflow_node_type: The workflow_node_type of this MLAppProfileWorkflow.
        :type workflow_node_type: str
        """

        self._workflow_node_type = workflow_node_type

    @property
    def rest_server_port(self):
        """Gets the rest_server_port of this MLAppProfileWorkflow.


        :return: The rest_server_port of this MLAppProfileWorkflow.
        :rtype: int
        """
        return self._rest_server_port

    @rest_server_port.setter
    def rest_server_port(self, rest_server_port):
        """Sets the rest_server_port of this MLAppProfileWorkflow.


        :param rest_server_port: The rest_server_port of this MLAppProfileWorkflow.
        :type rest_server_port: int
        """

        self._rest_server_port = rest_server_port

    @property
    def parallelism(self):
        """Gets the parallelism of this MLAppProfileWorkflow.


        :return: The parallelism of this MLAppProfileWorkflow.
        :rtype: int
        """
        return self._parallelism

    @parallelism.setter
    def parallelism(self, parallelism):
        """Sets the parallelism of this MLAppProfileWorkflow.


        :param parallelism: The parallelism of this MLAppProfileWorkflow.
        :type parallelism: int
        """

        self._parallelism = parallelism

    @property
    def pipeline_mode(self):
        """Gets the pipeline_mode of this MLAppProfileWorkflow.


        :return: The pipeline_mode of this MLAppProfileWorkflow.
        :rtype: str
        """
        return self._pipeline_mode

    @pipeline_mode.setter
    def pipeline_mode(self, pipeline_mode):
        """Sets the pipeline_mode of this MLAppProfileWorkflow.


        :param pipeline_mode: The pipeline_mode of this MLAppProfileWorkflow.
        :type pipeline_mode: str
        """

        self._pipeline_mode = pipeline_mode

    @property
    def id(self):
        """Gets the id of this MLAppProfileWorkflow.


        :return: The id of this MLAppProfileWorkflow.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MLAppProfileWorkflow.


        :param id: The id of this MLAppProfileWorkflow.
        :type id: str
        """

        self._id = id

    @property
    def is_visible(self):
        """Gets the is_visible of this MLAppProfileWorkflow.


        :return: The is_visible of this MLAppProfileWorkflow.
        :rtype: bool
        """
        return self._is_visible

    @is_visible.setter
    def is_visible(self, is_visible):
        """Sets the is_visible of this MLAppProfileWorkflow.


        :param is_visible: The is_visible of this MLAppProfileWorkflow.
        :type is_visible: bool
        """

        self._is_visible = is_visible

    @property
    def pipeline_type(self):
        """Gets the pipeline_type of this MLAppProfileWorkflow.


        :return: The pipeline_type of this MLAppProfileWorkflow.
        :rtype: str
        """
        return self._pipeline_type

    @pipeline_type.setter
    def pipeline_type(self, pipeline_type):
        """Sets the pipeline_type of this MLAppProfileWorkflow.


        :param pipeline_type: The pipeline_type of this MLAppProfileWorkflow.
        :type pipeline_type: str
        """

        self._pipeline_type = pipeline_type

    @property
    def pipeline_agent_set(self):
        """Gets the pipeline_agent_set of this MLAppProfileWorkflow.


        :return: The pipeline_agent_set of this MLAppProfileWorkflow.
        :rtype: MLAppProfilePipelineAgentSet
        """
        return self._pipeline_agent_set

    @pipeline_agent_set.setter
    def pipeline_agent_set(self, pipeline_agent_set):
        """Sets the pipeline_agent_set of this MLAppProfileWorkflow.


        :param pipeline_agent_set: The pipeline_agent_set of this MLAppProfileWorkflow.
        :type pipeline_agent_set: MLAppProfilePipelineAgentSet
        """

        self._pipeline_agent_set = pipeline_agent_set

    @property
    def pipeline_pattern_id(self):
        """Gets the pipeline_pattern_id of this MLAppProfileWorkflow.


        :return: The pipeline_pattern_id of this MLAppProfileWorkflow.
        :rtype: str
        """
        return self._pipeline_pattern_id

    @pipeline_pattern_id.setter
    def pipeline_pattern_id(self, pipeline_pattern_id):
        """Sets the pipeline_pattern_id of this MLAppProfileWorkflow.


        :param pipeline_pattern_id: The pipeline_pattern_id of this MLAppProfileWorkflow.
        :type pipeline_pattern_id: str
        """

        self._pipeline_pattern_id = pipeline_pattern_id

    @property
    def cron_schedule(self):
        """Gets the cron_schedule of this MLAppProfileWorkflow.


        :return: The cron_schedule of this MLAppProfileWorkflow.
        :rtype: str
        """
        return self._cron_schedule

    @cron_schedule.setter
    def cron_schedule(self, cron_schedule):
        """Sets the cron_schedule of this MLAppProfileWorkflow.


        :param cron_schedule: The cron_schedule of this MLAppProfileWorkflow.
        :type cron_schedule: str
        """

        self._cron_schedule = cron_schedule
