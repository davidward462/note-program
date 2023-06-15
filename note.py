import sys
import pickle # For saving and loading objects

# Global variables 
pickelFile = "data.pickle"
prompt = "> "
space = " "

# Master object to store notes
class NoteList():
    def __init__(self):
        self.count = 0
        self.noteList = []

    def GetCount(self):
        return self.count

    def ClearList(self):
        self.count = 0
        self.noteList = []

    # Look for inputName in noteList list.
    # return: true if name found, false otherwise.
    def NameFound(self, inputName):
        for note in self.noteList:
            if note.name == inputName:
                return True
            else:
                return False

    def AddNote(self, note):
        self.noteList.append(note)
        self.count = self.count + 1

    def CreateNote(self, noteName):
        print("Creating note...")

        # if note name is empty, get the user input for the name.
        if noteName == "":
            noteName = input()

        if self.NameFound(noteName):
            noteName = noteName + "-copy"
        n = Note(noteName)
        text = input()
        n.body = text
        self.AddNote(n)

    def PrintList(self, number):
        count = 0
        if number == "":
            number = self.count
        else:
            number = int(number)

        for note in self.noteList:
            if count < number:
                print(f"{note}")
            count = count + 1

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
    print("\texit\n\tlist\n\tnum\n\tnew\n\tsave\n\tload\n\tclear")

def main():
    CheckArgs()

    running = True

    activeList = NoteList()

    # main loop
    while running:
        text = GetUserInput()
        cmdArg = ""

        splitText = text.split(space)
        cmd = splitText[0]

        # check if an argument was supplied to the command.
        if len(splitText) > 1:
            cmdArg = splitText[1]
            print(f"arg: {cmdArg}") # for testing purposes

        # Determine which command was entered
        match cmd:
            case "help":
                ShowHelp()
            case "new":
               activeList.CreateNote(cmdArg)
            case "exit":
                running = False # Stop running
            case "num":
                count = activeList.GetCount()
                print(f"{count} notes in memory.")
            case "list":
                activeList.PrintList(cmdArg)
            case "save":
                SaveObject(activeList)
                count = activeList.GetCount()
                print(f"{count} notes saved.")
            case "load":
                tempNoteList = LoadObject(pickelFile)
                if isinstance(tempNoteList, NoteList):
                    activeList = tempNoteList
                    count = activeList.GetCount()
                    print(f"{count} notes loaded.")
            case "clear":
                activeList.ClearList()
            case "":
                print(end='')
            case _:
                print(f"Unrecognized command '{text}'")

main()
