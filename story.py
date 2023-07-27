import sys
import time
import game, player, enemy
import randomize

def travelAnim():
    #Travel animation
    #Print traveling with moving dots
    print("Traveling", end="")
    for i in range(4):
        time.sleep(.5)
        sys.stdout.write(".")
        sys.stdout.flush()
    return ""

def intro (player):
    name = player.name
    print(f"Beginning your adventure in {randomize.randPlace()}")
    travelAnim()
    return ""

