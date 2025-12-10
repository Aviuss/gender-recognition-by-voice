import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def drawPlot(data):
    x = [d[0] for d in data]
    values = [d[-1] for d in data]

    max_value = max(values)
    max_points = list(filter(lambda x:x[-1] == max_value, data))
    print("Point(s) with highest value:", max_points)
    for mx, _, my in max_points:
        plt.scatter(mx, my, color='red')
        
    plt.plot(x, values, marker='', linestyle='-', color='blue')
    plt.xlabel('hpc iterations')
    plt.ylabel('correct percentage')
    plt.legend()
    plt.show()


def calculatePercentage(list, threshold):
    correct = 0
    for e in list:
        r = "M"
        if e[1] >= threshold:
            r = "K"
        if r == e[2]:
            correct += 1
    return correct / len(list)

if __name__ == "__main__":
    file = open("results.json", "r")
    results = json.load(file) # [from_hz, to_hz, iterations, result (threshold), gender]
    file.close()
    
    config_and_results = []

    while len(results) != 0:
        sample = results[0]
        print("Left to be done:", len(results))
        selected_config = list(filter(lambda x:x[0] == sample[0], results))
        results = list(filter(lambda x:not (x[0] == sample[0]), results))

        best_threshold = None
        percentage_value = None
        PRECISION = 100
        for t in range(85, 255 + 1, 1):
            for i in range(PRECISION):
                threshold = t + i/PRECISION
                perct = calculatePercentage(selected_config, threshold)
                
                if best_threshold == None:
                    percentage_value = perct
                    best_threshold = threshold
                if percentage_value < perct:
                    percentage_value = perct
                    best_threshold = threshold

        config_and_results.append([sample[0], best_threshold, percentage_value])

    with open('./config_and_results.json', 'w+') as f:
        f.write(json.dumps(config_and_results))

    drawPlot(config_and_results)