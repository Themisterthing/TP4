import arcade
import random

SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 1000

COLORS = [arcade.color.LIME_GREEN, arcade.color.BLAST_OFF_BRONZE, arcade.color.RED_DEVIL, arcade.color.PALATINATE_BLUE, arcade.color.PURPUREUS, arcade.color.AMAZON]


class Balle:
    #classe balle
    def __init__(self, x, y, rayon, color):
        self.x = x
        self.y = y
        self.change_x = 10
        self.change_y = 10
        self.rayon = rayon
        self.color = color
    #fait bouger la balle
    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        if self.x < self.rayon:
            self.change_x *= -1
        elif self.x > SCREEN_WIDTH - self.rayon:
            self.change_x *= -1
        if self.y < self.rayon:
            self.change_y *= -1
        elif self.y > SCREEN_HEIGHT - self.rayon:
            self.change_y *= -1
    #dessine la balle
    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)


class Rectangle:
    #classe rectangle
    def __init__(self, x, y, width, height, color, angle):
        self.x = x
        self.y = y
        self.change_x = -10
        self.change_y = 10
        self.width = width
        self.height = height
        self.color = color
        self.angle = angle
    #fait bouger le rectangle
    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        if self.x < self.width/2:
            self.change_x *= -1
        elif self.x > SCREEN_WIDTH - self.width/2:
            self.change_x *= -1
        if self.y < self.height/2:
            self.change_y *= -1
        elif self.y > SCREEN_HEIGHT - self.height/2:
            self.change_y *= -1
    #dessine le rectangle
    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color, self.angle)


class MyGame(arcade.Window):
    #ouvre la fenetre
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.balles = []
        self.rectangles = []
    #changer la couleur de l'arriere plan
    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)
    #dessine les formes
    def on_draw(self):
        arcade.start_render()
        for balle in self.balles:
            balle.draw()
        for rectangle in self.rectangles:
            rectangle.draw()
    #fait bouger les formes
    def on_update(self, delta_time):
        for balle in self.balles:
            balle.update()
        for rectangle in self.rectangles:
            rectangle.update()
    #creer un rectangle ou un cercle
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            balle = Balle(x, y, 30, random.choice(COLORS))
            self.balles.append(balle)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            rectangle = Rectangle(x, y, 50, 50, random.choice(COLORS), 0)
            self.rectangles.append(rectangle)


def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


if __name__ == "__main__":
    main()