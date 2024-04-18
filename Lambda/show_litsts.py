import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('lists_names')

def lambda_handler(event, context):
    try:
        # Definiere die Standard-Header
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS,GET,POST,PUT,DELETE'
        }
        
        # Überprüfen, ob der Anforderungskörper nicht None ist
        if 'body' in event and event['body'] is not None:
            # Extrahiere den Benutzernamen aus dem Anforderungskörper
            body = json.loads(event['body'])
            user_name = body.get('UserName')
            if user_name is not None:
                # Abfrage zum Abrufen aller Listennamen für den angegebenen Benutzer
                response = table.query(
                    KeyConditionExpression='UserName = :user_name',
                    ExpressionAttributeValues={
                        ':user_name': user_name
                    }
                )
                # Extrahiere die Listennamen aus der Antwort
                table_names = [item['ListName'] for item in response['Items']]

                # Erfolgreiche Antwort mit den Listennamen
                return {
                    'statusCode': 200,
                    'headers': headers,
                    'body': json.dumps(table_names)
                }
            else:
                # Fehlermeldung, wenn kein Benutzername bereitgestellt wurde
                return {
                    'statusCode': 400,
                    'headers': headers,
                    'body': json.dumps({'error': 'No UserName provided'})
                }
        else:
            # Fehlermeldung, wenn kein Anforderungskörper bereitgestellt wurde
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': 'No body provided in the request'})
            }
    except Exception as e:
        # Fehlerbehandlung für andere Ausnahmen
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': str(e)})
        }

