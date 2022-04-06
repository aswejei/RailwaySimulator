import random
from station import Station


class GameMap:
    def __init__(self):
        self.__stationsList = [Station(i) for i in ['a', 'b', 'c', 'd', 'e', 'f']]
        self.__stationsGraph = {
            self.__stationsList[0].name:
                {
                    self.__stationsList[1].name: self.__stationsList[1],
                    self.__stationsList[2].name: self.__stationsList[2]
                },
            self.__stationsList[1].name:
                {
                    self.__stationsList[0].name: self.__stationsList[0],
                    self.__stationsList[3].name: self.__stationsList[3],
                    self.__stationsList[4].name: self.__stationsList[4]
                },
            self.__stationsList[2].name:
                {
                    self.__stationsList[0].name: self.__stationsList[0],
                    self.__stationsList[5].name: self.__stationsList[5]
                },
            self.__stationsList[3].name:
                {
                    self.__stationsList[1].name: self.__stationsList[1]
                },
            self.__stationsList[4].name:
                {
                    self.__stationsList[1].name: self.__stationsList[1],
                    self.__stationsList[5].name: self.__stationsList[5]
                },
            self.__stationsList[5].name:
                {
                    self.__stationsList[2].name: self.__stationsList[2],
                    self.__stationsList[4].name: self.__stationsList[4]
                }
        }

    def GenerateGoods(self):
        self.__stationsList[random.randint(0, 5)].capacity += 5

    def CheckIfOverloaded(self, train):
        for station in self.__stationsList:
            if station.capacity >= station.size or train.Capacity >= 25:
                return False
        return True


    @property
    def StationsGraph(self):
        return self.__stationsGraph

    @property
    def StationsList(self):
        return self.__stationsList

    @StationsGraph.setter
    def StationsGraph(self, x):
        self.__stationsGraph = x

    @StationsList.setter
    def StationsList(self, x):
        self.__stationsList = x

    def CheckStationsState(self):
        for station in self.__stationsList:
            print(f'На станции [{str(station.name)}] -- {str(station.capacity)} товаров')

    def __str__(self):
        for station in self.__stationsList:
            print(f'На станции [{str(station.name)}] -- {str(station.capacity)} товаров')