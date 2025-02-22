import pytest
from bot.data_fetcher import DataFetcher

def test_data_fetcher():
    config = {"dex": {"pool_address": "0x123"}}
    fetcher = DataFetcher(config, "https://mainnet.infura.io/v3/YOUR_KEY")
    data = fetcher.fetch()
    assert "price" in data
