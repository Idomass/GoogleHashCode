import argparse
from street import Street
from intersection import Intersection
class MetaData():
    def __init__(self, simulation_duration, intersections_number, streets_number, cars_number, bonus_points):
        self.simulation_duration = simulation_duration
        self.intersections_number = intersections_number
        self.streets_number = streets_number
        self.cars_number = cars_number
        self.bonus_points = bonus_points


def get_args():
    args = argparse.ArgumentParser()
    args.add_argument('file_name', help='The name of the input data file')
    return args.parse_args()

def handle_input(data_file):
    with open(data_file) as data:
        data_lines = data.readlines()

    meta_data = data_lines[0].split()
    meta_data = MetaData(int(meta_data[0]), int(meta_data[1]), int(meta_data[2]), int(meta_data[3]), int(meta_data[4]))
    streets = []
    for street in data_lines[1:meta_data.streets_number + 1]:
        splitted_street = street.split()
        streets.append(Street(Intersection(int(splitted_street[0])), Intersection(int(splitted_street[1])), splitted_street[2], int(splitted_street[3])))
