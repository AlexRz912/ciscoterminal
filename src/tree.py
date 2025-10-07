class TerminalTree():
    def __init__(self, firstLevelNode):
        self.firstLevelNode = firstLevelNode

    def prompt_tree(self):
        self.firstLevelNode.test_prompt()

class Node():
    def __init__(self, levelNode, parentNode=None):
        self.levelNode = levelNode
        self.parentLevelNode = parentNode
        self.childLevelNodes = None

    def test_prompt(self):
        if self.__has_no_child():
            print(self.levelNode.name)
            return
        
        if self.__has_multiple_childs():
            #print(self.levelObject.name)
            for child in self.childLevelNodes:
                print(child.levelNode.name)
                child.test_prompt()
            return
        
        print(self.levelNode.name)
        self.childLevelNodes.test_prompt()

    def provide_child(self, child):
        self.childLevelNodes = child

    def __has_no_child(self):
        return self.childLevelNodes == None

    def __has_multiple_childs(self):
        return isinstance(self.childLevelNodes, list)
    
    def __has_parents(self):
        return not self.parentLevelNode == None
    