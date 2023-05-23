import json
import statistics
import logging
import traceback


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def lambda_handler(event, context):
    logger.info('Received event: {}'.format(json.dumps(event)))
    
    outputDict = {}
    
    try: 
        # keeping the 2 methods together considering low traffic app would have a higher chance of warm start on Lambda
        if event['httpMethod'] == 'GET':
            # if non-integer type getting passed in, it will also raise valueError
            numbers = list(map(int, event['multiValueQueryStringParameters']['numbers']))
        elif event['httpMethod'] == 'POST':
            numbers = json.loads(event['body'])['numbers']
            if any(not isinstance(i,int) for i in numbers): 
                raise ValueError("List elements are not int")
        
    except ValueError as e:
        logger.error(traceback.format_exc())
        return {
            'statusCode': 400,
            'body': 'Invalid input. Please provide an array of integers.'
        }
    except TypeError as e:
        logger.error(traceback.format_exc())
        return {
            'statusCode': 400,
            'body': 'Invalid input. Please format Json correctly.'
        }
    except Except as e:
        logger.error(traceback.format_exc())
        return {
            'statusCode': 400,
            'body': 'Bad request.'
        }

    calculate_stats(numbers, outputDict)
        
    return {
        'statusCode': 200,
        'body': json.dumps(outputDict)
    }

def calculate_stats(numbers, outputDict):
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    mode = statistics.mode(numbers)
        
    outputDict['mean'] = mean
    outputDict['median'] = median
    outputDict['mode'] = mode
