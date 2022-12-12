# easyapi.EasyCalendarMeetingApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**easy_calendar_feed_json_get**](EasyCalendarMeetingApi.md#easy_calendar_feed_json_get) | **GET** /easy_calendar/feed.json | List of Easy Meetings
[**easy_meetings_format_post**](EasyCalendarMeetingApi.md#easy_meetings_format_post) | **POST** /easy_meetings.{format} | Create EasyMeeting
[**easy_meetings_id_format_delete**](EasyCalendarMeetingApi.md#easy_meetings_id_format_delete) | **DELETE** /easy_meetings/{id}.{format} | Destroy EasyMeeting
[**easy_meetings_id_format_get**](EasyCalendarMeetingApi.md#easy_meetings_id_format_get) | **GET** /easy_meetings/{id}.{format} | Get EasyMeeting
[**easy_meetings_id_format_put**](EasyCalendarMeetingApi.md#easy_meetings_id_format_put) | **PUT** /easy_meetings/{id}.{format} | Update EasyMeeting


# **easy_calendar_feed_json_get**
> easy_calendar_feed_json_get(start, end, enabled_calendars=enabled_calendars)

List of Easy Meetings

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.EasyCalendarMeetingApi()
start = NULL # object | get meetings only starts in this time
end = NULL # object | get meetings only ends in this time
enabled_calendars = NULL # object | list of types - Meetings, Attendance, etc.... by default its `easy_meeting_calendar` (optional)

try:
    # List of Easy Meetings
    api_instance.easy_calendar_feed_json_get(start, end, enabled_calendars=enabled_calendars)
except ApiException as e:
    print("Exception when calling EasyCalendarMeetingApi->easy_calendar_feed_json_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | [**object**](.md)| get meetings only starts in this time | 
 **end** | [**object**](.md)| get meetings only ends in this time | 
 **enabled_calendars** | [**object**](.md)| list of types - Meetings, Attendance, etc.... by default its &#x60;easy_meeting_calendar&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **easy_meetings_format_post**
> easy_meetings_format_post(format)

Create EasyMeeting

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.EasyCalendarMeetingApi()
format = NULL # object | specify format of response

try:
    # Create EasyMeeting
    api_instance.easy_meetings_format_post(format)
except ApiException as e:
    print("Exception when calling EasyCalendarMeetingApi->easy_meetings_format_post: %s\n" % e)
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

# **easy_meetings_id_format_delete**
> easy_meetings_id_format_delete(format, id)

Destroy EasyMeeting

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.EasyCalendarMeetingApi()
format = NULL # object | specify format of response
id = NULL # object | ID of EasyMeeting

try:
    # Destroy EasyMeeting
    api_instance.easy_meetings_id_format_delete(format, id)
except ApiException as e:
    print("Exception when calling EasyCalendarMeetingApi->easy_meetings_id_format_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **id** | [**object**](.md)| ID of EasyMeeting | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **easy_meetings_id_format_get**
> easy_meetings_id_format_get(id, format)

Get EasyMeeting

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.EasyCalendarMeetingApi()
id = NULL # object | ID of EasyMeeting
format = NULL # object | specify format of response

try:
    # Get EasyMeeting
    api_instance.easy_meetings_id_format_get(id, format)
except ApiException as e:
    print("Exception when calling EasyCalendarMeetingApi->easy_meetings_id_format_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID of EasyMeeting | 
 **format** | [**object**](.md)| specify format of response | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **easy_meetings_id_format_put**
> easy_meetings_id_format_put(format, id)

Update EasyMeeting

### Example
```python
from __future__ import print_function
import time
import easyapi
from easyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = easyapi.EasyCalendarMeetingApi()
format = NULL # object | specify format of response
id = NULL # object | ID of EasyMeeting

try:
    # Update EasyMeeting
    api_instance.easy_meetings_id_format_put(format, id)
except ApiException as e:
    print("Exception when calling EasyCalendarMeetingApi->easy_meetings_id_format_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | [**object**](.md)| specify format of response | 
 **id** | [**object**](.md)| ID of EasyMeeting | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

