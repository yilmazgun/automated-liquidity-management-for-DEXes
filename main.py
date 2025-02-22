import os
import yaml
from dotenv import load_dotenv
from bot.data_fetcher import DataFetcher
from bot.analyzer import Analyzer
from bot.strategy_engine import StrategyEngine
from bot.executor import Executor

# Loading configuration
load_dotenv()
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Initializing modules
data_fetcher = DataFetcher(config, os.getenv("RPC_URL"))
analyzer = Analyzer(config)
strategy_engine = StrategyEngine(config)
executor = Executor(config, os.getenv("PRIVATE_KEY"))

# Bot's main loop
def main():
    while True:
        data = data_fetcher.fetch()
        analysis = analyzer.analyze(data)
        strategy = strategy_engine.decide(analysis)
        executor.execute(strategy)

if __name__ == "__main__":
    main()
