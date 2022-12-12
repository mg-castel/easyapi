# easyapi.RoleApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**roles_format_get**](RoleApi.md#roles_format_get) | **GET** /roles.{format} | List of Roles
[**roles_id_format_get**](RoleApi.md#roles_id_format_get) | **GET** /roles/{id}.{format} | Get Role


# **roles_format_get**
> roles_format_get(format, easy_query_q=easy_query_q, set_filter=set_filter, limit=limit, offset=offset)

List of Roles

For filtering send parameter `set_filter=1` and specify filters

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.RoleApi()
format = NULL # object | specify format of response
easy_query_q = NULL # object | free-text filter of current entity (optional)
set_filter = NULL # object | enable filter through Easy Query (optional)
limit = NULL # object | the number of items to be present in the response (default is 25, maximum is 100) (optional)
offset = NULL # object | the offset of the first object to retrieve (optional)

try:
    # List of Roles
    api_instance.roles_format_get(format, easy_query_q=easy_query_q, set_filter=set_filter, limit=limit, offset=offset)
except ApiException as e:
    print("Exception when calling RoleApi->roles_format_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **easy_query_q** | [**object**](.md)| free-text filter of current entity | [optional] 
 **set_filter** | [**object**](.md)| enable filter through Easy Query | [optional] 
 **limit** | [**object**](.md)| the number of items to be present in the response (default is 25, maximum is 100) | [optional] 
 **offset** | [**object**](.md)| the offset of the first object to retrieve | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_id_format_get**
> roles_id_format_get(id, format)

Get Role

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.RoleApi()
id = NULL # object | ID of Role
format = NULL # object | specify format of response

try:
    # Get Role
    api_instance.roles_id_format_get(id, format)
except ApiException as e:
    print("Exception when calling RoleApi->roles_id_format_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID of Role | 
 **format** | [**object**](.md)| specify format of response | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

