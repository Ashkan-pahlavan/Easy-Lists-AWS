import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('lists_names')
table_items = dynamodb.Table('items')

def lambda_handler(event, context):
    try:
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS,GET,POST,PUT,DELETE'
        }
        request_body = json.loads(event['body'])
        userName = request_body.get('UserName')
        listName = request_body.get('listName')

        if not userName or not listName:
            raise ValueError('Ungültige Anfrage: Benutzername und Listennamen sind erforderlich')

        # Löschen des Eintrags aus der Tabelle "lists_names"
        table.delete_item(
            Key={
                'UserName': userName,
                'ListName': listName
            }
        )

        # Löschen aller Einträge mit dem angegebenen Benutzernamen und Listenamen aus der Tabelle "items"
        response_items = table_items.scan(
            FilterExpression=boto3.dynamodb.conditions.Attr('ListName').eq(listName) & boto3.dynamodb.conditions.Attr('UserName').eq(userName)
        )

        for item in response_items['Items']:
            table_items.delete_item(
                Key={
                    'ListName': item['ListName'],
                    'TaskDescription': item['TaskDescription']
                }
            )

        response = {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({'message': f'ListName {listName} für Benutzer {userName} erfolgreich gelöscht'})
        }

    except Exception as e:
        response = {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

    return response
