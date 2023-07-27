#imports
import time, random
import game, player, story


def main():
    p1 = game.start()

    print("Welcome! "+str(p1.displayTitle()))
    print(p1.displayStats())
    print(story.intro(p1))

if __name__ == "__main__":
    main()