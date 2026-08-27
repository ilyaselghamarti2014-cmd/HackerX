from art import *
from colorama import *

def start_tool_animation1(text) :
    art_text = text2art(text)
    print(Fore.YELLOW + art_text)
    return text
def start_tool_animation2(text) :
    print(Fore.GREEN + text)
    return text

def start_tool_animation3(text) :
    print(Fore.CYAN + text)
    return text