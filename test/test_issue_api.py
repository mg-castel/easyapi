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
from easyapi.api.issue_api import IssueApi  # noqa: E501
from easyapi.rest import ApiException


class TestIssueApi(unittest.TestCase):
    """IssueApi unit test stubs"""

    def setUp(self):
        self.api = easyapi.api.issue_api.IssueApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_issues_format_get(self):
        """Test case for issues_format_get

        List of Issues  # noqa: E501
        """
        pass

    def test_issues_format_post(self):
        """Test case for issues_format_post

        Create Issue  # noqa: E501
        """
        pass

    def test_issues_id_format_delete(self):
        """Test case for issues_id_format_delete

        Destroy Issue  # noqa: E501
        """
        pass

    def test_issues_id_format_get(self):
        """Test case for issues_id_format_get

        Get Issue  # noqa: E501
        """
        pass

    def test_issues_id_format_put(self):
        """Test case for issues_id_format_put

        Update Issue  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
