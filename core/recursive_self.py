class RecursiveSelf:
    def __init__(self):
        self.identity_state = 0

    def update(self, predicted_state):
        self.identity_state += predicted_state["future_state"]
        return self

    def perturbation_score(self):
        return abs(self.identity_state % 1)

    def respond(self):
        return {"type": "response", "content": "I am evolving"}
