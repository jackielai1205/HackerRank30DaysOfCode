class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    # Add your code here
    def computeDifference(self):
        maximum_difference = 0
        for a in range(len(self.__elements) - 1):
            for b in range(a, len(self.__elements)):
                result = abs(self.__elements[a] - self.__elements[b])
                if result > maximum_difference:
                    maximum_difference = result
        self.maximumDifference = maximum_difference


_ = 3
a = [1, 2, 5]
d = Difference(a)
d.computeDifference()
print(d.maximumDifference)