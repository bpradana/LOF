class LOF:
    def __init__(self):
        self.data = []
        self.proximity_matrix = []
        self.sort_array = []

    def euclidean_distance(self, a, b):
        sum = 0

        for a_, b_ in zip(a, b):
            sum += (a_ - b_) ** 2

        sum = sum ** 0.5
        sum = round(sum, 2)
        return sum

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

    def preprocess_sort_array(self):
        for row in self.proximity_matrix:
            temp = [[data, i] for i, data in enumerate(row)]
            self.sort_array.append(temp)


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

    lof = LOF()
    lof.load_data(data)
    lof.calculate_proximity_matrix()
    lof.preprocess_sort_array()
    print(lof.sort_array)
