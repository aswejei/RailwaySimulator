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
        amount = int(input('Сколько загрузить: '))
        while amount < 0 or self.__currentStation.capacity - amount < 0:
            print('На станции:', self.__currentStation.capacity)
            print('В поезде', self.__capacity)
            amount = int(input('Сколько загрузить: '))
        if self.__capacity + amount <= self.__size:
            self.__capacity += amount
            self.__currentStation.capacity -= amount
        else:
            buf = self.__size - self.__capacity
            self.__capacity = self.__size
            self.__currentStation.capacity += -buf + amount

    def UnloadTrain(self):
        print('На станции:', self.__currentStation.capacity)
        print('В поезде:', self.__capacity)
        amount = int(input('Сколько выгрузить '))
        while amount < 0 or self.__capacity - amount < 0:
            print('На станции:', self.__currentStation.capacity)
            print('в поезде сейчас столько груза:', self.__capacity)
            amount = int(input('В поезде: '))
        self.__capacity -= amount
        self.__currentStation.capacity += amount

    def PrintNextStationsList(self):
        for station in self.__gameMap.StationsGraph[self.__currentStation.name].values():
            print(station.name, end=' ')

    def GetNextStationsList(self):
        return self.__gameMap.StationsGraph[self.__currentStation.name]

    @property
    def follow_stations(self):
        return len(self.__gameMap.StationsGraph[self.__currentStation])

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
