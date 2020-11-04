import traceback
from datetime import datetime

teraz = str(datetime.now())




class Bledy:


    def blad(self):
            
        with open("errorz.log", "a") as errors:
            errors.write(teraz + "\n")
            traceback.print_exc(file=errors)
            errors.write("\n\n")
            errors.close
