#Game by Lucas W. Kuipers a.k.a Coppertone

title ="""  _______              _          _           ______  __        _   __        __
|_   __ \            (_)        | |        .' ___  |[  |      (_) [  |      |  ]
  | |__) |  __   _   __   _ .--.\_|.--.   / .'   \_| | |--.   __   | |  .--.| |
  |  __ /  [  | | | [  | [ `.-. | ( (`\]  | |        | .-. | [  |  | |/ /'`\' |
 _| |  \ \_ | \_/ |, | |  | | | |  `'.'.  \ `.___.'\ | | | |  | |  | || \__/  |
|____| |___|'.__.'_/[___][___||__][\__) )  `.____ .'[___]|__][___][___]'.__.;__] """

#Import Modules
from replit import clear
from readchar import readkey
import random
import numpy as np
import re
import sys
from time import sleep

# Settings
fade_time = 0.4  #Factor to the default time it takes for a message to be erased
typing_time = 0.4  #Factor to the default time it takes for each letter to be printed
difficulty = 1  #Factor to the default enemies' stats


# Custom text
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


# Typing effect
def typing(words):
	for char in words:
		sleep(typing_time * 0.07)
		sys.stdout.write(f"{bcolors.BOLD}%s{bcolors.ENDC}" % char)
		sys.stdout.flush()
	sleep(fade_time * len(words) / 10)
	clear()

typing(title)

# Initialize Character
player = {
    'name': 'DEFAULT',
    'health': 2,
    'total_health': 100,
    'current_health': 100,
    'strength': 30,
    'dextery': 100,
    'armor': 100,
    'xp': 0,
    'level': 1,
    'times_left': 0,
    'times_right': 0,
    'rounds': 0,
    'treasure_count': 0,
    'monster_count': 0,
    'potion_count': 0,
    'points': 0
}

# Introduction
typing("Wake up, kid, you gotta keep moving")
typing("What's your name?")
player['name'] = input("> ")
sleep(0.5)
clear()
typing('May you fight with the strength of ten full grown men, ' + player['name'])


# Level up
def level_up():
	xp_to_level_up = 15 * np.ln(player['level'] + 1)
	if playe['xp'] >= xp_to_level_up:
		player['level'] += 1
		typing('You leveled up! Now you are level ' + player['level'])
		player['xp'] = player['xp'] - xp_to_level_up


# Updating rounds
def update_round():
	player['rounds'] = player['times_left'] + player['times_right']


# Enemy List
enemies = {
    'skeleton': {
        'name':
        'skeleton',
        'total_health':
        40,
        'current_health':
        40,
        'strength':
        5,
        'dextery':
        100,
        'odds':
        60,
        'message':
        'The noise of bones cracking gets louder as you finally see a human skeleton heading towards you with boiling rage'
    },
    'goblin': {
        'name':
        'goblin',
        'total_health':
        30,
        'current_health':
        30,
        'strength':
        10,
        'dextery':
        80,
        'odds':
        40,
        'message':
        'An ugly scary goblin jumps in front of you... salivating to eat your interiors'
    }
}
chance_enemy = []
for key in enemies:
	chance_enemy = chance_enemy + enemies[key]['odds'] * [key]
enemy = dict()


# Pick Enemy
def pick_enemy():
	global enemy
	enemy = enemies[random.choice(chance_enemy)]
	typing(enemy['message'])


# Choose Path
def choose():
	typing(
	    'As you continue to walk the dungeon, you must choose which way to go')
	print('Which way do you wish to go,', player['name'],
	      '? (Press "A" to go left and "D" to go right.')
	while True:
		choice = str(readkey())
		if choice == 'a':
			player['times_left'] += 1
			typing('You decide to go left')
			break
		elif choice == 'd':
			player['times_right'] += 1
			typing('You decide to go right')
			break


# Encounter
def encounter():
	encounters = ['Treasure'] * 2+ ['Monster'] * 8
	result = random.choice(encounters)
	if result == 'Treasure':
		typing(
		    'Your eyes shine as they glimpse the treasure lying in front of you'
		)
		player['treasure_count'] += 1
		reward()
	else:
		typing(
		    'The ruins echo in agony as something lurking in the dark approaches...'
		)
		player['monster_count'] += 1
		combat()


# Reward (points and: potion, armor or nothing)
def reward():
	update_round()
	# Points
	points = 100 * (np.log(player['rounds']) + 1)
	player['points'] += points
	typing('You just received %d points' % (points))
	typing('Now you have %d points!' % (player['points']))
	# Times to reward
	times_reward = int(np.log(player['rounds'] + 1)) + 1
	for i in range(times_reward):
		# Potion
		chances_potion = 1* ['Yes'] + 10* ['No']
		potion = random.choice(chances_potion)
		if potion == 'Yes':
			player['potion_count'] += 1
			typing('You just found a potion!')
			typing('You now have ' + str(player['potion_count']) +
			       ' potion(s)')
		# Armor
		if player['armor'] < 200:
			chances_armor = 1 * ['Yes']+10*['No']
			armor = random.choice(chances_armor)
			if armor == 'Yes':
				player['armor'] += 5
				typing('You just found a new piece of armor!')
				typing('You now have ' + str(player['armor']) +
				       ' of armor status')
				if player['armor'] == 200:
					typing('You have the maximum armor status!')


# Enemy Stats
def enemy_stats():
	global enemy
	enemy['level'] = np.log(player['rounds'] + 1) + 1
	factor = enemy['level'] * difficulty
	enemy['strength'] = factor * enemy['strength']
	enemy['total_health'] = factor * enemy['total_health']
	enemy['dextery'] = factor * enemy['dextery']
	enemy['current_health'] = factor * enemy['current_health']
	print(enemy)


# Combat Initialize
def combat_initialize():
	update_round()
	pick_enemy()
	enemy_stats()


# Player Attack
def player_attack():
	typing('You rush onto the %s, slashing feriously' % (enemy['name']))


# Player Run Away
def run_away():
	print("You run away")


# Taking Potion
def taking_potion():
	print("You take a potion")


# Player Death
def player_death():
	print('You died')


# Show Player Stats
# def player_stats():
# 	msg_name = "Name: " + player['name']
#   if player['current_health']


# Player Turn
def player_turn():
	print(
	    'What do you wish to do,' + player['name'] +
	    '? Press "A" to attack, "R" to run away, "P" to use a potion and "S" to see your stats'
	)
	while True:
		choice = str(readkey())
		if choice == 'a':
			player_attack()
			break
		elif choice == 'r':
			run_away()
			break
		elif choice == 'p':
			taking_potion()
			break
		elif choice == 's':
			player_stats()
			continue


# Enemy Death
def enemy_death():
	print('Enemy dies')


# Enemy Turn
def enemy_turn():
	print('The %s attacks you' % (enemy['name']))


# Combat Turns
def combat_turns():
	while True:
		if enemy['current_health'] > 0:
			player_turn()
		else:
			enemy_death()
			break
		if player['current_health'] > 0:
			enemy_turn()
		else:
			player_death()
			break


# Combat Finish
def combat_finish():
	player['xp'] += 100


# Combat
def combat():
	combat_initialize()
	combat_turns()
	combat_finish()


while True:
	choose()
	encounter()
