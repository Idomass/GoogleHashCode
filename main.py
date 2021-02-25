from algorithm import UltimateSolver
from input_parser import get_args, handle_input

def main():
    args = get_args()
    meta_data, streets, cars = handle_input(args.file_name)
    solver = UltimateSolver(meta_data, streets, cars)
    solver.solver()

if __name__ == '__main__':
    main()