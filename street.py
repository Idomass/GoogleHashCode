#! /usr/bin/env python3
from data import GlobalData

class Street:
    def __init__(self, intersection1: str, intersection2: str, name: str, length: str):
        self.intersection1 = int(intersection1)
        self.intersection2 = int(intersection2)
        self.name = name
        self.length = int(length)

    def __str__(self):
        out_str = f'{self.name} Street:\n'
        out_str += f'   {self.intersection1=}\n'
        out_str += f'   {self.intersection2=}\n'
        out_str += f'   {self.length=}'
        return out_str


if __name__ == '__main__':
    print(Street('1', '17', 'Eli Eildis blvd.', 18))
