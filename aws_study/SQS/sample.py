import json

import boto3

# Get the service resource
sqs = boto3.client("sqs", 'us-west-2')

queue_url = "https://sqs.us-west-2.amazonaws.com/123454/testq"

# Send Message
sample_message = {
    "scene": "upload",
    "pid": 12345,
    "type": "go",
    "detail": {
        "name": "test",
        "id_list": [11, 12, 31]
    }
}

detail_message = {'job_id': '35436', 'kind': 'production', 'mid': '1h1q', 'cid': '1',
                  'ensemble': '0', 'success': 'failure', 'table_name': 'test-dev'}

joblist_message = {
    'table_name': '-dev',
}

submit_message = "python3 -m test.submit "


response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody=json.dumps(new_submit_message)
)

print(json.dumps(response, indent=2))


# Get the queue
response = sqs.receive_message(
    QueueUrl=queue_url, MaxNumberOfMessages=10, MessageAttributeNames=['type'])

for message in response.get("Messages"):
    if message:
        MessageId = message.get("MessageId")
        print(MessageId, message.get("Body"))
print("length", len(response.get("Messages")))
# sqs.delete_message(QueueUrl=queue_url,
#                    ReceiptHandle=message.get("ReceiptHandle"))
body = json.loads(message.get("Body"))
print(body)
