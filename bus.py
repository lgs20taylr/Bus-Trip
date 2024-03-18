def main():
    players = int(input("How many players are on the bus?\n"))
    while players < 0 or players > 20:
        players = int(input("Invalid number of players. How many players are on the bus?\n"))
    plan = fillBus(players,3,4)
    printPlan(plan)

def fillBus(players, busX, busY):
    plan = initPlan(busX+1,busY+1)
    for _ in range(players):
        name = input("Please enter your name.")
        row, seatNo = getSeat(plan,busX,busY)
        plan[row][seatNo] = name
        print("Thank you, your name has been added.")
    return plan

def getSeat(plan,x,y):
    row, seatNo = getSeatCoords(x,y)
    while plan[row][seatNo] != "Empty":
        print("Seat is already taken. Please pick a new seat.")
        row, seatNo = getSeatCoords(x,y)
    return row, seatNo

def getSeatCoords(x,y):
    row = int(input("Which row would you like to sit in?"))
    while row > y or row < 0:
        row = int(input("Invalid row. Which row would you like to sit in?"))
    seatNo = int(input("Which seat number would you like to sit in?"))
    while seatNo > x or seatNo < 0:
        seatNo = int(input("Invalid seat number. Which seat number would you like to sit in?"))
    return row, seatNo

def initPlan(x,y):
    plan = {}
    for row in range(y):
        plan[row] = {}
        for seatNo in range(x):
            plan[row][seatNo] = "Empty"
    return plan

def printPlan(plan):
    print("Seating Plan:")
    for row in plan:
        print(row,end=". ")
        for seatNo in plan[row]:
            print(plan[row][seatNo],end=" ")
        print("")

if __name__ == "__main__":
    main()