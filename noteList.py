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
