import subprocess
import os
import sys

keyboardName = "AT Translated Set 2 keyboard"

output = subprocess.Popen("xinput", shell=True, stdout=subprocess.PIPE)
for line in output.stdout:
    if keyboardName in str(line):
        box = str(line).split("\\");
        for section in box:
            if "id" in section:
                id = 0;
                for char in section:
                    if(char.isdigit()):
                        id = (id*10)+int(char);
os.system("xinput float " + str(id));
