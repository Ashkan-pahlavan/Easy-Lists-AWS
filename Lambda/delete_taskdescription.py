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
        # Extrahiere die Daten aus dem Request-Body
        request_body = json.loads(event['body'])
        list_name = request_body['listName']
        task_description = request_body['taskDescription']

        # Löschen des vorhandenen Elements
        response = table.delete_item(
            Key={
                'ListName': list_name,
                'TaskDescription': task_description
            }
        )

        # Erfolgreiche Antwort
        response = {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({'message': 'TaskDescription und checked erfolgreich gelöscht'})
        }

    except Exception as e:
        # Fehlerbehandlung
        response = {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

    return response
