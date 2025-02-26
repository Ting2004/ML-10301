"""
a knn algo
for fun

happened to be helpful for homework
unfinished
"""

import argparse
import numpy as np


def hamming(x, y):
    return np.sum(x != y)


def euclidean(x, y):
    return np.sqrt(np.sum(np.square(x) + np.square(y)))

def knn(dataset, x, k=1, distance="euclidean"):
    """
    args:
        dataset  - labeled data
        x        - unseen point
        k        - k nearest
        distance - method for distance calculation
    output:
        label for the unseen point
    """
    distance_metric = euclidean if distance == "euclidean" else hamming

     # Compute distances
    distances = np.apply_along_axis(lambda point: distance_metric(x, point), 1, dataset[:, :-1])
    
    # Get the indices of the k nearest neighbors
    sorted_indices = np.argsort(distances)

     # Find the distance threshold for the k-th nearest neighbor
    kth_distance = distances[sorted_indices[k-1]]
    
    # Select all neighbors within the k-th distance (handling ties)
    nearest_indices = sorted_indices[distances <= kth_distance]
    
    # Extract the labels of the nearest neighbors
    nearest_labels = dataset[nearest_indices, -1]
    
    # Determine the majority label, handle ties
    label_counts = np.bincount(nearest_labels.astype(int))
    max_count = np.max(label_counts)
    majority_labels = np.where(label_counts == max_count)[0]
    print(nearest_labels)
    return majority_labels[0] if len(majority_labels) == 1 else "?"




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("train_input", type=str, help='path to training input .tsv file')
    parser.add_argument("test_input", type=str, help='path to the test input .tsv file')
    parser.add_argument("k", type=int, help='number of nearest neighbors')
    parser.add_argument("distance", type=str, help='metric of distance, either "euclidean" or "hamming"')
    parser.add_argument("test_out", type=str, 
                        help='path to output .txt file to which the labels')
    # parser.add_argument("metrics_out", type=str, 
    #                     help='path of the output .txt file to which metrics such as train and test error should be written')
    # parser.add_argument("print_out", type=str,
    #                     help='path of the output .txt file to which the printed tree should be written')
    args = parser.parse_args()
    
    #Here's an example of how to use argparse
    train_set = np.genfromtxt(fname=args.train_input, delimiter="\t", skip_header=1)
    attrs = np.genfromtxt(fname=args.train_input, delimiter="\t", dtype=str)[0,:]
    test_set = np.genfromtxt(fname=args.test_input, delimiter="\t", skip_header=1)


    with open(args.test_out, 'w') as f:
        for point in test_set:
            prediction = knn(train_set, point, k=args.k, distance=args.distance)
            f.write(np.array2string(prediction) + "\n")

