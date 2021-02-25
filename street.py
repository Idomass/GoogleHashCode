from intersection import Intersection

class Street:
    #                                                   ingoing     outgoing
    def __init__(self, name, duration, intersections: (Intersection, Intersection)):
        self.name = name
        self.duartion = duration

        self.ingoing_intersection = intersections[0]
        self.outgoing_intersection = intersections[1]

        self.ingoing_intersection.add_ingoing_street(self.name)
        self.outgoing_intersection.add_outgoing_street(self.name)
