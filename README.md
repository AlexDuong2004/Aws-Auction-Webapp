# Serverless Auction Platform (AWS + React)

A full-stack, serverless online auction application. Users can register, create auctions, and place bids in real time — built entirely on AWS managed services with a React/TypeScript frontend and an automated CI/CD pipeline.

## Overview

This project demonstrates an end-to-end serverless architecture: a static React SPA calls a REST API backed by AWS Lambda functions, which read and write to DynamoDB. Infrastructure is deployed via GitHub Actions, with no servers to manage.

**Core flows:**
- **Users** — create accounts and set an account balance
- **Auctions** — list open auctions and create new items with a reserve price
- **Bidding** — select an auction, place bids against it, and view the live bid history

## Architecture

```
React SPA (S3 static hosting)
        |
        v
   API Gateway
        |
        v
  AWS Lambda (Python)  --->  DynamoDB
   - get/post users            - Users table
   - get/post auctions         - Auctions table
   - get bids                  - Bids table
```

## Tech Stack

| Layer          | Technology                                 |
|----------------|---------------------------------------------|
| Frontend       | React 19, TypeScript, React Router, Vite, Axios |
| Backend        | AWS Lambda (Python 3, boto3)               |
| Data           | Amazon DynamoDB                            |
| API            | Amazon API Gateway                         |
| Hosting        | Amazon S3 (static website hosting)         |
| CI/CD          | GitHub Actions (self-hosted runners)       |

## Getting Started

### Prerequisites
- Node.js 18+
- An AWS account with API Gateway, Lambda, and DynamoDB already provisioned (see [Backend Setup](#backend-setup))

### Local Development
```bash
cd AWSAuctionApp
npm install
```

Create a `.env` file in `hw09-webapp/` pointing at your API Gateway stage:
```
VITE_REACT_APP_API_BASE=https://<your-api-id>.execute-api.us-east-1.amazonaws.com/prod
```

```bash
npm run dev      # local dev server
npm run build    # production build -> dist/
```

### Deployment
1. Run `npm run build` to generate the `dist/` folder.
2. Upload the contents of `dist/` to an S3 bucket configured for static website hosting.
3. Set the bucket's index document to `index.html`.
4. Browse to the bucket's website endpoint.

### Backend Setup
Each Lambda function expects a corresponding DynamoDB table (`Users`, `Auctions`, `Bids`) and is wired to API Gateway routes for `GET`/`POST` on `/users`, `/auctions`, and `/bids`. Lambda source lives in `AWSAuctionApp/LambdaCode/`.

## CI/CD

GitHub Actions workflows in `.github/workflows/` automatically zip and deploy each Lambda function to AWS on push, using `aws lambda update-function-code`, with credentials injected via repository secrets and jobs running on self-hosted runners.

## Project Structure
```
AWSAuctionApp/
├── src/
│   ├── App.tsx        # routes: /users, /auctions, /bidding/:auctionId
│   ├── Users.tsx
│   ├── Auctions.tsx
│   └── Bidding.tsx
├── LambdaCode/
│   ├── get_user_lambda / post_user_lambda
│   ├── get_auction_lambda.py / post_auction_lambda.py
│   └── get_bid_lambda.py
└── package.json
.github/workflows/       # per-feature CI/CD pipelines
```
