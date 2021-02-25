from street import Street

class Intersection:
    def __init__(self, id):
        self.id = id

        self.ingoing_streets = []
        self.outgoing_streets = []
        queue_in_street = {}
        self.scheduler = {}



    def add_ingoing_street(self, street_name: Street):
        self.ingoing_streets.append(street_name)

    def add_outgoing_street(self, street_name: Street):
        self.outgoing_streets.append(street_name)

    def add_car_to_street_queue(self, car: Car):
        if car.is_driving:
            return
        else:
            if car.path[car.current_street_index].street_name in queue_in_street:
                queue_in_street[car.path[car.current_street_index].street_name].append(car)
            else:
                queue_in_street[car.path[car.current_street_index].street_name] = [car]

    def calculate_scheduler():
    	self.scheduler.add_ingoing_streets(self.ingoing_streets)
    	self.scheduler.calculate()

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