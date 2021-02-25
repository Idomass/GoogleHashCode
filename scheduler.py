#!/bin/env/python

scheduler_list_example = [("ben guryon street", 2), ("shderot yerushalim street", 3)]

class scheduler:
	# this clase is used for every intersection.
	# list of incoming start + time

	def __init__(scheduler_list):
		self.scheduler_list = scheduler_list

	def add_street(street, duration):
		for street_name, duration in self.scheduler_list:
			if street == street_name:
				assert False, "scheduler can't contain two streets!"

		self.scheduler_list.append((street, duration))			
