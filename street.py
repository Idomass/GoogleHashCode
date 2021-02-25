from intersection import Intersection

class Street:
    def __init__(self, intersection1, intersection2, name: str, length: int):
        self.name = name
        self.length = length

        self.ingoing_intersection = intersection1
        self.outgoing_intersection = intersection2

        self.ingoing_intersection.add_ingoing_street(self.name)
        self.outgoing_intersection.add_outgoing_street(self.name)

if __name__ == '__main__':
    a = Intersection(1)
    b = Intersection(2)
    c = Intersection(3)

    street = Street(a, b, 'Bruh', 3)
    street2 = Street(b, c, "Eli eildis blvd.", 6)
    print('Street ->', street.__dict__)
    print('Street ->', street2.__dict__)
    print('Intersection ->', a.__dict__)
    print('Intersection ->', b.__dict__)
