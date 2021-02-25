class Intersection:
    def __init__(self, id):
        self.id = id

        self.ingoing_streets = []
        self.outgoing_streets = []

    def add_ingoing_street(self, street_name: str):
        self.ingoing_streets.append(street_name)

    def add_outgoing_street(self, street_name: str):
        self.outgoing_streets.append(street_name)

    def __str__(self):
        out_str = '--------------------------\n'
        out_str += 'Intersection Object:\n'
        out_str += 'Id: ' + str(self.id) + '\n'
        out_str += 'Ingoing streets: '
        for street in self.ingoing_streets:
            out_str += street + ','
        out_str += '\nOutgoing streets: '
        for street in self.outgoing_streets:
            out_str += street + ','
        out_str += '\n--------------------------\n'

        return out_str