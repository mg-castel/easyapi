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
from easyapi.api.group_api import GroupApi  # noqa: E501
from easyapi.rest import ApiException


class TestGroupApi(unittest.TestCase):
    """GroupApi unit test stubs"""

    def setUp(self):
        self.api = easyapi.api.group_api.GroupApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_groups_format_get(self):
        """Test case for groups_format_get

        List of Groups  # noqa: E501
        """
        pass

    def test_groups_format_post(self):
        """Test case for groups_format_post

        Create Group  # noqa: E501
        """
        pass

    def test_groups_id_format_delete(self):
        """Test case for groups_id_format_delete

        Destroy Group  # noqa: E501
        """
        pass

    def test_groups_id_format_get(self):
        """Test case for groups_id_format_get

        Get Group  # noqa: E501
        """
        pass

    def test_groups_id_format_put(self):
        """Test case for groups_id_format_put

        Update Group  # noqa: E501
        """
        pass

    def test_groups_id_users_format_post(self):
        """Test case for groups_id_users_format_post

        Add User to Group  # noqa: E501
        """
        pass

    def test_groups_id_users_user_id_format_delete(self):
        """Test case for groups_id_users_user_id_format_delete

        Remove User from Group  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
