import random

# This is a proof of concept of an idea I had. Basically I am trying to build
# artificial intelligence from the ground up, with the simplest game possible

# The game is simple, I choose a boolean, and to win, you need to choose the
# same boolean.


# Here is a definition of the game:
class CopyCatGame:
    def __init__(self):
        self.player = Player()

    def play(self, myInput):
        response = self.player.play(myInput)
        return myInput == response

# As you can see, all the player class needs to be able to do is return myInput,
# untouched, a "Perfect" AI in this case would have the following implementation

class PerfectPlayer:
    def play(self, givenInput):
        return givenInput

# However, we're not interested in hard coding the solution to this, what we
# need to do is to get the player to understand how to play and win the game

# So now the game has taken up a level, the game is no longer trying to return
# the same value as given, the game is to work out what the game is

# If you consider if you yourself were introduced to this game, without any
# description of the rules, you are taken straight into it. You would endevour
# to try and work out what the actual rules are so that you can win

# The player is now a Meta Player that given the cases that it has tried before
# returns a player that it thinks will work

# This Meta Player needs to have knowledge of multiple sessions, so therefore
# the meta game includes the loop that teaches the meta player what player
# to give

# I'll need a quick definition of a random boolean for use later:
def randomBoolean():
    return bool(random.getrandbits(1))

# Heres a definition of the meta game
class MetaCopyCatGame:
    def __init__(self):
        self.metaplayer = MetaPlayer()

    def play(self):
        correctCount = 0
        while correctCount < 10:
            myInput = randomBoolean()
            print("My Input: " + str(myInput))

            player = self.metaplayer.get_player()
            response = player.play(myInput)
            print("Player's response: " + str(response))

            outcome = response == myInput
            print("Outcome: " + str(outcome))
            print()

            if outcome:
                correctCount += 1
            else:
                correctCount = 0

            self.metaplayer.add_case((myInput, response, outcome))

# There shouldn't be too much of a suprise here. Again, doing this in real life
# would be exactly the same. What is the game? The instanciated players are
# your strategies.

# How many possible players are there? Well, assuming that it's always possible
# to win and always possible to loose, 4. Choose the same, choose the opposite,
# always choose True and always choose False

# However, that's assuming that it's always possible to win or loose. I'll call this
# The assumption of infuence

# Our player class needs to have the ability to swap out different methods of
# play in it's constructor.

class Player:
    def __init__(self, method):
        self.method = method;

    def play(self, givenValue):
        return self.method(givenValue)

# Where the possible methods are
methods = [
    lambda x: x,
    lambda x: not x,
    lambda x: True,
    lambda x: False
]

# Finally, I need to define the MetaPlayer
class MetaPlayer:
    def __init__(self):
        self.cases = []

    def add_case(self, case):
        self.cases.append(case)

    def resultOf(self, givenInputs):
        for case in self.cases:
            if case[0] == givenInputs[0] and case[1] == givenInputs[1]:
                return case[2]
        return None

    def get_possible_methods(self):
        possible_methods = methods[:]
        for case in self.cases:
            for method in possible_methods[:]:
                # If it didn't work last time
                if method(case[0]) == case[1] and not case[2]:
                    possible_methods.remove(method)

                # If it worked last time using a different method
                if method(case[0]) != case[1] and case[2]:
                    possible_methods.remove(method)
        return possible_methods

    def get_player(self):
        possible_methods = self.get_possible_methods()
        viable_method = random.choice(possible_methods)
        return Player(viable_method)

# Lets try it out!
game = MetaCopyCatGame()
game.play()

# I will work on this, but I beleive that if I go high enough with these meta-games,
# it will become obvious a situation that can loop back on itself in order to
# create general purpose intelligence. Pretty naive, but should be interesting
