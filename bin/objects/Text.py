from bin.objects.Proof import Proof
class Text(Proof):
    def __init__(self, text, reason):
        super().__init__(reason)
        self.text = text