#Token_get_login
import json
import boto3
import hashlib

def calculate_md5(string):
    md5_hash = hashlib.md5()
    md5_hash.update(string.encode('utf-8'))
    return md5_hash.hexdigest()
    

def lambda_handler(event, context):
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps(event)
    # }
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('user_todo')  

    salt = 'secret_string'
    
    # Extrahiere Benutzername und Passwort aus dem Pfadparameter (nicht aus dem Anfragekörper)
    # username = event['body']['UserName']
    # password = event['body']['Password'] + salt
    
    username = json.loads(event['body'])['UserName']
    password = json.loads(event['body'])['Password'] + username + salt
    
    print(username)
    # username = event['pathParameters']['UserName']
    # password = event['body']['Password'] + salt
    
    

    # username = 'CCC'
    # password = '111' + salt


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
        # input_password_hash2 = calculate_md5(password2)

        # print(stored_password_hash)
        # print(input_password_hash)
        # print(input_password_hash2)

        if stored_password_hash == input_password_hash:
            # Passwort ist korrekt
            # token_for_auth = 'aB3dE7fG2hI9jK4l'
            response = {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps({'message': 'Registrierung erfolgreich!'})
            }
            
            return response
            # {'token': token_for_auth}
        else:
            # Passwort ist falsch
            return {
                'statusCode': 401,
                'body': json.dumps({'message': 'Unauthorized'})
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }
