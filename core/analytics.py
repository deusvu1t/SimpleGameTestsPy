class GameAnalytics:
    def __init__(self):
        self.events = []

    def track_event(self, event):
        self.events.append(event)