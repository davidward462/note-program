import sys
import pickle # For saving and loading objects
import noteList

# Global variables 
pickelFile = "data.pickle"
prompt = "> "

class Commands():
    def __init__(self):
        self.clear = "clear"
        self.delete = "delete"
        self.exit= "exit"
        self.find = "find"
        self.help = "help"
        self.list = "list"
        self.load = "load"
        self.new = "new"
        self.num = "count"
        self.save = "save"

        self.cmdList = [self.clear, self.delete, self.exit, self.find, self.help, self.list, self.load, self.new, self.num, self.save]

    def PrintCommands(self):
        for cmd in self.cmdList:
            print(f" {cmd}")

        
    
class Note():
    def __init__(self, name):
        # name is an instance variable
        self.name = name
        self.body = ""

    def SetBody(self, data):
        self.body = data

    def __repr__(self):
        return f" Name: {self.name}\n Body: {self.body}\n"

def default():
    return "default"

# Show filename and command line arguments.
def CheckArgs():
    argLen = len(sys.argv)
    if argLen > 1:
        for arg in sys.argv[1:]:
            print(arg)
    else:
        print(" No arguments passed.")

# Save object to pickle file
def SaveObject(obj):
    print(" Saving...")
    try:
        with open(pickelFile, "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as e:
            print(f" Error occured during pickling object (possibly unsupported): {e}")

# Load object from given pickle file
def LoadObject(filename):
    print(" Loading...")
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as e:
        print(f" Error during unpickling object (Possibly unsupported): {e}")

# Handle user input and possible EOF
def GetUserInput():
    try:
        userIn = input(prompt)
        return userIn
    except EOFError:
        print()
        return 'exit'

def main():
    CheckArgs()

    running = True

    # Create objects
    activeList = noteList.NoteList()
    cmds = Commands()

    # main loop
    while running:
        text = GetUserInput()
        cmdArg = ""

        splitText = text.split(space)
        cmd = splitText[0]

        # check if an argument was supplied to the command.
        if len(splitText) > 1:
            cmdArg = splitText[1]
            print(f" arg: {cmdArg}") # for testing purposes

        # Determine which command was entered
        match cmd:
            case cmds.help:
                cmds.PrintCommands()

            case cmds.new:
               activeList.CreateNote(cmdArg)
               
            case cmds.exit:
                running = False # Stop running

            case cmds.num:
                count = activeList.GetCount()
                print(f" {count} notes in memory.")
                
            case cmds.list:
                activeList.PrintNames(cmdArg)

            case cmds.save:
                SaveObject(activeList)
                count = activeList.GetCount()
                print(f" {count} notes saved.")

            case cmds.load:
                tempNoteList = LoadObject(pickelFile)
                if isinstance(tempNoteList, NoteList):
                    activeList = tempNoteList
                    count = activeList.GetCount()
                    print(f" {count} notes loaded.")

            case cmds.delete:
                activeList.DeleteNote(cmdArg)

            case cmds.find:
                activeList.FindNote(cmdArg)

            case cmds.clear:
                activeList.ClearList()

            case "":
                print(end='')

            case _:
                print(f" Unrecognized command '{splitText[0]}'")

main()
