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

class SkillProfileCreationDto(object):
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
        'job_history': 'str',
        'professional_interests': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'job_history': 'jobHistory',
        'professional_interests': 'professionalInterests',
        'user_id': 'userId'
    }

    def __init__(self, job_history=None, professional_interests=None, user_id=None):  # noqa: E501
        """SkillProfileCreationDto - a model defined in Swagger"""  # noqa: E501
        self._job_history = None
        self._professional_interests = None
        self._user_id = None
        self.discriminator = None
        if job_history is not None:
            self.job_history = job_history
        if professional_interests is not None:
            self.professional_interests = professional_interests
        self.user_id = user_id

    @property
    def job_history(self):
        """Gets the job_history of this SkillProfileCreationDto.  # noqa: E501

        Used to validate that the user is the owner of the target repository.  # noqa: E501

        :return: The job_history of this SkillProfileCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._job_history

    @job_history.setter
    def job_history(self, job_history):
        """Sets the job_history of this SkillProfileCreationDto.

        Used to validate that the user is the owner of the target repository.  # noqa: E501

        :param job_history: The job_history of this SkillProfileCreationDto.  # noqa: E501
        :type: str
        """

        self._job_history = job_history

    @property
    def professional_interests(self):
        """Gets the professional_interests of this SkillProfileCreationDto.  # noqa: E501


        :return: The professional_interests of this SkillProfileCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._professional_interests

    @professional_interests.setter
    def professional_interests(self, professional_interests):
        """Sets the professional_interests of this SkillProfileCreationDto.


        :param professional_interests: The professional_interests of this SkillProfileCreationDto.  # noqa: E501
        :type: str
        """

        self._professional_interests = professional_interests

    @property
    def user_id(self):
        """Gets the user_id of this SkillProfileCreationDto.  # noqa: E501


        :return: The user_id of this SkillProfileCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this SkillProfileCreationDto.


        :param user_id: The user_id of this SkillProfileCreationDto.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

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
        if issubclass(SkillProfileCreationDto, dict):
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
        if not isinstance(other, SkillProfileCreationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
