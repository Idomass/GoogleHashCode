class Intersection:
    def __init__(self, id):
        self.id = id

        self.ingoing_streets = []
        self.outgoing_streets = []

    def add_ingoing_street(self, street_name: str):
        self.ingoing_streets.append(street_name)

    def add_outgoing_street(self, street_name: str):
        self.outgoing_streets.append(street_name)