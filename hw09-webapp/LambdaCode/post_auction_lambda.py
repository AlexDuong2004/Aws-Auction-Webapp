import json
import boto3
import decimal

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table("HW09-Auctions")

def convert_decimals(obj):
    for key, value in obj.items():
        if isinstance(value, decimal.Decimal):
            obj[key] = float(value)
    return obj


def post_auction_handler(event, context):
    try:
        auctionId = event["auctionId"]
        item_name = event["itemName"]
        reserve = decimal.Decimal(str(event["reserve"]))   
        description = event["description"]
        status = event["status"]
        winningUserId = event["winningUserId"]

        item = {
            "auctionId": auctionId,
            "itemName": item_name,
            "reserve": reserve,
            "description": description,
            "status": status,
            "winningUserId": winningUserId
        }
        print(convert_decimals(item))
        table.put_item(Item=item)

        return {
            "statusCode": 201,
            "body": json.dumps({
                "message": "Auction item created",
                "data": convert_decimals(item)
            })
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"The auction items were not created": str(e)})
        }