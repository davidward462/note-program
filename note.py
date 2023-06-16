import sys
import pickle # For saving and loading objects

# Global variables 
pickelFile = "data.pickle"
prompt = "> "
space = " "

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
        isFound = False
        for note in self.noteList:
            if note.name == inputName:
                isFound = True
        return isFound

    def GetNoteIndex(self, noteName):
        currentIndex = 0
        for note in self.noteList:
            if note.name == noteName:
                return currentIndex
            currentIndex = currentIndex + 1

    def AddNote(self, note):
        self.noteList.append(note)
        self.count = self.count + 1

    def DeleteNote(self, inputName):
        if self.NameFound(inputName):
            index = self.GetNoteIndex(inputName)
            print(f" deleting {inputName} at {index}...")
            del self.noteList[index]
            self.count = self.count - 1

    def FindNote(self, inputName):
        if self.NameFound(inputName):
            index = self.GetNoteIndex(inputName)
            print(f" Note {inputName} has index {index}.")
        else:
            print(f" Note {inputName} note found.")

    def CreateNote(self, noteName):
        print(" Creating note...")

        # if note name is empty, get the user input for the name.
        if noteName == "":
            noteName = input(space)

        # if note name is taken, append text
        if self.NameFound(noteName):
            noteName = noteName + "-copy"
        n = Note(noteName)
        text = input(space)
        n.body = text
        self.AddNote(n)

    def PrintNames(self, number):
        count = 0
        if number == "":
            number = self.count
        else:
            number = int(number)

        for note in self.noteList:
            if count < number:
                print(f" {note.name}", end=' ')
            count = count + 1
        print()

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
        return f" Count: {self.count}\n"
        
    
class Note():
    def __init__(self, name):
        # name is an instance variable
        self.name = name
        self.body = ""

    def SetBody(self, data):
        self.body = data

    def __repr__(self):
        return f" Name: {self.name}\n Body: {self.body}\n"

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
    activeList = NoteList()
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
