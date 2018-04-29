import random
class Game:
    def __init__(self):
        self.player = Player()

    def start(self):
        correctCount = 0;
        while correctCount < 10:
            myInput = bool(random.getrandbits(1))
            print("Me: " + str(myInput))
            playerInput = self.player.play(myInput)
            print("Copycat: " + str(playerInput))
            print()
            output = myInput == playerInput
            if output:
                correctCount += 1
            self.player.learner.addCase((myInput, playerInput, output))

class Player:
    def __init__(self):
        self.learner = Learner()

    def play(self, givenValue):
        output = self.learner.resultOf((givenValue, True))
        if output == None:
            return bool(random.getrandbits(1))
        else:
            return output

class Learner:
    def __init__(self):
        self.cases = []

    def addCase(self, case):
        self.cases.append(case)

    def resultOf(self, givenInputs):
        for case in self.cases:
            if case[0] == givenInputs[0] and case[1] == givenInputs[1]:
                return case[2]
        return None
game = Game()
game.start()
