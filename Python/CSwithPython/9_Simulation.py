from random import random

def printIntro():
    print("This program simulates a game of racquetball between two")
    print("players called 'A' and 'B'. The ability of each player is")
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.")

def getInputs():
    # 시뮬레이션에 필요한 세 가지 정보 probA, probB, n을 리턴한다. 
    a = float(input("What is the prob. player A wins a serve?"))
    b = float(input("What is the prob. player B wins a serve?"))
    n = int(input("How many games to simulate?"))
    return a, b, n

def simNGames(n, probA, probB):
    winsA = 0
    winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsB + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simOneGame(probA, probB):
    scoreA = 0
    scoreB = 0
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOver(a, b):
    # a와 b 는 두 선수의 현재 득점이다. 
    # 경기 종료 조건 (a == 15, or b == 15)을 만족하면 True 그렇지 않으면 False를 리턴한다. 
    return a == 15 or b == 15

def printSummary(winsA, winsB):
    n = winsA + winsB
    print("n\Games simulated: ", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))


def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

if __name__ == '__main__': 
    main()