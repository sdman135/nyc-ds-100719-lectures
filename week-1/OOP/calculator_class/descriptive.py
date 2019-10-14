class Calculator:

    def __init__(self, data):
        self.data = data
        def cal_mean(self):
            return sum(self.data)/len(self.data)
        def cal_length(self):
            return len(self.data)
        def cal_median(self):
                self.data.sort()
                k = len(self.data)
                if k%2 ==1:
                    return self.data[int((k-1)/2)]
                else:
                    return self.data[int((k-1)/2)]+(self.data)[int]((k/2))/2
        def variance(self):
            for d in self.data:
                var_sum = ((self.data) - cal_median(self.data))^2
            return var_sum/length(self.data)
        def stand_dev (self):
            return sqrt(variance(data))
        def add_to_data(self):
            return self.data.append(self.data)
        def remove_from_data(self):
            return self.data.remove(self)





