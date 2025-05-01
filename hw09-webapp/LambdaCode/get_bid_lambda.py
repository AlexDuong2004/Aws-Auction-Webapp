import json
import boto3
import decimal


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table("HW09-Bids") 

def decimal_to_float(item):
    for key, value in item.items():
        if isinstance(value, decimal.Decimal):
            item[key] = float(value)
    return item

def get_bid_handler(event, context):
    try:
        
        auction_Id = event.get('auctionId')

        if not auction_Id:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "Missing 'auctionId' query parameter"})
            }

        response = table.scan(
            FilterExpression=boto3.dynamodb.conditions.Attr("auctionId").eq(auction_Id)
        )

        bids = [decimal_to_float(item) for item in response.get("Items", [])]

        return {
            "statusCode": 200,
            "body": json.dumps(bids)
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "An error occurred while fetching bids"})
        }
