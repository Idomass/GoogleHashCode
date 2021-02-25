#!/bin/env/python
from typing import List
from street import Street

class Scheduler:
	# this clase is used for every intersection.
	# list of incoming start + time

	def __init__(self, ingoing_streets : List[Street]):
		self.ingoing_streets = ingoing_streets

	def very_stupid_schedule(self):
		return [(street, 1) for street in self.ingoing_streets]

	def calculate_according_to_total_cars(self):
		total_cars_in_scheduler = 0
		average_seconds_for_street = 5
		my_scheduler = []
		for street in self.ingoing_streets:
			total_cars_in_scheduler += street.total_cars_number

		for street in self.ingoing_streets:
			street_green_time = int((street.total_cars_number / total_cars_in_scheduler) * average_seconds_for_street * len(self.ingoing_streets))
			my_scheduler.append((street.name, street_green_time))

		return my_scheduler



