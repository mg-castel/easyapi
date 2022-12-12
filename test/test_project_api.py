# coding: utf-8

"""
    Easy Redmine API

    https://app.swaggerhub.com/apis/easysoftware/EasySwagger  # noqa: E501

    OpenAPI spec version: 3.1.11
    Contact: support@easyredmine.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import easyapi
from easyapi.api.project_api import ProjectApi  # noqa: E501
from easyapi.rest import ApiException


class TestProjectApi(unittest.TestCase):
    """ProjectApi unit test stubs"""

    def setUp(self):
        self.api = easyapi.api.project_api.ProjectApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_projects_format_get(self):
        """Test case for projects_format_get

        List of Projects  # noqa: E501
        """
        pass

    def test_projects_format_post(self):
        """Test case for projects_format_post

        Create Project  # noqa: E501
        """
        pass

    def test_projects_id_archive_format_post(self):
        """Test case for projects_id_archive_format_post

        Archive Project  # noqa: E501
        """
        pass

    def test_projects_id_close_format_post(self):
        """Test case for projects_id_close_format_post

        Close Project  # noqa: E501
        """
        pass

    def test_projects_id_format_delete(self):
        """Test case for projects_id_format_delete

        Destroy Project  # noqa: E501
        """
        pass

    def test_projects_id_format_get(self):
        """Test case for projects_id_format_get

        Get Project  # noqa: E501
        """
        pass

    def test_projects_id_format_put(self):
        """Test case for projects_id_format_put

        Update Project  # noqa: E501
        """
        pass

    def test_projects_id_reopen_format_post(self):
        """Test case for projects_id_reopen_format_post

        Reopen Project  # noqa: E501
        """
        pass

    def test_projects_id_unarchive_format_post(self):
        """Test case for projects_id_unarchive_format_post

        Unarchive Project  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
