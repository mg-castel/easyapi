# easyapi.EasyAttendanceApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**easy_attendances_format_get**](EasyAttendanceApi.md#easy_attendances_format_get) | **GET** /easy_attendances.{format} | List of EasyAttendances
[**easy_attendances_format_post**](EasyAttendanceApi.md#easy_attendances_format_post) | **POST** /easy_attendances.{format} | Create EasyAttendance
[**easy_attendances_id_format_delete**](EasyAttendanceApi.md#easy_attendances_id_format_delete) | **DELETE** /easy_attendances/{id}.{format} | Destroy EasyAttendance
[**easy_attendances_id_format_get**](EasyAttendanceApi.md#easy_attendances_id_format_get) | **GET** /easy_attendances/{id}.{format} | Get EasyAttendance
[**easy_attendances_id_format_put**](EasyAttendanceApi.md#easy_attendances_id_format_put) | **PUT** /easy_attendances/{id}.{format} | Update EasyAttendance


# **easy_attendances_format_get**
> easy_attendances_format_get(format, easy_query_q=easy_query_q, set_filter=set_filter, limit=limit, offset=offset)

List of EasyAttendances

For filtering send parameter `set_filter=1` and specify filters

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.EasyAttendanceApi()
format = NULL # object | specify format of response
easy_query_q = NULL # object | free-text filter of current entity (optional)
set_filter = NULL # object | enable filter through Easy Query (optional)
limit = NULL # object | the number of items to be present in the response (default is 25, maximum is 100) (optional)
offset = NULL # object | the offset of the first object to retrieve (optional)

try:
    # List of EasyAttendances
    api_instance.easy_attendances_format_get(format, easy_query_q=easy_query_q, set_filter=set_filter, limit=limit, offset=offset)
except ApiException as e:
    print("Exception when calling EasyAttendanceApi->easy_attendances_format_get: %s\n" % e)
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

# **easy_attendances_format_post**
> easy_attendances_format_post(format)

Create EasyAttendance

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.EasyAttendanceApi()
format = NULL # object | specify format of response

try:
    # Create EasyAttendance
    api_instance.easy_attendances_format_post(format)
except ApiException as e:
    print("Exception when calling EasyAttendanceApi->easy_attendances_format_post: %s\n" % e)
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

# **easy_attendances_id_format_delete**
> easy_attendances_id_format_delete(format, id)

Destroy EasyAttendance

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.EasyAttendanceApi()
format = NULL # object | specify format of response
id = NULL # object | ID of EasyAttendance

try:
    # Destroy EasyAttendance
    api_instance.easy_attendances_id_format_delete(format, id)
except ApiException as e:
    print("Exception when calling EasyAttendanceApi->easy_attendances_id_format_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **id** | [**object**](.md)| ID of EasyAttendance | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **easy_attendances_id_format_get**
> easy_attendances_id_format_get(id, format)

Get EasyAttendance

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.EasyAttendanceApi()
id = NULL # object | ID of EasyAttendance
format = NULL # object | specify format of response

try:
    # Get EasyAttendance
    api_instance.easy_attendances_id_format_get(id, format)
except ApiException as e:
    print("Exception when calling EasyAttendanceApi->easy_attendances_id_format_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID of EasyAttendance | 
 **format** | [**object**](.md)| specify format of response | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **easy_attendances_id_format_put**
> easy_attendances_id_format_put(format, id)

Update EasyAttendance

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.EasyAttendanceApi()
format = NULL # object | specify format of response
id = NULL # object | ID of EasyAttendance

try:
    # Update EasyAttendance
    api_instance.easy_attendances_id_format_put(format, id)
except ApiException as e:
    print("Exception when calling EasyAttendanceApi->easy_attendances_id_format_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **id** | [**object**](.md)| ID of EasyAttendance | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

