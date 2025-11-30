import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def drawPlot(data):
    x = [d[0] for d in data]
    y = [d[1] for d in data]
    z = [d[2] for d in data]
    values = [d[-1] for d in data]

    max_point = max(data, key=lambda d: d[-1])
    print("Point with highest value:", max_point)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    sc = ax.scatter(x, y, z, c=values, cmap='viridis', s=50)
    ax.scatter(max_point[0], max_point[1], max_point[2], color='red', s=150, label='Max value')


    cbar = plt.colorbar(sc)
    cbar.set_label('percentage')

    ax.set_xlabel('from hz')
    ax.set_ylabel('to hz')
    ax.set_zlabel('iterations')

    plt.savefig("3d_plot.png", dpi=300)
    plt.show()

def calculatePercentage(list, threshold):
    correct = 0
    for e in list:
        r = "M"
        if e[3] >= threshold:
            r = "K"
        if r == e[4]:
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
        selected_config = list(filter(lambda x:x[0] == sample[0] and x[1] == sample[1] and x[2] == sample[2], results))
        results = list(filter(lambda x:not (x[0] == sample[0] and x[1] == sample[1] and x[2] == sample[2]), results))

        best_threshold = None
        percentage_value = None
        for t in range(85, 255 + 1, 1):
            for i in range(100):
                threshold = t + i/100
                perct = calculatePercentage(selected_config, threshold)
                
                if best_threshold == None:
                    percentage_value = perct
                    best_threshold = threshold
                if percentage_value < perct:
                    percentage_value = perct
                    best_threshold = threshold

        config_and_results.append([sample[0], sample[1], sample[2], best_threshold, percentage_value])

    with open('./config_and_results.json', 'w+') as f:
        f.write(json.dumps(config_and_results))

    drawPlot(config_and_results)