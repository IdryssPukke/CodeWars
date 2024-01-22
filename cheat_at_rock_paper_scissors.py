from random import choices
solutions = {
    "paper": ["rock", "scissors"],
    "rock" : ["scissors", "paper"],
    "scissors": ["paper", "rock"]
}

def r_p_s_cheat(choice):
    return choices(solutions[choice], weights=[10, 90])[0]

print(r_p_s_cheat("rock"))