# %%


def move(fromLoc, toLoc):
    print(f"Move disk from location {fromLoc} to {toLoc}")


def moveVia(fromLoc, viaLoc, toLoc):
    move(fromLoc, viaLoc)
    move(viaLoc, toLoc)


def towerOfHanoi(numOfDisks, fromLoc, helperLoc, toLoc):
    if numOfDisks == 0:
        pass
    else:
        towerOfHanoi(numOfDisks-1, fromLoc, toLoc, helperLoc)
        move(fromLoc, toLoc)
        towerOfHanoi(numOfDisks-1, helperLoc, fromLoc, toLoc)
# %%


if __name__ == "__main__":
    numOfDiks = int(input("Please give number of disks  :"))
    towerOfHanoi(numOfDiks, "A", "B", "C")
