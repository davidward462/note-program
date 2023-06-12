import sys
import pickle # For saving and loading objects

# Master object to store notes
class NoteList():
    def __init__(self):
        self.count = 0
        self.noteList = []
    
    def CreateNote(self):
        print("Creating note...")
        n = Note("temp")
        text = input()
        n.body = text
    
class Note():
    def __init__(self, name):
        # name is an instance variable
        self.name = name
        self.body = ""

    def SetBody(self, data):
        self.body = data

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
        with open("data.pickle", "wb") as f:
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
        userIn = input("> ")
        return userIn
    except EOFError:
        print()
        return 'exit'

def main():
    CheckArgs()

    running = True

    noteList = NoteList()

    # main loop
    while running:
        text = GetUserInput()

        # Determine which command was entered
        match text:
            case "new":
                NoteList().CreateNote()
            case "exit":
                running = False # Stop running
            case "list":
                print("Notes:")
            case "":
                print(end='')
            case _:
                print(f"Unrecognized command '{text}'")

main()