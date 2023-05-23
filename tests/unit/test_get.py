import json

import pytest

from calculateStats import app


@pytest.fixture()
def apigw_good_numbers_event():

    return {
        "httpMethod": "GET",
        "multiValueQueryStringParameters": {
            "numbers": [
                "1",
                "2",
                "3",
                "1"
            ]
        }
    }

@pytest.fixture()
def apigw_bad_number_event():

    return {
        "httpMethod": "GET",
        "multiValueQueryStringParameters": {
            "numbers": [
                "bar",
                "foo",
                "3",
                "1"
            ]
        }
    }

@pytest.fixture()
def apigw_neg_number_event():

    return {
        "httpMethod": "GET",
        "multiValueQueryStringParameters": {
            "numbers": [
                "-1",
                "-2",
                "3"
            ]
        }
    }

def test_lambda_handler(apigw_good_numbers_event, mocker):

    ret = app.lambda_handler(apigw_good_numbers_event, "")

    assert ret["statusCode"] == 200
    assert ret["body"] == "{\"mean\": 1.75, \"median\": 1.5, \"mode\": 1}"

def test_bad_number(apigw_bad_number_event, mocker):
    ret = app.lambda_handler(apigw_bad_number_event, "")
    assert ret["statusCode"] == 400
    assert ret["body"] == "Invalid input. Please provide an array of integers."

def test_neg_number(apigw_neg_number_event, mocker):
    ret = app.lambda_handler(apigw_neg_number_event, "")

    assert ret["statusCode"] == 200
    assert ret["body"] == "{\"mean\": 0, \"median\": -1, \"mode\": -1}"


