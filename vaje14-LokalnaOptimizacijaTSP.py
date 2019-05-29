# -*- coding: utf-8 -*-
import math
import random
import time
import tkinter as tk


def dolzina(problem):
    tocke = problem["tocke"]
    obhod = problem["obhod"]
    d = 0
    for i in range(len(obhod)):
        z, k = obhod[i - 1], obhod[i]
        d += ((tocke[z][0] - tocke[k][0]) ** 2 + (tocke[z][1] - tocke[k][1]) ** 2) ** 0.5
    problem["dolzina"] = d
    return problem


def novaRazporeditev(problem):
    obhod = problem["obhod"]
    tocke = problem["tocke"]
    novi_obhod = obhod[:]
    random.shuffle(novi_obhod)
    return {"tocke": tocke, "obhod": novi_obhod}

def zamenjava(problem):
    obhod = problem["obhod"]
    tocke = problem["tocke"]
    l = len(obhod)
    a, b = random.randrange(l), random.randrange(l)
    if a > b:
        a, b = b, a
    novi_obhod = obhod[:a] + list(reversed(obhod[a:b])) + obhod[b:]
    return {"tocke": tocke, "obhod": novi_obhod}

def naslednji_problem(problem, f):
    novi_problem = dolzina(f(problem))
    if novi_problem["dolzina"] < problem["dolzina"]:
        return novi_problem
    else:
        return problem

def kroznica(n):
    fi = 2 * math.pi / n
    return [(0.5 + math.cos(k * fi) / 2,
             0.5 + math.sin(k * fi) / 2) for k in range(n)]

def oboje(p):
    return lambda problem: (novaRazporeditev if random.random() < p else zamenjava)(problem)

# Algoritem lahko preizkušaš na:
# >>> preizkusi(tocke)                 - seznamu točk tocke
# >>> preizkusi(kroznica(20))          - seznamu 20 točk na krožnici
# >>> preizkusi(n=20)                  - seznamu 20 naključnih točk
# >>> preizkusi()                      - seznamu 50 naključnih točk

# Izbereš lahko tudi način iskanja nove rešitve:
# >>> preizkusi()                      - naključna razporeditev
# >>> preizkusi(next=zamenjava)        - zamenjava dveh povezav
# >>> preizkusi(next=oboje(p))         - naključna razporeditev z verjetnostjo
#                                        p, sicer zamenjava dveh povezav

class Lokalna:
    def __init__(self, master, problem, next, width=500, height=500):
        self.master = master
        self.canvas = tk.Canvas(master, width=width, height=height)
        self.canvas.pack()

        self.running = False
        self.problem = problem
        self.real_coords = [(10 + x * (width - 20), 10 + y * (height - 20)) for (x, y) in self.problem["tocke"]]

        self.elapsed = 0
        self.elapsed_timer = tk.Label(master, text="Čas: 0.000")
        self.elapsed_timer.pack(side="left")

        self.steps = -1
        self.step_counter = tk.Label(master, text="Koraki: 0")
        self.step_counter.pack(side="left")

        self.length = problem["dolzina"]
        self.length_display = tk.Label(master, text="Dolžina: {:02.3f}".format(self.length))
        self.length_display.pack(side="left")

        self.next = next
        self.next_button = tk.Button(master, text="Korak", command=self.next_step)
        self.next_button.pack(side="right")

        self.run_button = tk.Button(master, text="Zaženi", command=self.toggle_running)
        self.run_button.pack(side="right")

        self.draw_path(True, 0)

    def make_step(self):
        next = naslednji_problem(self.problem, self.next)
        if next is None:
            return False
        else:
            self.problem = next
            return True

    def next_step(self):
        start = time.time()
        draw = self.make_step()
        finish = time.time()
        self.draw_path(draw, finish - start)

    def toggle_running(self):
        self.running = not self.running
        if self.running:
            self.run_button.configure(text="Ustavi")
            self.run()
        else:
            self.run_button.configure(text="Zaženi")

    def run(self):
        if self.running:
            n = 0
            start = time.time()
            while n < 100 and self.make_step():
                n += 1
            finish = time.time()
            self.draw_path(n, finish - start)
            if n == 100:
                self.master.after(10, self.run)
            else:
                self.toggle_running()

    def draw_path(self, steps, elapsed):
        self.elapsed += elapsed
        self.elapsed_timer.configure(text="Čas: {:02.3f}".format(self.elapsed), anchor="w")
        self.steps += steps
        self.step_counter.configure(text="Koraki: {}".format(self.steps), anchor="w")
        self.length = self.problem["dolzina"]
        self.length_display.configure(text="Dolžina: {:02.3f}".format(self.length), anchor="w")
        if steps:
            self.canvas.delete(tk.ALL)
            for i in range(len(self.problem["obhod"])):
                z, k = self.problem["obhod"][i - 1], self.problem["obhod"][i]
                self.canvas.create_line(self.real_coords[z][0], self.real_coords[z][1],
                                        self.real_coords[k][0], self.real_coords[k][1])
            for x, y in self.real_coords:
                self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill='red')


def preizkusi(tocke=None, n=50, next=novaRazporeditev, seed=None, sirina=500, visina=500):
    if seed:
        random.seed(seed)
    if tocke is None:
        tocke = [(random.random(), random.random()) for i in range(n)]
    obhod = list(range(len(tocke)))
    random.shuffle(obhod)
    root = tk.Tk()
    root.title("Lokalna optimizacija problema trgovskega potnika")
    Lokalna(root, dolzina({'tocke': tocke, 'obhod': obhod}), next=next, width=sirina, height=visina)
    root.mainloop()
