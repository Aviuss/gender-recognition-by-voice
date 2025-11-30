import os
from main import main
import json 

if __name__ == "__main__":
    train_dataset = list(map(lambda x:("./train/"+x, x[-5]), os.listdir("./train")))
    
    
    from_hz_range = [40, 43, 46, 49, 52]
    to_hz_range = [300, 400, 500, 10000]
    iterations_range = [4]
    
    
    it = 0
    to_do = len(from_hz_range) * len(to_hz_range) * len(iterations_range)

    results = []
    with open('./results.json', 'r') as f:
        results = json.load(f)


    calculated = []
    for r in results:
        found = False
        for c in calculated:
            if c[0] == r[0] and c[1] == r[1] and c[2] == r[2]:
                found = True
                break
        if not found:
            calculated.append([r[0], r[1], r[2]])

    for from_hz in from_hz_range:
        for to_hz in to_hz_range:
            if to_hz <= from_hz:
                break
            for iterations in iterations_range:
                it += 1
                found = False
                for r in calculated:
                    if from_hz == r[0] and to_hz == r[1] and iterations == r[2]:
                        found = True
                        break
                if found:
                    break

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
                    
                print("done:", round(it / to_do * 10000) / 100, "%")
        
        with open('./results.json', 'w+') as f:
            f.write(json.dumps(results))
            print("saved current results")

    with open('./results.json', 'w+') as f:
        f.write(json.dumps(results))