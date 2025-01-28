# HTTP Requests

## Common request types

- GET
- POST
- Put
- DELETE

## Using requests module

```python
requests.get()
requests.post()
requests.put()
requests.delete()
```

## Basic Definitions

- `GET`: We use a `GET` request when we want to ask an external system for some data.
- `POST`: We use a `POST` request when we want to send data to an external system.
- `PUT`: We use a `PUT` request when we want to update data within an external service.
- `DELETE`: We use a `DELETE` request when we want to delete data from an external service.

## Using requests.post()

Signature:

```python
response = requsts.post(url, json, timeout=5)
```

The `json` keyword accepts the params, so the params must be in json format `"string": "string"`.

Test the response `print(response.text)`.

## Using requests.put()

Signature:

```python
response = requests.put(url, json, timeout=5)
```

## Using requests.delete()

Signature:

```python
response = requests.delete(url, timeout=5)
```

## Headers

Much like a letter, our requests must consist of both a `header` and a `body`. In the context of our
request, the body is the data we are passing over - the params. However, the params is not a secure
method of passing our secret information.

The params are essentially the same as appending the information to the end of the endpoint address:

```text
https://endpoint-address?secret-info&data
```

Headers allow us to pass our secret information securely.

We can do this by passing headers:

```python
headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url, json, headers, timeout=5)
```

