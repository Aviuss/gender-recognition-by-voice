import os
from main import main
import json

if __name__ == "__main__":
    train_dataset = list(map(lambda x:("./train/"+x, x[-5]), os.listdir("./train")))
    
    
    from_hz_range = [0, 40, 80]
    to_hz_range = [100, 260, 300, 340, 380, 1000, 1500]
    iterations_range = [3, 4, 5]
    
    
    it = 0
    to_do = len(train_dataset) * len(from_hz_range) * len(to_hz_range) * len(iterations_range)

    results = []
    with open('./results.json', 'r') as f:
        results = json.load(f)

    for from_hz in from_hz_range:
        for to_hz in to_hz_range:
            if to_hz <= from_hz:
                break
            for iterations in iterations_range:
                for (path, gender) in train_dataset:
                    for r in results:
                        if from_hz == r[0] and from_hz == r[1] and iterations == r[2]:
                            break

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