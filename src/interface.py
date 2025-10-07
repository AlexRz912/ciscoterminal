class InterfaceLevel():
    def __init__(
            self, 
            name, 
            interface, 
            commands, 
            levelDownCommands, 
            parentCommand=None
            ):
        

        self.name              = name
        self.interface         = interface
        self.commands          = commands
        self.levelDownCommands = levelDownCommands
        self.parentCommand     = parentCommand