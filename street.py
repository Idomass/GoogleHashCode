from intersection import Intersection

class Street:
    #                                                   ingoing     outgoing
    def __init__(self, name: str, length: int, intersections: (Intersection, Intersection)):
        self.name = name
        self.length = length

        self.ingoing_intersection = intersections[0]
        self.outgoing_intersection = intersections[1]

        self.ingoing_intersection.add_ingoing_street(self.name)
        self.outgoing_intersection.add_outgoing_street(self.name)

if __name__ == '__main__':
    a = Intersection(1)
    b = Intersection(2)

    street = Street("Bruh", 3, (a, b))
    print('Street ->', street.__dict__)
    print('Intersection ->', a.__dict__)
    print('Intersection ->', b.__dict__)
