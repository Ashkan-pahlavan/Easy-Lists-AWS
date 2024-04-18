#Token_get_login
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

    salt = 'secret_string'
    

    
    username = json.loads(event['body'])['UserName']
    password = json.loads(event['body'])['Password'] + username + salt
    
    try:
      
        response = table.get_item(
            Key={
                'UserName': username
            }
        )

        item = response.get('Item')
        if not item:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'User not found'})
            }
            
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'OPTIONS,GET,POST,PUT,DELETE'
        } 

        # Überprüfe das Passwort
        stored_password_hash = item.get('Password')
        input_password_hash = calculate_md5(password)

        if stored_password_hash == input_password_hash:
            response = {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps({'message': 'Registrierung erfolgreich!'})
            }
            
            return response
        else:

            return {
                'statusCode': 401,
                'body': json.dumps({'message': 'Unauthorized'})
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }
