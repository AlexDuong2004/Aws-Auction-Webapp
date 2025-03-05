import json

print("Loading Function In")

def my_function4(event, context):
    # TODO implement
    print(event)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
