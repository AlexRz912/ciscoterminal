class TerminalTree():
    def __init__(self, rootNode):
        self.rootNode = rootNode
        self.selected = rootNode

    def prompt_tree(self):
        self.rootNode.prompt_all()

    def select_node(self, command):
        if command == "end":
            self.selected = self.rootNode.childNodes
            return
        if command == "exit":
            self.selected = self.selected.parentNode
            return

        self.__handle_adjacents(command)

    def __handle_adjacents(self, command):
        if self.__selected_has_multiple_childs():
            self.__select_child_on_matching_command(command)

        if command == self.selected.levelDownCommands:
            self.selected = self.selected.childNodes

    def __selected_has_multiple_childs(self):
        return isinstance(self.levelDownCommands, list)
    
    def __select_child_on_matching_command(self, command):
        for index, levelDownCommand in enumerate(self.selected.levelDownCommands):
            if command == levelDownCommand and levelDownCommand == self.selected.childNodes[index].parentCommand:
                self.selected_mode = self.selected.childNodes[index]


class Node():
    def __init__(self, activeNode, parentNode=None):
        self.activeNode = activeNode
        self.parentNode = parentNode
        self.childNodes = None

    def prompt_all(self):
        if self.__has_no_child():
            print(self.activeNode.name)
            return
        
        if self.__has_multiple_childs():
            print(self.activeNode.name)
            for child in self.childNodes:
                child.prompt_all()
            return
        
        print(self.activeNode.name)
        self.childNodes.prompt_all()

    def provide_child(self, child):
        self.childNodes = child

    def __has_no_child(self):
        return self.childNodes == None

    def __has_multiple_childs(self):
        return isinstance(self.childNodes, list)
    
    def __has_parents(self):
        return not self.parentNode == None
    