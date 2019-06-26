# main file for the Duo API calls
import duo_client
import json
import sys

# Constants for Duo Admin API calls
from keys_duo import *

# authorization information for Duo API call
Admin = duo_client.Admin(
    ikey=DUO_ADMINAPI_IKEY,
    skey=DUO_ADMINAPI_SKEY,
    host=DUO_ADMINAPI_APIHOSTNAME
)

Auth = duo_client.Auth(
    ikey=DUO_AUTHAPI_IKEY,
    skey=DUO_AUTHAPI_SKEY,
    host=DUO_AUTHAPI_APIHOSTNAME
)

def clean(x, indent=2):
    print(json.dumps(x, indent=indent))

print("Welcome to the DuoAPI Playground!")
print("Use clean() on compact JSON to get a human-readable version")
