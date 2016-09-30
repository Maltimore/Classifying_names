import numpy as np
import math
import random
import pdb


class name_classifier:
    def __init__(self):
        self.names = set()
        self.load("names_from_wikipedia.txt")
        self.load("CSV_Database_of_First_Names.txt")
        self.load("CSV_Database_of_Last_Names.txt")
        pass

    def load(self, dataset):
        with open(dataset, "r") as f:
            for idx, name in enumerate(f.readlines()[1:]):
                self.names.add(name.split("\n")[0].lower())
        print("Loaded " + str(idx) + " names")


    def classify(self, input_string):
        input_string = input_string.lower()

        # replace "-" in a name with " " so that
        # double names will be seen as two single names
        input_string = input_string.replace("-", " ")

        words = input_string.split(" ")

        all_words_existent = True

        for word in words:
            if word == "":
                continue
            if word not in self.names:
                return False
        return True

    def predict(self, X):
        """
        predict takes either a string or a sequence of strings
        and returns a string or a sequence accordingly
        """
        if type(X) == str:
            return self._classify(X)

        y_hat = np.empty(len(X), dtype=np.int)
        for idx, name in enumerate(X):
            y_hat[idx] = self.classify(name)
        return y_hat

    def evaluate(self, X, y, return_errors=False):
        """
        inputs:
            X: sequence of strings
            y: sequence of integers (1 for name, 0 for no name)
            return_errors: bool, whether to return a list of errors
        
        returns:
            metrics: dictionary, including accuracy, precision,
                     recall, and f1 score
        """
        # predict elements
        y_hat = self.predict(X)

        # accuracy
        accuracy = np.sum(y_hat == y) / len(X)

        # precision, recall and f1
        total_names = np.sum(y == 1)
        true_pos = np.sum((y_hat == 1) & (y == 1))
        detected_names = np.sum(y_hat == 1)
        precision = true_pos / detected_names
        recall = true_pos / total_names
        f1 = 2 * (precision * recall) / (precision + recall)

        metrics = {"accuracy": accuracy,
                   "precision": precision,
                   "recall": recall,
                   "f1": f1}

        if return_errors:
            error_mask = (y_hat != y)
            error_list = []
            for i in range(len(error_mask)):
                if error_mask[i] == 1:
                    error_list.append([X[i], y_hat[i]])
            return metrics, error_list
        else:
            return metrics


def generate_random_data(n, names_file, words_file):
    # load random names
    names = set()
    with open(names_file, "r") as f:
        for idx, name in enumerate(f.readlines()[1:]):
            names.add(name.split("\n")[0].lower())

    # load random words
    words = set()
    with open(words_file, "r") as f:
        for idx, word in enumerate(f.readlines()[1:]):
            words.add(word.split("\n")[0].lower())

    data = []
    for i in range(math.floor(n/2)):
        sample = random.sample(names, np.random.randint(2, 4))
        entry = ""
        for word in sample:
            entry = entry + word + " "
        data.append([entry, 1])

    for i in range(math.ceil(n/2)):
        sample = random.sample(words, np.random.randint(2, 4))
        entry = ""
        for word in sample:
            entry = entry + word + " "
        data.append([entry, 0])
    
    return np.array(data)


def print_error_list(error_list):
    for error in error_list:
        if error[1] == 1:
            print(error[0] + " was incorrectly predicted to be a name")
        elif error[1] == 0:
            print(error[0] + " was incorrectly predicted to be not a name")

def print_metrics(metrics):
    print("Accuracy was: " + str(metrics["accuracy"]))
    print("Precision was: " + str(metrics["precision"]))
    print("Recall was: " + str(metrics["recall"]))
    print("F1-score was: " + str(metrics["f1"]))
