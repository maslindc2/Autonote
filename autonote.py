import sys
import os
import glob


python = ".py"
text = ".txt"
java = ".java"



extensions = {
    "python" : python,
    ".py" : python,
    "text" : text,
    ".txt" : text,
    "java" : java
}

def checkFileAndFolder():

    extension = str(sys.argv[3])
    fileName = str(sys.argv[2]) + str(sys.argv[3])
    folderName = str(sys.argv[1])
    
    if not (os.path.isdir(folderName)):
        
        # Create the directory and change to it using specified folder name
        os.mkdir(folderName)
        os.chdir(folderName)

        # Calls the createFile function
        createFile(folderName, fileName, extension)
        
    else:
        os.chdir(folderName)
        openFile(fileName)
        

def openFile(fileName):
    
    os.system("nano " + fileName)

def lazyOpen(folderName):
    
    # Function to open an already made folder and the last modifed file
    os.chdir(folderName)
    filelist = os.listdir(os.getcwd())
    filelist = filter(lambda x: not os.path.isdir(x), filelist)
    newest = max(filelist, key=lambda x: os.stat(x).st_mtime)
    
    # Opens the newest file in nano
    os.system("nano " + newest)
    

def createFile(folderName, fileName, extension):
    

    # Checks to see if the specified file type is in our dictionary of extensions
    # If it isn't then let the user know and default it to a txt file
    try:
        extension = extensions[extension]
    except Exception:
        print(extension + " is an unknown extension")
        print("I have changed it to a txt file")
        extension = ".txt"    

    # Creates a new filename
    open(fileName, "a").close()
    # Opens the file name in atom
    os.system("nano " + fileName)
    



if __name__ == "__main__":
    
    #Decides which method to call based on the length of the given command
    
    # File creation command has a length of 4 so it calls checkFileAndFolder function
    if(len(sys.argv) == 4):
        checkFileAndFolder()

    # If the length is 2 then the user's command should be ane folder_name
    elif(len(sys.argv) == 2):
        
        # gets the folder name that the user specified
        folderName = sys.argv[1]

        #try to call lazyOpen if it fails due to the folder not existing if an error happens print the error message
        try:
            lazyOpen(folderName)
        except OSError:

            print("The folder has not been created yet please run the below command")
            print("ane " + folderName +" name_of_file .extension_name ")
    else:
        print("Incorrect syntax")
        print("To create a new note and folder use the below command")
        print("ane name_of_folder name_of_file .extension_name")
        
    
