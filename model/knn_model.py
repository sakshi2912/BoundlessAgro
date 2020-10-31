from collections import Counter
import math
import csv

def knn(data, query, k, distance_fn, choice_fn):
    neighbor_distances_and_indices = []    
    for index, example in enumerate(data):
        distance = distance_fn(example[:-1], query)
        neighbor_distances_and_indices.append((distance, index))    
    sorted_neighbor_distances_and_indices = sorted(neighbor_distances_and_indices)
    k_nearest_distances_and_indices = sorted_neighbor_distances_and_indices[:k]
    k_nearest_labels = [data[i][1] for distance, i in k_nearest_distances_and_indices]
    return k_nearest_distances_and_indices , choice_fn(k_nearest_labels)

def mean(labels):
    return sum(labels) / len(labels)

def mode(labels):
    return Counter(labels).most_common(1)[0][0]

def euclidean_distance(point1, point2):
    sum_squared_distance = 0
    for i in range(len(point1)):
        sum_squared_distance += math.pow(point1[i] - point2[i], 2)
    return math.sqrt(sum_squared_distance)

def main_knn(pH,ppm,temp):
    clf_data_pH = []
    clf_data_ppm = []
    clf_data_temp = []
    with open('dataset.csv', newline='') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
        pH_label = []
        pH_label.append(float(row['pH']))
        pH_label.append(int(row['ph pump']))
        ppm_label = []
        ppm_label.append(float(row['ppm']))
        ppm_label.append(int(row['ppm pump']))
        temp_label = []
        temp_label.append(float(row['temp']))
        temp_label.append(int(row['temp pump']))
        clf_data_pH.append(pH_label)
        clf_data_ppm.append(ppm_label)
        clf_data_temp.append(temp_label)

    pH_query = [pH] #1
    clf_k_nearest_neighbors, clf_prediction_pH = knn(
        clf_data_pH, pH_query, k=3, distance_fn=euclidean_distance, choice_fn=mode
    )

    print(clf_prediction_pH,"pH Indicator (0 - Normal, 1 - Increase pH, 2 - Reduce pH)")
    ppm_query = [ppm] #0
    clf_k_nearest_neighbors, clf_prediction_ppm = knn(
        clf_data_ppm, ppm_query, k=3, distance_fn=euclidean_distance, choice_fn=mode
    )

    print(clf_prediction_ppm,"ppm Indicator (0 - Normal, 1 - Increase ppm, 2 - Reduce ppm)")
    temp_query = [temp] #0
    clf_k_nearest_neighbors, clf_prediction_temp = knn(
        clf_data_temp, temp_query, k=3, distance_fn=euclidean_distance, choice_fn=mode
    )
    print(clf_prediction_temp,"Temperature Indicator (0 - Normal, 1 - Increase Temp, 2 - Reduce Temp)")
    return clf_prediction_pH,clf_prediction_ppm,clf_prediction_temp
def main():
  return None

if __name__ == '__main__':
    main()