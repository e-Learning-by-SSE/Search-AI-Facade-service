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

class SearchLearningUnitCreationDto(object):
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
        'processing_time': 'str',
        'rating': 'str',
        'content_creator': 'str',
        'content_provider': 'str',
        'target_audience': 'str',
        'semantic_density': 'str',
        'semantic_gravity': 'str',
        'content_tags': 'list[str]',
        'context_tags': 'list[str]',
        'link_to_help_material': 'str',
        'title': 'str',
        'resource': 'str',
        'language': 'str',
        'description': 'str',
        'teaching_goals': 'list[str]',
        'required_skills': 'list[str]'
    }

    attribute_map = {
        'processing_time': 'processingTime',
        'rating': 'rating',
        'content_creator': 'contentCreator',
        'content_provider': 'contentProvider',
        'target_audience': 'targetAudience',
        'semantic_density': 'semanticDensity',
        'semantic_gravity': 'semanticGravity',
        'content_tags': 'contentTags',
        'context_tags': 'contextTags',
        'link_to_help_material': 'linkToHelpMaterial',
        'title': 'title',
        'resource': 'resource',
        'language': 'language',
        'description': 'description',
        'teaching_goals': 'teachingGoals',
        'required_skills': 'requiredSkills'
    }

    def __init__(self, processing_time=None, rating=None, content_creator=None, content_provider=None, target_audience=None, semantic_density=None, semantic_gravity=None, content_tags=None, context_tags=None, link_to_help_material=None, title=None, resource=None, language=None, description=None, teaching_goals=None, required_skills=None):  # noqa: E501
        """SearchLearningUnitCreationDto - a model defined in Swagger"""  # noqa: E501
        self._processing_time = None
        self._rating = None
        self._content_creator = None
        self._content_provider = None
        self._target_audience = None
        self._semantic_density = None
        self._semantic_gravity = None
        self._content_tags = None
        self._context_tags = None
        self._link_to_help_material = None
        self._title = None
        self._resource = None
        self._language = None
        self._description = None
        self._teaching_goals = None
        self._required_skills = None
        self.discriminator = None
        if processing_time is not None:
            self.processing_time = processing_time
        if rating is not None:
            self.rating = rating
        if content_creator is not None:
            self.content_creator = content_creator
        if content_provider is not None:
            self.content_provider = content_provider
        if target_audience is not None:
            self.target_audience = target_audience
        if semantic_density is not None:
            self.semantic_density = semantic_density
        if semantic_gravity is not None:
            self.semantic_gravity = semantic_gravity
        if content_tags is not None:
            self.content_tags = content_tags
        if context_tags is not None:
            self.context_tags = context_tags
        if link_to_help_material is not None:
            self.link_to_help_material = link_to_help_material
        self.title = title
        self.resource = resource
        self.language = language
        if description is not None:
            self.description = description
        self.teaching_goals = teaching_goals
        self.required_skills = required_skills

    @property
    def processing_time(self):
        """Gets the processing_time of this SearchLearningUnitCreationDto.  # noqa: E501


        :return: The processing_time of this SearchLearningUnitCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._processing_time

    @processing_time.setter
    def processing_time(self, processing_time):
        """Sets the processing_time of this SearchLearningUnitCreationDto.


        :param processing_time: The processing_time of this SearchLearningUnitCreationDto.  # noqa: E501
        :type: str
        """

        self._processing_time = processing_time

    @property
    def rating(self):
        """Gets the rating of this SearchLearningUnitCreationDto.  # noqa: E501


        :return: The rating of this SearchLearningUnitCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this SearchLearningUnitCreationDto.


        :param rating: The rating of this SearchLearningUnitCreationDto.  # noqa: E501
        :type: str
        """

        self._rating = rating

    @property
    def content_creator(self):
        """Gets the content_creator of this SearchLearningUnitCreationDto.  # noqa: E501


        :return: The content_creator of this SearchLearningUnitCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._content_creator

    @content_creator.setter
    def content_creator(self, content_creator):
        """Sets the content_creator of this SearchLearningUnitCreationDto.


        :param content_creator: The content_creator of this SearchLearningUnitCreationDto.  # noqa: E501
        :type: str
        """

        self._content_creator = content_creator

    @property
    def content_provider(self):
        """Gets the content_provider of this SearchLearningUnitCreationDto.  # noqa: E501


        :return: The content_provider of this SearchLearningUnitCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._content_provider

    @content_provider.setter
    def content_provider(self, content_provider):
        """Sets the content_provider of this SearchLearningUnitCreationDto.


        :param content_provider: The content_provider of this SearchLearningUnitCreationDto.  # noqa: E501
        :type: str
        """

        self._content_provider = content_provider

    @property
    def target_audience(self):
        """Gets the target_audience of this SearchLearningUnitCreationDto.  # noqa: E501


        :return: The target_audience of this SearchLearningUnitCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._target_audience

    @target_audience.setter
    def target_audience(self, target_audience):
        """Sets the target_audience of this SearchLearningUnitCreationDto.


        :param target_audience: The target_audience of this SearchLearningUnitCreationDto.  # noqa: E501
        :type: str
        """

        self._target_audience = target_audience

    @property
    def semantic_density(self):
        """Gets the semantic_density of this SearchLearningUnitCreationDto.  # noqa: E501


        :return: The semantic_density of this SearchLearningUnitCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._semantic_density

    @semantic_density.setter
    def semantic_density(self, semantic_density):
        """Sets the semantic_density of this SearchLearningUnitCreationDto.


        :param semantic_density: The semantic_density of this SearchLearningUnitCreationDto.  # noqa: E501
        :type: str
        """

        self._semantic_density = semantic_density

    @property
    def semantic_gravity(self):
        """Gets the semantic_gravity of this SearchLearningUnitCreationDto.  # noqa: E501


        :return: The semantic_gravity of this SearchLearningUnitCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._semantic_gravity

    @semantic_gravity.setter
    def semantic_gravity(self, semantic_gravity):
        """Sets the semantic_gravity of this SearchLearningUnitCreationDto.


        :param semantic_gravity: The semantic_gravity of this SearchLearningUnitCreationDto.  # noqa: E501
        :type: str
        """

        self._semantic_gravity = semantic_gravity

    @property
    def content_tags(self):
        """Gets the content_tags of this SearchLearningUnitCreationDto.  # noqa: E501


        :return: The content_tags of this SearchLearningUnitCreationDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._content_tags

    @content_tags.setter
    def content_tags(self, content_tags):
        """Sets the content_tags of this SearchLearningUnitCreationDto.


        :param content_tags: The content_tags of this SearchLearningUnitCreationDto.  # noqa: E501
        :type: list[str]
        """

        self._content_tags = content_tags

    @property
    def context_tags(self):
        """Gets the context_tags of this SearchLearningUnitCreationDto.  # noqa: E501


        :return: The context_tags of this SearchLearningUnitCreationDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._context_tags

    @context_tags.setter
    def context_tags(self, context_tags):
        """Sets the context_tags of this SearchLearningUnitCreationDto.


        :param context_tags: The context_tags of this SearchLearningUnitCreationDto.  # noqa: E501
        :type: list[str]
        """

        self._context_tags = context_tags

    @property
    def link_to_help_material(self):
        """Gets the link_to_help_material of this SearchLearningUnitCreationDto.  # noqa: E501


        :return: The link_to_help_material of this SearchLearningUnitCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._link_to_help_material

    @link_to_help_material.setter
    def link_to_help_material(self, link_to_help_material):
        """Sets the link_to_help_material of this SearchLearningUnitCreationDto.


        :param link_to_help_material: The link_to_help_material of this SearchLearningUnitCreationDto.  # noqa: E501
        :type: str
        """

        self._link_to_help_material = link_to_help_material

    @property
    def title(self):
        """Gets the title of this SearchLearningUnitCreationDto.  # noqa: E501


        :return: The title of this SearchLearningUnitCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this SearchLearningUnitCreationDto.


        :param title: The title of this SearchLearningUnitCreationDto.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def resource(self):
        """Gets the resource of this SearchLearningUnitCreationDto.  # noqa: E501

        Should point to a resource (e.g. a website) which contains the learning unit.  # noqa: E501

        :return: The resource of this SearchLearningUnitCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this SearchLearningUnitCreationDto.

        Should point to a resource (e.g. a website) which contains the learning unit.  # noqa: E501

        :param resource: The resource of this SearchLearningUnitCreationDto.  # noqa: E501
        :type: str
        """
        if resource is None:
            raise ValueError("Invalid value for `resource`, must not be `None`")  # noqa: E501

        self._resource = resource

    @property
    def language(self):
        """Gets the language of this SearchLearningUnitCreationDto.  # noqa: E501


        :return: The language of this SearchLearningUnitCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this SearchLearningUnitCreationDto.


        :param language: The language of this SearchLearningUnitCreationDto.  # noqa: E501
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def description(self):
        """Gets the description of this SearchLearningUnitCreationDto.  # noqa: E501


        :return: The description of this SearchLearningUnitCreationDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SearchLearningUnitCreationDto.


        :param description: The description of this SearchLearningUnitCreationDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def teaching_goals(self):
        """Gets the teaching_goals of this SearchLearningUnitCreationDto.  # noqa: E501


        :return: The teaching_goals of this SearchLearningUnitCreationDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._teaching_goals

    @teaching_goals.setter
    def teaching_goals(self, teaching_goals):
        """Sets the teaching_goals of this SearchLearningUnitCreationDto.


        :param teaching_goals: The teaching_goals of this SearchLearningUnitCreationDto.  # noqa: E501
        :type: list[str]
        """
        if teaching_goals is None:
            raise ValueError("Invalid value for `teaching_goals`, must not be `None`")  # noqa: E501

        self._teaching_goals = teaching_goals

    @property
    def required_skills(self):
        """Gets the required_skills of this SearchLearningUnitCreationDto.  # noqa: E501


        :return: The required_skills of this SearchLearningUnitCreationDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._required_skills

    @required_skills.setter
    def required_skills(self, required_skills):
        """Sets the required_skills of this SearchLearningUnitCreationDto.


        :param required_skills: The required_skills of this SearchLearningUnitCreationDto.  # noqa: E501
        :type: list[str]
        """
        if required_skills is None:
            raise ValueError("Invalid value for `required_skills`, must not be `None`")  # noqa: E501

        self._required_skills = required_skills

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
        if issubclass(SearchLearningUnitCreationDto, dict):
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
        if not isinstance(other, SearchLearningUnitCreationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
