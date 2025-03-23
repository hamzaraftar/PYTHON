# l = [10 , 20 , 30 , 40]
# iter_obj = iter(l)
# print(iter_obj)

class PowerOfTwo:
    def __init__(self,max_value):
        self.limit = max_value
        self.current = 1
        
        
    def __iter__(self):
        return self

    def __next__(self):
        result = self.current
        return result



n = int(input("Enter the limit: "))
iter_obj = PowerOfTwo(n)
