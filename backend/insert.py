import boto3

def insert_data(event):
    instance = event['fname']
    region = event['lname']
    action = event['action']

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('connect-ec2')

    table.put_item(Item={
        'instanceid': instance,
        'region': region,
        'action': action
    })

    return {"message": "data saved to DynamoDB"}
