import subprocess

from src.interface import InterfaceLevel
from src.tree import TerminalTree, Node

user_mode_command_list = [
    "ping",
    "traceroute", 
    "show version",
    "show running-config",
    "show ip interface brief",
    "show flash",
    "show protocols",
    "exit",
    "logout"
]

privileged_mode_command_list = [
    "configure terminal",
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
    "disable"
]

global_mode_command_list = [
    "hostname",
    "interface",
    "line",
    "router",
    "ip route",
    "access-list",
    "banner motd"
]

user_mode = Node(InterfaceLevel("user exec mode", ">:", user_mode_command_list, "enable"))
privileged_mode = Node(InterfaceLevel("privileged exec mode", "Switch#:", privileged_mode_command_list, "config terminal"), user_mode)
user_mode.provide_child(privileged_mode)
global_mode = Node(InterfaceLevel("global config mode", "Switch(config)#", global_mode_command_list, ["interface", "line", "router"]), privileged_mode)
privileged_mode.provide_child(global_mode)

config_interfaces_mode = [
    Node(
        InterfaceLevel
            (
                "interface", 
                "Switch(config-if)#:", 
                "blob", 
                None, 
                "interface"
            ), 
        global_mode),
    Node(
        InterfaceLevel
            (
                "line", 
                "Switch(config-line)#", 
                "blob", 
                None, 
                "line"
            ), 
            global_mode
        ),
    Node(
        InterfaceLevel
            (
                "router", 
                "Switch(config-router)#", 
                "blob", 
                None, 
                "router"
            ), 
            global_mode
        )
]

global_mode.provide_child(config_interfaces_mode)
interface = TerminalTree(user_mode)

def handle_input():
    command = input(f"{interface.selected.activeNode.interface} ")
    subprocess.run("cls", shell=True)
    return command

def terminal():
    log = ""
    subprocess.run("cls", shell=True)
    while True:
        user_input = handle_input()
        #print(log)
        #if interface.is_no_command(user_input):
        #    log = f"% invalid input detected at '^' marker"
        #    continue
#
        #if interface.is_ambiguous(user_input):
        #    log = f"% ambiguous command: {user_input}"
        #    continue

        if user_input != "":
            interface.select_node(user_input)

terminal()

