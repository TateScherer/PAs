import random
from tabulate import tabulate
import time

times = []
#%%
def dimension1(num_steps):
    
    count = 0
    for i in range(100):
        x = 0
        for j in range(num_steps):
            step = random.choice([-1,1])
            x += step
            if x == 0:
                count += 1
                break
        
    return count
#%%
def dimension2(num_steps):
    
    count = 0
    for i in range(100):
        x, y = 0, 0
        for j in range(num_steps):
            axis = random.choice(['x', 'y'])
            step = random.choice([-1,1])
            if axis == 'x':
                x += step
            else:
                y += step
            if x == 0 and y == 0:
                count += 1
                break
        
    return count
#%%
def dimension3(num_steps):
    
    global times
    
    start = time.time()
    count = 0
    for i in range(100):
        x, y, z = 0, 0, 0
        for j in range(num_steps):
            axis = random.choice(['x', 'y', 'z'])
            step = random.choice([-1,1])
            if axis == 'x':
                x += step
            elif axis == 'y':
                y += step
            else:
                z += step
            if x == 0 and y == 0 and z == 0:
                count += 1
                break
    end = time.time()
    time_passed = end - start
    times.append(time_passed)
    return count

#%%
def main():
    
    data = [
        ["1D", dimension1(20), dimension1(200), dimension1(2000), dimension1(20000), dimension1(200000), dimension1(2000000)],
        ["2D", dimension2(20), dimension2(200), dimension2(2000), dimension2(20000), dimension2(200000), dimension2(2000000)],
        ["3D", dimension3(20), dimension3(200), dimension3(2000),dimension3(20000), dimension3(200000),dimension3(2000000)]]

    headers = ["Number of Steps", "20", "200", "2,000", "20,000", "200,000", "2,000,000"]

    table = tabulate(data, headers, tablefmt="grid")

    print("Percentages of time particle returned to origin:")
    print(table)
    print()
    print("Run time (seconds):")
    print(f"3D    {sum(times)}")

main()
















    