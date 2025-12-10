import os
from main import main
import json 

if __name__ == "__main__":
    train_dataset = list(map(lambda x:("./train/"+x, x[-5]), os.listdir("./train")))
    
    
    it = 0
    to_do = len(train_dataset)
    correct = 0

    y_true = []
    y_pred = []
    for (path, gender) in train_dataset:
        result = main( path, no_print=True)
        if result == gender:
            correct += 1
        it += 1
        y_true.append(gender)
        y_pred.append(result)
        print("done:", round(it / to_do * 10000) / 100, "%")

    classes = ["K", "M"]
    
    conf_matrix = [[0 for _ in classes] for _ in classes]

    for t, p in zip(y_true, y_pred):
        conf_matrix[classes.index(t)][classes.index(p)] += 1

    print("Macierz Pomyłek:")
    print(classes)
    for row in conf_matrix:
        print(row)


    print("correct:", round(correct / to_do * 10000) / 100)