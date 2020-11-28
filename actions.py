import sys


class action:
    def __init__(self, name, aliases):
        self.name = name
        self.aliases = aliases

class actInventory(action):
    def __init__(self):
        aliases = ('show inventory', 'show inv', 'inventory', 'inv', 'i')
        action.__init__(self, 'Show inventory', aliases)

    def run(self, args):
        print('PRINT INVENTORY')


class actMap(action):
    def __init__(self):
        aliases = ('show map', 'show m', 'map', 'ma')
        action.__init__(self, 'Show map', aliases)

    def run(self, args):
        print('PRINT MAP')


class actMove(action):
    def __init__(self):
        aliases = ('move', 'mo', 'm')
        action.__init__(self, 'Move', aliases)

    def run(self, args):
        directions = ('up', 'down', 'right', 'left')
        # Check if first argument exists and is valid
        if (len(args) < 1 or not args[0] in directions):
            print('Invalid arguments! Example usage: move up')
            return
        print(f'MOVED {args[0].upper()}')


class actQuit(action):
    def __init__(self):
        aliases = ('quit', 'exit', 'quit game', 'exit')
        action.__init__(self, 'Quit Game', aliases)

    def run(self, args):
        print('Goodbye!')
        sys.exit(0)


actions = [actInventory(), actMap(), actMove(), actQuit()]


def runCommand(playerInput):
    # Parse action input into action (string) and arguments (list)
    args = playerInput.lower().strip().split(' ')
    command = args.pop(0)
    # handling edge cases for multi word commands
    if (command in ('show', 'use', 'quit', 'exit') and len(args) > 0):
        command += ' ' + args.pop(0)

    # Find and run action, note if successful
    successful = False
    for action in actions:
        for alias in action.aliases:
            if (alias == command):
                action.run(args)
                successful = True
    if (not successful):
        print('Invalid Action!')
    print()
