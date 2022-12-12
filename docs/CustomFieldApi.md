# easyapi.CustomFieldApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_fields_format_get**](CustomFieldApi.md#custom_fields_format_get) | **GET** /custom_fields.{format} | List of CustomFields
[**custom_fields_format_post**](CustomFieldApi.md#custom_fields_format_post) | **POST** /custom_fields.{format} | Create CustomField
[**custom_fields_id_format_delete**](CustomFieldApi.md#custom_fields_id_format_delete) | **DELETE** /custom_fields/{id}.{format} | Destroy CustomField
[**custom_fields_id_format_get**](CustomFieldApi.md#custom_fields_id_format_get) | **GET** /custom_fields/{id}.{format} | Get CustomField
[**custom_fields_id_format_put**](CustomFieldApi.md#custom_fields_id_format_put) | **PUT** /custom_fields/{id}.{format} | Update CustomField


# **custom_fields_format_get**
> custom_fields_format_get(format, easy_query_q=easy_query_q, set_filter=set_filter, limit=limit, offset=offset)

List of CustomFields

For filtering send parameter `set_filter=1` and specify filters

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.CustomFieldApi()
format = NULL # object | specify format of response
easy_query_q = NULL # object | free-text filter of current entity (optional)
set_filter = NULL # object | enable filter through Easy Query (optional)
limit = NULL # object | the number of items to be present in the response (default is 25, maximum is 100) (optional)
offset = NULL # object | the offset of the first object to retrieve (optional)

try:
    # List of CustomFields
    api_instance.custom_fields_format_get(format, easy_query_q=easy_query_q, set_filter=set_filter, limit=limit, offset=offset)
except ApiException as e:
    print("Exception when calling CustomFieldApi->custom_fields_format_get: %s\n" % e)
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

# **custom_fields_format_post**
> custom_fields_format_post(format, type=type)

Create CustomField

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.CustomFieldApi()
format = NULL # object | specify format of response
type = NULL # object | Name of custom field class (optional)

try:
    # Create CustomField
    api_instance.custom_fields_format_post(format, type=type)
except ApiException as e:
    print("Exception when calling CustomFieldApi->custom_fields_format_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **type** | [**object**](.md)| Name of custom field class | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_fields_id_format_delete**
> custom_fields_id_format_delete(format, id)

Destroy CustomField

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.CustomFieldApi()
format = NULL # object | specify format of response
id = NULL # object | ID of CustomField

try:
    # Destroy CustomField
    api_instance.custom_fields_id_format_delete(format, id)
except ApiException as e:
    print("Exception when calling CustomFieldApi->custom_fields_id_format_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **id** | [**object**](.md)| ID of CustomField | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_fields_id_format_get**
> custom_fields_id_format_get(id, format)

Get CustomField

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.CustomFieldApi()
id = NULL # object | ID of CustomField
format = NULL # object | specify format of response

try:
    # Get CustomField
    api_instance.custom_fields_id_format_get(id, format)
except ApiException as e:
    print("Exception when calling CustomFieldApi->custom_fields_id_format_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID of CustomField | 
 **format** | [**object**](.md)| specify format of response | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_fields_id_format_put**
> custom_fields_id_format_put(format, id)

Update CustomField

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.CustomFieldApi()
format = NULL # object | specify format of response
id = NULL # object | ID of CustomField

try:
    # Update CustomField
    api_instance.custom_fields_id_format_put(format, id)
except ApiException as e:
    print("Exception when calling CustomFieldApi->custom_fields_id_format_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **id** | [**object**](.md)| ID of CustomField | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

