class LOF:
    def __init__(self):
        self.data = []
        self.proximity_matrix = []
        self.sort_array = []
        self.average_density = []
        self.average_relative_density = []

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
            total = total / 3 / self.average_density[i]
            self.average_relative_density.append(total)




if __name__ == '__main__':
    data = [
        [26, 35],
        [13, 12],
        [11, 5],
        [10, 15],
        [50, 45],
        [200, 200],
        [18, 20],
        [21, 14],
        [16, 20],
        [21, 75]
    ]
    k = 3

    lof = LOF()
    lof.load_data(data)
    lof.calculate_proximity_matrix()
    lof.sort()
    lof.calculate_average_density(k)
    lof.calculate_average_relative_density(k)
    print(lof.average_relative_density)
