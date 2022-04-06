# noinspection PyPep8Naming
class Train:
    def __init__(self, gameMap, size=25, capacity=0):
        self.__gameMap = gameMap
        self.__currentStation = gameMap.StationsList[0]
        self.__size = size
        self.__capacity = capacity

    def GoToStation(self, key):
        self.__currentStation = self.__gameMap.StationsGraph[self.__currentStation.name][key]

    def LoadTrain(self):
        print('На станции:', self.__currentStation.capacity)
        print('В поезде:', self.__capacity)
        amount = input('Сколько загрузить: ')
        while amount not in [f'{s}' for s in range(1, self.__currentStation.capacity + 1)]:
            amount=input('Некорректный ввод, попробуйте еще раз:\n')
        if self.__capacity + int(amount) <= self.__size:
            self.__capacity += int(amount)
            self.__currentStation.capacity -= int(amount)
        else:
            buf = self.__size - self.__capacity
            self.__capacity = self.__size
            self.__currentStation.capacity += -buf + int(amount)

    def UnloadTrain(self):
        print('На станции:', self.__currentStation.capacity)
        print('В поезде:', self.__capacity)
        amount = input('Сколько выгрузить: ')
        while amount not in [f'{s}' for s in range(1, self.__capacity + 1)]:
            amount=input('Некорректный ввод, попробуйте еще раз:\n')
        self.__capacity -= int(amount)
        self.__currentStation.capacity += int(amount)

    def PrintNextStationsList(self):
        for station in self.__gameMap.StationsGraph[self.__currentStation.name].values():
            print(station.name, end=' ')

    def GetNextStationsList(self):
        return self.__gameMap.StationsGraph[self.__currentStation.name]

    @property
    def CurrentStation(self):
        return self.__currentStation

    @property
    def Capacity(self):
        return self.__capacity

    @Capacity.setter
    def Capacity(self, capacity):
        self.__capacity = capacity

    @CurrentStation.setter
    def CurrentStation(self, station):
        self.__currentStation = station
