'''import time

beg = time.time()
end = beg + 2
l = ["|Loading   ", "/Loading.  ", "-Loading.. ", "\\Loading..."]
while time.time() < end:
    for i in l:
        time.sleep(0.1)
        print(i, end="\r")
        '''


import cmd

class Player(object):

    def __init__(self,name="Rodrigo",attack=5,life=30,alive=True):
        self.name = name
        self.attack = attack
        self.life = life
        self.alive = alive

    def do_damage(self,other):
        other.life -= self.attack
        return other.life <= 0

    def get_damage(self,other):
        self.life -= other.attack
        return self.life <= 0


class Enemy(object):

    def __init__(self,name="Enemy",attack=3,life=8,alive=True):
        self.name = name
        self.attack = attack
        self.life = life
        self.alive = alive

    def do_damage(self,other):
        other.life -= self.attack
        if other.life <= 0:
            other.alive = False

    def get_damage(self,other):
        self.life -= other.attack
        if self.life <= 0:
            self.alive = False


class Arena(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self) # Find out what this does
        # Found! Remember that, in class inheritance, you have
        #to call the parents' __init__ function
        self.p = Player()
        self.e = Enemy()
        self.intro = "Welcome"
        self.prompt = "(Arena):("+self.p.name+")"


    def do_attack(self,s):
        if self.p.do_damage(self.e):
            print("You win")
        if self.p.get_damage(self.e):
            print("You lose")

    def do_rest(self,s):
        if self.p.get_damage(self.e):
            print("You lose")

    def do_test(self,s):
        print(s)

    def default(self, line):
        print("I don't understand " + line)
Arena().cmdloop()
