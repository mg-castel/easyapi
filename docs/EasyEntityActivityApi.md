# easyapi.EasyEntityActivityApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**easy_entity_activities_format_post**](EasyEntityActivityApi.md#easy_entity_activities_format_post) | **POST** /easy_entity_activities.{format} | Create EasyEntityActivity
[**easy_entity_activities_id_format_delete**](EasyEntityActivityApi.md#easy_entity_activities_id_format_delete) | **DELETE** /easy_entity_activities/{id}.{format} | Destroy EasyEntityActivity
[**easy_entity_activities_id_format_get**](EasyEntityActivityApi.md#easy_entity_activities_id_format_get) | **GET** /easy_entity_activities/{id}.{format} | Get EasyEntityActivity
[**easy_entity_activities_id_format_put**](EasyEntityActivityApi.md#easy_entity_activities_id_format_put) | **PUT** /easy_entity_activities/{id}.{format} | Update EasyEntityActivity


# **easy_entity_activities_format_post**
> easy_entity_activities_format_post(format)

Create EasyEntityActivity

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.EasyEntityActivityApi()
format = NULL # object | specify format of response

try:
    # Create EasyEntityActivity
    api_instance.easy_entity_activities_format_post(format)
except ApiException as e:
    print("Exception when calling EasyEntityActivityApi->easy_entity_activities_format_post: %s\n" % e)
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

# **easy_entity_activities_id_format_delete**
> easy_entity_activities_id_format_delete(format, id)

Destroy EasyEntityActivity

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.EasyEntityActivityApi()
format = NULL # object | specify format of response
id = NULL # object | ID of EasyEntityActivity

try:
    # Destroy EasyEntityActivity
    api_instance.easy_entity_activities_id_format_delete(format, id)
except ApiException as e:
    print("Exception when calling EasyEntityActivityApi->easy_entity_activities_id_format_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **id** | [**object**](.md)| ID of EasyEntityActivity | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **easy_entity_activities_id_format_get**
> easy_entity_activities_id_format_get(id, format)

Get EasyEntityActivity

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.EasyEntityActivityApi()
id = NULL # object | ID of EasyEntityActivity
format = NULL # object | specify format of response

try:
    # Get EasyEntityActivity
    api_instance.easy_entity_activities_id_format_get(id, format)
except ApiException as e:
    print("Exception when calling EasyEntityActivityApi->easy_entity_activities_id_format_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID of EasyEntityActivity | 
 **format** | [**object**](.md)| specify format of response | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **easy_entity_activities_id_format_put**
> easy_entity_activities_id_format_put(format, id)

Update EasyEntityActivity

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.EasyEntityActivityApi()
format = NULL # object | specify format of response
id = NULL # object | ID of EasyEntityActivity

try:
    # Update EasyEntityActivity
    api_instance.easy_entity_activities_id_format_put(format, id)
except ApiException as e:
    print("Exception when calling EasyEntityActivityApi->easy_entity_activities_id_format_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **id** | [**object**](.md)| ID of EasyEntityActivity | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

