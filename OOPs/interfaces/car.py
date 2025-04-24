from interfaces.vehicle import Vehicle

class Car(Vehicle):
    def start(self):
        print("Car starts...")

    def stop(self):
        print("Car stops...")

if __name__ == "__main__":
    car = Car()
    car.start()
    car.stop()