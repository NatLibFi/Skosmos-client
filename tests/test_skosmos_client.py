"""Unit tests for SkosmosClient class"""

from skosmos_client import SkosmosClient, API_BASE
import os.path
import json
import unittest.mock
import pytest


@pytest.fixture(scope='module')
def client():
    return SkosmosClient()


def test_create_client_default():
    client = SkosmosClient()
    assert isinstance(client, SkosmosClient)
    assert client.api_base == API_BASE


def test_create_client_api_base():
    client = SkosmosClient('http://localhost/Skosmos/rest/v1/')
    assert isinstance(client, SkosmosClient)
    assert client.api_base == 'http://localhost/Skosmos/rest/v1/'


def test_vocabularies(client):
   with unittest.mock.patch('requests.get') as mock_request:
        # create a mock response whose .json() method returns the JSON data
        # that we read from a file
        mock_response = unittest.mock.Mock()
        datafile = os.path.join(os.path.dirname(__file__), 'data/vocabularies.json')
        with open(datafile) as jsonfile:
            mock_response.json.return_value = json.load(jsonfile)
        mock_request.return_value = mock_response

        result = client.vocabularies('fi')
        assert len(result) == 3
