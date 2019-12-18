import sys
import os





def create():

    print(sys.argv)
    #         Gets the file name  Gets the extension
    fileName = str(sys.argv[1]) + str(sys.argv[3])
    #Open fileName specified from above and open for writing and then close
    open(fileName, "a").close()
    #Opens the file name in atom
    os.system("atom " + fileName)
    



if __name__ == "__main__":
    create()
