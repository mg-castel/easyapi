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
from easyapi.api.easy_attendance_api import EasyAttendanceApi  # noqa: E501
from easyapi.rest import ApiException


class TestEasyAttendanceApi(unittest.TestCase):
    """EasyAttendanceApi unit test stubs"""

    def setUp(self):
        self.api = easyapi.api.easy_attendance_api.EasyAttendanceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_easy_attendances_format_get(self):
        """Test case for easy_attendances_format_get

        List of EasyAttendances  # noqa: E501
        """
        pass

    def test_easy_attendances_format_post(self):
        """Test case for easy_attendances_format_post

        Create EasyAttendance  # noqa: E501
        """
        pass

    def test_easy_attendances_id_format_delete(self):
        """Test case for easy_attendances_id_format_delete

        Destroy EasyAttendance  # noqa: E501
        """
        pass

    def test_easy_attendances_id_format_get(self):
        """Test case for easy_attendances_id_format_get

        Get EasyAttendance  # noqa: E501
        """
        pass

    def test_easy_attendances_id_format_put(self):
        """Test case for easy_attendances_id_format_put

        Update EasyAttendance  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
