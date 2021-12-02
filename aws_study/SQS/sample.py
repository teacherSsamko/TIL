import boto3

# Get the service resource
sqs = boto3.client("sqs")

queue_url = "https://sqs.us-west-2.amazonaws.com/123451341234/testq"

# Get the queue
queue = sqs.receive_message(QueueUrl=queue_url)

print(queue)
for message in queue.get("Messages"):
    if message:
        MessageId = message.get("MessageId")
        print(MessageId, message.get("Body"))
