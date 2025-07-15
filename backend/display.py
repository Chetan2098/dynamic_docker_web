import boto3

def get_items():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('connect-ec2')

    response = table.scan()
    return response.get('Items', [])[:3]
