import json
import urllib.request

import yaml

JASIMA = "https://raw.githubusercontent.com/lipu-linku/jasima/master/data.json"

JASIMA_LOCAL = "./data.json"


def get_from_internet() -> bytes:
    req = urllib.request.Request(JASIMA)
    resp = urllib.request.urlopen(req).read()
    return resp


def get_from_filesystem():
    return yaml.safe_load(open(JASIMA_LOCAL, "r"))


def get_data(local: bool = True):
    if local:
        return get_from_filesystem()
    return json.loads(get_from_internet())
