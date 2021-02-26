#! /usr/bin/env python3
from argparse import ArgumentParser

class MetaData:
    def __init__(self, duration: str, intersections: str, streets: str, cars: str, bonus: str):
        self.duration       = int(duration)
        self.intersections  = int(intersections)
        self.streets        = int(streets)
        self.cars           = int(cars)
        self.bonus          = int(bonus)

    def __str__(self):
        out_str = 'MetaData Class:\n'
        out_str += f'   {self.duration=}\n'
        out_str += f'   {self.intersections=}\n'
        out_str += f'   {self.streets=}\n'
        out_str += f'   {self.cars=}\n'
        out_str += f'   {self.bonus=}'
        return out_str


class GlobalData:
    meta_data = []
    cars = []
    streets = []
    intersections = []


def parse_file(file):
    GlobalData.meta_data = MetaData(*file.readline().split())


if __name__ == '__main__':
    parser = ArgumentParser('GoogleHashCode solver')
    parser.add_argument('filename', help='Input file for the problem')

    args = parser.parse_args()

    with open(args.filename) as input_file:
        parse_file(input_file)
