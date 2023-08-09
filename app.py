from credentials.credentials import CredentialsEnum
from consumers.api_consumer import ApiConsumer
import pandas as pd


def main():
    base_url = CredentialsEnum.coin_market_cap.value["base_url"]
    api_key = CredentialsEnum.coin_market_cap.value["api_key"]
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": api_key,
    }
    consumer = ApiConsumer(base_url, headers)

    data = consumer.get(
        parameters={
            "endpoint": "/v2/cryptocurrency/quotes/latest",
            "request_parameters": {
                "symbol": "BTC",
                "convert": "BRL",
            },
        }
    )

    df = pd.json_normalize(data["data"]["BTC"])
    print(df.head())


if __name__ == "__main__":
    main()
