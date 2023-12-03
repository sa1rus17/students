from tkinter import Tk, Canvas, ARC, W
from human import human


class Hero(human):
    def __init__(self, canvas, name, x, y, gen):
        super().__init__(canvas, name, x, y, gen)
        self.health = 100
        self._wp = None

        self.health_bar_width = 100
        self.health_bar_height = 10
        self.health_bar_x = self.x + 1.5
        self.health_bar_y = self.y - 250
        self.health_bar_color = "green"
        self.dead_color = "red"

    def _drawName(self):
        self.canvas.create_text(self.x + 1.5, self.y - 280, text=self.name, font="Times 18", anchor=W, fill="black")
        self.canvas.create_rectangle(self.health_bar_x,
                                     self.health_bar_y,
                                     self.health_bar_x + self.health_bar_width,
                                     self.health_bar_y + self.health_bar_height,
                                     fill=self.health_bar_color)

    def setWeapon(self, weapon):
        self._wp = weapon

    def attack(self, enemy):
        damage=self._wp.hit()
        print(f'{self.name} нанес(ла){damage} урона {enemy.name}!')

    def _drawWeapon(self):
        self._wp.display(self.x+100, self.y-100)

    def display(self):
        #self._drawName()
        super().display()
        self._drawWeapon()
