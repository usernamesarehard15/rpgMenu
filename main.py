# Anthony Clark
# CS 30 Period 2
# November 25th 2020
# rpgMenu system for use in game
from actions import runCommand
from actions import actions

# Create printed list of actions player do
actionsDisplay = 'Enter an action\n'
for action in actions:
    actionsDisplay += f'-{action.name}\n'

playing = True
while (playing):
	runCommand(input(actionsDisplay))

