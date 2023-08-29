# coding: utf-8

"""
    SEARCH Gateway Service

    SEARCH Gateway Service using Flask, OpenAPI and Connexion  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PathGoalDto(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'title': 'str',
        'target_audience': 'str',
        'description': 'str',
        'requirements': 'list[ResolvedSkillDto]',
        'path_goals': 'list[ResolvedSkillDto]'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'target_audience': 'targetAudience',
        'description': 'description',
        'requirements': 'requirements',
        'path_goals': 'pathGoals'
    }

    def __init__(self, id=None, title=None, target_audience=None, description=None, requirements=None, path_goals=None):  # noqa: E501
        """PathGoalDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._title = None
        self._target_audience = None
        self._description = None
        self._requirements = None
        self._path_goals = None
        self.discriminator = None
        self.id = id
        self.title = title
        if target_audience is not None:
            self.target_audience = target_audience
        if description is not None:
            self.description = description
        self.requirements = requirements
        self.path_goals = path_goals

    @property
    def id(self):
        """Gets the id of this PathGoalDto.  # noqa: E501


        :return: The id of this PathGoalDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PathGoalDto.


        :param id: The id of this PathGoalDto.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def title(self):
        """Gets the title of this PathGoalDto.  # noqa: E501


        :return: The title of this PathGoalDto.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PathGoalDto.


        :param title: The title of this PathGoalDto.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def target_audience(self):
        """Gets the target_audience of this PathGoalDto.  # noqa: E501


        :return: The target_audience of this PathGoalDto.  # noqa: E501
        :rtype: str
        """
        return self._target_audience

    @target_audience.setter
    def target_audience(self, target_audience):
        """Sets the target_audience of this PathGoalDto.


        :param target_audience: The target_audience of this PathGoalDto.  # noqa: E501
        :type: str
        """

        self._target_audience = target_audience

    @property
    def description(self):
        """Gets the description of this PathGoalDto.  # noqa: E501


        :return: The description of this PathGoalDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PathGoalDto.


        :param description: The description of this PathGoalDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def requirements(self):
        """Gets the requirements of this PathGoalDto.  # noqa: E501


        :return: The requirements of this PathGoalDto.  # noqa: E501
        :rtype: list[ResolvedSkillDto]
        """
        return self._requirements

    @requirements.setter
    def requirements(self, requirements):
        """Sets the requirements of this PathGoalDto.


        :param requirements: The requirements of this PathGoalDto.  # noqa: E501
        :type: list[ResolvedSkillDto]
        """
        if requirements is None:
            raise ValueError("Invalid value for `requirements`, must not be `None`")  # noqa: E501

        self._requirements = requirements

    @property
    def path_goals(self):
        """Gets the path_goals of this PathGoalDto.  # noqa: E501


        :return: The path_goals of this PathGoalDto.  # noqa: E501
        :rtype: list[ResolvedSkillDto]
        """
        return self._path_goals

    @path_goals.setter
    def path_goals(self, path_goals):
        """Sets the path_goals of this PathGoalDto.


        :param path_goals: The path_goals of this PathGoalDto.  # noqa: E501
        :type: list[ResolvedSkillDto]
        """
        if path_goals is None:
            raise ValueError("Invalid value for `path_goals`, must not be `None`")  # noqa: E501

        self._path_goals = path_goals

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PathGoalDto, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PathGoalDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
