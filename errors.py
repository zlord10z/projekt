import traceback
from datetime import datetime
import subprocess


now = str(datetime.now())

def error():
        
    with open("errorz.log", "a") as errors:
        errors.write(now + "\n")
        traceback.print_exc(file=errors)
        errors.write("\n\n")
        errors.close


        subject = "log " + str(now)
        message = str(traceback.format_exc()) 
        command = ("mail -s \""+str(subject)+"\" address@mail.com <<< \""+str(message)+"\"")
        print(command)
        subprocess.Popen(['/bin/bash', '-c', command])

