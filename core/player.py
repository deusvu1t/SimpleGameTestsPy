class Player:
    def __init__(self, analytics, logger):
        self.coins = 0
        self.analytics = analytics
        self.logger = logger

    def add_coins(self, amount):
        self.coins += amount
        self.analytics.track_event("coins_added")
        self.logger.log(f"Coins added: {amount}")

    def spend_coins(self, amount):
        if self.coins >= amount:
            self.coins -= amount
            self.analytics.track_event("purchase_success")
            self.logger.log(f"Purchase success: {amount}")
            return True

        self.analytics.track_event("purchase_failed")
        self.logger.log(f"Purchase failed: {amount}")
        return False