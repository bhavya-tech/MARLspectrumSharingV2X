import numpy as np
from modified_main_test import a
import csv

payload = np.arange(1,6,0.5)

# Write header
with open('test2.csv','w') as f:
    write = csv.writer(f)
    write.writerow(['payload', 'marl_sum', 'marl_pr', 'sarl_sum', 'sarl_pr', 'rand_sum', 'rand_pr', 'drpa_sum', 'drpa_pr'])


for demand_size in payload:
    with open('test2.csv','a') as f:
        write = csv.writer(f)
        out = [float(n) for n in a(demand_size)]
        print(out)
        print(type(out))     
        write.writerow(out)

# df = pd.DataFrame(out, columns=['payload', 'marl_sum', 'marl_pr', 'sarl_sum', 'sarl_pr', 'rand_sum', 'rand_pr', 'drpa_sum', 'drpa_pr'])
# df.to_csv(r'./out.csv', header= True)

