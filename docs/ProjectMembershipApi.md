# easyapi.ProjectMembershipApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**memberships_projects_id_memberships_format_get**](ProjectMembershipApi.md#memberships_projects_id_memberships_format_get) | **GET** /memberships/projects/{id}/memberships.{format} | Retrieve memberships of the Project with specified id
[**memberships_projects_id_memberships_format_post**](ProjectMembershipApi.md#memberships_projects_id_memberships_format_post) | **POST** /memberships/projects/{id}/memberships.{format} | Create a membership in a Project with specified id


# **memberships_projects_id_memberships_format_get**
> memberships_projects_id_memberships_format_get(format, id)

Retrieve memberships of the Project with specified id

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.ProjectMembershipApi()
format = NULL # object | specify format of response
id = NULL # object | ID of Project

try:
    # Retrieve memberships of the Project with specified id
    api_instance.memberships_projects_id_memberships_format_get(format, id)
except ApiException as e:
    print("Exception when calling ProjectMembershipApi->memberships_projects_id_memberships_format_get: %s\n" % e)
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

# **memberships_projects_id_memberships_format_post**
> memberships_projects_id_memberships_format_post(format, id)

Create a membership in a Project with specified id

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.ProjectMembershipApi()
format = NULL # object | specify format of response
id = NULL # object | ID of Project

try:
    # Create a membership in a Project with specified id
    api_instance.memberships_projects_id_memberships_format_post(format, id)
except ApiException as e:
    print("Exception when calling ProjectMembershipApi->memberships_projects_id_memberships_format_post: %s\n" % e)
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

