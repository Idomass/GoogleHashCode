from algorithm import UltimateSolver
from input_parser import get_args, handle_input
from submittor import create_submittion
def main():
    args = get_args()
    meta_data, streets, cars = handle_input(args.file_name)
    solver = UltimateSolver(meta_data, streets, cars)
    result = solver.solve()
    create_submittion(result)


if __name__ == '__main__':
    main()