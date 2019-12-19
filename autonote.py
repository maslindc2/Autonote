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
        
        #Create the directory and change to it using specified folder name
        os.mkdir(folderName)
        os.chdir(folderName)
        createFile(folderName, fileName, extension)
        
    else:
        os.chdir(folderName)
        openFile(fileName)
        

def openFile(fileName):
    
    os.system("nano " + fileName)   

def lazyOpen(folderName):
    
    os.chdir(folderName)
    filelist = os.listdir(os.getcwd())
    filelist = filter(lambda x: not os.path.isdir(x), filelist)
    newest = max(filelist, key=lambda x: os.stat(x).st_mtime)
    
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

        #Prints out specified usage TODO delete this line in final version
        print(sys.argv)

    open(fileName, "a").close()

    #Opens the file name in atom
    os.system("nano " + fileName)
    



if __name__ == "__main__":
    
    if(len(sys.argv) == 4):
        checkFileAndFolder()
    elif (len(sys.argv) == 2):
        lazyOpen(sys.argv[1])
    
