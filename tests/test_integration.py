import unittest
from typing import Dict, List

from fastapi.testclient import TestClient
from requests import Response

from main import app
from tests.utilities import generate_parameters_list


class IntegrationTests(unittest.TestCase):
    _client: TestClient = TestClient(app)
    _grid: List[Dict[str, int | bool]] = generate_parameters_list()
    _path: str = "/profit_calculator"

    def test_api_call(self):
        for params in list(self._grid):
            response: Response = self._client.get(self._path, params=params)
            self.assertEqual(200, response.status_code)
            result: Dict[str, int] = response.json()
            self.assertTrue("profit" in result)
            self.assertTrue(isinstance(result["profit"], int))

    def test_wrong_params(self):
        response: Response = self._client.get(self._path, params={})
        self.assertEqual(422, response.status_code)