# -*- coding: utf-8 -*-
"""Untitled42.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qsu8me60EwizE_729zAeUBNQuNQRaQp2
"""

import sys
import os
import random
import time
import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


class player:
    def __init__(self, location, health, items):
        self.location = location
        self.health = health
        self.items = items

hero = player("entry", 100, 0)

class NPC:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def talk(self):
        game_functions.fprint(f"A {self.name} emerges from the shadows.")
        game_functions.fprint("'Hisssss! Stay away from me!'")

    def move(self):
        available_locations = ["entry", "door", "lake", "alarming", "cavern", "hallway", "pit", "gold"]
        self.location = random.choice(available_locations)


goblin = NPC("goblin", "hallway")

class GUI:
    
    def __init__(self, window):
        self.window = window

# window = tkinter.Tk()
        window.title("Adventure Game")

        window.geometry("966x745")
        window.minsize(width=966, height=745)
        window.maxsize(width=966, height=745)

        frame = Frame(window)
        frame.pack()
        
        print("Medkits", hero.items)


        # Getting and setting up image
        
        self.img = ImageTk.PhotoImage(Image.open("start.png"))

        # Loading Background Image
        self.label = tkinter.Label(frame, image=self.img)
        self.label.pack()

        self.l1 = tkinter.Label(frame, text="WELCOME TO OUR ADVERNTURE GAME")
        self.l1.pack()

        health_text = "HEALTH = " + str(hero.health)

        self.l2 = tkinter.Label(frame, text=health_text, bg="Black", fg="White")
        self.l2.pack()

        medkit_text = "MEDKITS = " + str(hero.items)

        self.l3 = tkinter.Label(frame, text=medkit_text, bg="Black", fg="White")
        self.l3.pack()

        self.b1 = tkinter.Button(frame, width=15, height=3, text="START", command=self.Entry)
        self.b1.pack()

        self.yes_1 = tkinter.Button(frame, width=15, height=1, text="YES")
        # yes_1.pack()

        self.no_1 = tkinter.Button(frame, width=15, height=1, text="NO")
        # no_1.pack()

        self.use_medkit = tkinter.Button(frame, width=15, height=1, text="USE MEDKIT")

    def medkit(self):
        medkit_find = random.choice([True, False])
        if medkit_find is True:
            hero.items += 1
            tkinter.messagebox.showinfo( "Medkit", "Medkit Found!!")
            medkit_text = "MEDKITS = " + str(hero.items)
            self.l3.configure(text=medkit_text)
            self.l3.pack()
            # game_functions.fprint("You found a medkit!", 2)
            # print("Enter 'm' to use it.")

    def using_medkit(self):
        if hero.items >= 1:
            hero.health = 100
            health_text = "HEALTH = " + str(hero.health)

            hero.items -= 1

            medkit_text = "MEDKITS = " + str(hero.items)
            self.l3.configure(text=medkit_text)
            self.l3.pack()

            self.l2.configure(text=health_text)

    def bat_attack(self):
        bat_attack = random.choice([True, False])
        if bat_attack is True:
            tkinter.messagebox.showinfo( "Attack", "Bat Attack!!")
            hero.health -= random.randint(1, 100)
            health_text = "HEALTH = " + str(hero.health)
            self.l2.configure(text=health_text)

            # Killin the Game
            if hero.health <= 0:
                tkinter.messagebox.showinfo( "Death", "You Died!!")
                self.window.destroy()
                sys.exit()

    
    def handle_goblin(self):
        goblin.move()
        if hero.location == goblin.location:
            print("ATTACK")

    # Creatig Button function
    def create_btn(self, str, cmd):
        btn = self.tkinter.Button(self.frame, width=15, height=1, text=str, command=cmd)
        return btn

    # # Creating Yes and No Buttons
    # yes_1 = create_btn("YES", "")
    # no_1 = create_btn("NO", "")

# # Healt Bar
# l2 = tkinter.Label(frame, text="HEALTH = 100", bg="Black", fg="White")

    # Clearin Frame of all widets
    def clear_frame(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()

    def change_img(self,str):
        self.img2=ImageTk.PhotoImage(Image.open(str))
        self.label.configure(image=self.img2)
        self.label.image=self.img2




    def Entry(self):
        self.change_img("Cave2.png")
        self.b1.destroy()
        
        self.yes_1.pack()
        self.no_1.pack()
        
        self.l2.pack()
        self.l1.config(text="You are in a dark cave. The entry has been sealed by fallen rocks. There is no way out. Ahead, you can see a door. Will you continue?")


        # yes_1 = tkinter.Button(frame, width=15, height=1, text="YES" command=Kick)
        self.yes_1.configure(command=self.yes_kick)
        self.yes_1.pack()
        

        self.no_1.configure(command=self.no_kick)
        self.no_1.pack()

        self.use_medkit.configure(command=self.using_medkit)
        self.use_medkit.pack()



    def yes_kick(self):
        print("Location", hero.location)
        self.medkit()
        self.bat_attack()

        self.change_img("door.png")
        self.l1.config(text="Door is opened by kick. Contains fast wind. Hero crawls to groung and reach end. Will you crawl?")
        self.yes_1.configure(command=self.Door)
        # yes_1.pack()

    def no_kick(self):
        self.change_img("bat.png")
        self.l1.config(text="A bat flies over your head and you hear screetches in the distance. You sit in total darkness wondering if there's a way out.")


    def Door(self):
        self.medkit()
        self.bat_attack()

        self.change_img("Lake2.png")
        self.l1.config(text="It's a long lake and there are two crocodiles in it. Ahead, you can see a rope. Will you swing from rope to get to end point?")
        self.l2.pack()
        self.no_1.configure(command=self.no_Door)
        self.yes_1.configure(command=self.Alarming)

    def no_Door(self):
        self.l1.config(text="You are injured because crocodile hits you. You are thinking any other way except using rope.")
        self.l2.pack()

    def Alarming(self):
        self.medkit()
        self.bat_attack()

        self.change_img("sand_dune.png")
        self.l1.config(text="Space contains fire with sand dunes. Hero puts off fire with sand. Will you do this?")
        self.l2.pack()
        self.no_1.configure(command=self.no_Alarming)
        self.yes_1.configure(command=self.Cavern)

    def no_Alarming(self):
        self.l1.config(text="Your one leg and arm has burned because of fire.")
        self.l2.pack()


    def Cavern(self):
        self.medkit()
        self.bat_attack()

        self.change_img("Cavern.png")
        self.l1.config(text="You stumble into a dimly lit cavern. You cannot go right or left but the cave continues ahead. Will you go on?")
        self.l2.pack()
        self.no_1.configure(command=self.no_Cavern)
        self.yes_1.configure(command=self.Hallway)

    def no_Cavern(self):
        self.l1.config(text="You sit down and eat some food you brought with you.")
        self.l2.pack()

    def Hallway(self):
        self.medkit()
        self.bat_attack()

        self.change_img("hallway.png")
        self.l1.config(text="You are in a wide hallway. It continues on indefinitely. There's no turning back. Will you go on?")
        self.l2.pack()
        self.no_1.configure(command=self.no_Hallway)
        self.yes_1.configure(command=self.Pit)

    def no_Hallway(self):
        self.l1.config(text="You try to call your help but no one is there.")
        self.l2.pack()

    def Pit(self):
        self.medkit()
        self.bat_attack()

        self.change_img("Pit.png")
        self.l1.config(text="You fall head first into an ominous and languid pit. Luckly, you only landed on your back. You can try to climb out. Will you try?")
        self.l2.pack()
        self.no_1.configure(command=self.no_Pit)
        self.yes_1.configure(command=self.Gold)

    def no_Pit(self):
        self.l1.config(text="You sit in utter darkness.")
        self.l2.pack()

    def Gold(self):
        self.change_img("Gold.png")
        self.l1.config(text="You reached to your final destination.Finally, you can see gold. You can take the gold. Will you take?")
        self.l2.pack()
        self.no_1.configure(command=self.Lose)
        self.yes_1.configure(command=self.Win)


    def Lose(self):
        self.change_img("Lose.png")
        self.l1.config(text="You did not take the Gold. GAME OVER!")

    def Win(self):
        self.change_img("Win.png")
        self.l1.config(text="You took enough gold. GAME OVER!")
        self.l2.pack()


class Game:

    def print_slow(self, str, delay=0.1):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(delay)
        print("\n")


    def reset_console(self):
        print("\n")
        os.system('cls||clear')


    def fprint(self, str, delay=0):
        print("\n" + str)
        time.sleep(delay)


    def sprint(self, str, delay=0):
        print(str)
        time.sleep(delay)


game_functions = Game()








class World:

    def entry(self):
        hero.location = "entry"
        print(f"\nHealth: {hero.health}")
        game_functions.fprint("You are in a dark cave. The entry has been sealed by fallen rocks. There is no way out.", 2)
        print("Ahead, you can see a door. Will you continue?")
        print("Enter 'yes' or 'no'.")
        self.check_medkit()
        self.handle_goblin()
        while True:
            action = input("\n> ")
            if action == "yes":
                self.door()
            elif action == "no":
                game_functions.fprint("A bat flies over your head and you hear screetches in the distance.")
            elif action == "m":
                self.use_medkit()
            else:
                game_functions.fprint("You sit in total darkness wondering if there's a way out.")

    def door(self):
        hero.location = "door"
        print(f"\nHealth: {hero.health}")
        game_functions.fprint("Door is opened by kick. Contains fast wind.", 2)
        print("Hero crawls to groung and reach end. Will you crawl?")
        print("Enter 'yes' or 'no'.")
        self.check_medkit()
        self.handle_goblin()
        while True:
            action = input("\n> ")
            if action == "yes":
                self.lake()
            elif action == "no":
                game_functions.fprint("You hear loud voices of wind.")
            elif action == "m":
                self.use_medkit()
            else:
                game_functions.fprint("You are scare of voices.")

    def lake(self):
        hero.location = "lake"
        print(f"\nHealth: {hero.health}")
        game_functions.fprint("It's a long lake and there are two crocodiles in it.", 2)
        print("Ahead, you can see a rope. Will you swing from rope to get to end point?")
        print("Enter 'yes' or 'no'.")
        self.check_medkit()
        self.handle_goblin()
        while True:
            action = input("\n> ")
            if action == "yes":
                self.alarming()
            elif action == "no":
                game_functions.fprint("You are injured because crocodile hits you.")
            elif action == "m":
                self.use_medkit()
            else:
                game_functions.fprint("You are thinking any other way except using rope.")

    def alarming(self):
        hero.location = "alarming"
        print(f"\nHealth: {hero.health}")
        game_functions.fprint("Space contains fire with sand dunes.", 2)
        print("Hero puts off fire with sand. Will you do this?")
        print("Enter 'yes' or 'no'.")
        self.check_medkit()
        while True:
            action = input("\n> ")
            if action == "yes":
                self.cavern()
            elif action == "no":
                game_functions.fprint("Your one leg and arm has burned because of fire.")
            elif action == "m":
                self.use_medkit()
            else:
                game_functions.fprint("You are feeling very hot.")

    def cavern(self):
        hero.location = "cavern"
        print(f"\nHealth: {hero.health}")
        game_functions.fprint("You stumble into a dimly lit cavern.", 2)
        print("You cannot go right or left but the cave continues ahead. Will you go on?")
        print("Enter 'yes' or 'no'.")
        self.check_bat_attack()
        self.handle_goblin()
        while True:
            action = input("\n> ")
            if action == "yes":
                self.hallway()
            elif action == "no":
                game_functions.fprint("You sit down and eat some food you brought with you.")
            elif action == "m":
                self.use_medkit()
            else:
                game_functions.fprint("You shiver from the cold.")

    def hallway(self):
        hero.location = "hallway"
        print(f"\nHealth: {hero.health}")
        game_functions.fprint("You are in a wide hallway. It continues on indefinitely.", 2)
        print("There's no turning back. Will you go on?")
        print("Enter 'yes' or 'no'.")
        self.handle_goblin()
        while True:
            action = input("\n> ")
            if action == "yes":
                self.pit()
            elif action == "no":
                game_functions.fprint("You try to call your help but no one is there.")
            elif action == "m":
                self.use_medkit()
            else:
                game_functions.fprint("You wonder what time it is.")

    def pit(self):
        hero.location = "pit"
        print(f"\nHealth: {hero.health}")
        game_functions.fprint("You fall head first into an ominous and languid pit. Luckly, you only landed on your back", 2)
        print("You can try to climb out. Will you try?")
        print("Enter 'yes' or 'no'.")
        self.handle_goblin()
        while True:
            action = input("\n> ")
            if action == "yes":
                self.gold()
            elif action == "no":
                game_functions.fprint("You sit in utter darkness.")
            elif action == "m":
                self.use_medkit()
            else:
                game_functions.fprint("You feel hopeless.")

    def gold(self):
        hero.location = "gold"
        print(f"\nHealth: {hero.health}")
        game_functions.fprint("You reached to your final destination.", 2)
        game_functions.sprint("Finally, you can see gold.", 2)
        print("You can take the gold. Will you take?")
        print("Enter 'yes' or 'no'.")
        while True:
            action = input("\n> ")
            if action == "yes":
                game_functions.fprint("You take enough gold.", 2)
                print("GAME OVER.")
                sys.exit()
            elif action == "no":
                game_functions.fprint("You don't find the gold, you lose.")
            elif action == "m":
                self.use_medkit()
            else:
                game_functions.fprint("You give up.")




    def use_medkit(self):
        if "medkit" in hero.items:
            hero.items -= 1
            game_functions.fprint("You used your medkit")
            hero.health = 100
            print(f"\nHealth: {hero.health}")
        else:
            game_functions.fprint("You don't have a medkit.")


    def handle_goblin(self):
        goblin.move()
        if hero.location == goblin.location:
            goblin.talk()


    def check_medkit(self):
        medkit_find = random.choice([True, False])
        if medkit_find is True:
            hero.items += 1
            game_functions.fprint("You found a medkit!", 2)
            print("Enter 'm' to use it.")


    def check_bat_attack(self):
        bat_attack = random.choice([True, False])
        if bat_attack is True:
            game_functions.fprint("You were attacked by a bat!", 2)
            hero.health -= random.randint(1, 100)
            print(f"\nHealth: {hero.health}")
            if hero.health == 0:
                game_functions.fprint("You are dead!")
                sys.exit()


root = Tk()
gui = GUI(root)
root.mainloop()

# new_world = World()


# new_world.entry()