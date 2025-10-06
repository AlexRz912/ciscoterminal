class TerminalTree():
    def __init__(self, firstLevelNode):
        self.firstLevelNode = firstLevelNode

    def prompt_tree(self):
        self.firstLevelNode.test_prompt()

class Node():
    def __init__(self, levelObject, childLevelObjects):
        self.levelObject = levelObject
        self.nextLevelObjects = childLevelObjects

    def test_prompt(self):
        if self.__has_multiple_childs():
            for levelObject in self.nextLevelObjects:
                print(levelObject.level)
            return
        print(self.levelObject.level)
        self.nextLevelObjects.test_prompt()

    def __has_multiple_childs(self):
        return isinstance(self.nextLevelObject.name, list)
    