import cmd

class Player(object):
    
    def __init__(self,name,sex,hp=0,strength=0,defense=0,agility=0,intelect=0
                 ,luck=0,swag=0,money=0,inventory=[]):
        
        def check_stat(stat):
            '''check if the passed argument is an integer'''
            return not(type(stat) == int)
        
        # Loads of control flow to ensure that the arguments passed as stats
        #are only the ones we want. Prevent integers/floats/etc. in the name,
        #floats and other creepy stuff in the integer stats
        
        # RuntimeErrors to print when a wrong type of argument was passed
        if type(name) != str:
            raise RuntimeError("Fuck... The name should be a string..." \
            "(__init__ of Player) Passed a " + str(type(name)))
        self.name = name
        
        
        if not (sex in ["male", "female"]):
            raise RuntimeError("The sex should only be male/female (__init__ " \
            "Player)")
        self.sex = sex
        
        
        if check_stat(hp):
            raise RuntimeError("The HP stat can only be an integer (__init__ " \
            "Player) Passed a " + str(type(hp)))
        self.hp = hp
        
        
        if check_stat(strength):
            raise RuntimeError("The strength stat can only be an integer " \
            "(__init__ of Player) Passed a " + str(type(strength)))
        self.strength = strength
        
        
        if check_stat(defense):
            raise RuntimeError("The defense stat can only be an integer " \
            "(__init__ of Player) Passed a " + str(type(defense)))
        self.defense = defense
        
        
        if check_stat(agility):
            raise RuntimeError("The agility stat can only be an integer " \
            "(__init__ of Player) Passed a " + str(type(agility)))
        self.agility = agility
        
        
        if check_stat(intelect):
            raise RuntimeError("The intelect stat can only be an integer " \
            "(__init__ of Player) Passed a " + str(type(intelect)))
        self.intelect = intelect
        
        
        if check_stat(luck):
            raise RuntimeError("The luck stat can only be an integer " \
            "(__init__ of Player) Passed a " + str(type(luck)))
        self.luck = luck
        
        
        if not(type(money) in [int, float]):
            raise RuntimeError("The money has to be, either a float or an " \
            "integer (__init__ of Player) Passed a " + str(type(money)))
        self.money = money
        
        
        if check_stat(swag):
            raise RuntimeError("Your swag points should only be integers " \
            "(__init__ of Player); Passed a " + str(type(swag)))
        self.swag = swag
        
            
        if type(inventory) != list:
            raise RuntimeError("Your inventory should be a list of items! " \
            "(__init__ of Player)")
            
            
        def get_data(self):
            return tuple(self.name, self.sex, self.hp, self.strength, 
            self.defense, self.agility, self.intelect, self.luck, self.swag,
            self.money, self.inventory)
            
            
class StatAssigner(cmd.Cmd):
    
    def __init__(self, name, first=False, tokens=5, player=None):
        
        cmd.Cmd.__init__(self)
        
        if first:
            print()
            print("#"*40)
            print("Welcome to the stat assigner " + name + ".")
            print("Please remember that whenever you may need help, you can type ? or help")
            print("In here you will set your initial stats for the game!")
            print("#"*40)
            input()
            print("These are the existing stats:")
            print("\tHP: Your hitpoints times 10 give you your maximum health")
            print("\tStrength: Strength influences the amount of damage you "\
            "deal")
            print("\tDefense: Reduces the amount of damage you take per hit")
            print("\tAgility: It is agility that defines your dodging chance")
            print("\tIntelect: Affects the spells you can use and their effects")
            print("\tLuck: Dictates wether you will deal a critical hit or not")
            print("#"*40)
            input()
            print("Please be aware that every stat can also influence some random "\
            "events.\nFor example, your agility could dictate if you would dodge "\
            "a falling rock in an unknown ravine")
            print()
            print("You also have swag points. These are earnt ingame and help you get "\
            "discounts when buying new stuff and weapons, amongst other very swaggy things")
            print("#"*40)

            state = [1,1,1,1,1,1]

        if not(first) and player == None:
            
            raise RuntimeError("If this isn't the part were you create a "\
                               "player in the beginning of the game, we should"\
                               " have got some player as argument")

        self.first = first
        self.player = player
        self.p_name = name
        self.available_tokens = tokens
        self.prompt = "(Stat Assigner) >> "
        self.skills = ["hp","strength","defense","agility","intelect","luck"]
        self.init_stats = {self.skills[i]: state[i] for i in range(len(state))}
        self.values = {self.skills[i]: state[i] for i in range(len(state))}
        
        
    def do_help(self, s):
        """Help function that displays help about the commands"""
        
        if s == "":
            print("To assign a stat, you can either use the <increase>, <set>, "\
            "<reset> and <max> commands, followed by the skill you wish.")
            print("Example: set strength 7 sets your strength to level 7.")
            print("You can also randomly assign all your stats with <random>")
        cmd.Cmd.do_help(self, s)


    def parse(self, s):
        """A little helper that gets rid of annoying characters, replacing them
with spaces"""

        chars = [",",";","/",".",":"]
        for char in chars:
            while char in s:
                s = s[:s.index(char)] + " " + s[s.index(char)+1:]
        return s


    def do_set(self, s):
        """Command used to set one or more skills to a certain level (passed as
 argument)"""
        
        # parse all the weird characters in the argument string
        s = self.parse(s)
        # list all the skills we want to change
        args = s.lower().split()
        # try to get the new level
        try:
            n = int(args[0])
        # if we can't, the user wrote the command in the wrong way
        # tell him to get some help
        # maybe some rehab
        # LOL
        except ValueError:
            # try to catch the case where <set> <skill> <amount> is used
            if len(args) == 2:
                # Do some sneaky stuff so the rest of the function works
                #properly: put the arguments in the default order
                try:
                    n = int(args[1])
                    args[0], args[1] = args[1], args[0]
                except ValueError:
                    print("*** Syntax Error: <set> <amount> <skill1> "\
                          "<skill2> ...")
                    print("Please type <help> <set> for help with the set "\
                          "command")
                    return
            else:
                print("*** Syntax Error: <set> <amount> <skill1> <skill2> ...")
                print("Please type <help> <set> for help with the set command")
                return
        # pop the new level from the string
        args.pop(0)
        # if no args are remaining the user missed the skills in the command
        if len(args) == 0:
            print("*** Syntax Error: missing <skill> argument")
            print("Please type <help> <set> for help with the set command")
        # parse the other skills
        # if the only argument missing is "all", swap it with all the skills
        elif len(args) == 1 and args[0] == "all":
            args.pop()
            args = self.skills
        # loop through the arguments
        for skill in args:
            # if we don't recognize the skill, warn the user
            if skill not in self.skills:
                print("*** Unknown skill " + skill)
            else:
                # don't let the user reduce a skill further than it was
                if n < self.init_stats[skill]:
                    print("You can't set " + skill + " to a lower level "\
                          "than the one it had when we started (" +
                          str(self.init_stats[skill]) + ")...")
                    continue
                # else, find the difference (new - old)
                d = n - self.values[skill]
                # if we are reducing a skill, (new-old) gives a negative int
                #so the following "if" statement ALWAYS lets us reduce it
                # if (new-old) is >0, evaluate if we have enough tokens
                #to set that skill to that level
                if self.available_tokens >= d:
                    self.values[skill] = n
                    # remember that if we were reducing a skill, d is <0
                    #so this subtraction actually increases available_tkns
                    self.available_tokens -= d
                    print(skill.capitalize() + " set to level " + str(n))
                # If we don't have enough tokens, warn the user and exit
                else:
                    print("You do not have enough skill tokens ("
                          + str(self.available_tokens) + ") to set "\
                          + skill + " to level " + str(n))
                    return
        # Remind the user how many tokens he has left
        print("You have " + str(self.available_tokens) +" available tokens.")


    def do_increase(self, s):
        """Command used to increase one or more skills by the amount passed"""
        
        # parse all the commas in the argument string
        s = self.parse(s)
        # list all the skills we want to change
        args = s.lower().split()
        # try to get the new level
        try:
            n = int(args[0])
        # if we can't, the user wrote the command in the wrong way
        # tell him to get some help
        # maybe some rehab
        except ValueError:
            print("*** Syntax Error: <increase> <amount> <skill1> <skill2> ...")
            print("Please type <help> <increase> for help with the increase "\
                  "command")
            return
        # pop the new level from the string
        args.pop(0)
        # if no args are remaining the user missed the skills in the args
        if len(args) == 0:
            print("*** Syntax Error: missing <skill> argument")
            print("Please type <help> <increase> for help with the set command")
        # if the only remaining argument is "all", swap it with all the other
        #stats!
        elif len(args) == 1 and args[0] == "all":
            args.pop()
            args = self.skills
        # 't' is the total tokens we will need
        t = len(args) * n
        # If we don't have enough tokens, change NO skills, warn user, exit
        if self.available_tokens < n:
            print("You don't have enough tokens (" + str(self.available_tokens)+
                  ") to increase by " + str(n) + " " +str(len(args)) +" skills")
        else:
            # Deduce the tokens needed ;)
            self.available_tokens -= t
            # if we do have the needed tokens, change the skills
            for skill in args:
                # if we don't recognize the skill, warn the user
                if skill not in self.skills:
                    print("*** Unknown skill " + skill)
                    # If the skill wasn't recognize, give him back those tokens!
                    self.available_tokens += n
                else:
                    self.values[skill] += n
                    print(skill.capitalize() + " increased by " + str(n) +
                          " to level " + str(self.values[skill]))
            print("You have " + str(self.available_tokens) +" tokens available")


    def do_reset(self, s):
        """Command used to reset one or more skills to the initial value"""

        # parse all the weird characters in s
        s = parse(s)
        args = s.lower().split()
        if ((len(args) == 1) and (args[0] == "all")) or (len(args) == 0):
            args.pop()
            args = self.skills
        for skill in args:
            d = self.values[skill] - self.init_stats[skill]
            self.available_tokens -= d
            self.values[skill] = self.init_stats[skill]
            print(skill.capitalize() + " reset to level " +
                  str(self.values[skill]))


    def do_max(self, s):
        """Command used to max ou a certain skill, spending all available
tokens"""

        # parse all the weird characters in s
        s = parse(s)
        args = s.lower().split()
        # <max> only takes 1 argument! deal with that
        if len(args) != 1:
            print("*** Syntax Error: <max> takes exactly one argument <skill>")
            print("Type <help> <max> for help with the <max> command")
        # if the argument provided is not recognized
        elif args[0] not in self.skills:
            print("*** Syntax Error: Unknown <skill> argument " + args[0])
        # Valid argument! Max that skill >> Spend all the tokens in it
        else:
            self.values[args[0]] += self.available_tokens
            self.available_tokens = 0
            print("Maxed skill " + args[0] + " to level " + str(self.values[
                args[0]]))
        

    def do_check(self, s):
        """Command to print neatly all the skills and their levels"""
        
        # ignore all the arguments passed to the command
        if s != "":
            print(s + " ignored... <check> takes no arguments")

        # find the maximum word length amongst all the skills
        # has to do with formatting the table
        m = 0
        for skill in self.skills:
            m = len(skill) if len(skill) > m else m
        # increase it by two because of the ' ' before and after the word
        m += 2
        print(" Skill | Set (initial)")
        # the m size, plus 3 "|", plus 10 spaces for the <level set> (init)
        print("-"*(m+14))
        # parse every skill
        for skill in self.skills:
            # create the string with the skill
            s_skill = " " + skill
            # while it doesn't have 'm' size, add spaces!
            while len(s_skill) < m:
                s_skill += " "
            # string with the initial value surrounded by ()
            s_init = "(" + str(self.init_stats[skill]) + ") "
            # string with the current value plus an ending space
            s_stat_now = str(self.values[skill]) + " "
            # add it all up
            s_init_now = s_stat_now + s_init
            # while it doesn't have size 10, add spaces in front of it!
            #why 11? 3 for each skill (6) + the two spaces (before and after)
            # + the space between skill and (init) + the ()
            while len(s_init_now) < 11:
                s_init_now = " " + s_init_now
            # print() it all nice and good looking
            print("|" + s_skill + "|" + s_init_now + "|")
        print("-"*(m+14))


    def do_tokens(self, s):
        """Tell the user how many tokens he has got left"""

        print("You have " + str(self.available_tokens) + " available tokens.")


    def default(self, s):
        """Implement a slight exchange"""

        if s in self.skills:
            print("Your " + s.capitalize() + " skill entered the assigner with"\
                  " a level " + str(self.init_stats[s]) + ",\nAnd is now set "\
                  "to level " + str(self.values[s]))
        elif s[0] == "<" and s[-1] == ">":
            print("The commands shouldn't be surrounded by <>")
            print("That is just our way of distinguishing the print of a "\
                  "command from the print of a single \"normal\" word.")
        else:
            cmd.Cmd().default(s)


    def do_exit(self, s):
        """Command to exit the stat assigner"""

        # Don't let the user leave if he hasn't used all the tokens
        if self.available_tokens != 0:
            print("You still have unused available tokens.")
            print("You cannot leave the Stat Assigner while there are tokens "\
                  "to be used.")
            return
        print("Are you sure you want to exit??")
        ans = input("Y/N >> ").strip().lower()
        if ans.startswith("y"):
            for skill in self.skills:
                exec("self.player."+skill+" = "+str(self.values[skill]))
            return True
        else:
            return

    # define all the helps
    # layout:
    ## print with usage
    ### blank print
    ## further explanation

    def help_exit(self):
        """Help function on command <exit>"""

        print("Command usage: <exit>")
        print()
        print("Use the <exit> command when you are finished from the stat "\
              "assignment.\n\tYou won't be able to leave before spending all "\
              "the available tokens.")
        

    def help_tokens(self):
        """Help function on command <tokens>"""

        print("Command usage: <tokens>")
        print()
        print("Tells you how many tokens you have left")
        

    def help_set(self):
        """Help function on command <set>"""

        s = ""
        for skill in self.skills:
            s += skill + "; "
        s = s[:-2]
        s += "."
        print("Command usage: <set> <value> <skill 1> (<skill 2> <skill ..>)")
        print(" * If you want to pass only one skill, you can swap <skill> "\
              "with <value> in the arguments.")
        print(" * <all> is an alias for all the stats.")
        print()
        print("Use the <set> command to define the new levels for the specified"\
              " skills. These are " + s)


    def help_increase(self):
        """Help function on command <increase>"""

        s = ""
        for skill in self.skills:
            s += skill + "; "
        s = s[:-2]
        s += "."
        print("Command usage: <increase> <value> <skill 1> (<skill 2> <skill "\
              "..>)")
        print(" * <all> is an alias for all the skills.")
        print()
        print("Use the <increase> command to increase by a specified value, "\
              "all the specified skills. These are " + s)


    def help_reset(self):
        """Help function on command <reset>"""

        print("Command usage: <reset> (<skill 1> <skill ..>)")
        print(" * <all> is an alias for all the skills")
        print(" * Using no arguments defaults the command to all the skills")
        print()
        print("Use the <reset> command to define the specified skills to the "\
              "values they had before starting the assignment.")


    def help_max(self):
        """Help function on command <max>"""

        print("Command usage: <max> <skill>")
        print()
        print("Use the <max> command to spend all the available tokens on the "\
              "specified skill.")


    def help_check(self):
        """Help function on command <check>"""

        print("Command usage: <check>")
        print()
        print("Check the current state of all skills.")
        print("To check just one skill, type in only the name of the skill.")
        print("Like <" + self.skills[0] + ">")
