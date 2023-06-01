# coding: utf-8

"""
    Skill Repository

    The API description of the Skill Repository.  # noqa: E501

    OpenAPI spec version: 0.4.13
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SkillRepositorySearchDto(object):
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
        'page_size': 'float',
        'page': 'float',
        'name': 'str',
        'version': 'str',
        'owner': 'str'
    }

    attribute_map = {
        'page_size': 'pageSize',
        'page': 'page',
        'name': 'name',
        'version': 'version',
        'owner': 'owner'
    }

    def __init__(self, page_size=None, page=None, name=None, version=None, owner=None):  # noqa: E501
        """SkillRepositorySearchDto - a model defined in Swagger"""  # noqa: E501
        self._page_size = None
        self._page = None
        self._name = None
        self._version = None
        self._owner = None
        self.discriminator = None
        if page_size is not None:
            self.page_size = page_size
        if page is not None:
            self.page = page
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if owner is not None:
            self.owner = owner

    @property
    def page_size(self):
        """Gets the page_size of this SkillRepositorySearchDto.  # noqa: E501


        :return: The page_size of this SkillRepositorySearchDto.  # noqa: E501
        :rtype: float
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this SkillRepositorySearchDto.


        :param page_size: The page_size of this SkillRepositorySearchDto.  # noqa: E501
        :type: float
        """

        self._page_size = page_size

    @property
    def page(self):
        """Gets the page of this SkillRepositorySearchDto.  # noqa: E501


        :return: The page of this SkillRepositorySearchDto.  # noqa: E501
        :rtype: float
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this SkillRepositorySearchDto.


        :param page: The page of this SkillRepositorySearchDto.  # noqa: E501
        :type: float
        """

        self._page = page

    @property
    def name(self):
        """Gets the name of this SkillRepositorySearchDto.  # noqa: E501


        :return: The name of this SkillRepositorySearchDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SkillRepositorySearchDto.


        :param name: The name of this SkillRepositorySearchDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def version(self):
        """Gets the version of this SkillRepositorySearchDto.  # noqa: E501


        :return: The version of this SkillRepositorySearchDto.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SkillRepositorySearchDto.


        :param version: The version of this SkillRepositorySearchDto.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def owner(self):
        """Gets the owner of this SkillRepositorySearchDto.  # noqa: E501


        :return: The owner of this SkillRepositorySearchDto.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this SkillRepositorySearchDto.


        :param owner: The owner of this SkillRepositorySearchDto.  # noqa: E501
        :type: str
        """

        self._owner = owner

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
        if issubclass(SkillRepositorySearchDto, dict):
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
        if not isinstance(other, SkillRepositorySearchDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other