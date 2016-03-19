import random
import math

stopOnJackpot = True # switch for stopping ticket processing
printEvery = 1000000 # interval of amount spent to that will be printed
grandPrize = 1500000000
jackpotOdds = 292201338 # odds of winning jackpot are 1 in 292,201,338

ticketNums = set(range(1,6)) # ticket numbers are preset as they won't affect the simulation result
ticketPNum = 1;

balls = tuple(range(1, 70))
powerballs = tuple(range(1, 27))

        # prize money will be looked up from a diction`ary
prizes = {(0, False): 0,
          (1, False): 0,
          (2, False): 0,
          (3, False): 7,
          (4, False): 100,
          (5, False): 1000000,
          (0, True): 4,
          (1, True): 4,
          (2, True): 7,
          (3, True): 100,
          (4, True): 50000,
          (5, True): grandPrize}

# initial conditions
won = 0
spent = 0
jackpot = False

while not jackpot or not stopOnJackpot:
    chosenBalls = random.sample(balls, 5)
    chosenPBall = random.choice(powerballs)

    hits = 0
    for ball in chosenBalls:
        if ball in ticketNums:
            hits += 1

    pballHit = (chosenPBall == ticketPNum)

    matches = (hits, pballHit)
    won += prizes[matches]
    spent += 2
    jackpot = ((5, True) == matches)

    if spent % printEvery == 0 or jackpot:
        results = "spent: {:,}, won: {:,}, net: {:,}".format(spent, won, won - spent)
        print(results)

    # given a large sample size, n number of tickets bought, p probability of a winning ticket
    # the expected number of people who wins the jackpot is given by E(X) = np
    if jackpot:
        ticketsBought = spent / 2
        np = int(round(ticketsBought / jackpotOdds));

        netWon = "Net won (no split): {:,}".format(won - spent)

        if np <= 1:
            adjustedWon = "Net won (split): {:,}".format(won - spent)
        else:
            adjustedWon = "Net won (split): {:,}".format(((won - spent) - grandPrize) / np)

        print("----JACKPOT----")
        print(netWon)
        print(adjustedWon)
