class Proof:
    def __init__(self, reason):
        self.reason = reason

    def __dict__(self):
        return {"reason": self.reason}