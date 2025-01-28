# Pixela setup

## Creating an account

We can create an account simply by submitting a post request and passing our desired details in the
params.

We can choose our own token and username in this process. The response will tell us if it was successful.

```python
import requests

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": "ARtartAT232rtr",
    "username": "LeonLonsdale",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params, timeout=5)
print(response.text)
```

## Creating a Graph

When creating a graph, the endpoint changes and now includes our username:

```python
import requests


USERNAME="LeonLonsdale"
TOKEN="ARtartAT232rtr"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
```

For the json/params when making a graph post request, we have the following requirements:

- `id` - a string that identifies the graph.
  - rule: must start with a letter. Can include numbers. 1 - 16 characters.
- `name` - a string that names the graph.
- `unit` - a string that identifies the unit for our habbit measurement. i.e., calory, kilogram, etc,.
- `type` - a string that indicates the `type` of the data that the graph will handle: `int` or `float`.
- `color` - a string that indicates the color we want to use in the graph.

note: `color` only supports:
    - shibafu (green)
    - momiji (red)
    - sora (blue)U
    - ichou (yellow)
    - ajisai (purple)
    - kuro (black)

```python
graph_id = "graph1"

graph_config = {
    "id": graph_id,
    "name": "Walking",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
```

This will fail of course, as we are providing our username in the api endpoint, butat no point are we
entering our token.

To provide the token, we must provide it in a `header`.

```python
headers = {
    "X-USER-TOKEN": TOKEN,
}

response = requests.post(url=graph_endpoint, json=user_params, headers=headers, timeout=5)
print(respons.text)
```

If this worked, we can view our graph at:

```text
https://pixe.la/v1/users/{USERNAME}/graphs{graph_id}.html
```

## Adding a record

To add a new record, we need another endpoint. This time it's in this format:

```python
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
```

The config for this requires 2 fields:

- The date in the format `yyyyMMdd`.
- The quatity of units completed.

```python
todays_date = datetime.datetime.now().strftime("%Y%m%d")

pixel_config = {
        "date": todays_date,
        "quantity": "24.2"
    }
```

This also needs header verification:

```python
response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers, timeout=5)
```


## Update a record

For this, we need to change the method to `put` and provide the date we want to update.

The date appends the endpoint:

```python
mutate_endpoint = f"{pixel_endpoint}/yyyyMMdd"
```

The only required field is the quantity.

```python
update_config = {
    "quantity": "25.2"
}


response = requests.put(url=update_endpoint, json=update_config, headers=headers, timeout=5)
```

## Delete a record

To delete a record, we need to change the method to `delete` and provide the date we want to delete.

The endpoint is the same as the update endpoint. Since we are deleting, we don't need to provide any
additional information.

```python
response = requests.delete(url=mutate_endpoint, headers=headers, timeout=5)
```
