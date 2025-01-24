# API

Definition: An API (Application Programming Interface) is a set of rules and protocols that allow 
one software application to interact with another. APIs are used to define the methods for 
communication between different software components.

## Endpoints

An endpoint is a specific URL within an API that accepts requests. 
Each endpoint defines a specific function within the API.
This is usually a URL that points to a specific resource or action.

##  Requests

In order to interact with an API, a client sends an `api request` to an endpoint.
The API may require some security details or parameters to be included in the request before it will
respond with the requested data.

## Example

The ISS (International Space Station) API provides information about the current location of the ISS.
Its endpoint is `http://api.open-notify.org/iss-now.json` and it returns the current latitude and 
longitude of the ISS. The data is returned in JSON format.

```python
import requests # need to install requests package

response = requests.get("http://api.open-notify.org/iss-now.json")
data = response.json()
```

## Response

The response received from the API request will contain the requested data. It exposes a number of
moehtods and attributes that can be used to access the data.

```python
response = requests.get("http://api.open-notify.org/iss-now.json")

print(response.status_code) # the status code
print(response.text) # the text of the response
print(response.json()) # the response in JSON format
```

### Codes

The API will respond with a status code that indicates the success or failure of the request.

If the request is successful, the API will respond with a `200 OK` status code.

Some common status codes include:

```
400 Bad Request - The request was invalid or cannot be served.
401 Unauthorized - The request requires an authentication token.
403 Forbidden - The server understood the request, but is refusing to fulfill it.
404 Not Found - The requested resource could not be found.
```

As a general rule:

- A `1xx` status code indicates an informational response.
- A `2xx` status code indicates success.
- A `3xx` status code indicates a redirection / no access.
- A `4xx` status code indicates a client error.
- A `5xx` status code indicates a server error.


## Handling Status Codes

The `requests` library provides a way to check the status code of the response. This is the 
`raise_for_status()` method. This method will raise an exception if the status code is not `200`.

```python
response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()
```

## Accessing Data

```python
response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
position = data['iss_position']
latitude = position['latitude']
longitude = position['longitude']

iss_position = (latitude, longitude)
```

## API parameters

APIs can accept parameters in the request to filter the data that is returned. These parameters are
included in the URL as query parameters. The API documentation will specify the parameters that are
required or optional. When passing parameters in the request, you can use the `params` argument of the
requests.get() method. The keys of the parameters must match the names specified in the API documentation.

For example, using the Sunrise Sunset API, you can specify the latitude and longitude of a location
and the date for which you want to get the sunrise and sunset times. 

What if we want to get the times of the sunrise and sunset and then use this to deterimine if the ISS
is passing over at night?

```python
response = requests.get(
    "https://api.sunrise-sunset.org/json", 
    params={
        "lat": 36.7201600, 
        "lng": -4.4203400, 
        "date": "2022-03-21",
        "formatted": 0
        }
    )
response.raise_for_status()
data = response.json()
sunrise_hour = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset_hour = data['results']['sunset'].split('T')[1].split(':')[0]
```
