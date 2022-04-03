import random as r
from time import sleep
import time as t

loading = ['Loading -', 'Loading \\', 'Loading |', 'Loading /']
for i in range(15):
    for load in loading:
        sleep(0.25)
        print(f'\r{load}', end='')
print()
print("Welcome to...")
sleep(1)
print("Happy Hour!")
sleep(1)
name = input("Please enter your name: ")
health = 100
money = 0
start_time = t.time()

def loadingbar():
    print("Loading...")
    for i in range(51):
        sleep(r.uniform(0.05, 0.2))
        bar = ('□' * i) + '-' * (50 - i)
        print(f'\r[{bar}]', end='')
    print()
    print('-=!LOADED!=-')

def timer(time):
    current_time = t.time()
    result = current_time - time
    seconds = int(result)
    minutes = seconds / 60
    minutes_string = str(minutes)
    minutes_list = minutes_string.split('.')
    seconds_decimal = round(float("0." + minutes_list[1]) * 60)
    minutes_time = int(minutes)

    return "%02d minutes and %02d seconds" % (minutes_time, seconds_decimal)


def checkpoint(point):
    if point.lower() == 'mysteriousworld':
        sleep(1)
        loadingbar()
        sleep(2)
        act_two()
    elif point.lower() == 'fieldofwonders':
        sleep(1)
        loadingbar()
        sleep(2)
        act_three()
    elif point.lower() == 'thetruthoftheworld':
        sleep(1)
        loadingbar()
        sleep(2)
        act_four()

    elif point.lower() == 'thebigbadbar':
        sleep(1)
        loadingbar()
        sleep(2)
        act_five()
    else:
        sleep(1)
        print(f"{name} forgets his place...")
        sleep(2)
        menu()

def waiting():
    useless = input('')

def death(cause):
    global health
    global money
    if cause == '1':
        health = 100
        money = 0
        print("""
            You pretty much died of laziness in bed...                                 
        """)
        waiting()
        menu()
    elif cause == '2':
        health = 100
        money = 0
        print("""
            Died of cowardice.. Maybe cross the river next time.
        """)
        waiting()
        menu()
    elif cause == '3':
        health = 100
        money = 0
        print("""
        Wow, you died to a mushroom...
        """)
        waiting()
        menu()
    elif cause == '4':
        health = 100
        money = 0
        print("""
        Died from an explosion huh... Not too shabby!
        """)
        waiting()
        menu()
    elif cause == '5':
        health = 100
        money = 0
        print("""
        A real shame that was...
        """)
        waiting()
        menu()
    elif cause == '6':
        health = 100
        money = 0
        print("""
        There was still much for you to enjoy in life...
        """)
        menu()

def update_health_money(h, m):
    global health
    global money
    health += h
    money += m



def menu():
    menu_choice = input("What would you like to do?\n[a]Play!\n[b]Check point\n[c]Credits\n[d]Quit\n>")
    choice = menu_choice.lower()
    if choice == 'a':
        sleep(1)
        loadingbar()
        act_one()
    elif choice == 'b':
        sleep(1)
        checkpoint(input("What is your point passphrase?\n>"))
    elif choice == 'c':
        credits()
    elif choice == 'd':
        sleep(1)
        response = False
        while not response:
            confirm = input("Are you sure you want to quit? y/n\n>")
            if confirm.lower() == 'y':
                quit()
            elif confirm.lower() == 'n':
                response = True
                return menu()
            else:
                print("Invalid reply...")

def credits(): # Make a cool credit sequence
    sleep(1)
    print("__Credits__")
    sleep(0.5)
    print("Lead Developer: Alan")
    sleep(0.5)
    print("Lead Director: Alan")
    sleep(0.5)
    print("Original Idea: Alan")
    sleep(0.5)
    print("Sponsors: Alan")
    return menu()


class Backpack:
    inventory = ['note']

    def __init__(self, user):
        self.name = user
    def __repr__(self):
        return f"The current user is {self.name}"
    def add_item(self, item):
        self.inventory.append(item)
    def boss_override(self):
        if 'mushroom' in self.inventory:
            new_inventory = list(filter(lambda item: item == 'mushroom', self.inventory))
            self.inventory = new_inventory
        else:
            self.inventory = []
    def trash_item(self, item):
        response = False
        while not response:
            choice = input(f"{self.name}, are you sure you wish to throw away your {item}? y/n\n>" )
            if choice.lower() == 'y':
                response = True
                sleep(1)
                try:
                    print("TESTING 1")
                    index = self.inventory.index(item)
                    print("INDEX:")
                    print(index)
                    self.inventory.pop(index) # could also use .remove(item)
                    print("TESTING 3")
                    print(f"{self.name} has thrown away his {item}")
                except ValueError:
                    print(f"{self.name} does not have this item...")
            elif choice.lower() == 'n':
                response = True
                sleep(1)
                print("Good choice...")
            else:
                print("Invalid response!")

    def view_backpack(self):
        print((", ".join(self.inventory)))

    def use_item(self, item):
        global health
        global money

        if item.lower() == 'health potion' and item in self.inventory:
            sleep(1)
            print(f"{self.name} feels power surge through his veins...")
            update_health_money(25, 0)
            self.inventory.remove(item)
        elif item.lower() == 'banknote' and item in self.inventory:
            sleep(1)
            print(f"{self.name} jumps out of pure joy!\n'TEN DOLLARS!!!' he exclaims...")
            update_health_money(0, 10)
            self.inventory.remove(item)
        elif item.lower() == 'mushroom' and item in self.inventory:
            sleep(1)
            print(f"{name} decides that he wants to eat the strange mushroom.")
            update_health_money(-25, 0)
            sleep(1)
            print("*VOMITS*")
            sleep(1)
            self.inventory.remove(item)
            print(f"{name} wakes up after being unconscious...\nWhat happened..?")
            if health <= 0:
                death('3')
        elif item.lower() == 'note' and item in self.inventory:
            sleep(1)
            print(f"I'm trapped in an endless cycle... \n       From: ~~~~~~")
            sleep(1)
            print("The note suddenly disappears...")
            self.inventory.remove(item)
        else:
            sleep(1)
            print(f"{self.name} searches his backpack, only to realize that he is a fool.")

backpack = Backpack(name)

def show_stats():
    print(f"Health: {health}")
    print(f"Money: {money}")
    print("Time Played: {}".format(timer(start_time)))
    print(backpack.inventory)

def use_backpack():
    choice = input("What would you like to do?\n[a]Throw an item away\n[b]Use an item\n[c]View inventory\n[d]Exit\n>")
    c = choice.lower()
    if c == 'a':
        sleep(2)
        show_stats()
        sleep(2)
        trash = input("Which item would you like to throw away?\n>")
        t = trash.lower()
        sleep(2)
        show_stats()
        backpack.trash_item(t)
        show_stats()
    elif c == 'b':
        sleep(2)
        show_stats()
        sleep(2)
        use = input("Which item would you like to use?\n>")
        u = use.lower()
        sleep(2)
        show_stats()
        backpack.use_item(u)
        show_stats()
    elif c == 'c':
        sleep(2)
        print(f"{name} opens his backpack to see what things he has collected so far...")
        show_stats()
    elif c == 'd':
        sleep(2.5)
        print(f"{name} stops rummaging through his backpack and gets on his feet.")
    else:
        print(f"Confused, {name} closes up his bag and continues his journey.")

def games(game):
    if game == 'rps':
        tries = 3
        wins = 0
        while tries > 0:
            tries -= 1
            bot = r.randint(1, 3)
            bot_c = ''
            if bot == 1:
                bot_c = 'rock'
            elif bot == 2:
                bot_c = 'paper'
            else:
                bot_c = 'scissors'

            choice = input("Choose:\n[1]Rock\n[2]Paper\n[3]Scissors\n>")
            if choice.isdigit():
                user = int(choice)
            else:
                user = 10

            user_c = ''
            if user == 1:
                user_c = 'ROCK!'
            elif user == 2:
                user_c = 'PAPER!'
            elif user == 3:
                user_c = 'SCISSORS!'
            else:
                user_c = 'NOTHING!'

            print("ROCK, PAPER, SCISSORS, SHOOT!")
            if user == bot:
                waiting()
                print(f"{name} chose ROCK!")
                waiting()
                print(f"Opponent: {bot_c}")
                sleep(0.5)
                print("IT'S A TIE!")
            elif user == 1 and bot == 3:
                waiting()
                print(f"{name} chose ROCK!")
                waiting()
                print(f"Opponent: {bot_c}")
                sleep(0.5)
                print(f"{name} WINS!")
                backpack.add_item('banknote')
                print("Banknote added to inventory.")
                wins += 1
            elif user == 2 and bot == 1:
                waiting()
                print(f"{name} chose PAPER!")
                waiting()
                print(f"Opponent: {bot_c}")
                sleep(0.5)
                print(f"{name} WINS!")
                backpack.add_item('banknote')
                print("Banknote added to inventory.")
                wins += 1
            elif user == 3 and bot == 2:
                waiting()
                print(f"{name} chose SCISSORS!")
                waiting()
                print(f"Opponent: {bot_c}")
                sleep(0.5)
                print(f"{name} WINS!")
                backpack.add_item('banknote')
                print("Banknote added to inventory.")
                wins += 1
            else:
                waiting()
                print(f"{name} chose {user_c}")
                waiting()
                print(f"Opponent: {bot_c}")
                sleep(0.5)
                print("OPPONENT WINS!")
        sleep(1)
        print("GAME ENDED!")
        waiting()
        if wins >= 2:
            print(f"{name} earned a bonus banknote!")
            backpack.add_item('banknote')
        else:
            print(f"{name} is saddened by his loss, but is content with the results.")

    elif game == 'minefield':
        print("MINEFIELD! You have twenty-four rocks to throw into the field... If a rock happens to hit a mine, GAME OVER!")
        board = [['□'] * 5 for i in range(5)]
        rocks = 25
        while rocks > 0:
            for row in board:
                print("  ".join(row))
            user_row = input("Enter the row: ")
            user_col = input("Enter the column: ")
            if user_row.isdigit() and user_col.isdigit():
                if int(user_row) > 0 and int(user_col) > 0:
                    if int(user_row) < 6 and int(user_col) < 6:
                        user1_row = int(user_row) - 1
                        user1_col = int(user_col) - 1
                        rand_row = r.randint(0, 4)
                        rand_col = r.randint(0, 4)
                        while board[rand_row][rand_col] == 'X':
                            rand_row = r.randint(0, 4)
                            rand_col = r.randint(0, 4)
                        if board[user1_row][user1_col] == 'X':
                            print("You already chose that plot!!!")
                        else:
                            rocks -= 1
                            if user1_row == rand_row and user1_col == rand_col:
                                board[user1_row][user1_col] = 'X'
                                sleep(1)
                                print("💣💣💣💣💣")
                                sleep(0.25)
                                print("BOOOM!")
                                update_health_money(-25, 0)
                                waiting()
                            else:
                                board[user1_row][user1_col] = 'X'
                    else:
                        print("That's too high!")
                else:
                    print("That's too low!")
            else:
                print("Invalid response.")
        sleep(1)
        if health <= 0:
            death('4')
        else:
            print("That seems like enough rocks to safely assume the mines are duds.")

    elif game == 'letter':
        with open("letter1529.txt", "w") as f:
            f.write("""
            - .... .. ... .-- --- .-. .-.. -.. .. ... -. --- - .-. . .- .-..
            |To whom finds this letter,                                     |
              |  I wish you the best of luck on your adventures.             |
            |    I wish the greatest of success if you continue your goal.   |
             |   Though I must warn you about the truth of the world.         |
            |    It may be not as you wish it to be.                          |
              |  The world is simply not as you perceive it to be.           |
             |   The simple state of being is a construct of the human mind.|
             |   The basic state of the world may such a construct.          |
            |    Unfortunately, it is simply not possible to tell such a fact.|
              |                                                              |
               | As for me, I also once had grandiose goals of greatness.   |
              |  With the greatest resolve possible, I sought the truth.    |
             |   Instead of meaning, I found nothingness.                    |
            |    On the completions of my goals, I found that life is dull. |
             |   My actions in this world have no value.                    |
             |   I am an expendable piece of a bigger program.              |
            |    A simple being of semi-sentience that should not exist.     |
             |   The place where this letter lie, is where I shall remain.  |
              |                                                             |
             |   A simple piece of advice for you, remember to find that    |
            |    flickering light at the end of the tunnel.                |
            |                                                              |
            |  From, mysterious traveler.                                  |
            - .... .. ... .-- --- .-. .-.. -.. .. ... -. --- - .-. . .- .-..
            """)
        # with open("letter1529.txt", "r") as f:
        #     print(f.read())
        with open("letter1529.txt", "r") as f:
            print("*Look at your files for letter1529.txt*")
        solved = False
        waiting()
        print("A transparent wavering wall suddenly blocks off the exit to the cave.")
        waiting()
        print("I'M TRAPPED!")
        waiting()
        print(f"Anxious, {name} refers back to the letter he found.")
        tries = 5
        while not solved:
            sleep(1)
            if tries <= 0:
                hint = input("Would you like a hint? y/n\n>")
                if hint.lower() == 'y':
                    sleep(1)
                    print("It seems you are in trouble, perhaps an SOS signal would suffice.")
                else:
                    sleep(1)
                    print("Very well...")
            answer = input("What is the answer?\n>")
            if answer.upper() == 'THISWORLDISNOTREAL':
                sleep(2)
                solved = True
                print("The wall disappears, and light fills the cave.")
                break
            else:
                tries -= 1
            sleep(0.25)
            print("That is incorrect...")

    elif game == 'dice':
        sleep(2)
        print("Gambler: *flips a coin*")
        sleep(0.5)
        print("Gambler: Well..? Heads or tails?")
        sleep(1.5)
        coin = r.randint(1, 2)
        response = False
        while not response:
            sleep(1)
            guess = input("[1]Heads or [2]Tails\n>")
            if guess.isdigit():
                number = int(guess)
                if 2 >= number >= 1:
                    response = True
                    if number == coin:
                        sleep(1)
                        print("Gambler: Damn... you beat me!")
                        sleep(1)
                        return True
                    else:
                        sleep(1)
                        print("Gambler: HAHAHA, thanks for the money kid!")
                        sleep(1)
                        return False
                else:
                    sleep(1)
                    print("Gambler: That is a stupid guess...")
            else:
                sleep(0.25)
                print("Gambler: I didn't catch that...")

    elif game == 'boss':
        sleep(1)
        boss_hp = 100
        print("Boss: I'm sorry, but I can't let you leave...")
        waiting()
        print("Leave..? Leave what?")
        waiting()
        print("Boss: Goodbye...")
        sleep(0.5)
        print("*swings sword*")
        update_health_money(-5, 0)
        sleep(0.25)
        print(f"'GAAHH!' {name} cries in pain!")
        waiting()
        while boss_hp >= 0:
            if health >= 0:
                sleep(1)
                action = input("What will you do?\n[a]Sword slash\n[b]Fire arrow\n[c]Dodge\n[d]Flee\n>")
                if action.lower() == 'a':
                    sleep(0.5)
                    damage = r.randint(1, 15)
                    boss_hp -= damage
                    print(f"{name} sprints towards the boss and slashes it with his sword doing {damage} damage.")
                    sleep(0.5)
                    print("Boss: GRRR!")
                    sleep(0.5)
                    print("Boss: *swords sword*")
                    boss_dmg = r.randint(5,10)
                    sleep(0.25)
                    update_health_money(-boss_dmg, 0)
                    print(f"{name} took {boss_dmg} damage...")
                elif action.lower() == 'b':
                    sleep(0.5)
                    dmg = r.randint(1, 10)
                    boss_hp -= dmg
                    print(f"{name} fires an arrow for {dmg} damage!")
                    sleep(1)
                    damage_boss = [0, 10]
                    damage_index = r.randint(0, 1)
                    damage_arrow = damage_boss[damage_index]
                    update_health_money(-damage_arrow, 0)
                    if damage_arrow == 0:
                        print("*boss stumbles back*")
                    elif damage_arrow == 10:
                        print("Boss: FOOL!")
                        sleep(0.5)
                        print("*boss swings sword*")
                        sleep(0.5)
                        print(f"{name} took {damage_arrow} damage!")
                elif action.lower() == 'c':
                    sleep(0.5)
                    dodged = r.randint(1, 2)
                    if dodged == 2:
                        sleep(0.5)
                        print(f"{name} dodges the boss's attack!")
                        sleep(0.5)
                        health_gain = r.randint(1,5)
                        update_health_money(health_gain, 0)
                        print(f"{name} regains {health_gain} health...")
                        sleep(0.5)
                    else:
                        sleep(0.5)
                        print("Boss: Ha Ha Ha! That won't work!")
                        sleep(0.5)
                        boss_attack = r.randint(1, 15)
                        update_health_money(-boss_attack, 0)
                elif action.lower() == 'd':
                    sleep(1)
                    print("Boss: Scurry back into line...")
                    sleep(0.5)
                    act_four()
                elif action.lower() == 'inventory':
                    if 'health potion' in backpack.inventory:
                        sleep(1)
                        print("Boss: OH NO YOU DON'T!")
                        backpack.boss_override()
                        sleep(0.5)
                        print(f"'Why is my backpack so light?!?' {name} exclaimed!")
                        sleep(1)
                        use_backpack()
                    else:
                        use_backpack()
                else:
                    sleep(0.5)
                    print(f"*{name} is confused...*")
            else:
                sleep(1)
                print(f"{name} falls on the floor...")
                waiting()
                print(f"{name} feels his life force fleeting his body..")
                waiting()
                death('6')
        print("Boss: NOOOO!")
        waiting()
        print("Boss: YOU CAN'T LEAVE!")
        waiting()
        print(f"{name} sees clusters of light appear around him...")
        waiting()
        print(f"Suddenly... {name} is transported to a place he immediately recognizes...")
        waiting()
        print(f"MY HOME!")
        waiting()
        print("I'M FINALLY HOME!!!")
        waiting()
        print(f"{name} looks at his computer and sees the boss he was fighting.")
        waiting()
        print(f"{name}'s computer shuts off and restarts.")
        waiting()
        print(f"{name} loses consciousness...")
        for i in range(4):
            sleep(0.9)
            print(".")
        waiting()
        print("Aargh, what happened..?")
        waiting()
        print("Where am I..?")
        waiting()
        print("Something isn't right here.")
        credits()
    elif game == 'unknown':
        pass




def act_one():
    sleep(2)
    print("Aargh, what happened..?")
    waiting()
    print("Where am I..?")
    waiting()
    print("Something isn't right here.")
    waiting()
    print("----------INTERMISSION----------")
    sleep(1)
    print("Remember that you can access your inventory at any place where you need to make a decision by saying 'inventory'!")
    sleep(1)
    print("Be careful not to run through dialogue too fast! You just might end up answering a question with something you didn't desire!")
    print("--------------------------------")
    check1 = False
    while not check1:
        sleep(1)
        leavebed = input("How did I end up in my bed..?\nHmmm... Should I investigate? y/n\n>")
        if leavebed.lower() == 'y':
            check1 = True
            sleep(2)
            print("I guess I should explore what happened outside...")
            waiting()
            print(f"{name} walks outside to see a river raging about.")
            waiting()
            print("Hmmm.. I wonder... Maybe it was just a dream...")
            waiting()
            print("Is it really worth the trouble of having to risk my life to cross a river..?")
            sleep(0.5)
            check2 = False
            while not check2:
                choice = input("Should I cross the river..? y/n\n>")
                if choice.lower() == 'y':
                    check2 = True
                    sleep(2)
                    print(f"{name} steps outside to see a vast unrecognizable world.")
                    waiting()
                    print("What is this place!")
                    waiting()
                    print("This is not my home!")
                    waiting()
                    print("Boy: HEY YOU!!!")
                    waiting()
                    print("Me..?")
                    waiting()
                    print("Boy: YES YOU!!!")
                    waiting()
                    print("Boy: Want to play a game with me!?!?")

                    response2 = False
                    while not response2:
                        sleep(0.5)
                        choice2 = input("Should I play a game with him?\n[a]Yes\n[b]No! I don't have time to waste!\n[c]What game?\n>")
                        if choice2.lower() == 'a':
                            response2 = True
                            sleep(2)
                            print("Boy: GREAT! Lets play rock, paper, scissors!")
                            waiting()
                            games('rps')
                        elif choice2.lower() == 'b':
                            response2 = True
                            sleep(2)
                            print("Boy: What if I were to offer you.... money?")
                            playornot = False
                            while not playornot:
                                choice3 = input("Play the boy's game? y/n\n>")
                                if choice3.lower() == "y":
                                    playornot = True
                                    sleep(2)
                                    print("Boy: YAHOOO! LETS BEGIN!!!")
                                    waiting()
                                    games('rps')
                                elif choice3.lower() == 'n':
                                    playornot = True
                                    sleep(2)
                                    print("Boy: Fine... Old geezer...")
                                else:
                                    sleep(2)
                                    print("Boy: What did you say???")
                        elif choice2.lower() == 'c':
                            response2 = True
                            sleep(2)
                            print("Boy: Just a casual game of rock, paper, scissors!")
                            waiting()
                            print("Boy: Well what about it?? Wanna play?")
                            play = False
                            while not play:
                                sleep(3)
                                choice4 = input("Hmmmm. y/n \n>")
                                if choice4.lower() == 'y':
                                    play = True
                                    sleep(3)
                                    print("Boy: GOOD CHOICE!!!")
                                    waiting()
                                    games('rps')
                                elif choice4.lower() == 'n':
                                    play = True
                                    sleep(3)
                                    print("Boy: What a party pooper...")
                                elif choice4.lower() == 'inventory':
                                    use_backpack()
                                else:
                                    sleep(2)
                                    print("Boy: I didn't catch that...")
                        elif choice2.lower() == 'inventory':
                            use_backpack()
                        else:
                            sleep(2)
                            print("Boy: What's that??? Didn't catch that.")
                    sleep(2)
                    print(f"After that strange occurrence, {name} continued to search for an answer as to how he got here...")
                    waiting()
                    print("END OF ACT ONE!\nCheckpoint One Password: mysteriousworld")
                    waiting()
                    act_two()
                elif choice.lower() == 'n':
                    check2 = True
                    sleep(1)
                    print(f"{name} thinks about it for a moment...")
                    waiting()
                    print("Yeah, it isn't worth the trouble.")
                    waiting()
                    death('2')
                elif choice.lower() == 'inventory':
                    use_backpack()
                else:
                    sleep(1)
                    print("That choice is not valid!")
        elif leavebed.lower() == 'n':
            check1 = True
            sleep(2)
            print(f"Overpowered by a sudden burst of drowsiness, {name} retreats to his bed.")
            waiting()
            print(f"A dark cloud invades {name}'s mind... He loses consciousness")
            sleep(2)
            for i in range(5):
                sleep(1.5)
                print(".")
            waiting()
            death('1')
        elif leavebed.lower() == 'inventory':
            use_backpack()
        else:
            sleep(1)
            print("Invalid choice...")

def act_two():
    sleep(2)
    print(f"{name} continues walking aimlessly trying to find anything familiar.")
    waiting()
    print(f"{name} while walking suddenly trips on something.\n'OW!' he exclaims")
    waiting()
    print("What the heck is that thing..?")
    waiting()
    print(f"{name} had tripped over a brown burlap sack.")
    waiting()

    response = False
    while not response:
        choice = input("Should I look inside it..? y/n\n>")
        if choice.lower() == 'y':
            response = True
            sleep(1)
            print("OOOOOH! WHAT'S THIS WE HAVE HERE???")
            waiting()
            print(f"To {name}'s delight, he had just found a banknote and some strange mushroom.")
            waiting()
            print(f"{name} puts both the items in his backpack.")
            backpack.add_item('banknote')
            backpack.add_item('mushroom')
        elif choice.lower() == 'n':
            response = True
            sleep(1)
            print(f"{name}'s curiosity fades so he continues to wander aimlessly...")
        elif choice.lower == 'inventory':
            use_backpack()
        else:
            print("Invalid option...")
    waiting()
    print(f"After a long while, {name} approaches a forest with two entries...")
    waiting()
    print("The left entrance looks dark and mysterious, while the right looks peaceful yet creepy.")
    waiting()

    response2 = False
    while not response2:
        choice2 = input(f"What path should {name} take?\n[a]Right\n[b]Left\n>")
        if choice2.lower() == 'inventory':
            use_backpack()
        elif choice2.lower() == 'b':
            response2 = True
            sleep(1)
            print(f"Mysterious figures of light whizz past {name}'s eyes...")
            waiting()
            print("Though, the light creatures seemed quite docile.")
        elif choice2.lower() == 'a':
            response2 = True
            sleep(1)
            print(f"Owls hoot in the distance, while echoes of crawling animals send chills up {name}'s spine...")
        else:
            print("Invalid response.")

    waiting()
    print("After a while, the forest groves clear...")
    waiting()
    print(f"{name} sees a large plain...")
    waiting()
    print("Though, something seems off about the landscape.")
    waiting()
    print("There seems to be small circular patches of upturned dirt.")
    waiting()
    print(f"Cautiously, {name} walks through the plains...")
    waiting()
    games('minefield')
    waiting()
    print(f"{name} carefully crosses the supposed minefield and happens to find a banknote!")
    backpack.add_item('banknote')
    waiting()
    print("With the sun setting, I should find a place to rest.")
    waiting()
    print(f"{name} sees a cave in the distance.")
    waiting()
    print(f"The cave is dripping wet, but {name} finds a spot among the rocks to lie down and rest.")
    waiting()
    print("END OF ACT TWO!\nCheckpoint Two Password: fieldofwonders")
    act_three()

def act_three():
    sleep(2)
    print("*Next morning*")
    waiting()
    print(f"After a restful night, {name} packs his things and prepares to leave the cave.")
    waiting()
    print(f"However, as {name} was about to leave, he notices something from the corner of his eye.")
    waiting()
    print("Is that a letter?")
    waiting()
    print(f"Interested, {name} makes his way towards the letter wedged in between two rocks.")
    waiting()
    print(f"{name} picks up the letter and opens it.")
    waiting()
    games('letter')
    waiting()
    print(f"{name} feels the warmth of the sun beams and is glad to have escaped that frightening occurrence.")
    waiting()
    print(f"{name} after walking for a while stumbles across a homeless man.")
    waiting()
    print("Homeless man: Hey kid... I'm a little short on change... would you care to spare a banknote..?")
    spare = False
    while not spare:
        sleep(1)
        choice = input("Do you wish to donate? y/n\n>")
        if choice.lower() == 'y':
            spare = True
            if 'banknote' in backpack.inventory:
                backpack.inventory.remove('banknote')
                sleep(1)
                print("Homeless man: So there is kindness left in the world!")
                waiting()
                print("Homeless man: I shall grant you this in exchange...")
                waiting()
                print("The homeless man passes to you a bottle, filled with red liquid")
                waiting()
                print("Homeless man: Put it to good use...")
                backpack.add_item('health potion')
            else:
                print(f"{name} checks his wallet to realize that he is poor...")
                waiting()
                print("Sorry old man, I don't have anything to spare...")
        elif choice.lower() == 'n':
            spare = True
            sleep(1)
            print("Homeless man: No kindness left in the world... a shame...")
            waiting()
            print("The homeless quickly darts at you!")
            sleep(0.25)
            print("*stab*")
            waiting()
            print("The homeless man steals something...")
            if 'banknote' in backpack.inventory:
                backpack.inventory.remove('banknote')
            update_health_money(-25, 0)
            waiting()
            print("The homeless man darts into a nearby forest and disappears.")
            waiting()
            if health > 0:
                print(f"{name} feels dizzy from blood loss, but seems to be alright.")
            else:
                print(f"{name} feels dizzy...")
                waiting()
                print(f"{name} suddenly collapses...")
                death('5')
        elif choice.lower() == 'inventory':
            use_backpack()
        else:
            sleep(0.25)
            print("Homeless man: What..?")
    waiting()
    print(f"{name} seeking shelter looks for the nearest village.")
    waiting()
    print("After around five hours, a village is seen on the horizon.")
    waiting()
    print("A banknote was also found along the way!")
    backpack.add_item('banknote')
    waiting()
    print(f"{name} makes his way towards the village.")
    waiting()
    print(f"{name} approaches a big fanciful building labelled Ze Gamblos.")
    waiting()
    print("END OF ACT THREE\nCheckpoint Three Password: thetruthoftheworld")
    waiting()
    act_four()

def act_four():
    sleep(2)
    print(f"{name} walks into a bar filled with life.")
    waiting()
    print(f"{name} walks up to the bar tender.")
    waiting()
    drink = True
    while drink:
        need = input("Bar Tender: Need a drink? It'll cost you ten bucks. y/n\n>")
        if need.lower() == 'y':
            if money >= 10:
                update_health_money(0, -10)
                backpack.add_item('health potion')
                sleep(1.5)
                print("*The Bar Tender vigorously shakes a reddish liquid*")
                sleep(1.5)
                print("*The Bar Tender hands you the drink...*")
                sleep(1)
                print(f"{name} acquired a 'health potion'")
            else:
                print("Bar Tender: You're too poor kid...")
                sleep(1)
        elif need.lower() == 'n':
            drink = False
            sleep(2)
            print("Bar Tender: Fine with me...")
        elif need.lower() == 'inventory':
            use_backpack()
        else:
            sleep(0.25)
            print("Bar Tender: What was that kid..?")
    waiting()
    print(f"{name} continues to walk around the bar..")
    waiting()

    while True:
        game = input("Gambler: Want to play a game..? y/n\n>")
        if game.lower() == 'y':
            if money > 0:
                sleep(1)
                bet = input("How much money are you willing to bet?\nEnter amount: ")
                if bet.isdigit():
                    amount = int(bet)
                    if amount <= money:
                        update_health_money(0, -amount)
                        sleep(1)
                        print(f"Gambler: {bet} dollars ey? Fine with me!")
                        sleep(1)
                        result = games('dice')
                        if result:
                            update_health_money(0, amount * 2)
                        elif not result:
                            pass
                    else:
                        print("Gambler: You don't even have that much kid...")
                        sleep(1)
                else:
                    print("Gambler: Are you joking with me?")
                    sleep(1)
            else:
                print("Gambler: You smell like poor...")
                sleep(1)
        elif game.lower() == 'n':
            sleep(1)
            print("Gambler: Suit yourself...")
            break
        elif game.lower() == 'inventory':
            use_backpack()
        else:
            sleep(0.25)
            print("Gamber: Huh..")
    waiting()
    print(f"After an eventful night, {name} decides he should rest up, for he feels something life changing might happen tomorrow.")
    waiting()
    if money <= 0:
        print(f"Weakened by his budget, {name} is forced to return home to retrieve money.")
        act_two()
    print("END OF ACT FOUR\nCheckpoint Four Password: thebigbadbar")
    waiting()
    act_five()

def act_five():
    sleep(2)
    print(f"After leaving the bar, {name} headed towards a distant building.")
    waiting()
    print("The building was massive, with rings of light flying around the perimeter.")
    waiting()
    print(f"When {name} approached the gate, he noticed something.")
    waiting()
    print("There was a giant imprint on the door, the shape of a sword.")
    waiting()
    if not 'sword' in backpack.inventory:
        print("Directly right of the door was a sword stuck in a rock.")
        waiting()
        print("A scripture written on the rock read: 'Life comes at a Price'")
        waiting()
        bought = False
        while not bought:
            sleep(1)
            buy = input('Would you like to buy the sword for 100 dollars? y/n\n>')
            if buy.lower() == 'y':
                sleep(1.5)
                if money >= 100:
                    bought = True
                    update_health_money(0,-100)
                    sleep(1.5)
                    backpack.add_item('sword')
                    print("The sword lifts itself off the rock and disappears...")
                    waiting()
                    print(f"Suddenly, {name} feels his backpack grow heavy...")
                    waiting()
                    print(backpack.inventory)
                    waiting()
                else:
                    print("You cannot afford this...")
                    waiting()
                    print(f"{name} suddenly feels dizzy...")
                    waiting()
                    print("A voice whispers....")
                    waiting()
                    print("you are not worthy")
                    waiting()
                    print(f"{name} feels time warp and change around him...")
                    waiting()
                    act_four()
            elif buy.lower() == 'n':
                sleep(1.5)
                print("Very well...")
                waiting()
                print(f"{name} suddenly feels dizzy...")
                waiting()
                print("A voice whispers....")
                waiting()
                print("you are not worthy")
                waiting()
                print(f"{name} feels time warp and change around him...")
                waiting()
                act_four()
            elif buy.lower() == 'inventory':
                use_backpack()
            else:
                print("That is not a valid answer...")
    print(f"The sword in {name}'s backpack suddenly flies out...")
    waiting()
    print("The sword quickly darts towards the door imprint.")
    waiting()
    print("The sword fits itself in the imprint...")
    waiting()
    print("*door opens*")
    waiting()
    print(f"{name} enters building...")
    waiting()
    print("*door closes*")
    waiting()
    games('boss')

menu()
