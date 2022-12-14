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


class IssueApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def issues_format_get(self, format, **kwargs):  # noqa: E501
        """List of Issues  # noqa: E501

        For filtering send parameter `set_filter=1` and specify filters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.issues_format_get(format, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object format: specify format of response (required)
        :param object easy_query_q: free-text filter of current entity
        :param object set_filter: enable filter through Easy Query
        :param object limit: the number of items to be present in the response (default is 25, maximum is 100)
        :param object offset: the offset of the first object to retrieve
        :param object include: explicitly specify the associations you want to be included in the query result  * **children** (list of issue children) * **attachments** () * **relations** () * **changesets** () * **journals** () * **watchers** ()
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.issues_format_get_with_http_info(format, **kwargs)  # noqa: E501
        else:
            (data) = self.issues_format_get_with_http_info(format, **kwargs)  # noqa: E501
            return data

    def issues_format_get_with_http_info(self, format, **kwargs):  # noqa: E501
        """List of Issues  # noqa: E501

        For filtering send parameter `set_filter=1` and specify filters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.issues_format_get_with_http_info(format, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object format: specify format of response (required)
        :param object easy_query_q: free-text filter of current entity
        :param object set_filter: enable filter through Easy Query
        :param object limit: the number of items to be present in the response (default is 25, maximum is 100)
        :param object offset: the offset of the first object to retrieve
        :param object include: explicitly specify the associations you want to be included in the query result  * **children** (list of issue children) * **attachments** () * **relations** () * **changesets** () * **journals** () * **watchers** ()
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['format', 'easy_query_q', 'set_filter', 'limit', 'offset', 'include']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method issues_format_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'format' is set
        if self.api_client.client_side_validation and ('format' not in params or
                                                       params['format'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `format` when calling `issues_format_get`")  # noqa: E501

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
        if 'include' in params:
            query_params.append(('include', params['include']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/issues.{format}', 'GET',
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

    def issues_format_post(self, format, **kwargs):  # noqa: E501
        """Create Issue  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.issues_format_post(format, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object format: specify format of response (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.issues_format_post_with_http_info(format, **kwargs)  # noqa: E501
        else:
            (data) = self.issues_format_post_with_http_info(format, **kwargs)  # noqa: E501
            return data

    def issues_format_post_with_http_info(self, format, **kwargs):  # noqa: E501
        """Create Issue  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.issues_format_post_with_http_info(format, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object format: specify format of response (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method issues_format_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'format' is set
        if self.api_client.client_side_validation and ('format' not in params or
                                                       params['format'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `format` when calling `issues_format_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            '/issues.{format}', 'POST',
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

    def issues_id_format_delete(self, format, id, **kwargs):  # noqa: E501
        """Destroy Issue  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.issues_id_format_delete(format, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object format: specify format of response (required)
        :param object id: ID of Issue (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.issues_id_format_delete_with_http_info(format, id, **kwargs)  # noqa: E501
        else:
            (data) = self.issues_id_format_delete_with_http_info(format, id, **kwargs)  # noqa: E501
            return data

    def issues_id_format_delete_with_http_info(self, format, id, **kwargs):  # noqa: E501
        """Destroy Issue  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.issues_id_format_delete_with_http_info(format, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object format: specify format of response (required)
        :param object id: ID of Issue (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['format', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method issues_id_format_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'format' is set
        if self.api_client.client_side_validation and ('format' not in params or
                                                       params['format'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `format` when calling `issues_id_format_delete`")  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `issues_id_format_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'format' in params:
            path_params['format'] = params['format']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/issues/{id}.{format}', 'DELETE',
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

    def issues_id_format_get(self, id, format, **kwargs):  # noqa: E501
        """Get Issue  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.issues_id_format_get(id, format, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object id: ID of Issue (required)
        :param object format: specify format of response (required)
        :param object include: explicitly specify the associations you want to be included in the query result  * **children** (list of issue children) * **attachments** () * **relations** () * **changesets** () * **journals** () * **watchers** ()
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.issues_id_format_get_with_http_info(id, format, **kwargs)  # noqa: E501
        else:
            (data) = self.issues_id_format_get_with_http_info(id, format, **kwargs)  # noqa: E501
            return data

    def issues_id_format_get_with_http_info(self, id, format, **kwargs):  # noqa: E501
        """Get Issue  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.issues_id_format_get_with_http_info(id, format, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object id: ID of Issue (required)
        :param object format: specify format of response (required)
        :param object include: explicitly specify the associations you want to be included in the query result  * **children** (list of issue children) * **attachments** () * **relations** () * **changesets** () * **journals** () * **watchers** ()
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'format', 'include']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method issues_id_format_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `issues_id_format_get`")  # noqa: E501
        # verify the required parameter 'format' is set
        if self.api_client.client_side_validation and ('format' not in params or
                                                       params['format'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `format` when calling `issues_id_format_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'format' in params:
            path_params['format'] = params['format']  # noqa: E501

        query_params = []
        if 'include' in params:
            query_params.append(('include', params['include']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/issues/{id}.{format}', 'GET',
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

    def issues_id_format_put(self, format, id, **kwargs):  # noqa: E501
        """Update Issue  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.issues_id_format_put(format, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object format: specify format of response (required)
        :param object id: ID of Issue (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.issues_id_format_put_with_http_info(format, id, **kwargs)  # noqa: E501
        else:
            (data) = self.issues_id_format_put_with_http_info(format, id, **kwargs)  # noqa: E501
            return data

    def issues_id_format_put_with_http_info(self, format, id, **kwargs):  # noqa: E501
        """Update Issue  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.issues_id_format_put_with_http_info(format, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object format: specify format of response (required)
        :param object id: ID of Issue (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['format', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method issues_id_format_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'format' is set
        if self.api_client.client_side_validation and ('format' not in params or
                                                       params['format'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `format` when calling `issues_id_format_put`")  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `issues_id_format_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'format' in params:
            path_params['format'] = params['format']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/issues/{id}.{format}', 'PUT',
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
