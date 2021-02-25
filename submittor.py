from scheduler import Scheduler
from typing import Dict

# scheds_list = {inter1_id:[(ingoing_street_name1, green_time), (), ()..], inter2_id:(ingoing_street_name2, green_time)}...

def create_submittion(scheds_list: Dict[int, tuple]):
    with open("solution.txt", 'x') as f:
        f.write(len(sched_list), "\n")
        for intersection, sched in scheds,items():
            f.write(intersection)
            f.write(len(sched), "\n")
            f.write()



