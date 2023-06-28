class Note():
    def __init__(self, name):
        # name is an instance variable
        self.name = name
        self.body = ""

    def SetBody(self, data):
        self.body = data

    def __repr__(self):
        return f" Name: {self.name}\n Body: {self.body}\n"
