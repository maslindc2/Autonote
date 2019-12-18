import sys
import os


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
    folderName = str(sys.argv[1])
    fileName = str(sys.argv[2]) + str(sys.argv[3])
    if(os.path.isdir(folderName)):
        #os.mkdir(folderName)
        os.chdir(folderName)
        if not (os.path.isfile(fileName)):
            createFile()
   
def createFile():
    extension = str(sys.argv[3])
    fileName = str(sys.argv[2])
    folderName = str(sys.argv[1])

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

    
    fileName += extension

    open(fileName, "a").close()

    #Opens the file name in atom
    os.system("nano " + fileName)
    



if __name__ == "__main__":
    checkFileAndFolder()
