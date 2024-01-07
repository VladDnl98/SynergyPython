from pynput import keyboard
from clouds import Clouds
from map import Map
import time
import os
import json
from helicopter import Helicopter as Helico

TICK_SLEEP = 0.05
CLOUDS_UPDATE = 100
THREE_UPDATE = 20
FIRE_UPDATE = 90
MAP_SIZES = {
    "small": (10, 10),
    "large": (15, 15),
    "big": (20,20)
}
MAP_W, MAP_H = MAP_SIZES["small"]

field = Map(MAP_W, MAP_H)
clouds = Clouds(MAP_W, MAP_H)
helico = Helico(MAP_W, MAP_H)
tick = 1

MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}

def choose_map_size(size):
    global MAP_W, MAP_H, field, clouds, helico
    if size in MAP_SIZES:
        MAP_W, MAP_H = MAP_SIZES[size]
        field = Map(MAP_W, MAP_H)
        clouds = Clouds(MAP_W, MAP_H)
        helico = Helico(MAP_W, MAP_H)
        print(f"Размер карты установлен на {size}")

def process_key(key):
    global helico, tick, clouds, field
    c = key.char.lower()
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)
    elif c  == 'f':
        data = {"helicopter": helico.export_data(),
                "clouds": clouds.export_data(),
                "field": field.export_data(),
                "tick" : tick}
        
        with open("level.json", "w") as lvl:
            json.dump(data, lvl)
    
    elif c == 'g':
        with open("level.json", "r") as lvl:
            data = json.load(lvl)
            tick = data["tick"] or 1
            helico.import_data(data["helicopter"])
            field.import_data(data["field"])
            clouds.import_data(data["clouds"])
    elif c == '1':
        choose_map_size("small")  # Вызов функции для установки маленького размера карты
    elif c == '2':
        choose_map_size("large")  # Вызов функции для установки большого размера карты
    elif c == '3':
        choose_map_size("big")  # Вызов функции для установки большого размера карты


listener = keyboard.Listener(
    on_press=None,
    on_release=process_key)
listener.start()

while True:
    os.system("clear") #cls
    field.process_helicopter(helico, clouds)
    helico.print_stats()
    field.print_map(helico, clouds)
    print("X================================X")
    print("TICK", tick)
    print("X================================X")
    print("X Нажми F чтобы - сохранить игру X")
    print("X Нажми G чтобы - загрузить игру X")
    print("X================================X")
    print("X Нажми 1  - карта маленькая     X")
    print("X Нажми 2  - карта средняя       X")
    print("X Нажми 3  - карта большая       X")
    print("X================================X")
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % THREE_UPDATE == 0):
        field.generate_tree()
    if (tick % FIRE_UPDATE == 0):
        field.update_fires()
    if (tick % CLOUDS_UPDATE == 0):
        clouds.update()


