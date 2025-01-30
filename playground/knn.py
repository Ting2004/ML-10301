"""
a coloring knn algo
for fun
"""
import numpy as np


def euclidean(x, y):
    return np.sqrt(np.sum(x^2 + y^2))

def knn(dataset, x, k=1, distance_metric=euclidean):
    """
    args:
        dataset  - labeled data
        x        - unseen point
        k        - k nearest
        distance - method for distance calculation
    output:
        label for the unseen point
    """
    distances = np.apply_along_axis(lambda point: distance_metric(x, point), dataset[:,:-1])
    nearest_k = np.sort()   # TODO
    
    nearest_k_labels = nearest_k[:,-1]
    majority_label = 1 # TODO
    return majority_label




def main():
    return


if __name__ == "__main__":
    main()
