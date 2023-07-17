from src.channel import Channel

if __name__ == '__main__':
    # Создаем два экземпляра класса
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    highload = Channel('UCwHL6WHUarjGfUM_586me8w')

    # Используем различные магические методы
    print(moscowpython)  # 'MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)'
    print(int(repr(moscowpython)) + int(repr(highload)))  # 100100
    print(int(repr(moscowpython)) - int(repr(highload)))  # -48300
    print(int(repr(highload)) - int(repr(moscowpython)))  # 48300
    print(int(repr(moscowpython)) > int(repr(highload)))  # False
    print(int(repr(moscowpython)) >= int(repr(highload)))  # False
    print(int(repr(moscowpython)) < int(repr(highload)))  # True
    print(int(repr(moscowpython)) <= int(repr(highload)))  # True
    print(int(repr(moscowpython)) == int(repr(highload)))  # False
    
