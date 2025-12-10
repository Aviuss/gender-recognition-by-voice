import os
from main import main
import json 

if __name__ == "__main__":
    train_dataset = list(map(lambda x:("./train/"+x, x[-5]), os.listdir("./train")))
    
    
    it = 0
    to_do = len(train_dataset)
    correct = 0


    for (path, gender) in train_dataset:
        result = main( path, no_print=True)
        if result == gender:
            correct += 1
        it += 1
        print("done:", round(it / to_do * 10000) / 100, "%")

    print("correct:", round(correct / to_do * 10000) / 100)