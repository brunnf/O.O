from package.agenda import Agenda
import os

def workspace():
    sistema = Agenda()
    sistema.iniciar()

if __name__ == "__main__":
    workspace()
    os.system('rm -rf package/__pycache__')