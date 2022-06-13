from __future__ import print_function

import os.path

import requests

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


# If modifying these scopes, delete the file token.json.
# SCOPES = ['https://www.googleapis.com/auth/contacts.readonly', ]
SCOPES = ["https://www.googleapis.com/auth/directory.readonly"]


def main():
    """Shows basic usage of the People API.
    Prints the name of the first 10 connections.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secrets.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            print("new token:\n", creds.token)
            token.write(creds.to_json())

    access_token = creds.token
    header = {
        "Authorization": f"Bearer {access_token}"
    }
    params = {
        "readMask":"names",
        "sources":"DIRECTORY_SOURCE_TYPE_DOMAIN_PROFILE"
    }
    url = f"https://people.googleapis.com/v1/people:listDirectoryPeople"

    results = requests.get(
        url,
        params=params,
        headers=header
    )
    print(results.json())


if __name__ == '__main__':
    main()