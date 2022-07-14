from pprint import pprint

import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException


# from django.contrib.auth.models import User

# from accounts.models import UserInfo

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = "SENDINBLUE API KEY"

api_instance = sib_api_v3_sdk.ContactsApi(sib_api_v3_sdk.ApiClient(configuration))

userinfo = {
    "email": "test@gmail.com",
    "first_name": "Eunsub",
    "last_name": "LEE"
}

TEST_LIST_ID = 5
MOVE_TEST_LIST_ID = 2
TEST_USER_ID = 3
MARKETING_AUTOMATION_FOLDER_ID = 3


def create_contact(userinfo):
    create_contact = sib_api_v3_sdk.CreateContact(
        email=userinfo.get("email"),
        attributes={
            "first_name": "Eunsub",
            "last_name": "LEE"
        }, # The attributes need to exsist already
        list_ids=[2]
    ) # CreateContact | Values to create a contact

    try:
        # Create a contact
        api_response = api_instance.create_contact(create_contact)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactsApi->create_contact: %s\n" % e)

def get_contacts():
    limit = 50 # int | Number of documents per page (optional) (default to 50)
    offset = 0 # int | Index of the first document of the page (optional) (default to 0)
    modified_since = 'modified_since_example' # str | Filter (urlencoded) the contacts modified after a given UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). Prefer to pass your timezone in date-time format for accurate result. (optional)
    sort = 'desc' # str | Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed (optional) (default to desc)

    try:
        # Get all the contacts
        api_response = api_instance.get_contacts(limit=limit, offset=offset, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactsApi->get_contacts: %s\n" % e)

def update_contact(instance):
    user_data = {
        "EMAIL":instance.get("email"),
        "FNAME":instance.get("first_name"),
        "LNAME":instance.get("last_name"),
    }
    update_contact = sib_api_v3_sdk.UpdateContact(user_data)
    try:
        res = api_instance.update_contact(instance.get("email"), update_contact)
        print("RESPONSE:\n\t", res)
    except ApiException as e:
        print("Exception when calling ContactsApi->update_contact: %s\n" % e)

def get_lists():
    limit = 10 # int | Number of documents per page (optional) (default to 10)
    offset = 0 # int | Index of the first document of the page (optional) (default to 0)
    sort = 'desc' # str | Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed (optional) (default to desc)

    try:
        # Get all the lists
        api_response = api_instance.get_lists(limit=limit, offset=offset, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactsApi->get_lists: %s\n" % e)

def add_to_list(instance: dict):
    list_id = TEST_LIST_ID
    # list_id = settings.SENDINBLUE_WAIT_LIST_ID
    contact_emails = sib_api_v3_sdk.AddContactToList([instance.get("email")])
    try:
        res = api_instance.add_contact_to_list(list_id, contact_emails)
        print("RESPONSE:\n\t", res)
    except ApiException as e:
        print("Exception when calling ContactsApi->add_contact_to_list: %s\n" % e)

def move_to_another_list(instance):
    TARGET_LIST_ID = MOVE_TEST_LIST_ID
    ORIGIN_LIST_ID = TEST_LIST_ID

    print("BEFORE MOVING")
    get_contacts()

    # Add to target list
    contact_emails = sib_api_v3_sdk.AddContactToList([instance.get("email")])
    try:
        res = api_instance.add_contact_to_list(TARGET_LIST_ID, contact_emails)
        print("RESPONSE:\n\t", res)
    except ApiException as e:
        print("Exception when calling ContactsApi->add_contact_to_list: %s\n" % e)

    # Remove from origin list
    contact_emails = sib_api_v3_sdk.RemoveContactFromList([instance.get("email")]) # RemoveContactFromList | Emails addresses OR IDs of the contacts

    try:
        # Delete a contact from a list
        api_response = api_instance.remove_contact_from_list(ORIGIN_LIST_ID, contact_emails)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactsApi->remove_contact_from_list: %s\n" % e)

    print("AFTER MOVING")
    get_contacts()

def create_list(name):
    create_list = sib_api_v3_sdk.CreateList(name=name, folder_id=MARKETING_AUTOMATION_FOLDER_ID) # CreateList | Values to create a list

    try:
        # Create a list
        api_response = api_instance.create_list(create_list)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactsApi->create_list: %s\n" % e)

def get_folders():
    limit = 10 # int | Number of documents per page (default to 10)
    offset = 0 # int | Index of the first document of the page (default to 0)
    sort = 'desc' # str | Sort the results in the ascending/descending order of record creation. Default order is **descending** if `sort` is not passed (optional) (default to desc)

    try:
        # Get all folders
        api_response = api_instance.get_folders(limit, offset, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactsApi->get_folders: %s\n" % e)

if __name__ == '__main__':
    # create_contact(userinfo)
    # get_contacts()
    # update_contact(userinfo)
    get_lists()
    # add_to_list(userinfo)
    # move_to_another_list(userinfo)
    # create_list()
    # get_folders()
