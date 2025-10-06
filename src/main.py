from interface import InterfaceLevel
from tree import TerminalTree, Node

user_mode = Node(InterfaceLevel("user exec mode", ">:", "enable"))
privileged_mode = Node(InterfaceLevel("privileged exec mode", "#:", "config_terminal"))
user_mode.provide_child(privileged_mode)
global_mode = Node(InterfaceLevel("global config mode", "(config)#:", "fa0/0"))
privileged_mode.provide_child(global_mode)

config_interfaces_mode = [
    Node(InterfaceLevel("interface", "##:", "blob")),
    Node(InterfaceLevel("router", "##:", "blob")),
    Node(InterfaceLevel("line", "###:", "blob"))
]
global_mode.provide_child(config_interfaces_mode)

interface_tree = TerminalTree(user_mode)
interface_tree.prompt_tree()