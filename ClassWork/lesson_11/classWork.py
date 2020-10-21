import json
import requests

url_base = "http://54.37.125.181/api/v1/basic"
url_hello = f"{url_base}/hello-world/"
url_ip = f"{url_base}/get-my-ip/"
url_status = f"{url_base}/status/"
url_text = f"{url_base}/text/"


def get_response(url):
    response = requests.get(url)
    return response.json()


def post_response(url, data):
    response = requests.post(url, data=data)
    return response.status_code


res_json = get_response(url_text)
print(json.dumps(res_json, indent=2))

data = {"text": "my_text"}
post_request = post_response(url_text, data)

res_json = get_response(url_text)
print(json.dumps(res_json, indent=2))