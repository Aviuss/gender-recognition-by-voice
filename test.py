import os
from main import main
import json

if __name__ == "__main__":
    train_dataset = list(map(lambda x:("./train/"+x, x[-5]), os.listdir("./train")))
    
    
    from_hz_range = [60, 70, 80, 85, 90]
    to_hz_range = [250, 255, 260, 270, 280]
    iterations_range = [3, 4, 5, 6]
    
    
    it = 0
    to_do = len(train_dataset) * len(from_hz_range) * len(to_hz_range) * len(iterations_range)

    results = []

    for from_hz in from_hz_range:
        for to_hz in to_hz_range:
            for iterations in iterations_range:
                for (path, gender) in train_dataset:
                    result = main(
                        path,
                        no_print=True,
                        return_dominant_freq = True,
                        from_hz = from_hz,
                        to_hz = to_hz,
                        iterations = iterations
                    )

                    results.append([from_hz, to_hz, iterations, result, gender])
                    it += 1
                    
            print("done:", round(it / to_do * 10000) / 100, "%")

    with open('./results.json', 'w+') as f:
        f.write(json.dumps(results))