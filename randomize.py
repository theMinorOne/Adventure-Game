import random, time
import game, player, enemy

#generate random location
def randPlace():
    return random.choice(list(game.places.values()))

#random enemy types
def rand_enemyType():
    return random.choice(enemy.type)

#random enemy
def randEnemy():
    return enemy.Enemy(None, game.randRace(), rand_enemyType())