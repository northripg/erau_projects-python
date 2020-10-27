def math(a, b):
    def result(c):
        return ((((a + b) / c) * (c ** b ** a) - 17))

    return result


nums = math(2, 3)
print(nums(7))