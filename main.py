import matplotlib.pyplot as plt
import pandas as pd


class LOF:
    def __init__(self):
        self.data = []
        self.proximity_matrix = []
        self.sort_array = []
        self.average_density = []
        self.average_relative_density = []
        self.outlier = {
            'index': [],
            'coord': [],
            'value': []
        }

    def euclidean_distance(self, a, b):
        total = 0

        for a_, b_ in zip(a, b):
            total += (a_ - b_) ** 2

        total = total ** 0.5
        return total

    def load_data(self, data):
        self.data = data

    def calculate_proximity_matrix(self):
        row = []
        temp = []

        for fp in data:
            for sp in data:
                dist = self.euclidean_distance(fp, sp)
                dist = round(dist, 2)
                temp.append(dist)
            row = temp.copy()
            temp.clear()
            self.proximity_matrix.append(row)

    def sort(self):
        index = [i for i in range(10)]
        for row in self.proximity_matrix:
            temp = [[data, i] for data, i in sorted(zip(row, index)) if data != 0]
            self.sort_array.append(temp)

    def calculate_average_density(self, k):
        for row in self.sort_array:
            total = 0
            for i in range(k):
                total += row[i][0]
            average_density = k / total
            self.average_density.append(average_density)

    def calculate_average_relative_density(self, k):
        for i, row in enumerate(self.sort_array):
            total = 0
            for j in range(k):
                index = row[j][1]
                total += self.average_density[index]
            total = total / k / self.average_density[i]
            self.average_relative_density.append(total)

    def find_outlier(self, treshold):
        self.outlier['index'] = [index for index, data in enumerate(self.average_relative_density) if data > treshold]
        self.outlier['coord'] = [point for data, point in zip(self.average_relative_density, self.data) if data > treshold]
        self.outlier['value'] = [value for value in self.average_relative_density if value > treshold]

    def print_data(self, data):
        for i, row in enumerate(data):
            print(i, row)
        print('')

    def calculate_lof(self, k, treshold):
        self.calculate_proximity_matrix()
        self.sort()
        self.calculate_average_density(k)
        self.calculate_average_relative_density(k)
        self.find_outlier(treshold)



if __name__ == '__main__':
    file = 'data.csv'
    k = 3
    t = 5


    df = pd.read_csv(file, delimiter=',')
    data = [list(data) for data in df.values]

    lof = LOF()
    lof.load_data(data)
    lof.calculate_lof(k, t)

    print('=== DATA ===')
    lof.print_data(lof.data)

    print('=== PROXIMITY MATRIX ===')
    lof.print_data(lof.proximity_matrix)

    print('=== SORTED ARRAY ===')
    lof.print_data(lof.sort_array)

    print('=== AVERAGE DENSITY ===')
    lof.print_data(lof.average_density)

    print('=== AVERAGE RELATIVE DENSITY ===')
    lof.print_data(lof.average_relative_density)

    print('=== OUTLIERS ===')
    lof.print_data(zip(lof.outlier['index'], lof.outlier['coord'], lof.outlier['value']))


    normal_point_x = [point[0] for point in lof.data if point not in lof.outlier['coord']]
    normal_point_y = [point[1] for point in lof.data if point not in lof.outlier['coord']]
    outlier_point_x = [point[0] for point in lof.outlier['coord']]
    outlier_point_y = [point[1] for point in lof.outlier['coord']]

    plt.scatter(normal_point_x, normal_point_y)
    plt.scatter(outlier_point_x, outlier_point_y, c='red')
    plt.legend(['normal', 'outlier'])
    plt.title('Outlier')

    plt.show()
