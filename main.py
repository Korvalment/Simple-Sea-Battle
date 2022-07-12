from tkinter import *
from tkinter import messagebox
import random
import locale
import time
from accessify import protected
from abc import ABC

locale.setlocale(locale.LC_ALL, '')


class Color(ABC):

    white = '#FFFFFF'
    dark_red = '#aa0000'
    pink = '#fa87bf'
    violet = '#660066'
    brown = '#4d0000'
    light_cyan = '#E0FFFF'
    maroon = '#2F4F4F'  # destroyed ship
    static = "#f0f0f0"


class Navy(Color):

    def __init__(self, s_x=9):
        self._ships = (s_x // 2) # określenie maksymalnej liczby statków
        self.ship_len1 = s_x // 5  # długość statków pierwszego typu
        self.ship_len2 = s_x // 3  # długość statków drugiego typu
        self.ship_len3 = s_x // 2  # długość statków trzeciego typu

    enemy_ships = [[0 for i in range(9 + 1)] for i in range(9 + 1)]  # (9 + 1) = s_x and s_y
    enemy_ships2 = [[0 for i in range(9 + 1)] for i in range(9 + 1)]

    def generate_enemy_ships(self, s_x=9, s_y=9):
        global enemy_ships

        ships_list = []

        for i in range(0, self._ships):
            ships_list.append(random.choice([self.ship_len1, self.ship_len2, self.ship_len3]))

        sum_1_all_ships = sum(ships_list)
        sum_1_enemy = 0

        while sum_1_enemy != sum_1_all_ships:

            enemy_ships = [[0 for i in range(s_x + 1)] for i in
                           range(
                               s_y + 1)]

            for i in range(0, self._ships):

                len = ships_list[i]
                horizont_vertikal = random.randrange(1, 3)
                primerno_x = random.randrange(0, s_x)
                if primerno_x + len > s_x:
                    primerno_x = primerno_x - len

                primerno_y = random.randrange(0, s_y)
                if primerno_y + len > s_y:
                    primerno_y = primerno_y - len

                if horizont_vertikal == 1:
                    if primerno_x + len <= s_x:
                        for j in range(0, len):
                            try:
                                check_near_ships = 0
                                check_near_ships = enemy_ships[primerno_y][primerno_x - 1] + \
                                                   enemy_ships[primerno_y][primerno_x + j] + \
                                                   enemy_ships[primerno_y][primerno_x + j + 1] + \
                                                   enemy_ships[primerno_y + 1][primerno_x + j + 1] + \
                                                   enemy_ships[primerno_y - 1][primerno_x + j + 1] + \
                                                   enemy_ships[primerno_y + 1][primerno_x + j] + \
                                                   enemy_ships[primerno_y - 1][primerno_x + j]
                                # print(check_near_ships)
                                if check_near_ships == 0:
                                    enemy_ships[primerno_y][primerno_x + j] = i + 1
                            except Exception:
                                pass
                if horizont_vertikal == 2:
                    if primerno_y + len <= s_y:
                        for j in range(0, len):
                            try:
                                check_near_ships = 0
                                check_near_ships = enemy_ships[primerno_y - 1][primerno_x] + \
                                                   enemy_ships [primerno_y + j][primerno_x] + \
                                                   enemy_ships[primerno_y + j + 1][primerno_x] + \
                                                   enemy_ships[primerno_y + j + 1][primerno_x + 1] + \
                                                   enemy_ships[primerno_y + j + 1][primerno_x - 1] + \
                                                   enemy_ships[primerno_y + j][primerno_x + 1] + \
                                                   enemy_ships[primerno_y + j][primerno_x - 1]
                                # print(check_near_ships)
                                if check_near_ships == 0:
                                    enemy_ships[primerno_y + j][primerno_x] = i + 1
                            except Exception:
                                pass

            print(f"Сreating ships for the player {1}........")

            sum_1_enemy = 0
            for i in range(0, s_x):
                for j in range(0, s_y):
                    if enemy_ships[j][i] > 0:
                        sum_1_enemy = sum_1_enemy + 1



    def generate_enemy_ships2(self, s_x=9, s_y=9):
        global enemy_ships2

        ships_list = []

        for i in range(0, self._ships):
            ships_list.append(random.choice([self.ship_len1, self.ship_len2, self.ship_len3]))
        sum_1_all_ships = sum(ships_list)
        sum_1_enemy = 0

        while sum_1_enemy != sum_1_all_ships:
            enemy_ships2 = [[0 for i in range(s_x + 1)] for i in
                           range(
                               s_y + 1)]

            for i in range(0, self._ships):

                len = ships_list[i]
                horizont_vertikal = random.randrange(1, 3)

                primerno_x = random.randrange(0, s_x)
                if primerno_x + len > s_x:
                    primerno_x = primerno_x - len

                primerno_y = random.randrange(0, s_y)
                if primerno_y + len > s_y:
                    primerno_y = primerno_y - len


                if horizont_vertikal == 1:
                    if primerno_x + len <= s_x:
                        for j in range(0, len):
                            try:
                                check_near_ships = 0
                                check_near_ships = enemy_ships2[primerno_y][primerno_x - 1] + \
                                                   enemy_ships2[primerno_y][primerno_x + j] + \
                                                   enemy_ships2[primerno_y][primerno_x + j + 1] + \
                                                   enemy_ships2[primerno_y + 1][primerno_x + j + 1] + \
                                                   enemy_ships2[primerno_y - 1][primerno_x + j + 1] + \
                                                   enemy_ships2[primerno_y + 1][primerno_x + j] + \
                                                   enemy_ships2[primerno_y - 1][primerno_x + j]

                                if check_near_ships == 0:
                                    enemy_ships2[primerno_y][primerno_x + j] = i + 1
                            except Exception:
                                pass
                if horizont_vertikal == 2:
                    if primerno_y + len <= s_y:
                        for j in range(0, len):
                            try:
                                check_near_ships = 0
                                check_near_ships = enemy_ships2[primerno_y - 1][primerno_x] + \
                                                   enemy_ships2[primerno_y + j][primerno_x] + \
                                                   enemy_ships2[primerno_y + j + 1][primerno_x] + \
                                                   enemy_ships2[primerno_y + j + 1][primerno_x + 1] + \
                                                   enemy_ships2[primerno_y + j + 1][primerno_x - 1] + \
                                                   enemy_ships2[primerno_y + j][primerno_x + 1] + \
                                                   enemy_ships2[primerno_y + j][primerno_x - 1]

                                if check_near_ships == 0:
                                    enemy_ships2[primerno_y + j][primerno_x] = i + 1
                            except Exception:
                                pass

            print(f"Сreating ships for the player {2}........")

            sum_1_enemy = 0
            for i in range(0, s_x):
                for j in range(0, s_y):
                    if enemy_ships2[j][i] > 0:
                        sum_1_enemy = sum_1_enemy + 1

    def __del__(self):
        del self._ships
        print(f"Destruktor {Navy}")


class Window(Color):

    def __init__(self):
        self.tk = Tk()
        self.app_running = True
        self.size_canvas_x = 450
        self.size_canvas_y = 450
        self.tk.resizable(0, 0)
        self.tk.title("Statki 'beta test'")
        self.tk.protocol("WM_DELETE_WINDOW", self.on_closing)

        # liczba komórek w rozkładzie s_x * s_y
        self.s_x = 9
        self.s_y = 9
        self.step_x = self.size_canvas_x // self.s_x  # długość podziału komórki w pionie
        self.step_y = self.size_canvas_y // self.s_y  # długość podziału komórki w poziomie

        # sekcja pod menu, wielokrotność 4*(rozmiar komórki)
        self.menu_x =  self.step_x * 4

        # dodatkowa sekcja do podpisu wszystkich uczestników
        self.menu_y = 25
        self.delta_menu_x = 4

        # obszar roboczy dla komórek
        # pierwsza sekcja
        self.canvas = Canvas(self.tk, width=self.size_canvas_x + self.menu_x + self.size_canvas_x,
                             height=self.size_canvas_y + self.menu_y, bd=0, highlightthickness=0)
        self.canvas.create_rectangle(0, 0, self.size_canvas_x, self.size_canvas_y, fill=Color.light_cyan)
        # druga sekcja
        self.canvas.create_rectangle(self.size_canvas_x + self.menu_x, 0,self.size_canvas_x + self.menu_x +
                                     self.size_canvas_x, self.size_canvas_y, fill=Color.light_cyan)

        self.canvas.pack()
        self.tk.update()
        self.canvas.bind_all("<Button-1>", self.add_to_all)  # Left --typ: 0
        self.canvas.bind_all("<Button-3>", self.add_to_all)  # Right --typ: 1
        self.list_ids = []

        # points - lista miejsc, w które kliknęliśmy myszą
        # -1 = bez naciskania
        self.points = [[-1 for i in range(self.s_x)] for i in range(self.s_y)]
        self.points2 = [[-1 for i in range(self.s_x)] for i in range(self.s_y)]

    def draw_table(self):
        for i in range(0, self.s_x + 1):
            self.canvas.create_line(self.step_x * i, 0, self.step_x * i, self.size_canvas_y)
        for i in range(0, self.s_y + 1):
            self.canvas.create_line(0, self.step_y * i, self.size_canvas_x, self.step_y * i)

        b0 = Button(self.tk, text="Show ships Player №1", command=self.button_show_enemy1)
        b0.place(x=self.size_canvas_x + 20, y=30)

        b1 = Button(self.tk, text="Show ships Player №2", command=self.button_show_enemy2)
        b1.place(x=self.size_canvas_x + 20, y=70)

        b2 = Button(self.tk, text="Start again", command=self.button_begin_again)
        b2.place(x=self.size_canvas_x + 20, y=110)

        t0 = Label(self.tk, text="Player №1", font=("Helvetica", 48 >> 2)) # 12
        t0.place(x=self.size_canvas_x // 2 - t0.winfo_reqwidth() // 2, y=self.size_canvas_y + 3)
        t1 = Label(self.tk, text="Player №2", font=("Helvetica", 48 >> 2)) # 12
        t1.place(x=self.size_canvas_x + self.menu_x + self.size_canvas_x
                   // 2 - t1.winfo_reqwidth() // 2, y=self.size_canvas_y + 3)

        t0.configure(bg=Color.dark_red)
        t0.configure(bg=Color.static)

    def draw_table2(self,offset_x=0):
        offset_x = self.size_canvas_x + self.menu_x
        for i in range(0, self.s_x + 1):
            self.canvas.create_line(offset_x + self.step_x * i, 0, offset_x + self.step_x * i, self.size_canvas_y)
        for i in range(0, self.s_y + 1):
            self.canvas.create_line(offset_x, self.step_y * i, offset_x + self.size_canvas_x, self.step_y * i)

    def on_closing(self):
        global app_running
        if messagebox.askokcancel("Exit", "Get out of the game?"):
            app_running = False
            self.tk.destroy()

    def add_to_all(self, event):

        _type = 0  # left
        if event.num == 3:
            _type = 1  # right

        mouse_x = self.canvas.winfo_pointerx() - self.canvas.winfo_rootx()
        mouse_y = self.canvas.winfo_pointery() - self.canvas.winfo_rooty()

        ip_x = mouse_x // self.step_x
        ip_y = mouse_y // self.step_y

        if ip_x < self.s_x and ip_y < self.s_y:
            if self.points[ip_y][ip_x] == -1:
                self.points[ip_y][ip_x] = _type
                self.draw_point(ip_x, ip_y)

                if self.check_winner2():
                    time.sleep(2)
                    self.button_begin_again()
                    print("Victory!!!!!")
                    points = [[10 for i in range(self.s_x)] for i in range(self.s_y)]

        if ip_x >= self.s_x + self.delta_menu_x and ip_x <= self.s_x + self.s_x + self.delta_menu_x and ip_y < self.s_y:
            # print("ok")
            if self.points2[ip_y][ip_x - self.s_x - self.delta_menu_x] == -1:
                self.points2[ip_y][ip_x - self.s_x - self.delta_menu_x] = _type
                self.draw_point2(ip_x - self.s_x - self.delta_menu_x, ip_y)
                # if check_winner(ip_x, ip_y):
                if self.check_winner2():
                    time.sleep(2)
                    self.button_begin_again()
                    print("Victory!!!!!")
                    points2 = [[10 for i in range(self.s_x)] for i in range(self.s_y)]

    def draw_point(self, x, y):
        # print(enemy_ships[y][x])
        if enemy_ships[y][x] == 0:
            color = Color.violet
            id1 = self.canvas.create_oval(x * self.step_x, y * self.step_y, x * self.step_x + self.step_x,
                                          y * self.step_y + self.step_y, fill=color)
            id2 = self.canvas.create_oval(x * self.step_x + self.step_x // 3, y * self.step_y + self.step_y // 3,
                                     x * self.step_x + self.step_x - self.step_x // 3,
                                     y * self.step_y + self.step_y - self.step_y // 3, fill="white")
            self.list_ids.append(id1)
            self.list_ids.append(id2)

        if enemy_ships[y][x] > 0:
            color = Color.brown
            id1 = self.canvas.create_rectangle(x * self.step_x, y * self.step_y + self.step_y
                                               // 2 - self.step_y // 10, x * self.step_x + self.step_x,
                                          y * self.step_y + self.step_y // 2 + self.step_y // 10, fill=color)
            id2 = self.canvas.create_rectangle(x * self.step_x + self.step_x // 2 - self.step_x // 10, y * self.step_y,
                                          x * self.step_x + self.step_x // 2 + self.step_x
                                               // 10, y * self.step_y + self.step_y, fill=color)
            self.list_ids.append(id1)
            self.list_ids.append(id2)

    def draw_point2(self, x, y, offset_x=650):
        # print(enemy_ships1[y][x])
        if enemy_ships2[y][x] == 0:
            color = "red"
            id1 = self.canvas.create_oval(offset_x + x * self.step_x, y * self.step_y,
                                          offset_x + x * self.step_x + self.step_x,
                                     y * self.step_y + self.step_y, fill=color)
            id2 = self.canvas.create_oval(offset_x + x * self.step_x + self.step_x //
                                          3, y * self.step_y + self.step_y // 3,
                                     offset_x + x * self.step_x + self.step_x - self.step_x // 3,
                                     y * self.step_y + self.step_y - self.step_y // 3, fill="white")
            self.list_ids.append(id1)
            self.list_ids.append(id2)
        if enemy_ships2[y][x] > 0:
            color = "blue"
            id1 = self.canvas.create_rectangle(offset_x + x * self.step_x, y * self.step_y + self.step_y
                                               // 2 - self.step_y // 10,
                                          offset_x + x * self.step_x + self.step_x,
                                          y * self.step_y + self.step_y // 2 + self.step_y // 10, fill=color)
            id2 = self.canvas.create_rectangle(offset_x + x * self.step_x + self.step_x
                                               // 2 - self.step_x // 10, y * self.step_y,
                                          offset_x + x * self.step_x + self.step_x // 2 + self.step_x
                                               // 10, y * self.step_y + self.step_y,
                                          fill=color)
            self.list_ids.append(id1)
            self.list_ids.append(id2)

    def app_start(self):
        self.tk.mainloop()

    @protected
    def check_winner2(self):
        win = True
        for i in range(0, self.s_x):
            for j in range(0, self.s_y):
                if enemy_ships[j][i] > 0:
                    if self.points[j][i] == -1:
                        win = False
        # print(win)
        return win

    def button_show_enemy1(self):
        for i in range(0, self.s_x):
            for j in range(0, self.s_y):
                if enemy_ships[j][i] > 0:
                    color = "red"
                    if self.points[j][i] != -1:
                        color = "green"
                    _id = self.canvas.create_rectangle(i * self.step_x, j * self.step_y, i *
                                                       self.step_x + self.step_x, j * self.step_y + self.step_y,
                                                  fill=color)
                    self.list_ids.append(_id)

    def button_show_enemy2(self):
        for i in range(0, self.s_x):
            for j in range(0, self.s_y):
                if enemy_ships2[j][i] > 0:
                    color = "red"
                    if self.points2[j][i] != -1:
                        color = "green"
                    _id = self.canvas.create_rectangle(self.size_canvas_x + self.menu_x + i * self.step_x, j
                                                       * self.step_y,self.size_canvas_x + self.menu_x + i * self.step_x
                                                       +self.step_x, j * self.step_y + self.step_y,
                                                  fill=color)
                    self.list_ids.append(_id)

    def button_begin_again(self):  # start again

        for elements in self.list_ids:
            self.canvas.delete(elements)
        self.list_ids = []
        Navy().generate_enemy_ships()
        Navy().generate_enemy_ships2()
        self.points = [[-1 for i in range(self.s_x)] for i in range(self.s_y)]



if __name__ == '__main__':

    navy = Navy()

    navy.generate_enemy_ships()
    navy.generate_enemy_ships2()

    main_window = Window()

    main_window.draw_table()
    main_window.draw_table2()

    main_window.app_start()

