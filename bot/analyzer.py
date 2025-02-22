class Analyzer:
    def __init__(self, config):
        self.config = config

    def analyze(self, data):
        # Example: Checking price deviation
        target_range = self.config["price_control"]["target_range"]
        if data["price"] < target_range[0]:
            return {"action": "buy"}
        elif data["price"] > target_range[1]:
            return {"action": "sell"}
        return {"action": "hold"}
