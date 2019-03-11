
rules = {"rock":"scissors","scissors":"paper","paper":"rock"}

def checkResult(a, b):
    if a.lower() == b.lower():
        return "Match Drawn"
    for e in rules:
        if a.lower() == e and b.lower() == rules[e]:
            return "Player-1 Win the game"
        else:
            return "Player-2 Win the game"

def playerInputCheck(player):
    playerChoice = input("Player {}, you have to type only (Rock, Scissors, Paper): ".format(player))
    while playerChoice.lower() not in rules:
        print("You typed Wrong input")
    return playerChoice

while True:
    a = playerInputCheck("1")
    b = playerInputCheck("2")
    print(checkResult(a, b))
    ans = input("Play Again? Type 'Y/n'")
    if ans.lower() in ("n","no"): break
    
    
    

