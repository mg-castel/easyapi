# easyapi.GroupApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groups_format_get**](GroupApi.md#groups_format_get) | **GET** /groups.{format} | List of Groups
[**groups_format_post**](GroupApi.md#groups_format_post) | **POST** /groups.{format} | Create Group
[**groups_id_format_delete**](GroupApi.md#groups_id_format_delete) | **DELETE** /groups/{id}.{format} | Destroy Group
[**groups_id_format_get**](GroupApi.md#groups_id_format_get) | **GET** /groups/{id}.{format} | Get Group
[**groups_id_format_put**](GroupApi.md#groups_id_format_put) | **PUT** /groups/{id}.{format} | Update Group
[**groups_id_users_format_post**](GroupApi.md#groups_id_users_format_post) | **POST** /groups/{id}/users.{format} | Add User to Group
[**groups_id_users_user_id_format_delete**](GroupApi.md#groups_id_users_user_id_format_delete) | **DELETE** /groups/{id}/users/{user_id}.{format} | Remove User from Group


# **groups_format_get**
> groups_format_get(format, easy_query_q=easy_query_q, set_filter=set_filter, limit=limit, offset=offset, include=include)

List of Groups

For filtering send parameter `set_filter=1` and specify filters

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.GroupApi()
format = NULL # object | specify format of response
easy_query_q = NULL # object | free-text filter of current entity (optional)
set_filter = NULL # object | enable filter through Easy Query (optional)
limit = NULL # object | the number of items to be present in the response (default is 25, maximum is 100) (optional)
offset = NULL # object | the offset of the first object to retrieve (optional)
include = NULL # object | explicitly specify the associations you want to be included in the query result  * **users** (users which are in group) * **memberships** (list of projects which is user in role) (optional)

try:
    # List of Groups
    api_instance.groups_format_get(format, easy_query_q=easy_query_q, set_filter=set_filter, limit=limit, offset=offset, include=include)
except ApiException as e:
    print("Exception when calling GroupApi->groups_format_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **easy_query_q** | [**object**](.md)| free-text filter of current entity | [optional] 
 **set_filter** | [**object**](.md)| enable filter through Easy Query | [optional] 
 **limit** | [**object**](.md)| the number of items to be present in the response (default is 25, maximum is 100) | [optional] 
 **offset** | [**object**](.md)| the offset of the first object to retrieve | [optional] 
 **include** | [**object**](.md)| explicitly specify the associations you want to be included in the query result  * **users** (users which are in group) * **memberships** (list of projects which is user in role) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_format_post**
> groups_format_post(format)

Create Group

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.GroupApi()
format = NULL # object | specify format of response

try:
    # Create Group
    api_instance.groups_format_post(format)
except ApiException as e:
    print("Exception when calling GroupApi->groups_format_post: %s\n" % e)
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

# **groups_id_format_delete**
> groups_id_format_delete(format, id)

Destroy Group

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.GroupApi()
format = NULL # object | specify format of response
id = NULL # object | ID of Group

try:
    # Destroy Group
    api_instance.groups_id_format_delete(format, id)
except ApiException as e:
    print("Exception when calling GroupApi->groups_id_format_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **id** | [**object**](.md)| ID of Group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_id_format_get**
> groups_id_format_get(id, format, include=include)

Get Group

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.GroupApi()
id = NULL # object | ID of Group
format = NULL # object | specify format of response
include = NULL # object | explicitly specify the associations you want to be included in the query result  * **users** (users which are in group) * **memberships** (list of projects which is user in role) (optional)

try:
    # Get Group
    api_instance.groups_id_format_get(id, format, include=include)
except ApiException as e:
    print("Exception when calling GroupApi->groups_id_format_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID of Group | 
 **format** | [**object**](.md)| specify format of response | 
 **include** | [**object**](.md)| explicitly specify the associations you want to be included in the query result  * **users** (users which are in group) * **memberships** (list of projects which is user in role) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_id_format_put**
> groups_id_format_put(format, id)

Update Group

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.GroupApi()
format = NULL # object | specify format of response
id = NULL # object | ID of Group

try:
    # Update Group
    api_instance.groups_id_format_put(format, id)
except ApiException as e:
    print("Exception when calling GroupApi->groups_id_format_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **id** | [**object**](.md)| ID of Group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_id_users_format_post**
> groups_id_users_format_post(format, id)

Add User to Group

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.GroupApi()
format = NULL # object | specify format of response
id = NULL # object | ID of Group

try:
    # Add User to Group
    api_instance.groups_id_users_format_post(format, id)
except ApiException as e:
    print("Exception when calling GroupApi->groups_id_users_format_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **id** | [**object**](.md)| ID of Group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_id_users_user_id_format_delete**
> groups_id_users_user_id_format_delete(format, id, user_id)

Remove User from Group

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.GroupApi()
format = NULL # object | specify format of response
id = NULL # object | ID of Group
user_id = NULL # object | ID of User

try:
    # Remove User from Group
    api_instance.groups_id_users_user_id_format_delete(format, id, user_id)
except ApiException as e:
    print("Exception when calling GroupApi->groups_id_users_user_id_format_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **id** | [**object**](.md)| ID of Group | 
 **user_id** | [**object**](.md)| ID of User | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

