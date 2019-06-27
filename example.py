import boto3
import csv

with open('credentials.csv') as f:
    dr = next(csv.DictReader(f))


dynamodb = boto3.resource('dynamodb',
                          region_name='eu-central-1',
                          endpoint_url="https://dynamodb.eu-central-1.amazonaws.com",
                          aws_access_key_id=dr['Access key ID'],
                          aws_secret_access_key=dr['Secret access key']
                          )


table = dynamodb.create_table(
    TableName='Movies',
    KeySchema=[
        {
            'AttributeName': 'year',
            'KeyType': 'HASH'  # Partition key
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'  # Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={  # downloadable version of DynamoDB ignores it
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)
