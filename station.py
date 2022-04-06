class Station:
    def __init__(self, name, capacity=5, size=25):
        self.__capacity = capacity
        self.__size = size
        self.__name = name

    @property
    def size(self):
        return self.__size

    @property
    def capacity(self):
        return self.__capacity

    @property
    def name(self):
        return self.__name

    @size.setter
    def size(self, x):
        self.__size = x

    @capacity.setter
    def capacity(self, x):
        self.__capacity = x

    @name.setter
    def name(self, x):
        self.__name = x
