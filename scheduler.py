#!/bin/env/python
from typing import List
from street import Street

class scheduler:
	# this clase is used for every intersection.
	# list of incoming start + time

	def __init__(self, ingoing_streets : List[Street]):
		self.ingoing_streets = ingoing_streets

	def add_street(street, duration):
		for street_name, duration in self.scheduler_list:
			if street == street_name:
				assert False, "scheduler can't contain two streets!"

		self.scheduler_list.append((street, duration))			
