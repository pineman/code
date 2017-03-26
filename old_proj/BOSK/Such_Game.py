#!/usr/bin/python3
# Rodrigo Serrão @2014

'''
It has been conventioned that, as long as we refer to formulas, like combat
formulas, or the ones to set the Exp to the next level, attributes from
the 'self' come with a single letter representing it:
for example, in the damage formula A is the self.attack;
attributes from a second object are followed by a 2:
e.g., in the damage formula, D2 is the 'other'.defense

To run the formulas, .format() must be used to "fill in the gaps"
'''

from random import randint, random, choice, shuffle
from time import sleep
from sys import exit
from math import sqrt
import hashlib
import cmd

print("\"Such Game\" was created by Rodrigo Serrão.")
print("copyright @ 2014")
sleep(0)

# The skills a player has
SKILLS = ["hp", "strength", "attack", "defense", "luck", "energy", "magic",
        "speed"]
# The boundaries of a critical hit chance
LUCK_BOUNDS = [2, 60]
# player.hp * HP_MULT gives his actual health
HP_MULT = 10
# same with <ENERGY_MULT>
ENERGY_MULT = 6
PROMPT = " >> "
# defined beasts and levels at which they get unlocked
BEASTS = {"murloc" : 1}
# the drops of each beast
ITEMS = {"murloc": ["bone", "eye"]}

def DEBUG(g, l, e):
    '''Debugging function to be called when errors were expected.
    Receives as arguments the locals() and globals() of the scope in which the
    error was to be raised, just as the error. The error gets printed and a loop
    runs until the debugger exits with \'exit(X)\''''
    # <g> and <l> are both the globals and locals from which the debugging
    #function was called! This lets me play around with the problems
    print("You just entered the debugger")
    print("The error that took you here was:")
    print(e)
    print("#"*40)
    while True:
        try:
            exec(input("[debugger] > "), g, l)
        except Exception as error:
            print("[Error...]")
            print(error)


def assign_tokens(data, n, show_help=False):
    '''Given a 'n' number of skillpoints available, and data either a list of
    the levels of the skills, or a player with an attr <get_skills()>, run a
    loop to let the player spend those skillpoints'''
    # Check if <data> is of one of the required types
    if type(data) != list:
        try:
            data = data.get_skills()
        except Exception as e:
            print("Wrong type of data passed to <assign_tokens>")
            DEBUG(globals(), locals(), e)
    # Store the initial values to prevent the player to lower them too much
    ###NOTE: don't do <init_data = data>, because a change to <data> would
    ###change <init_data> too!!!
    init_data = [val for val in data]
    global SKILLS
    print("You have "+str(n)+" skill points available")
    print("You are to choose skills that you will level up, spending one skill"\
    "point per level.")
    print("You can divide it as you wish.")
    print()
    if show_help:
        print("The skills are:")
        print("HP : Determines your life total")
        print("Strength : Determines what weapons you can use and how much damage they deal")
        print("Attack : Determines whether you will hit or not and helps boosting the damage")
        print("Defense : Determines if the enemy hits, what shields you can use, and helps reducing the damage")
        print("Luck : Determines if you hit for a critical, and helps reducing the enemy chances of a critical hit")
        print("Energy : Sets the total energy you can have (it is used for magic spells and stronger blows")
        print("Magic : Determines which spells you can use and their effects")
        print("Speed : Determines who strikes first")
    input("...")
    print("Type &help to get help")
    sep = "#" * 40
    while True:
        # Run the loop. Let <c> store the command inputed
        c = input(">> ").lower().strip()
        if not(c.startswith("&")):
            print("Unknown command...")
            print(sep)
            continue
        # Split <c> into arguments for easier accessing
        args = c.split()
        if c.startswith("&help"):
            print("Skills are hp, strength, attack, defense, endurance and luck")
            print("Use <&add skill X> to add X points to given skill")
            print("Use <&set skill X> to set the given skill to level X")
            print("Use <&reset skill> to reset the skill to the initial value")
            print("Use <&check> to see how your skills are assigned")
            print(sep)
        elif args[0] == "&check":
            for i in range(len(SKILLS)):
                print("Your skill "+SKILLS[i]+":")
                print("\tCurrently at level "+str(data[i])+" and entered here at lvl "+str(init_data[i]))
            print("You also have "+str(n)+" skill points left")
            print(sep)
        elif args[0] == "&reset":
            if args[1] not in SKILLS:
                print("Unknown skill")
                print(sep)
                continue
            i = SKILLS.index(args[1])
            # calculate how many points have been used in this skill to re-add
            #them to 'n'
            dif = init_data[i] - data[i]
            data[i] = init_data[i]
            n += dif
        elif args[0] == "&add":
            try:
                try:
                    # let <p> be the points the user wants to add
                    p = int(args[2])
                except ValueError:
                    print("The argument X must be a number")
                    print(sep)
                    continue
            except IndexError:
                print("You must provide a level to add to the skill!")
                print(sep)
                continue
            if p > n: # the user is trying to add more than he has
                print("You only have "+str(n)+" points available")
                print(sep)
                continue
            else:
                if args[1] not in SKILLS:
                    print("Unknown skill... Use &help for help")
                    print(sep)
                    continue
                n -= p
                # find the index of the wanted skill and change its value
                # in the variable <data>
                data[SKILLS.index(args[1])] += p
                print("You have "+str(n)+" points left!")
                print(sep)
        elif args[0] == "&set":
            try:
                try:
                    p = int(args[2])
                except ValueError:
                    print("The argument X must be a number")
                    print(sep)
                    continue
            except IndexError:
                print("You must provide a level to set to!")
                print(sep)
                continue
            if args[1] not in SKILLS:
                print("Unknown skill. Use &help for help")
                print(sep)
                continue
            # compute the number of tokens needed to set the given skill
            # to the given level
            i = SKILLS.index(args[1])
            if p < init_data[i]:
                print("You cannot set a skill to a level lower than the one"\
                " you had when you entered the Stat Assigner")
                print(sep)
                continue
            # the next 7 lines work for both augmenting and reducing skills!
            dif = p - data[i]
            if dif > n:
                print("You only have "+str(n)+" points and you needed "+str(dif))
                print(sep)
                continue
            data[i] = p
            n -= dif
            print("You now have "+str(n)+" skill poins")
            print(sep)
        elif args[0] == "&done":
            if n != 0:
                print("You still have points to spend.")
                print(sep)
                continue
            else:
                print("Exiting the Stat Assigner")
                # return the list. if called by a Player, they can handle it
                return data
        else:
            print("Unknown command... Type &help for help!")
            print(sep)


class Player(object):
    
    def __init__(self, name, level, hp, strength, attack, defense, luck, energy,
                magic, speed, exp=0, money=0, inventory=None):
                    
        if inventory == None:
            inventory = {"Flashlight": 1}
        
        global SKILLS
        args = ["name", "level"] + SKILLS + ["exp", "money", "inventory"]
        # cheating a little bit, this does all that boring self.X = X
        for arg in args:
            exec("self."+arg+" = "+arg)
        self.INIT_EXP = 200
        self.RATIO = 1.2
        # Formula to give the total of exp needed for the next level:
        # int((init*(1-(r^(x))))/(1-r)) where init is the initial exp value
        # x is the level you are at and r is the ratio
        # that is also the formula to find the sum of 'x' terms in a GP
        self.EXP_FORMULA = "int(({I}*(1-(pow({R}, {L}"\
        "))))/(1-{R}))"
        # Combat formulas:
        # Damage
        # (0.1*self.strength + self.attack) * sqrt(self.attack/other.defense)
        self.DMG_FORMULA = "(0.1*{S} + {A}) *"\
                  " sqrt({A}/{D2})"
        # Critical hit chance (%)
        ##let a = 2.1885e-3; b = 0.07188552; c = 0.92592592;
        ## X1 = self.luck; X2 = other.luck
        # 2.3(aX1^2 + bX1 + c) - 0.5(aX2^2 + bX2 + c)
        # when X1 >> X2, the formula tends to 1.8(aX1^2 + bX1 + c),
        #which is purposedly slightly less than the initial desired values!
        # if it falls of the boundaries established in LUCK_BOUNDS, adjust
        self.CRIT_FORMULA = "2.3*(2.1885e-3*{L1}**2+0.07188552*{L1}+0.92592592)"\
        "-0.5*(2.1885e-3*{L2}**2+0.07188552*{L2}+0.92592592)"
        
        #Shouldn't happen, but be sure that the EXP is updated
        self.to_next_level = eval(self.EXP_FORMULA.format(
                L=self.level, R=self.RATIO, I=self.INIT_EXP))
        self.update_exp(False)

        print("Initialization executed cooly")
        
    def get_items(self):
        global ITEMS
        items = []
        beasts = self.get_beasts()
        for beast in beasts:
            items += ITEMS[beast]
        return items
        
    def get_beasts(self):
        global BEASTS
        return [key for key in BEASTS.keys() if BEASTS[key] >= self.level]
        
    def update_exp(self, display = True):
        
        global SKILLS, assign_tokens
        
        # <hit> will say how many times we have to call the <assign_tokens>
        hit = 0
        while self.exp >= self.to_next_level:
            self.level += 1
            if display:
                print("You have just advanced to level " + str(self.level) + "!")
            hit += 1
            self.to_next_level = eval(self.EXP_FORMULA.format(
                L=self.level, R=self.RATIO, I=self.INIT_EXP))
        if hit:
            new = assign_tokens(self, round(len(SKILLS)/2+0.01)*hit, False)
            self.set_skills(new)
        if display:
            print("To reach the next level you need a total " + str(
            self.to_next_level) + " exp.")
            print("You have " + str(self.exp))
            
    def get_skills(self):
        
        global SKILLS
        skills = []
        for skill in SKILLS:
            skills.append(eval("self."+skill))
        return skills
        
    def set_skills(self, data):
        
        global SKILLS
        
        if len(data) != len(SKILLS):
            e = IndexError("<data> and <SKILLS> have different sizes")
            DEBUG(globals(), locals(), e)
            
        for i in range(len(SKILLS)):
            exec("self." + SKILLS[i] + " = " + str(data[i]))
        
    def get_data(self):
        
        data = [self.name, self.level] + self.get_skills() + [self.exp]
        return data
        
    def deal_damage(self, enemy):

        if type(enemy) != Enemy:
            print("Got a problem here in the Player's deal_damage function")
            DEBUG(globals(), locals(),
                e = TypeError("Wrong type of enemy to check for damage."))

        d = eval(self.DMG_FORMULA.format(A=self.attack, S=self.strength, 
                                        D2=enemy.defense))

        if self.is_critical(enemy):
            if self.is_critical(enemy):
                print("Super Critical!")
                return round(d*2+0.01)
            else:
                print("Critical!")
                return round(d*1.5+0.01)
        else:
            return round(d+0.01)

    def is_critical(self, enemy):

        if type(enemy) != Enemy:
            print("Got a problem here in the Player's is_critical function")
            DEBUG(globals(), locals(),
                e = TypeError("Wrong type of enemy to check for critical."))
        
        v = eval(self.CRIT_FORMULA.format(L1=self.luck, L2=enemy.luck))
        v = 2 if v < 2 else v
        v = 60 if v > 60 else v
        
        return 100*random() <= v
        
    def pprint(self):
        
        global SKILLS

        m1 = len(self.name) + 5
        # m1 is just the width of the first column
        # m2 is the maximum width the display will have
        m2 = 50
        # top bar
        print("#"*m2)
        i = m1 - 5
        name_s = "# " + self.name + " "*i + "## Level " + str(self.level) +\
        "   ## Exp: " + str(self.exp) + "/" + str(self.to_next_level)
        # Find how many characters are missing for the total width
        i = m2-1-len(name_s)
        name_s += " "*i + "#"
        print(name_s)
        # Pseudo-GUI for the progress of exp
        # Find the difference of this level's total exp and the last one
        # Say that you are level 2. You need 440 exp. You needed 200. the diff is 240
        # If you have, say, 300, do 300-200 = 100; Find the % completed: 100/240
        a = eval(self.EXP_FORMULA.format(L=self.level, R=self.RATIO,
                I=self.INIT_EXP))
        b = eval(self.EXP_FORMULA.format(L=self.level-1, R=self.RATIO,
                I=self.INIT_EXP))
        diff = a-b
        done = (self.exp-b)/diff
        c = round(done*m2)
        print("-"*c + "#"*(50-c))
        for skill in SKILLS:
            # the same as above, but for each skill
            i = m1 - len(skill)
            s = "# " + skill + " "*i + "## Level " + str(eval("self."+skill))
            i = m2-1-len(s)
            s += " "*i + "#"
            print(s)
        s = "You also have " + str(self.money) + " $$ "
        i = m2-len(s)
        print(s + "#"*i)
        print("#"*m2)
        ###NOTE: Re-learn those nice shortcuts that .format() provides for these
        ###DUMBASS, string-manipulating tasks!


class Enemy(object):

    def __init__(self, p_lvl):
        
        try:
            self.create_stats(p_lvl)
        except Exception as e:
            DEBUG(globals(), locals(), e)
        print("Enemy object instantiated cooly")
        
        # Combat formulas equal to the player for most enemies

        self.DMG_FORMULA = "(0.1*{S} + {A}) *"\
                  " sqrt({A}/{D2})"
        self.CRIT_FORMULA = "2.3*(2.1885e-3*{L1}**2+0.07188552*{L1}+0.92592592)"\
        "-0.5*(2.1885e-3*{L2}**2+0.07188552*{L2}+0.92592592)"
    
    def deal_damage(self, player):

        if type(player) != Player:
            print("Got a problem here in the Enemy's deal_damage function")
            DEBUG(globals(), locals(),
                e = TypeError("Wrong type of player to check for damage."))

        d = eval(self.DMG_FORMULA.format(S=self.strength, A=self.attack,
                                        D2=player.defense))

        if self.is_critical(player):
            if self.is_critical(player):
                print("Super Critical!")
                return round(d*2+0.01)
            else:
                print("Critical!")
                return round(d*1.5+0.01)
        else:
            return round(d+0.01)

    def is_critical(self, player):

        if type(player) != Player:
            print("Got a problem here in the Enemy's is_critical function")
            DEBUG(globals(), locals(),
                e = TypeError("Wrong type of player to check for critical."))
                
        v = eval(self.CRIT_FORMULA.format(L1=self.luck, L2=player.luck))
        v = 2 if v < 2 else v
        v = 60 if v > 60 else v
        
        return 100*random() <= v
        
        
class Murloc(Enemy):
    
    def __init__(self, p_lvl):
        
        try:
            Enemy.__init__(self, p_lvl)
        except Exception as e:
            print("Error inside the Murloc __init__")
            DEBUG(globals(), locals(), e)
        print("Murloc created cooly...")
        
        
    def create_stats(self, p_lvl):
        
        global SKILLS
        
        l = randint(round(p_lvl*0.9), round(p_lvl*0.95))
        
        for skill in SKILLS:
            exec("self."+skill+" = l*2")
            
            
    def drops(self):
        
        global ITEMS
        
        
class Battlefield(cmd.Cmd):
    
    def __init__(self, player, enemy):
        
        cmd.Cmd.__init__(self)
        
        global ENERGY_MULT, HP_MULT
        
        self.player = player
        self.enemy = enemy
        self.player.max_hp = self.player.hp * HP_MULT
        self.player.max_energy = self.player.energy * ENERGY_MULT
        self.enemy.max_hp = self.enemy.hp * HP_MULT
        self.enemy.max_energy = self.enemy.energy * ENERGY_MULT
        
    def do_exit(self, s):
        
        return True
    
    def postloop(self):
        
        del self.player.max_hp, self.enemy.max_hp
        del self.player.max_energy, self.enemy.max_energy
        print("Exiting")
        
        
class Plains(cmd.Cmd):
    
    def __init__(self, player):
        
        cmd.Cmd.__init__(self)
        self.player = player
        # Time interval for the wandering function
        self.W_BOUNDS = [5, 30]
        
        global PROMPT
        
        self.prompt = "["+self.player.name+"\\Plains]" + PROMPT
        self.intro("To return to your Home Town use the command <return>")
        
    def do_return(self, s):
        
        print("You are about to return to your Home Town. Are you sure?")
        while True:
            inp = input("Y/N >> ").lower().strip()
            if inp == "y":
                return True
            elif inp == "n":
                return
            
    def help_return(self):
        
        print("Use the <return> command to return to your Home Town")
        
    def do_wander(self, s):
        
        global sleep, randint, ITEMS
        
        if s != "":
            print("<wander> takes no arguments!")
            return
            
            
    def postloop(self):
        
        return self.player

    
class HomeTown(cmd.Cmd):
    
    def __init__(self, player):
        
        global PROMPT
        
        cmd.Cmd.__init__(self)
        
        self.player = player
        
        self.prompt = "[" + self.player.name + "\\HomeTown]" + PROMPT
        self.intro = "Welcome"

        global p
        del p
        
    def do_go(self, s):
        
        places = ["plains", "market", "blacksmith"]
        s = s.lower().strip()
        if s not in places:
            print("*** Unknown argument <"+s+">")
            s2 = ""
            for place in places:
                s2 += place+", "
            s2 = s2[:-2]
            print("Try one of " + s2)
            return
        if s == "plains":
            self.player = Plains(self.player).cmdloop()
        
    def help_go(self):
        
        print("<go> <place> is a command that takes you to <place>")
        print("if <place> isn't recognised, returns without a problem")

    def do_console(self, s):

        p = "21232f297a57a5a743894a0e4a801fc3"
        global hashlib
        m = hashlib.md5(s.encode("utf8")).hexdigest()
        if p != m:
            print("Wrong password key")
            return
        del p, m
        while True:
            inp = input("[console] > ")
            if inp == "exit" or inp == "done" or inp == "quit":
                return
            try:
                exec(inp)
            except Exception as e:
                print("(Silent Error... stored in <err>)")
                err = e
                
    def help_console(self):
        
        print("<console> is a pretty simple command...")
        print("You just type in <console> and the password")
        print("If the password is accepted, you enter a debugging console!")

    def do_save(self, s):
        
        name = self.player.name
        with open(name+".dt", "r") as f2:
            h = f2.readline()
        with open(name+".dt", "w") as f1:
            f1.write(h)
            # mess the saving process a little bit! 
            f1.write(str(list(bytearray(str(
                self.player.get_data()
                ).encode("utf8")))))
            f1.write("\n")
            f1.write(str(list(bytearray(str(
                self.player.inventory
                ).encode("utf8")))))
        print("Data saved")
                
    def help_save(self):
        
        print("<save> takes no arguments.")
        print("Saves the gamestate to the correct .dt file")
                
    def do_admire(self, s):
        
        lol = [
            "You are truly, incredibly gorgeous!!",
            "Those jeans do fit you well...",
            "You look wonderful today!",
            "You carry a Godly look today!",
            "Kiss me!!!",
            "That toilette was brilliantly achieved!",
            "That total exp fits you like in no-one else!"
            ]
        global choice
        print(choice(lol))
        self.player.pprint()
        
    def help_admire(self):
        
        print("<admire> is a command that takes no arguments")
        print("Simply does a neat print of your skills, level, money, etc...")

                
while True:
    print("Do you want to load saved data or create a new player?")
    print("-load <name> <password>")
    print("-new <name>")
    inp = input(">> ").strip()
    if not(inp.startswith("-new") or inp.startswith("-load")):
        print("Unknown command <" + inp.split()[0] + ">")
        continue
    else:
        args = inp.split()
        if args[0] == "-new":
            # initialize the new player's data
            if len(args) != 2:
                print("The name cannot contain spaces.")
                continue
            name = args[1]
            level = 1
            l = assign_tokens([1]*len(SKILLS), 2*len(SKILLS), True)
            p = Player(name, level, *l)
            while True:
                print("Now please set a password for this save state")
                pass1 = input(">> ")
                if len(pass1) == 0:
                    print("Type a password!")
                    continue
                elif " " in pass1:
                    print("The password must not have spaces")
                    continue
                print("Please retype the password for confirmation")
                pass2 = input(">> ")
                if pass1 != pass2:
                    print("Passwords do not match!")
                    continue
                break
            # save the data and the password
            crypt = hashlib.md5(pass1.encode("utf8")).hexdigest()
            with open(name+".dt", "w") as f:
                f.write(crypt)
                f.write("\n")
                # Mess the saving a bit to make it harder for people to change
                #stuff...! ! ! FUNNY ME :D
                s = str(list(bytearray(str(p.get_data()).encode("utf8"))))
                f.write(s)
                f.write("\n")
                s = str(list(bytearray(str(p.inventory).encode("utf8"))))
                f.write(s)
            # start the game
        elif args[0] == "-load":
            # load player's data
            with open(args[1]+".dt", "r") as f:
                h = f.readline()[:-1]
                try:
                    args[1] == args[1]
                except IndexError:
                    print("Missing the name of the progress to load")
                    continue
                try:
                    args[2] == args[2]
                except IndexError:
                    print("Password argument missing")
                    continue
                h2 = hashlib.md5(args[2].encode("utf8")).hexdigest()
                if h != h2:
                    print("Wrong password!")
                    continue
                l = eval(f.readline())
                #--
                # reverse the mess made by the saving methods for the skills
                s = ""
                for char in l:
                    s += chr(char)
                p_data = eval(s)
                #--
                # same for the inventory
                #--
                d = eval(f.readline())
                s = ""
                for char in d:
                    s += chr(char)
                p_inv = eval(s)
                p = Player(*p_data, inventory=p_inv)
            # continue the game
            HomeTown(p).cmdloop()
        else:
            print("Unknown command <" + args[0] + ">")
            continue
