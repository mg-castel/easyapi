# easyapi.EasySettingApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_easy_settings_format_post**](EasySettingApi.md#admin_easy_settings_format_post) | **POST** /admin/easy_settings.{format} | Create EasySetting
[**admin_easy_settings_id_format_delete**](EasySettingApi.md#admin_easy_settings_id_format_delete) | **DELETE** /admin/easy_settings/{id}.{format} | Destroy EasySetting
[**admin_easy_settings_id_format_get**](EasySettingApi.md#admin_easy_settings_id_format_get) | **GET** /admin/easy_settings/{id}.{format} | Get EasySetting
[**admin_easy_settings_id_format_put**](EasySettingApi.md#admin_easy_settings_id_format_put) | **PUT** /admin/easy_settings/{id}.{format} | Update EasySetting


# **admin_easy_settings_format_post**
> admin_easy_settings_format_post(format)

Create EasySetting

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.EasySettingApi()
format = NULL # object | specify format of response

try:
    # Create EasySetting
    api_instance.admin_easy_settings_format_post(format)
except ApiException as e:
    print("Exception when calling EasySettingApi->admin_easy_settings_format_post: %s\n" % e)
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

# **admin_easy_settings_id_format_delete**
> admin_easy_settings_id_format_delete(format, id)

Destroy EasySetting

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.EasySettingApi()
format = NULL # object | specify format of response
id = NULL # object | ID of EasySetting

try:
    # Destroy EasySetting
    api_instance.admin_easy_settings_id_format_delete(format, id)
except ApiException as e:
    print("Exception when calling EasySettingApi->admin_easy_settings_id_format_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **id** | [**object**](.md)| ID of EasySetting | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_easy_settings_id_format_get**
> admin_easy_settings_id_format_get(id, format)

Get EasySetting

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.EasySettingApi()
id = NULL # object | ID of EasySetting
format = NULL # object | specify format of response

try:
    # Get EasySetting
    api_instance.admin_easy_settings_id_format_get(id, format)
except ApiException as e:
    print("Exception when calling EasySettingApi->admin_easy_settings_id_format_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID of EasySetting | 
 **format** | [**object**](.md)| specify format of response | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_easy_settings_id_format_put**
> admin_easy_settings_id_format_put(format, id)

Update EasySetting

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.EasySettingApi()
format = NULL # object | specify format of response
id = NULL # object | ID of EasySetting

try:
    # Update EasySetting
    api_instance.admin_easy_settings_id_format_put(format, id)
except ApiException as e:
    print("Exception when calling EasySettingApi->admin_easy_settings_id_format_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **id** | [**object**](.md)| ID of EasySetting | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

