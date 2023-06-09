# coding: utf-8

"""
    Skill Repository

    The API description of the Skill Repository.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RoleGroupDto(object):
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
        'name': 'str',
        'user_id': 'str',
        'id': 'str',
        'roles': 'list[RoleDto]'
    }

    attribute_map = {
        'name': 'name',
        'user_id': 'userId',
        'id': 'id',
        'roles': 'roles'
    }

    def __init__(self, name=None, user_id=None, id=None, roles=None):  # noqa: E501
        """RoleGroupDto - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._user_id = None
        self._id = None
        self._roles = None
        self.discriminator = None
        self.name = name
        self.user_id = user_id
        self.id = id
        self.roles = roles

    @property
    def name(self):
        """Gets the name of this RoleGroupDto.  # noqa: E501


        :return: The name of this RoleGroupDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RoleGroupDto.


        :param name: The name of this RoleGroupDto.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def user_id(self):
        """Gets the user_id of this RoleGroupDto.  # noqa: E501


        :return: The user_id of this RoleGroupDto.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this RoleGroupDto.


        :param user_id: The user_id of this RoleGroupDto.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def id(self):
        """Gets the id of this RoleGroupDto.  # noqa: E501


        :return: The id of this RoleGroupDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RoleGroupDto.


        :param id: The id of this RoleGroupDto.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def roles(self):
        """Gets the roles of this RoleGroupDto.  # noqa: E501


        :return: The roles of this RoleGroupDto.  # noqa: E501
        :rtype: list[RoleDto]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this RoleGroupDto.


        :param roles: The roles of this RoleGroupDto.  # noqa: E501
        :type: list[RoleDto]
        """
        if roles is None:
            raise ValueError("Invalid value for `roles`, must not be `None`")  # noqa: E501

        self._roles = roles

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
        if issubclass(RoleGroupDto, dict):
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
        if not isinstance(other, RoleGroupDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
