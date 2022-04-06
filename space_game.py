import time, re
from map import GameMap
from train import Train
from os import system


def menu(x, train,first_time):
    while x.CheckIfOverloaded(train):
        system('cls')
        x.GenerateGoods()
        print(f'Поезд на {train.CurrentStation.name} станции\nВ поезде {train.Capacity}')
        x.CheckStationsState()
        print('Что сделать?')
        key = input('(1) Следующая станция\n(2) Загрузить поезд\n(3) Разгрузить поезд\n')
        if key == '1':
            train.PrintNextStationsList()
            stations_state = input('\nКуда поедем?\n')
            while (stations_state not in train.GetNextStationsList()):
                stations_state = input('\nНекорректный ввод, попробуйте еще раз:\n')
            train.GoToStation(stations_state)
            print('...едем...')
            time.sleep(2)
            continue
        elif key == '2':
            train.LoadTrain()
            print('загружаю...')
            time.sleep(3)
        elif key == '3':
            train.UnloadTrain()
            print('разгружаю...')
            time.sleep(3)
        elif key == 'p':
            print('Игра сохранена')
            save(x,train,time.time()-first_time)
            exit()
        else:
            print('Некорректный формат ввода, попробуйте еще раз!')
        x.CheckIfOverloaded(train)


    print('ПОТРАЧЕНО')


def save(x, train,time):
    with open("rec.txt", 'w+') as f:
        for station in x.StationsList:
            f.write(str(station.Capacity) + '\n')
        f.write(str(train.Capacity) + '\n')
        f.write(str(time))

def continue_game(x, train):
    data=[]
    with open("rec.txt", 'r+') as f:
        for line in f:
            data.append(float(line))
    for line in range(len(x.StationsList)):
        x.StationsList[line].Capacity=data[line]
    train.Capacity=data[len(x.StationsList)]
    return data[len(x.StationsList) + 1]





def run():
    x = GameMap()
    train = Train(x)
    flag = input('''
H   ┈╱▔▔▔▔▔▔▔▔╲┈┈┈┈
E   ╱▔▔▔▔▔▔▔▔╲╱┈┈┈┈
L   ▏MY TRAIN▕╱▔▔╲┈
L   ▏         ▔▔╲╱▏
O   ▏1.NEW   ▕ ▕▉▕╱╲
!   ▇2.CONTINUE▔▔╲ ▕
!   ▇▇╱▔╲▇▇▇▇▇╱▔╲▕╱
!   ┈┈╲▂╱┈┈┈┈┈╲▂╱
       \n ''')
    while flag not in ['1','2']:
        flag = input('Некорректный ввод, попробуйте еще раз:\n')
    if flag == '2':
        my_time=continue_game(x, train)
    else:
        my_time=0
    first_time = time.time()-my_time
    menu(x, train,first_time)
    final_time = time.time() - first_time
    print('Ваш счёт:' ,round(final_time,1))




if __name__ == '__main__':
    run()

    # with open("rec.txt", 'w+') as f:
    #     f.write(str(final_time))
