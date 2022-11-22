class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        total = 0
        for x in range(1, n + 1):
            if (n % x) == 0:
                total += x
        return total
