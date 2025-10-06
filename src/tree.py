class TerminalTree():
    def __init__(self, firstLevelNode):
        self.firstLevelNode = firstLevelNode

    def prompt_tree(self):
        self.firstLevelNode.test_prompt()

class Node():
    def __init__(self, levelObject):
        self.levelObject = levelObject
        self.nextLevelObjects = None

    def test_prompt(self):
        if self.nextLevelObjects == None:
            print(self.levelObject.name)
            return
        
        if self.__has_multiple_childs():
            for levelObject in self.nextLevelObjects:
                print(levelObject.test_prompt(), levelObject.levelObject.name)
            return
        
        print(self.levelObject.name)
        self.nextLevelObjects.test_prompt()

    def provide_child(self, child):
        self.nextLevelObjects = child

    def __has_multiple_childs(self):
        return isinstance(self.nextLevelObjects, list)
    