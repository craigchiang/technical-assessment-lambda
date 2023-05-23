import json

import pytest

from calculateStats import app


@pytest.fixture()
def apigw_event():

    return {
        "version": "1.0",
        "resource": "/calculate",
        "path": "/Prod/calculate",
        "httpMethod": "GET",
        "headers": {
            "Content-Length": "0",
            "Host": "5m8x8eelki.execute-api.us-east-2.amazonaws.com",
            "Postman-Token": "c41553f5-94e0-4bc9-9bc1-2a1a845a4230",
            "User-Agent": "PostmanRuntime/7.32.2",
            "X-Amzn-Trace-Id": "Root=1-646c2ee1-4cab40ec55b3b1c653464e7e",
            "X-Forwarded-For": "99.43.84.152",
            "X-Forwarded-Port": "443",
            "X-Forwarded-Proto": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br"
        },
        "multiValueHeaders": {
            "Content-Length": [
                "0"
            ],
            "Host": [
                "5m8x8eelki.execute-api.us-east-2.amazonaws.com"
            ],
            "Postman-Token": [
                "c41553f5-94e0-4bc9-9bc1-2a1a845a4230"
            ],
            "User-Agent": [
                "PostmanRuntime/7.32.2"
            ],
            "X-Amzn-Trace-Id": [
                "Root=1-646c2ee1-4cab40ec55b3b1c653464e7e"
            ],
            "X-Forwarded-For": [
                "99.43.84.152"
            ],
            "X-Forwarded-Port": [
                "443"
            ],
            "X-Forwarded-Proto": [
                "https"
            ],
            "accept": [
                "*/*"
            ],
            "accept-encoding": [
                "gzip, deflate, br"
            ]
        },
        "queryStringParameters": {
            "numbers": "1"
        },
        "multiValueQueryStringParameters": {
            "numbers": [
                "1",
                "2",
                "3",
                "1"
            ]
        },
        "requestContext": {
            "accountId": "332914343642",
            "apiId": "5m8x8eelki",
            "domainName": "5m8x8eelki.execute-api.us-east-2.amazonaws.com",
            "domainPrefix": "5m8x8eelki",
            "extendedRequestId": "FWxDPgqTiYcEPew=",
            "httpMethod": "GET",
            "identity": {
                "accessKey": "",
                "accountId": "",
                "caller": "",
                "cognitoAmr": "",
                "cognitoAuthenticationProvider": "",
                "cognitoAuthenticationType": "",
                "cognitoIdentityId": "",
                "cognitoIdentityPoolId": "",
                "principalOrgId": "",
                "sourceIp": "99.43.84.152",
                "user": "",
                "userAgent": "PostmanRuntime/7.32.2",
                "userArn": ""
            },
            "path": "/Prod/calculate",
            "protocol": "HTTP/1.1",
            "requestId": "FWxDPgqTiYcEPew=",
            "requestTime": "23/May/2023:03:11:29 +0000",
            "requestTimeEpoch": 1684811489277,
            "resourceId": "GET /calculate",
            "resourcePath": "/calculate",
            "stage": "Prod"
        },
        "pathParameters": "",
        "stageVariables": "",
        "body": "",
        "isBase64Encoded": False
    }


def test_lambda_handler(apigw_event, mocker):

    ret = app.lambda_handler(apigw_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert ret["body"] == "{\"mean\": 1.75, \"median\": 1.5, \"mode\": 1}"
