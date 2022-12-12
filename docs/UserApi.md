# easyapi.UserApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_format_get**](UserApi.md#users_format_get) | **GET** /users.{format} | List of Users
[**users_format_post**](UserApi.md#users_format_post) | **POST** /users.{format} | Create User
[**users_id_format_delete**](UserApi.md#users_id_format_delete) | **DELETE** /users/{id}.{format} | Destroy User
[**users_id_format_get**](UserApi.md#users_id_format_get) | **GET** /users/{id}.{format} | Get User
[**users_id_format_put**](UserApi.md#users_id_format_put) | **PUT** /users/{id}.{format} | Update User


# **users_format_get**
> users_format_get(format, easy_query_q=easy_query_q, set_filter=set_filter, limit=limit, offset=offset, include=include)

List of Users

For filtering send parameter `set_filter=1` and specify filters

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.UserApi()
format = NULL # object | specify format of response
easy_query_q = NULL # object | free-text filter of current entity (optional)
set_filter = NULL # object | enable filter through Easy Query (optional)
limit = NULL # object | the number of items to be present in the response (default is 25, maximum is 100) (optional)
offset = NULL # object | the offset of the first object to retrieve (optional)
include = NULL # object | explicitly specify the associations you want to be included in the query result  * **groups** (groups which user is in) * **memberships** (list of projects which is user in role) (optional)

try:
    # List of Users
    api_instance.users_format_get(format, easy_query_q=easy_query_q, set_filter=set_filter, limit=limit, offset=offset, include=include)
except ApiException as e:
    print("Exception when calling UserApi->users_format_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **easy_query_q** | [**object**](.md)| free-text filter of current entity | [optional] 
 **set_filter** | [**object**](.md)| enable filter through Easy Query | [optional] 
 **limit** | [**object**](.md)| the number of items to be present in the response (default is 25, maximum is 100) | [optional] 
 **offset** | [**object**](.md)| the offset of the first object to retrieve | [optional] 
 **include** | [**object**](.md)| explicitly specify the associations you want to be included in the query result  * **groups** (groups which user is in) * **memberships** (list of projects which is user in role) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_format_post**
> users_format_post(format)

Create User

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.UserApi()
format = NULL # object | specify format of response

try:
    # Create User
    api_instance.users_format_post(format)
except ApiException as e:
    print("Exception when calling UserApi->users_format_post: %s\n" % e)
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

# **users_id_format_delete**
> users_id_format_delete(format, id)

Destroy User

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.UserApi()
format = NULL # object | specify format of response
id = NULL # object | ID of User

try:
    # Destroy User
    api_instance.users_id_format_delete(format, id)
except ApiException as e:
    print("Exception when calling UserApi->users_id_format_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **id** | [**object**](.md)| ID of User | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_format_get**
> users_id_format_get(id, format, include=include)

Get User

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.UserApi()
id = NULL # object | ID of User
format = NULL # object | specify format of response
include = NULL # object | explicitly specify the associations you want to be included in the query result  * **groups** (groups which user is in) * **memberships** (list of projects which is user in role) (optional)

try:
    # Get User
    api_instance.users_id_format_get(id, format, include=include)
except ApiException as e:
    print("Exception when calling UserApi->users_id_format_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID of User | 
 **format** | [**object**](.md)| specify format of response | 
 **include** | [**object**](.md)| explicitly specify the associations you want to be included in the query result  * **groups** (groups which user is in) * **memberships** (list of projects which is user in role) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_id_format_put**
> users_id_format_put(format, id)

Update User

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.UserApi()
format = NULL # object | specify format of response
id = NULL # object | ID of User

try:
    # Update User
    api_instance.users_id_format_put(format, id)
except ApiException as e:
    print("Exception when calling UserApi->users_id_format_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **id** | [**object**](.md)| ID of User | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

