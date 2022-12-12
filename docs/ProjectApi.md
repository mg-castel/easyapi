# easyapi.ProjectApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_format_get**](ProjectApi.md#projects_format_get) | **GET** /projects.{format} | List of Projects
[**projects_format_post**](ProjectApi.md#projects_format_post) | **POST** /projects.{format} | Create Project
[**projects_id_archive_format_post**](ProjectApi.md#projects_id_archive_format_post) | **POST** /projects/{id}/archive.{format} | Archive Project
[**projects_id_close_format_post**](ProjectApi.md#projects_id_close_format_post) | **POST** /projects/{id}/close.{format} | Close Project
[**projects_id_format_delete**](ProjectApi.md#projects_id_format_delete) | **DELETE** /projects/{id}.{format} | Destroy Project
[**projects_id_format_get**](ProjectApi.md#projects_id_format_get) | **GET** /projects/{id}.{format} | Get Project
[**projects_id_format_put**](ProjectApi.md#projects_id_format_put) | **PUT** /projects/{id}.{format} | Update Project
[**projects_id_reopen_format_post**](ProjectApi.md#projects_id_reopen_format_post) | **POST** /projects/{id}/reopen.{format} | Reopen Project
[**projects_id_unarchive_format_post**](ProjectApi.md#projects_id_unarchive_format_post) | **POST** /projects/{id}/unarchive.{format} | Unarchive Project


# **projects_format_get**
> projects_format_get(format, easy_query_q=easy_query_q, set_filter=set_filter, limit=limit, offset=offset, include=include)

List of Projects

For filtering send parameter `set_filter=1` and specify filters

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.ProjectApi()
format = NULL # object | specify format of response
easy_query_q = NULL # object | free-text filter of current entity (optional)
set_filter = NULL # object | enable filter through Easy Query (optional)
limit = NULL # object | the number of items to be present in the response (default is 25, maximum is 100) (optional)
offset = NULL # object | the offset of the first object to retrieve (optional)
include = NULL # object | explicitly specify the associations you want to be included in the query result  * **trackers** (List of enabled trackers on project) * **issue_categories** (List of IssueCategories) * **enabled_modules** (List of enabled project modules) (optional)

try:
    # List of Projects
    api_instance.projects_format_get(format, easy_query_q=easy_query_q, set_filter=set_filter, limit=limit, offset=offset, include=include)
except ApiException as e:
    print("Exception when calling ProjectApi->projects_format_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **easy_query_q** | [**object**](.md)| free-text filter of current entity | [optional] 
 **set_filter** | [**object**](.md)| enable filter through Easy Query | [optional] 
 **limit** | [**object**](.md)| the number of items to be present in the response (default is 25, maximum is 100) | [optional] 
 **offset** | [**object**](.md)| the offset of the first object to retrieve | [optional] 
 **include** | [**object**](.md)| explicitly specify the associations you want to be included in the query result  * **trackers** (List of enabled trackers on project) * **issue_categories** (List of IssueCategories) * **enabled_modules** (List of enabled project modules) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_format_post**
> projects_format_post(format)

Create Project

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.ProjectApi()
format = NULL # object | specify format of response

try:
    # Create Project
    api_instance.projects_format_post(format)
except ApiException as e:
    print("Exception when calling ProjectApi->projects_format_post: %s\n" % e)
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

# **projects_id_archive_format_post**
> projects_id_archive_format_post(format, id)

Archive Project

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.ProjectApi()
format = NULL # object | specify format of response
id = NULL # object | ID of Project

try:
    # Archive Project
    api_instance.projects_id_archive_format_post(format, id)
except ApiException as e:
    print("Exception when calling ProjectApi->projects_id_archive_format_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **id** | [**object**](.md)| ID of Project | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_id_close_format_post**
> projects_id_close_format_post(format, id)

Close Project

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.ProjectApi()
format = NULL # object | specify format of response
id = NULL # object | ID of Project

try:
    # Close Project
    api_instance.projects_id_close_format_post(format, id)
except ApiException as e:
    print("Exception when calling ProjectApi->projects_id_close_format_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **id** | [**object**](.md)| ID of Project | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_id_format_delete**
> projects_id_format_delete(format, id)

Destroy Project

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.ProjectApi()
format = NULL # object | specify format of response
id = NULL # object | ID of Project

try:
    # Destroy Project
    api_instance.projects_id_format_delete(format, id)
except ApiException as e:
    print("Exception when calling ProjectApi->projects_id_format_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **id** | [**object**](.md)| ID of Project | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_id_format_get**
> projects_id_format_get(id, format, include=include)

Get Project

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.ProjectApi()
id = NULL # object | ID of Project
format = NULL # object | specify format of response
include = NULL # object | explicitly specify the associations you want to be included in the query result  * **trackers** (List of enabled trackers on project) * **issue_categories** (List of IssueCategories) * **enabled_modules** (List of enabled project modules) (optional)

try:
    # Get Project
    api_instance.projects_id_format_get(id, format, include=include)
except ApiException as e:
    print("Exception when calling ProjectApi->projects_id_format_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID of Project | 
 **format** | [**object**](.md)| specify format of response | 
 **include** | [**object**](.md)| explicitly specify the associations you want to be included in the query result  * **trackers** (List of enabled trackers on project) * **issue_categories** (List of IssueCategories) * **enabled_modules** (List of enabled project modules) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_id_format_put**
> projects_id_format_put(format, id)

Update Project

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.ProjectApi()
format = NULL # object | specify format of response
id = NULL # object | ID of Project

try:
    # Update Project
    api_instance.projects_id_format_put(format, id)
except ApiException as e:
    print("Exception when calling ProjectApi->projects_id_format_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **id** | [**object**](.md)| ID of Project | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_id_reopen_format_post**
> projects_id_reopen_format_post(format, id)

Reopen Project

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.ProjectApi()
format = NULL # object | specify format of response
id = NULL # object | ID of Project

try:
    # Reopen Project
    api_instance.projects_id_reopen_format_post(format, id)
except ApiException as e:
    print("Exception when calling ProjectApi->projects_id_reopen_format_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **id** | [**object**](.md)| ID of Project | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_id_unarchive_format_post**
> projects_id_unarchive_format_post(format, id)

Unarchive Project

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.ProjectApi()
format = NULL # object | specify format of response
id = NULL # object | ID of Project

try:
    # Unarchive Project
    api_instance.projects_id_unarchive_format_post(format, id)
except ApiException as e:
    print("Exception when calling ProjectApi->projects_id_unarchive_format_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **id** | [**object**](.md)| ID of Project | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

