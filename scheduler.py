#!/bin/env/python
from typing import List
from street import Street

class Scheduler:
	# this clase is used for every intersection.
	# list of incoming start + time

	def __init__(self, ingoing_streets : List[Street]):
		self.ingoing_streets = ingoing_streets

	def very_stupid_schedule():
		return [(street.name, 2) for street in self.ingoing_streets]