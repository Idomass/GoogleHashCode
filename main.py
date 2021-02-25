#! /usr/bin/env python3
from algorithm import UltimateSolver
from input_parser import get_args, handle_input
from submittor import create_submittion
def main():
    args = get_args()
    meta_data, streets, cars = handle_input(args.file_name)
    solver = UltimateSolver(meta_data, streets, cars)
    result = solver.solve()
    create_submittion(result, args.file_name)


if __name__ == '__main__':
    main()