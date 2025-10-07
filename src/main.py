from interface import InterfaceLevel
from tree import TerminalTree, Node

user_mode_command_list = [
    "ping",
    "traceroute",
    "show version",
    "show running-config",
    "show ip interface brief",
    "show flash",
    "show protocols",
    "exit",
    "logout",
    "enable"  # pour passer en mode privilégié
]


privileged_mode_command_list = [
    "configure terminal",  # passer en mode configuration globale
    "copy running-config startup-config",
    "show running-config",
    "show startup-config",
    "show interfaces",
    "show ip route",
    "reload",
    "debug",
    "undebug all",
    "clear counters",
    "write memory",
    "disable"  # pour revenir en mode utilisateur
]

global_mode_command_list = [
    "hostname",
    "interface",
    "line",
    "router",
    "ip route",
    "access-list",
    "banner motd",
    "exit",
    "end"
]






user_mode = Node(InterfaceLevel("user exec mode", ">:", user_mode_command_list))
privileged_mode = Node(InterfaceLevel("privileged exec mode", "#:", privileged_mode_command_list), user_mode)
user_mode.provide_child(privileged_mode)
global_mode = Node(InterfaceLevel("global config mode", "(config)#:", global_mode_command_list), privileged_mode)
privileged_mode.provide_child(global_mode)

config_interfaces_mode = [
    Node(InterfaceLevel("interface", "##:", "blob"), global_mode), 
    Node(InterfaceLevel("router", "##:", "blob"), global_mode),
    Node(InterfaceLevel("line", "###:", "blob"), global_mode)
]
global_mode.provide_child(config_interfaces_mode)

interface_tree = TerminalTree(user_mode)
interface_tree.prompt_tree()