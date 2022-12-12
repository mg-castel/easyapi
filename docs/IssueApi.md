# easyapi.IssueApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**issues_format_get**](IssueApi.md#issues_format_get) | **GET** /issues.{format} | List of Issues
[**issues_format_post**](IssueApi.md#issues_format_post) | **POST** /issues.{format} | Create Issue
[**issues_id_format_delete**](IssueApi.md#issues_id_format_delete) | **DELETE** /issues/{id}.{format} | Destroy Issue
[**issues_id_format_get**](IssueApi.md#issues_id_format_get) | **GET** /issues/{id}.{format} | Get Issue
[**issues_id_format_put**](IssueApi.md#issues_id_format_put) | **PUT** /issues/{id}.{format} | Update Issue


# **issues_format_get**
> issues_format_get(format, easy_query_q=easy_query_q, set_filter=set_filter, limit=limit, offset=offset, include=include)

List of Issues

For filtering send parameter `set_filter=1` and specify filters

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.IssueApi()
format = NULL # object | specify format of response
easy_query_q = NULL # object | free-text filter of current entity (optional)
set_filter = NULL # object | enable filter through Easy Query (optional)
limit = NULL # object | the number of items to be present in the response (default is 25, maximum is 100) (optional)
offset = NULL # object | the offset of the first object to retrieve (optional)
include = NULL # object | explicitly specify the associations you want to be included in the query result  * **children** (list of issue children) * **attachments** () * **relations** () * **changesets** () * **journals** () * **watchers** () (optional)

try:
    # List of Issues
    api_instance.issues_format_get(format, easy_query_q=easy_query_q, set_filter=set_filter, limit=limit, offset=offset, include=include)
except ApiException as e:
    print("Exception when calling IssueApi->issues_format_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **easy_query_q** | [**object**](.md)| free-text filter of current entity | [optional] 
 **set_filter** | [**object**](.md)| enable filter through Easy Query | [optional] 
 **limit** | [**object**](.md)| the number of items to be present in the response (default is 25, maximum is 100) | [optional] 
 **offset** | [**object**](.md)| the offset of the first object to retrieve | [optional] 
 **include** | [**object**](.md)| explicitly specify the associations you want to be included in the query result  * **children** (list of issue children) * **attachments** () * **relations** () * **changesets** () * **journals** () * **watchers** () | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issues_format_post**
> issues_format_post(format)

Create Issue

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.IssueApi()
format = NULL # object | specify format of response

try:
    # Create Issue
    api_instance.issues_format_post(format)
except ApiException as e:
    print("Exception when calling IssueApi->issues_format_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issues_id_format_delete**
> issues_id_format_delete(format, id)

Destroy Issue

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.IssueApi()
format = NULL # object | specify format of response
id = NULL # object | ID of Issue

try:
    # Destroy Issue
    api_instance.issues_id_format_delete(format, id)
except ApiException as e:
    print("Exception when calling IssueApi->issues_id_format_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **id** | [**object**](.md)| ID of Issue | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issues_id_format_get**
> issues_id_format_get(id, format, include=include)

Get Issue

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.IssueApi()
id = NULL # object | ID of Issue
format = NULL # object | specify format of response
include = NULL # object | explicitly specify the associations you want to be included in the query result  * **children** (list of issue children) * **attachments** () * **relations** () * **changesets** () * **journals** () * **watchers** () (optional)

try:
    # Get Issue
    api_instance.issues_id_format_get(id, format, include=include)
except ApiException as e:
    print("Exception when calling IssueApi->issues_id_format_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID of Issue | 
 **format** | [**object**](.md)| specify format of response | 
 **include** | [**object**](.md)| explicitly specify the associations you want to be included in the query result  * **children** (list of issue children) * **attachments** () * **relations** () * **changesets** () * **journals** () * **watchers** () | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issues_id_format_put**
> issues_id_format_put(format, id)

Update Issue

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.IssueApi()
format = NULL # object | specify format of response
id = NULL # object | ID of Issue

try:
    # Update Issue
    api_instance.issues_id_format_put(format, id)
except ApiException as e:
    print("Exception when calling IssueApi->issues_id_format_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **id** | [**object**](.md)| ID of Issue | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

