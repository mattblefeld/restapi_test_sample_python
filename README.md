### Introduction
This is a basic set of restful api tests using the python 'requests' package. 
It demonstrates using the get method to get a response from an api, confirm successful responses, and assert pieces of data in the response.
It uses python, requests, and pytest to run the tests.

These tests can be extended into a framework to provide more robust data-driven api testing, as well. Using a csv file, or a database connection, we can retrieve large sets of data to run through the pytest paramterize fixture, which will run the same test on each piece of data.

### How To Run The Tests
Prerequisites: Python 3

Go to the root of this project and type the following:

`pip install -r requirements.txt`

After this next command, test collection should begin and the tests that have the pytest marker "geo" should run

`pytest -m "geo"`

After this next command, test collection should begin and the tests that have the pytest marker "ron" should run.

`pytest -m "ron"`


"# restapi_test_sample_python" 
