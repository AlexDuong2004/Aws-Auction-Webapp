# Auction App

## Build instructions

* Clone to your local machine
* Create a .env file in the root of the repo. Replace the value below with your prod stage url
    VITE_REACT_APP_API_BASE=https://xxxxxxxxxxxx.execute-api.us-east-1.amazonaws.com/prod
* In a terminal, cd to the root of the webapp
* npm install
* npm run dev   (for running locally)
* npm run build   (to build for deployment)
* Copy the contents of the /dist folder to a public S3 bucket that is enabled for website hosting. (You have a single index.html in the root of the bucket and a /assets folder in the root of the bucket. The /assets folder should have two files withing in.)
* In S3, make the index document be:   index.html
* Note the URL of your public website bucket in the AWS Management Console.
* Enter your website URL into a browser
* The React Web App should work without any further modifications, provided you have implemented all the required routes and methods.

## Users Screen

* Lists the Users and allows you to create new users. 
* Create a few users and give them each a different acctBalance

## Auctions Screen

* Lists the Auctions and allows you to create a new auction.
* Create a few auctions and set different prices for each item
* Select an open auction and press the "Go to Bidding" button navigate to the bidding screen

## Bidding Screen

* Shows the auction details at the top
* Shows all the users that can bid. Select a user and press "Place Bid" to attempt to bud on an item.
* The list of all bids for a given Auction appear to the right. You may need to press the "Refresh" button to refresh the list after attempting a bid.

