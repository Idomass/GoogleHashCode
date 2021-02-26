#! /usr/bin/env python3
from street import Street

class Car:
    def __init__(self, path_length: str, *streets: Street):
        self.path_length = path_length
        self.streets = streets

    def __str__(self):
        out_str = 'Car class:\n'
        out_str += f'{self.path_length=}\n'
        for street in self.streets:
            out_str += '   '.join(str(street).splitlines(True)) + '\n'
        return out_str


if __name__ == '__main__':
    streets = []
    streets.append(Street('1', '17', 'Eli Eildis blvd.', 18))
    streets.append(Street('9', '5', 'Moshe blvd.', 3))
    streets.append(Street('0', '1', 'Noder blvd.', 7))

    print(Car(len(streets), streets))
