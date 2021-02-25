from scheduler import Scheduler
from typing import Dict, List

# solution = {inter1_id:[(ingoing_street_name1, green_time), (), ()..], inter2_id:(ingoing_street_name2, green_time)}...

def create_submittion(solution: Dict[int, List[tuple]], file_name):
    with open("{name}_solution".format(name=file_name), 'w') as f:
        f.write(str(len(solution)) + '\n')
        for intersection, sched in solution.items():
            f.write(str(intersection) + '\n')
            f.write(str(len(sched)) + '\n')
            for street in sched:
                f.write(street[0] + " " + str(street[1]) + '\n')



