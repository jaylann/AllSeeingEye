class BaseAttribute:
    def __init__(self, proof):
        self.proof = proof if type(proof) == list else [proof]

    def add_prove(self, proof):
        self.proof.append(proof)
