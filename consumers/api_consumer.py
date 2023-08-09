from .abstract_consumer import AbstractConsumer
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import pandas as pd
import json


class ApiConsumer(AbstractConsumer):
    def __init__(self, base_url, headers: dict, **options) -> None:
        pass
        self.base_url = base_url
        self.headers = headers

    def get(self, parameters: dict, **options) -> json:
        """Get data from an API.

        Args:
            parameters (dict): Parameters to get data from the API.:
                endpoint (str): Path of the endpoint you want to consume to concat with the base_url you set to instance the Consumer.
                request_parameters (dict, optional): Parameters to include in the API request.

        Returns:
            json: JSON with the consumed data.
        """

        session = Session()
        session.headers.update(self.headers)

        options.update(parameters)
        endpoint = options.get("endpoint")
        url = self.base_url + endpoint
        request_parameters = options.get("request_parameters", {})

        try:
            response = session.get(url, params=request_parameters)
            data = json.loads(response.text)
            return data
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
