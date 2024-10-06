class RectangleIterator:
    def __init__(self, parameters):
        self.parameters = parameters
        self.index = 0
    
    def __next__(self):
        try:
            parameter = self.parameters[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return parameter


class Rectangle:
    def __init__(self, parameters):
        self.parameters = parameters

    def __iter__(self):
        return RectangleIterator(self.parameters)
    

length = int(input('Enter Length: '))
width = int(input('Enter width: '))

rectangle = Rectangle([{'length':length},{'width':width}])

for para in rectangle:
    print(para)