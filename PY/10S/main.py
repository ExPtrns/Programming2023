import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
list_robots = list()
list_humans = list()
for i in range(len(lst)):
    if lst[i] == 'robot':
        list_robots.append(1)
        list_humans.append(0)
    else:
        list_robots.append(0)
        list_humans.append(1)
data = pd.DataFrame({'robot': list_robots})
data.loc[:, "human"] = list_humans
print(data)

