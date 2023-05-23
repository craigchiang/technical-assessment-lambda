# Gaggle Lambda Calculate Stats App

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- calculateStats - Code for the application's Lambda function.
- events - Invocation events that you can use to invoke the function.
- tests - Unit tests for the application code. 
- template.yaml - A template that defines the application's AWS resources.

The application uses several AWS resources, including Lambda functions and an API Gateway API. These resources are defined in the `template.yaml` file in this project.

## Tools requirement
* AWS CLI - [Install the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* Python 3.9 (optional) - [Install Python 3.9](https://www.python.org/downloads/release/python-3916/)
* Pip (optional) - [Install Pip](https://pip.pypa.io/en/stable/installation/)
* Docker (optional) - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community) 
* Postman (optional) - [Install Postman](https://www.postman.com/downloads/) 

## Use the SAM CLI to build and test locally

Build your application with the `sam build` command.

```bash
$ sam build
```

With Docker installed and running on the system, you can test the lambda function by invoking it directly with a test event in events folder.

Run functions locally and invoke them with the `sam local invoke` command.

```bash
$ sam local invoke CalculateStatsFunction --event events/GetEvent.json
```

The SAM CLI can also emulate your application's API. Use the `sam local start-api` to run the API locally on port 3000.

```bash
$ sam local start-api
$ curl http://localhost:3000/
```

## Unit tests

Unit test can be done with the tests in the `tests` folder in this project. Use PIP to install the [pytest](https://docs.pytest.org/en/latest/) and run unit tests from your local machine.

```bash
$ pip install pytest pytest-mock --user
$ python -m pytest tests/ -v
```

## Deployment

To build and deploy your application for the first time, run the following in your shell:

```bash
sam build
sam deploy --guided
```
After successful deployment, you could do the following to tests the application.

- Using curl (with Post method as example)
```bash
curl --location 'https://${api_id}.execute-api.${AWS::Region}.amazonaws.com/Prod/calculate' \
--header 'Content-Type: application/json' \
--data '{
    "numbers": [
        1,
        2,
        3
    ]
}'
```
- Using Postman (with Post method as example)
Select a 'Post' request and for the body, put in the below structure:
```
{
    "numbers": [
        1,
        2,
        3
    ]
}
```

## Cleanup

To delete the application that you created, use the AWS CLI. Assuming you used the defualt project name for the stack name, you can run the following:

```bash
sam delete --stack-name "sam-app"
```
