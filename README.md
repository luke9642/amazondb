# Amazon DynamoDB
[Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)

## AWS Identity and Access Management (IAM)
IAM controlls, rights to use resources and who is sign in.

[IAM Admin](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)

## Docker

### Image installation
```
docker build -t dynamodb_python
```

### Container run
```
docker run -it -v "`pwd -W`/sampledata":/data dynamodb_python
```

# Downloaded data
[sample data](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/samples/sampledata.zip)

- Open the DynamoDB console at https://console.aws.amazon.com/dynamodb/.
- Choose Create Table.
- In the Create DynamoDB table screen, do the following:

### Create the ProductCatalog Table

- On the Table name box, type ProductCatalog.
- For the Primary key, in the Partition key box, type Id. Set the data type to Number.
- When the settings are as you want them, choose Create.

### Create the Forum Table
- In the Table name box, type Forum.
- For the Primary key, in the Partition key box, type Name. Set the data type to String.

### Create the Thread Table
- In the Table name box, type Thread.
- For the Primary key, do the following:
    - In the Partition key box, type ForumName. Set the data type to String.
    - Choose Add sort key.
    - In the Sort key box, type Subject. Set the data type to String.

### Create the Reply Table
- In the Table name box, type Reply.
- For the Primary key, do the following:
    - In the Partition key box, type Id. Set the data type to String.
    - Choose Add sort key.
    - In the Sort key box, type ReplyDateTime. Set the data type to String.
- In the Table settings section, clear Use default settings.
- In the Secondary indexes section, choose Add index.
- In the Add index window, do the following:
    - For the Primary key, do the following:
        - In the Partition key box, type PostedBy. Set the data type to String.
        - Select Add sort key.
        - In the Sort key box, type Message. Set the data type to String.
    - In the Index name box, type PostedBy-Message-Index.
    - Set the Projected attributes to All.
    - Choose Add index.


# AWS CLI example
```
aws dynamodb create-table
    --table-name Music
    --attribute-definitions AttributeName=Artist,AttributeType=S AttributeName=SongTitle,AttributeType=S
    --key-schema AttributeName=Artist,KeyType=HASH AttributeName=SongTitle,KeyType=RANGE
    --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1
```

### Region example
`eu-central-1`


### Add data

```
aws dynamodb batch-write-item --request-items file://ProductCatalog.json
aws dynamodb batch-write-item --request-items file://Forum.json
aws dynamodb batch-write-item --request-items file://Thread.json
aws dynamodb batch-write-item --request-items file://Reply.json
```

### Check data in console
- Choose the Items tab to view the data that you loaded into the table.
- To view an item in the table, choose its Id.