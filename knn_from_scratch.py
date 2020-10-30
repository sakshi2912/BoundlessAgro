from collections import Counter
import math
import csv

def knn(data, query, k, distance_fn, choice_fn):
    neighbor_distances_and_indices = []
    
    # 3. For each example in the data
    for index, example in enumerate(data):
        # 3.1 Calculate the distance between the query example and the current
        # example from the data.
        distance = distance_fn(example[:-1], query)
        
        # 3.2 Add the distance and the index of the example to an ordered collection
        neighbor_distances_and_indices.append((distance, index))
    
    # 4. Sort the ordered collection of distances and indices from
    # smallest to largest (in ascending order) by the distances
    sorted_neighbor_distances_and_indices = sorted(neighbor_distances_and_indices)
    
    # 5. Pick the first K entries from the sorted collection
    k_nearest_distances_and_indices = sorted_neighbor_distances_and_indices[:k]
    
    # 6. Get the labels of the selected K entries
    k_nearest_labels = [data[i][1] for distance, i in k_nearest_distances_and_indices]

    # 7. If regression (choice_fn = mean), return the average of the K labels
    # 8. If classification (choice_fn = mode), return the mode of the K labels
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
        clf_data_pH, pH_query, k=10, distance_fn=euclidean_distance, choice_fn=mode
    )

    print(clf_prediction_pH,"pH Label predicted")
    ppm_query = [ppm] #0
    clf_k_nearest_neighbors, clf_prediction_ppm = knn(
        clf_data_ppm, ppm_query, k=10, distance_fn=euclidean_distance, choice_fn=mode
    )

    print(clf_prediction_ppm,"ppm Label predicted")
    temp_query = [temp] #0
    clf_k_nearest_neighbors, clf_prediction_temp = knn(
        clf_data_temp, temp_query, k=10, distance_fn=euclidean_distance, choice_fn=mode
    )
    print(clf_prediction_temp,"temp Label predicted")
    return clf_prediction_pH,clf_prediction_ppm,clf_prediction_temp
def main():
  return None

if __name__ == '__main__':
    main()