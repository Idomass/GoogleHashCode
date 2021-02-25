from intersection import Intersection

class Street:
    def __init__(self, intersection1: Intersection, intersection2: Intersection, name: str, length: int):
        self.name = name
        self.length = length

        self.start_intersection = intersection1
        self.end_intersection = intersection2

        self.start_intersection.add_outgoing_street(self.name)
        self.end_intersection.add_ingoing_street(self.name)


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

if __name__ == '__main__':
    a = Intersection(1)
    b = Intersection(2)
    c = Intersection(3)

    street = Street(a, b, 'Bruh', 3)
    street2 = Street(b, c, "Eli eildis blvd.", 6)
    print(street)
    print(street2)
