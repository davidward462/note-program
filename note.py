import sys
import pickle # For saving and loading objects

# Global variables 
pickelFile = "data.pickle"
prompt = "> "

# Master object to store notes
class NoteList():
    def __init__(self):
        self.count = 0
        self.noteList = []

    def PrintCount(self):
        print(f"{self.count}")
    
    def CreateNote(self):
        print("Creating note...")
        noteName = input()
        n = Note(noteName)
        text = input()
        n.body = text
        self.noteList.append(n)
        self.count = self.count + 1

    def PrintList(self):
        for note in self.noteList:
            print(f"{note}")

    def __repr__(self):
        return f"Count: {self.count}\n"
        
    
class Note():
    def __init__(self, name):
        # name is an instance variable
        self.name = name
        self.body = ""

    def SetBody(self, data):
        self.body = data

    def __repr__(self):
        return f"Name: {self.name}\nBody: {self.body}\n"

# Show filename and command line arguments.
def CheckArgs():
    print(f"Filename: {sys.argv[0]}")
    argLen = len(sys.argv)
    if argLen > 1:
        for arg in sys.argv[1:]:
            print(arg)
    else:
        print("No arguments passed.")

# Save object to pickle file
def SaveObject(obj):
    print("Saving...")
    try:
        with open(pickelFile, "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as e:
            print(f"Error occured during pickling object (possibly unsupported): {e}")

# Load object from given pickle file
def LoadObject(filename):
    print("Loading...")
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as e:
        print(f"Error during unpickling object (Possibly unsupported): {e}")

# Handle user input and possible EOF
def GetUserInput():
    try:
        userIn = input(prompt)
        return userIn
    except EOFError:
        print()
        return 'exit'

def ShowHelp():
    print("\texit\n\tlist\n\tnum\n\tnew\n\tsave\n\tload")

def main():
    CheckArgs()

    running = True

    activeList = NoteList()

    # main loop
    while running:
        text = GetUserInput()

        # Determine which command was entered
        match text:
            case "help":
                ShowHelp()
            case "new":
                activeList.CreateNote()
            case "exit":
                running = False # Stop running
            case "num":
                activeList.PrintCount()
            case "list":
                activeList.PrintList()
            case "save":
                SaveObject(activeList)
            case "load":
                activeList = LoadObject(pickelFile)
            case "":
                print(end='')
            case _:
                print(f"Unrecognized command '{text}'")

main()