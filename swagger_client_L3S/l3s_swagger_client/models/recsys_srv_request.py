# coding: utf-8

"""
    L3S Gateway for SEARCH

    Welcome to the Swagger UI documentation site!  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RecsysSrvRequest(object):
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
        'uid': 'str',
        'cid': 'str',
        'catetory': 'str'
    }

    attribute_map = {
        'uid': 'uid',
        'cid': 'cid',
        'catetory': 'catetory'
    }

    def __init__(self, uid=None, cid=None, catetory=None):  # noqa: E501
        """RecsysSrvRequest - a model defined in Swagger"""  # noqa: E501
        self._uid = None
        self._cid = None
        self._catetory = None
        self.discriminator = None
        if uid is not None:
            self.uid = uid
        if cid is not None:
            self.cid = cid
        if catetory is not None:
            self.catetory = catetory

    @property
    def uid(self):
        """Gets the uid of this RecsysSrvRequest.  # noqa: E501

        user ID  # noqa: E501

        :return: The uid of this RecsysSrvRequest.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this RecsysSrvRequest.

        user ID  # noqa: E501

        :param uid: The uid of this RecsysSrvRequest.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def cid(self):
        """Gets the cid of this RecsysSrvRequest.  # noqa: E501

        company ID  # noqa: E501

        :return: The cid of this RecsysSrvRequest.  # noqa: E501
        :rtype: str
        """
        return self._cid

    @cid.setter
    def cid(self, cid):
        """Sets the cid of this RecsysSrvRequest.

        company ID  # noqa: E501

        :param cid: The cid of this RecsysSrvRequest.  # noqa: E501
        :type: str
        """

        self._cid = cid

    @property
    def catetory(self):
        """Gets the catetory of this RecsysSrvRequest.  # noqa: E501

        recsys category  # noqa: E501

        :return: The catetory of this RecsysSrvRequest.  # noqa: E501
        :rtype: str
        """
        return self._catetory

    @catetory.setter
    def catetory(self, catetory):
        """Sets the catetory of this RecsysSrvRequest.

        recsys category  # noqa: E501

        :param catetory: The catetory of this RecsysSrvRequest.  # noqa: E501
        :type: str
        """

        self._catetory = catetory

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
        if issubclass(RecsysSrvRequest, dict):
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
        if not isinstance(other, RecsysSrvRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other