import os
from main import main
import json 

if __name__ == "__main__":
    train_dataset = list(map(lambda x:("./train/"+x, x[-5]), os.listdir("./train")))
    
    
    iterations_range = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    
    
    it = 0
    to_do = len(iterations_range)

    results = []
    for iterations in iterations_range:
        it += 1

        for (path, gender) in train_dataset:
            result = main(
                path,
                no_print=True,
                return_dominant_freq = True,
                iterations = iterations
            )

            results.append([iterations, result, gender])
            
        print("done:", round(it / to_do * 10000) / 100, "%")


    with open('./results.json', 'w+') as f:
        f.write(json.dumps(results))