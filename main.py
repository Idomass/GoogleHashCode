#! /usr/bin/env python3
from argparse import ArgumentParser
from street import Street
from car import Car
from data import GlobalData, MetaData


def parse_file(file):
    GlobalData.meta_data = MetaData(*file.readline().split())

    for street_num in range(GlobalData.meta_data.streets):
        GlobalData.streets.append(Street(*file.readline().split()))

    for car_num in range(GlobalData.meta_data.cars):
        GlobalData.cars.append(Car(*file.readline().split()))

if __name__ == '__main__':
    parser = ArgumentParser('GoogleHashCode solver')
    parser.add_argument('filename', help='Input file for the problem')

    args = parser.parse_args()

    with open(args.filename) as input_file:
        parse_file(input_file)
