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
from easyapi.api.time_entry_api import TimeEntryApi  # noqa: E501
from easyapi.rest import ApiException


class TestTimeEntryApi(unittest.TestCase):
    """TimeEntryApi unit test stubs"""

    def setUp(self):
        self.api = easyapi.api.time_entry_api.TimeEntryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_time_entries_format_get(self):
        """Test case for time_entries_format_get

        List of TimeEntries  # noqa: E501
        """
        pass

    def test_time_entries_format_post(self):
        """Test case for time_entries_format_post

        Create TimeEntry  # noqa: E501
        """
        pass

    def test_time_entries_id_format_delete(self):
        """Test case for time_entries_id_format_delete

        Destroy TimeEntry  # noqa: E501
        """
        pass

    def test_time_entries_id_format_get(self):
        """Test case for time_entries_id_format_get

        Get TimeEntry  # noqa: E501
        """
        pass

    def test_time_entries_id_format_put(self):
        """Test case for time_entries_id_format_put

        Update TimeEntry  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
