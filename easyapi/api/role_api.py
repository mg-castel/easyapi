# coding: utf-8

"""
    Easy Redmine API

    https://app.swaggerhub.com/apis/easysoftware/EasySwagger  # noqa: E501

    OpenAPI spec version: 3.1.11
    Contact: support@easyredmine.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from easyapi.api_client import ApiClient


class RoleApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def roles_format_get(self, format, **kwargs):  # noqa: E501
        """List of Roles  # noqa: E501

        For filtering send parameter `set_filter=1` and specify filters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.roles_format_get(format, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object format: specify format of response (required)
        :param object easy_query_q: free-text filter of current entity
        :param object set_filter: enable filter through Easy Query
        :param object limit: the number of items to be present in the response (default is 25, maximum is 100)
        :param object offset: the offset of the first object to retrieve
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.roles_format_get_with_http_info(format, **kwargs)  # noqa: E501
        else:
            (data) = self.roles_format_get_with_http_info(format, **kwargs)  # noqa: E501
            return data

    def roles_format_get_with_http_info(self, format, **kwargs):  # noqa: E501
        """List of Roles  # noqa: E501

        For filtering send parameter `set_filter=1` and specify filters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.roles_format_get_with_http_info(format, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object format: specify format of response (required)
        :param object easy_query_q: free-text filter of current entity
        :param object set_filter: enable filter through Easy Query
        :param object limit: the number of items to be present in the response (default is 25, maximum is 100)
        :param object offset: the offset of the first object to retrieve
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['format', 'easy_query_q', 'set_filter', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method roles_format_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'format' is set
        if self.api_client.client_side_validation and ('format' not in params or
                                                       params['format'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `format` when calling `roles_format_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'format' in params:
            path_params['format'] = params['format']  # noqa: E501

        query_params = []
        if 'easy_query_q' in params:
            query_params.append(('easy_query_q', params['easy_query_q']))  # noqa: E501
        if 'set_filter' in params:
            query_params.append(('set_filter', params['set_filter']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/roles.{format}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def roles_id_format_get(self, id, format, **kwargs):  # noqa: E501
        """Get Role  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.roles_id_format_get(id, format, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object id: ID of Role (required)
        :param object format: specify format of response (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.roles_id_format_get_with_http_info(id, format, **kwargs)  # noqa: E501
        else:
            (data) = self.roles_id_format_get_with_http_info(id, format, **kwargs)  # noqa: E501
            return data

    def roles_id_format_get_with_http_info(self, id, format, **kwargs):  # noqa: E501
        """Get Role  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.roles_id_format_get_with_http_info(id, format, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object id: ID of Role (required)
        :param object format: specify format of response (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method roles_id_format_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `roles_id_format_get`")  # noqa: E501
        # verify the required parameter 'format' is set
        if self.api_client.client_side_validation and ('format' not in params or
                                                       params['format'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `format` when calling `roles_id_format_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'format' in params:
            path_params['format'] = params['format']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/roles/{id}.{format}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
