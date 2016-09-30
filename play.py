import numpy as np
import pdb
from classifier import name_classifier, generate_random_data
from classifier import print_error_list, print_metrics

# create classifier
clf = name_classifier()

#### classifying the examples from the task description ####
print("\nExamples from the task description")
example_data = np.array([ \
        ["Preembarrass Hippogryph", 0],
        ["nishant dahad", 1],
        ["thames river", 0],
        ["chinese new year", 0],
        ["Jun Wang", 1],
        ["alison cheung", 1],
        ["underclothe recloth", 0],
        ["naomi nguyen", 1],
        ["Fustellatrici Pazze Perugia e dintorni", 0]])
X = example_data[:, 0]
y = example_data[:, 1].astype(np.int)
metrics, error_list = clf.evaluate(X, y, return_errors=True)
print("Accuracy is: " + str(metrics["accuracy"]))
print_error_list(error_list)


#### classifying random data ####
print("\nEvaluating on some random data")
data = generate_random_data(2000, "random_names.txt", "random_words.txt")
X = data[:, 0]
y = data[:, 1].astype(int)
metrics, error_list = clf.evaluate(X, y, return_errors=True)
print_error_list(error_list)
print_metrics(metrics)
