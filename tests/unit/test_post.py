import json

import pytest

from calculateStats import app


@pytest.fixture()
def apigw_good_numbers_event():

    return {
        "httpMethod": "POST",
        "body": "{\n    \"numbers\": [\n        1,\n        2,\n        3\n    ]\n}"
    }

@pytest.fixture()
def apigw_empty_body_event():

    return {
        "httpMethod": "POST",
        "body": {}
    }

@pytest.fixture()
def apigw_bad_format_event():

    return {
        "httpMethod": "POST",
        "body": {
            "numbers": [1,2,3]
        }
    }

@pytest.fixture()
def apigw_bad_number_event():

    return {
        "httpMethod": "POST",
        "body": "{\n    \"numbers\": [\n        bar,\n        2,\n        3\n    ]\n}"
    }

@pytest.fixture()
def apigw_neg_number_event():

    return {
        "httpMethod": "POST",
        "body": "{\n    \"numbers\": [\n        -1,\n        -2,\n        3\n    ]\n}"
    }

def test_lambda_handler(apigw_good_numbers_event, mocker):

    ret = app.lambda_handler(apigw_good_numbers_event, "")

    assert ret["statusCode"] == 200
    assert ret["body"] == "{\"mean\": 2, \"median\": 2, \"mode\": 1}"

def test_bad_format(apigw_empty_body_event, mocker):
    ret = app.lambda_handler(apigw_empty_body_event, "")

    assert ret["statusCode"] == 400
    assert ret["body"] == "Invalid input. Please format Json correctly."

def test_bad_format(apigw_bad_format_event, mocker):
    ret = app.lambda_handler(apigw_bad_format_event, "")

    assert ret["statusCode"] == 400
    assert ret["body"] == "Invalid input. Please format Json correctly."

def test_bad_number(apigw_bad_number_event, mocker):
    ret = app.lambda_handler(apigw_bad_number_event, "")
    assert ret["statusCode"] == 400
    assert ret["body"] == "Invalid input. Please provide an array of integers."

def test_neg_number(apigw_neg_number_event, mocker):
    ret = app.lambda_handler(apigw_neg_number_event, "")

    assert ret["statusCode"] == 200
    assert ret["body"] == "{\"mean\": 0, \"median\": -1, \"mode\": -1}"


