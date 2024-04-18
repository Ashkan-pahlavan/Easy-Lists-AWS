import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('items')

def lambda_handler(event, context):
    try:
        # Extrahieren der Daten aus dem Request-Body
        request_body = json.loads(event['body'])
        list_name = request_body['listName']
        task_description = request_body['taskDescription']
        checked = request_body['Checked']

        # Aktualisieren des Status der Aufgabe
        response = table.update_item(
            Key={
                'ListName': list_name,
                'TaskDescription': task_description
            },
            UpdateExpression='SET checked = :c',
            ExpressionAttributeValues={
                ':c': checked
            }
        )

        # Erfolgreiche Antwort
        response = {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,GET,POST,PUT,DELETE'
            },
            'body': json.dumps({'message': 'Aufgabenstatus erfolgreich aktualisiert'})
        }

    except Exception as e:
        # Fehlerbehandlung
        response = {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,GET,POST,PUT,DELETE'
            },
            'body': json.dumps({'error': str(e)})
        }

    return response


