import logging

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


TECH_DOC_FILE_ID = "1mKtshared_fileIDto2VXAx3-SharedFileID"

logger = logging.getLogger(__name__)


def share_file(real_file_id, real_user):
    """Batch permission modification.
    Args:
        real_file_id: file Id
        real_user: User ID
    Prints modified permissions

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    creds, _ = google.auth.default()

    try:
        service = build('drive', 'v3', credentials=creds)

        ids = []
        file_id = real_file_id

        def callback(request_id, response, exception):
            if exception:
                # Handle error
                print(exception)
            else:
                print(f'Request_Id: {request_id}')
                print(F'Permission Id: {response.get("id")}')
                ids.append(response.get('id'))

        batch = service.new_batch_http_request(callback=callback)
        user_permission = {
            'type': 'user',
            'role': 'reader',
            'emailAddress': 'user@example.com'
        }
        user_permission['emailAddress'] = real_user

        batch.add(service.permissions().create(fileId=file_id,
                                               body=user_permission,
                                               fields='id',
                                               supportsAllDrives=True,
                                               ))
        
        batch.execute()

    except HttpError as error:
        print(F'An error occurred: {error}')
        ids = None

    return ids


if __name__ == '__main__':
    share_file(real_file_id=TECH_DOC_FILE_ID,real_user='teacher.ssamko@gmail.com',real_domain='gmail.com')
# [END drive_share_file]