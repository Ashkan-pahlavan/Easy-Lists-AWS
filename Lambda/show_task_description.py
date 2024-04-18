import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('items')

def lambda_handler(event, context):
    try:
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS,GET,POST,PUT,DELETE'
        }
        list_name = event['queryStringParameters']['listName']
        user_name = event['queryStringParameters']['UserName']  

        # Abfrage zum Abrufen aller Aufgaben für den angegebenen Listenname und Benutzername
        response = table.query(
            KeyConditionExpression='ListName = :list_name',  # Nach ListName filtern
            FilterExpression='UserName = :user_name',  # Nach UserName filtern
            ExpressionAttributeValues={
                ':list_name': list_name,
                ':user_name': user_name
            }
        )

        # Extrahiere die Aufgaben aus der Antwort
        tasks = [{
            'task': item['TaskDescription'],
            'checked': item['checked']
        } for item in response['Items']]

        # Erfolgreiche Antwort mit den Aufgaben
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps(tasks)
        }

    except Exception as e:
        # Fehlerbehandlung
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
