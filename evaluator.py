from scipy.spatial import distance
import numpy as np

def rms_without_normalize(test, target):
    distances = []

    for i in range(0, len(test)):
        point_dst = []
        for j in range(0, len(target)):
            point_dst.append(distance.euclidean(test[i], target[j]))
        distances.append(min(point_dst))

    distances = np.array(distances)

    return distances


def rms_with_normalize(test, target):
    distances = []

    for i in range(0, len(test)):
        point_dst = []
        for j in range(0, len(target)):
            point_dst.append(distance.euclidean(test[i], target[j]))
        distances.append(min(point_dst))

    distances = np.array(distances)

    distances = (distances - np.min(distances)) / np.ptp(distances)

    return distances

def chamfer_without_normalize(test, target):
    distances = []

    for i in range(0, len(test)):
        point_dst = []
        for j in range(0, len(target)):
            point_dst.append(distance.cityblock(test[i], target[j]))
        distances.append(min(point_dst))

    distances = np.array(distances)

    return distances


def chamfer_with_normalize(test, target):
    distances = []

    for i in range(0, len(test)):
        point_dst = []
        for j in range(0, len(target)):
            point_dst.append(distance.cityblock(test[i], target[j]))
        distances.append(min(point_dst))

    distances = np.array(distances)

    distances = (distances - np.min(distances)) / np.ptp(distances)

    return distances

