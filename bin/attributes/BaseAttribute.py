class BaseAttribute:
    def __init__(self, proof=None):
        self.proof = (proof if type(proof) == list else [proof]) if proof else None

    def add_prove(self, proof):
        self.proof.append(proof)
