# Pyisocapi
The Pyisocapi library provides convenient access to the Isocapi API from apps written in Python.
It includes client with multiple convenient methods to obtain data you need - both synchronously and asynchronously.

## Isocapi documentantion
See our page: [Isocapi](https://isocapi.com/docs/)

## Instalation
```sh
pip install --upgrade pyisocapi
```

#### Requirements
- Python 3.10+

## Usage:
<details open>
    <summary><b>synchronous</b></summary> 
    
```py
from pyisocapi import IsocapiClient

api_key = "YOUR_API_KEY"
url = "OLX_URL"

client = IsocapiClient(api_key)
response = client.get_olx_by_url(url)

print(response)

>>
```
</details>

<details>
    <summary><b>asynchronous</b></summary>

```python
import asyncio
from pyisocapi import IsocapiClient

async def main():
    api_key = "YOUR_API_KEY"
    url = "OLX_URL"

    client = IsocapiClient(api_key)
    response = client.get_olx_by_url_async(url)

    print(response)

asyncio.run(main())

>> 
```
</details>

#### Handling exceptions
Unsuccessful requests raise exceptions. The class of the exception will reflect the sort of error that occurred. To handle them yourself import them from `pyisocapi.exceptions`


## Support
If you have encountered a bug or have any ideas how to improve this library - don't be afraid to open an [issue](https://github.com/isocsoft/pyisocapi/issues/new) with an explanation.
