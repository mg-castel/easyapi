# easyapi.TimeEntryApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**time_entries_format_get**](TimeEntryApi.md#time_entries_format_get) | **GET** /time_entries.{format} | List of TimeEntries
[**time_entries_format_post**](TimeEntryApi.md#time_entries_format_post) | **POST** /time_entries.{format} | Create TimeEntry
[**time_entries_id_format_delete**](TimeEntryApi.md#time_entries_id_format_delete) | **DELETE** /time_entries/{id}.{format} | Destroy TimeEntry
[**time_entries_id_format_get**](TimeEntryApi.md#time_entries_id_format_get) | **GET** /time_entries/{id}.{format} | Get TimeEntry
[**time_entries_id_format_put**](TimeEntryApi.md#time_entries_id_format_put) | **PUT** /time_entries/{id}.{format} | Update TimeEntry


# **time_entries_format_get**
> time_entries_format_get(format, easy_query_q=easy_query_q, set_filter=set_filter, limit=limit, offset=offset)

List of TimeEntries

For filtering send parameter `set_filter=1` and specify filters

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.TimeEntryApi()
format = NULL # object | specify format of response
easy_query_q = NULL # object | free-text filter of current entity (optional)
set_filter = NULL # object | enable filter through Easy Query (optional)
limit = NULL # object | the number of items to be present in the response (default is 25, maximum is 100) (optional)
offset = NULL # object | the offset of the first object to retrieve (optional)

try:
    # List of TimeEntries
    api_instance.time_entries_format_get(format, easy_query_q=easy_query_q, set_filter=set_filter, limit=limit, offset=offset)
except ApiException as e:
    print("Exception when calling TimeEntryApi->time_entries_format_get: %s\n" % e)
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

# **time_entries_format_post**
> time_entries_format_post(format)

Create TimeEntry

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.TimeEntryApi()
format = NULL # object | specify format of response

try:
    # Create TimeEntry
    api_instance.time_entries_format_post(format)
except ApiException as e:
    print("Exception when calling TimeEntryApi->time_entries_format_post: %s\n" % e)
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

# **time_entries_id_format_delete**
> time_entries_id_format_delete(format, id)

Destroy TimeEntry

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.TimeEntryApi()
format = NULL # object | specify format of response
id = NULL # object | ID of TimeEntry

try:
    # Destroy TimeEntry
    api_instance.time_entries_id_format_delete(format, id)
except ApiException as e:
    print("Exception when calling TimeEntryApi->time_entries_id_format_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **id** | [**object**](.md)| ID of TimeEntry | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **time_entries_id_format_get**
> time_entries_id_format_get(id, format)

Get TimeEntry

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.TimeEntryApi()
id = NULL # object | ID of TimeEntry
format = NULL # object | specify format of response

try:
    # Get TimeEntry
    api_instance.time_entries_id_format_get(id, format)
except ApiException as e:
    print("Exception when calling TimeEntryApi->time_entries_id_format_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID of TimeEntry | 
 **format** | [**object**](.md)| specify format of response | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **time_entries_id_format_put**
> time_entries_id_format_put(format, id)

Update TimeEntry

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.TimeEntryApi()
format = NULL # object | specify format of response
id = NULL # object | ID of TimeEntry

try:
    # Update TimeEntry
    api_instance.time_entries_id_format_put(format, id)
except ApiException as e:
    print("Exception when calling TimeEntryApi->time_entries_id_format_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **id** | [**object**](.md)| ID of TimeEntry | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

