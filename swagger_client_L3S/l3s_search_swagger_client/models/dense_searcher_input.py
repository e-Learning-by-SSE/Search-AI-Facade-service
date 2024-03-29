# coding: utf-8

"""
    L3S Search Service for SEARCH

    Welcome to the Swagger UI documentation site test!  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DenseSearcherInput(object):
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
        'query': 'str',
        'language_model': 'str',
        'index_method': 'str',
        'dataset_name': 'str',
        'nr_result': 'int'
    }

    attribute_map = {
        'uid': 'uid',
        'cid': 'cid',
        'query': 'query',
        'language_model': 'language_model',
        'index_method': 'index_method',
        'dataset_name': 'dataset_name',
        'nr_result': 'nr_result'
    }

    def __init__(self, uid=None, cid=None, query='Elektrotechnik 1 Versuch 8: Wirkleistung von Wechselspannungen; Wirkleistung der Sinuswechselspannung in der praktischen Übung', language_model='bert-base-german-cased', index_method='flat-l2', dataset_name='mls-tasks', nr_result=None):  # noqa: E501
        """DenseSearcherInput - a model defined in Swagger"""  # noqa: E501
        self._uid = None
        self._cid = None
        self._query = None
        self._language_model = None
        self._index_method = None
        self._dataset_name = None
        self._nr_result = None
        self.discriminator = None
        if uid is not None:
            self.uid = uid
        if cid is not None:
            self.cid = cid
        self.query = query
        if language_model is not None:
            self.language_model = language_model
        if index_method is not None:
            self.index_method = index_method
        if dataset_name is not None:
            self.dataset_name = dataset_name
        if nr_result is not None:
            self.nr_result = nr_result

    @property
    def uid(self):
        """Gets the uid of this DenseSearcherInput.  # noqa: E501

        user ID  # noqa: E501

        :return: The uid of this DenseSearcherInput.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this DenseSearcherInput.

        user ID  # noqa: E501

        :param uid: The uid of this DenseSearcherInput.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def cid(self):
        """Gets the cid of this DenseSearcherInput.  # noqa: E501

        company ID  # noqa: E501

        :return: The cid of this DenseSearcherInput.  # noqa: E501
        :rtype: str
        """
        return self._cid

    @cid.setter
    def cid(self, cid):
        """Sets the cid of this DenseSearcherInput.

        company ID  # noqa: E501

        :param cid: The cid of this DenseSearcherInput.  # noqa: E501
        :type: str
        """

        self._cid = cid

    @property
    def query(self):
        """Gets the query of this DenseSearcherInput.  # noqa: E501


        :return: The query of this DenseSearcherInput.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this DenseSearcherInput.


        :param query: The query of this DenseSearcherInput.  # noqa: E501
        :type: str
        """
        if query is None:
            raise ValueError("Invalid value for `query`, must not be `None`")  # noqa: E501

        self._query = query

    @property
    def language_model(self):
        """Gets the language_model of this DenseSearcherInput.  # noqa: E501


        :return: The language_model of this DenseSearcherInput.  # noqa: E501
        :rtype: str
        """
        return self._language_model

    @language_model.setter
    def language_model(self, language_model):
        """Sets the language_model of this DenseSearcherInput.


        :param language_model: The language_model of this DenseSearcherInput.  # noqa: E501
        :type: str
        """

        self._language_model = language_model

    @property
    def index_method(self):
        """Gets the index_method of this DenseSearcherInput.  # noqa: E501


        :return: The index_method of this DenseSearcherInput.  # noqa: E501
        :rtype: str
        """
        return self._index_method

    @index_method.setter
    def index_method(self, index_method):
        """Sets the index_method of this DenseSearcherInput.


        :param index_method: The index_method of this DenseSearcherInput.  # noqa: E501
        :type: str
        """

        self._index_method = index_method

    @property
    def dataset_name(self):
        """Gets the dataset_name of this DenseSearcherInput.  # noqa: E501


        :return: The dataset_name of this DenseSearcherInput.  # noqa: E501
        :rtype: str
        """
        return self._dataset_name

    @dataset_name.setter
    def dataset_name(self, dataset_name):
        """Sets the dataset_name of this DenseSearcherInput.


        :param dataset_name: The dataset_name of this DenseSearcherInput.  # noqa: E501
        :type: str
        """

        self._dataset_name = dataset_name

    @property
    def nr_result(self):
        """Gets the nr_result of this DenseSearcherInput.  # noqa: E501


        :return: The nr_result of this DenseSearcherInput.  # noqa: E501
        :rtype: int
        """
        return self._nr_result

    @nr_result.setter
    def nr_result(self, nr_result):
        """Sets the nr_result of this DenseSearcherInput.


        :param nr_result: The nr_result of this DenseSearcherInput.  # noqa: E501
        :type: int
        """

        self._nr_result = nr_result

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
        if issubclass(DenseSearcherInput, dict):
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
        if not isinstance(other, DenseSearcherInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
