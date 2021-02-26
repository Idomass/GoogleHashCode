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
    streets = {}
    intersections = {}

    def __str__():
        out_str = 'GLOBAL DATA\n'
        out_str += f'{GlobalData.meta_data}\n'
        out_str += 'Cars:\n'
        for car in GlobalData.cars:
            out_str += '   '.join(str(car).splitlines(True)) + '\n'
        return out_str
