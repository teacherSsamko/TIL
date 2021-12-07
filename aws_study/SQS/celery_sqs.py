import os

from celery import Celery


#  Celery 4.3.0 was downgrading pycurl to ==7.19.3 instead of ==7.43.0.3.
# $ celery -A tasks worker --loglevel=INFO


access_key = os.environ.get("TF_VAR_access_key")
secret_key = os.environ.get("TF_VAR_secret_key")

broker_url = f"sqs://{access_key}:{secret_key}@"


broker_transport_options = {"region": "us-west-2"}
broker_transport_options["visibility_timeout"] = 30
broker_transport_options["polling_interval"] = 1
broker_transport_options["wait_time_seconds"] = 10
broker_transport_options["queue_name_prefix"] = "hitsweb_"
broker_transport_options["predefined_queues"] = {
    "request": {
        "url": "https://sqs.us-west-2.amazonaws.com/1234/request_dev",
        "access_key_id": access_key,
        "secret_access_key": secret_key,
        "backoff_policy": {
            1: 10,
            2: 20,
            3: 40,
            4: 80,
            5: 320,
            6: 640,
        },
    }
}

app = Celery("tasks", config_source=broker_transport_options)


@app.task
def add(x, y):
    return x + y
