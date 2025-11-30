import os
from main import main

if __name__ == "__main__":
    train_dataset = list(map(lambda x:("./train/"+x, x[-5]), os.listdir("./train")))
    
    correct = 0
    it = 0
    for (path, gender) in train_dataset:
        result = main(path, True)
        if  result == gender:
            correct += 1

        it += 1
        print("done:", round(it / len(train_dataset) * 10000) / 100, "%")

    print("\nAccuracy:", round(correct / len(train_dataset) * 10000) / 100, "%")
    print("Test set length:", len(train_dataset))