"""
    Benefits:
    - Simplifies complex subsystems for the client.
    - Reduces coupling between client and subsystem.
    - Makes code more readable and maintainable.

   Downsides:
    - May hide functionality you might later need access to.
    - If overused, can turn into a god object (doing too much).

   Real-World Uses:
    - UI frameworks (e.g., calling one method to set up a full screen)
    - Networking clients (e.g., HTTP libraries)
    - Game engines (e.g., loading assets, initializing physics, etc.)
"""



from abc import ABC, abstractmethod

class MovieI(ABC):
    @abstractmethod
    def play_movie(self):
        pass

class DVD:
    def turn_on(self):
        print(f"DVD turned on!")

    def select_movie(self, name):
        print(f"selected movie {name}")

class SoundSystem:
    def turn_on(self):
        print(f"Sound System turned on!")

    def set_volume(self, volume):
        print(f"selected volume {volume}")

class Screen:
    def turn_on(self):
        print(f"Turn on screen")

    def set_brightness(self, level):
        print(f"Select brightness {level}")

class Movie(MovieI):
    def __init__(self, dvd, sound, screen):
        self.dvd = dvd
        self.sound = sound
        self.screen = screen


    def play_movie(self):
        print("setting system")
        self.dvd.turn_on()
        self.dvd.select_movie("Social Network")
        self.sound.turn_on()
        self.sound.set_volume(8)
        self.screen.turn_on()
        self.screen.set_brightness(75)
        print("Movie started!")


if __name__ == '__main__':
    dvd = DVD()
    sound = SoundSystem()
    screen = Screen()
    movie = Movie(dvd, sound, screen)
    movie.play_movie()
