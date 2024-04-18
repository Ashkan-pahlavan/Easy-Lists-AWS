import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('lists_names')
table1 = dynamodb.Table('items')

def lambda_handler(event, context):
    try:
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS,GET,POST,PUT,DELETE'
        }
        request_body = json.loads(event['body'])
        userId = request_body.get('UserName')
        listName = request_body.get('listName')
        taskDescription = request_body.get('task')
        checked = request_body.get('checked', False)  # Standardwert von "checked" ist False, wenn nicht im Anforderungskörper vorhanden

        if userId and listName:  # Überprüfen, ob sowohl UserId als auch ListName vorhanden sind
            # Daten in die Tabelle "lists_names" einfügen
            table.put_item(
                Item={
                    'UserName': userId,
                    'ListName': listName,
                }
            )
        else:
            raise ValueError('Ungültige Anfrage: Benutzer-ID und Listennamen sind erforderlich')

        if listName and taskDescription:  # Überprüfen, ob ListName und TaskDescription vorhanden sind
            # Daten in die Tabelle "items" einfügen
            table1.put_item(
                Item={
                    'ListName': listName,
                    'UserName': userId,
                    'TaskDescription': taskDescription,
                    'checked': checked  # Setzen des "checked"-Attributs basierend auf dem Wert im Anforderungskörper
                }
            )
        else:
            raise ValueError('Ungültige Anfrage: Listennamen und Taskbeschreibung sind erforderlich')

        response = {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({'message': 'Daten erfolgreich in beide Tabellen eingefügt'})
        }

    except Exception as e:
        response = {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

    return response
