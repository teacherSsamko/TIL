# Restore local dynamodb for test

## Notice

- 8080 port is used for local dynamodb in this article (default port is 8000)

restore command:  
`aws dynamodb restore-table-from-backup \
--target-table-name david_test-dev \
--backup-arn arn:aws:dynamodb:us-west-2:123456123456:table/test_set/backup/01649221905474-e0b1816e \
--endpoint-url http://localhost:8080`

- restore-table-from-backup using backup-arn on real dynamodb is not working in local dynamodb

```bash
--generate-cli-skeleton (string) Prints a  JSON  skeleton  to  standard
       output without sending an API request. If provided with no value or the
       value input, prints a sample input JSON that can be used as an argument
       for --cli-input-json. Similarly, if provided yaml-input it will print a
       sample input YAML that can be used with --cli-input-yaml.  If  provided
       with  the  value  output, it validates the command inputs and returns a
       sample output JSON for that command.
```

## Describe Table

`aws dynamodb describe-table --table-name origin_table > table_description.json`

## Scan Table

`aws dynamodb scan --table-name origin_table > table_scan.json`

## Get CLI Skeleton

`aws dynamodb create-table --generate-cli-skeleton > dynamodb_skeleton.json`

```json
{
    "AttributeDefinitions": [
        {
            "AttributeName": "",
            "AttributeType": "S"
        }
    ],
    "TableName": "",
    "KeySchema": [
        {
            "AttributeName": "",
            "KeyType": "RANGE"
        }
    ],
    "LocalSecondaryIndexes": [
        {
            "IndexName": "",
            "KeySchema": [
                {
                    "AttributeName": "",
                    "KeyType": "HASH"
                }
            ],
            "Projection": {
                "ProjectionType": "ALL",
                "NonKeyAttributes": [
                    ""
                ]
            }
        }
    ],
    "GlobalSecondaryIndexes": [
        {
            "IndexName": "",
            "KeySchema": [
                {
                    "AttributeName": "",
                    "KeyType": "HASH"
                }
            ],
            "Projection": {
                "ProjectionType": "KEYS_ONLY",
                "NonKeyAttributes": [
                    ""
                ]
            },
            "ProvisionedThroughput": {
                "ReadCapacityUnits": 0,
                "WriteCapacityUnits": 0
            }
        }
    ],
    "BillingMode": "PROVISIONED",
    "ProvisionedThroughput": {
        "ReadCapacityUnits": 0,
        "WriteCapacityUnits": 0
    },
    "StreamSpecification": {
        "StreamEnabled": true,
        "StreamViewType": "KEYS_ONLY"
    },
    "SSESpecification": {
        "Enabled": true,
        "SSEType": "AES256",
        "KMSMasterKeyId": ""
    },
    "Tags": [
        {
            "Key": "",
            "Value": ""
        }
    ]
}
```

## Create Table

`aws dynamodb create-table --cli-input-json file://dynamodb_skeleton.json --endpoint-url http://localhost:8080`

## Set data

`aws dynamodb batch-write-item --generate-cli-skeleton >> batch_write_item_skeleton.json`

```json
{
    "RequestItems": {
        "KeyName": [
            {
                "PutRequest": {
                    "Item": {
                        "KeyName": {
                            "S": "",
                            "N": "",
                            "B": null,
                            "SS": [
                                ""
                            ],
                            "NS": [
                                ""
                            ],
                            "BS": [
                                null
                            ],
                            "M": {
                                "KeyName": {}
                            },
                            "L": [
                                {}
                            ],
                            "NULL": true,
                            "BOOL": true
                        }
                    }
                },
                "DeleteRequest": {
                    "Key": {
                        "KeyName": {
                            "S": "",
                            "N": "",
                            "B": null,
                            "SS": [
                                ""
                            ],
                            "NS": [
                                ""
                            ],
                            "BS": [
                                null
                            ],
                            "M": {
                                "KeyName": {}
                            },
                            "L": [
                                {}
                            ],
                            "NULL": true,
                            "BOOL": true
                        }
                    }
                }
            }
        ]
    },
    "ReturnConsumedCapacity": "NONE",
    "ReturnItemCollectionMetrics": "SIZE"
}
```
