from abc import abstractmethod

@abstractmethod
class Movable:
    def __init__(self, move="Jadę"):
        self.move = move

    def move(self) -> str:
        return move

def main():
    car_object = Movable()
    print(car_object.move)


if __name__ == "__main__":
    main()



