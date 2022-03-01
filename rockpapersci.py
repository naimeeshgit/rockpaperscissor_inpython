# two classes : user and computer
# choices : input 
# match input with r,p,s

# ask computer to choose r,p,s
# then compare and decide winner

from random import randint

list_choice = ['s', 'r', 'p']

class player:
    def __init__(self):
        self.choice = None
        self.score = 0
    
    def get_input(self, choice, run):
        z = 0
        for x in range(3):
            if choice == list_choice[x]:
                z = 1
        if z == 0:
            print('Invalid choice')
            run = False
            return run
        if z == 1:
            print('Valid choice')
            self.choice = choice
            return run

    def return_choice(self):
        return self.choice

    def check(self, comp_choice):
        if self.choice != "None":
            if self.choice == comp_choice:
                print('Tie')
            elif self.choice == 'r' and comp_choice == 'p':
                print('Computer wins')
                self.score += -1
            elif self.choice == 'r' and comp_choice == 's':
                print('Player wins')
                self.score += 1
            elif self.choice == 'p' and comp_choice == 'r':
                print('Player wins')
                self.score += 1
            elif self.choice == 'p' and comp_choice == 's':
                print('Computer wins')
                self.score += -1
            elif self.choice == 's' and comp_choice == 'r':
                print('Computer wins')
                self.score += -1
            elif self.choice == 's' and comp_choice == 'p':
                print('Player wins')
                self.score += 1
            else:
                 print('Invalid choice')

            

    def update_score(self):
        return self.score

run = True

player = player()

while run == True:
    run = player.get_input(input("enter your choice : "), run)
    if run == False:
        break
    comp_choice = list_choice[randint(0,2)]
    print(f"the computer choice is {comp_choice}")
    player.check(comp_choice)

    print(player.update_score())


