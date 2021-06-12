import numpy as np
from modified_main_test import a
import csv
from multiprocessing import Process

def interface(demand_size):
    out = a(demand_size)

    with open('fig3_4_async.csv','a') as f:
        write = csv.writer(f)
        write.writerow(out)


def main():
    with open('fig3_4_async.csv','w') as f:
        write = csv.writer(f)
        write.writerow(['payload', 'marl_sum', 'marl_pr', 'sarl_sum', 'sarl_pr', 'rand_sum', 'rand_pr', 'drpa_sum', 'drpa_pr'])

    payload = [[1,2,3],[4,5,6]]

    for _3_parallel_proc in payload:
        procs = [Process(target=interface, args=(demand_size,)) for demand_size in _3_parallel_proc]
        for p in procs:
            p.start()
        
        for p in procs:
            p.join()

if __name__ == '__main__':
    main()

