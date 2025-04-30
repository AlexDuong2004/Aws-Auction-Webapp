import json
import boto3
import decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table("HW09-Auctions")

def decimal_to_float(item):
    for key, value in item.items():
        if isinstance(value, decimal.Decimal):
            item[key] = float(value)
    return item

def get_auction_handler(event, context):
    auction_id = event.get('auctionId') 

    try:
        if auction_id:
            response = table.get_item(Key={'auctionId': auction_id})

            if 'Item' in response:
                item = decimal_to_float(response['Item'])
                print(item)
                return {
                    'statusCode': 200,
                    'body': json.dumps(item)
                }
            else:
                return {
                    'statusCode': 404,
                    'body': json.dumps({"message": "Auction not found"})
                }
        else:
            response = table.scan()
            items = [decimal_to_float(item) for item in response.get('Items', [])]
            print(items)
            return {
                'statusCode': 200,
                'body': json.dumps(items)
            }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({"message": "An error occurred while fetching auctions"})
        }
