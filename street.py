class Street:
    def __init__(self, intersection1: int, intersection2: int, name: str, length: int):
        self.name = name
        self.length = length

        self.start_intersection = intersection1
        self.end_intersection = intersection2

        self.total_cars_number = 0

    def __str__(self):
        out_str = '--------------------------\n'
        out_str += 'Street Object:\n'
        out_str += 'Name: ' + self.name + '\n'
        out_str += 'Length: ' + str(self.length) + '\n'
        out_str += 'Ingoing intersection:\n' + str(self.start_intersection)
        out_str += 'outgoing intersection:\n' + str(self.end_intersection)
        out_str += '--------------------------\n'

        return out_str
