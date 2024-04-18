
import json
import boto3
import hashlib

def calculate_md5(string):
    md5_hash = hashlib.md5()
    md5_hash.update(string.encode('utf-8'))
    return md5_hash.hexdigest()


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('user_todo')
    body = event.get('body')
    
    if not body:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Request body is missing'})
        }
    if not body.strip():  
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Request body is empty'})
        }
    
    try:
        body_dict = json.loads(body)
    except json.JSONDecodeError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid JSON format in the request body'})
        }
    
    salt = 'secret_string'
    
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'OPTIONS,GET,POST,PUT,DELETE'
    } 
    
    user_id = body_dict.get('UserName')
    password = body_dict.get('Password')
    
    if not user_id or not password:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Missing UserName or Password in the request'})
        }
    
    password_with_salt = password + user_id + salt
    md5_password = calculate_md5(password_with_salt)
    
    # Überprüfen, ob der Benutzer bereits existiert
    response = table.get_item(
        Key={
            'UserName': user_id
        }
    )
    if 'Item' in response:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'User already exists'})
        }
    
    # Benutzer hinzufügen
    table.put_item(
        Item={
            'UserName': user_id,
            'Password': md5_password
        }
    )
    
    # Tabelle für den Benutzer erstellen
    
    response = {
        'statusCode': 200,
        'headers': headers,
        'body': json.dumps({'message': 'Benutzer erfolgreich hinzugefügt'})
    }
    
    return response
