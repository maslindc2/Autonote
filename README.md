# Autonote
*Python note automation, to make note taking less painful*
## What is this
This is a simple python and shell script used to automatically create a new folder and text document. Once the folder and file has been created, it will then open the file in your text editor of choice.

## Useage
To use Autonote, and create a new folder and file run the below command in your terminal

*ane Folder_name name_of_file .extension_name*

Folder_name is the name of the folder you would like to store your new note in.

name_of_file is the name of your new file

.extension_name is your file type

### Acceptable file types are the following
.txt for text

.java for java

.python for python

## Installation
Unforutunately installing Autonote isn't the most elegant.  Works with WSL running bash or fish shells.

### Fish Shell
1. Create a function inside of your config.fish
    ```
    function ane
      cd Documents/
      python autonote.py $argv
    end
    ```
2. To set this up to your need change the line cd Documents/ to where you want to have your notes created and stored
3. Store autonote.py inside the directory we are going to cd into. For this example I want my notes to be stored inside of Documents. So I will be placing autonote.py inside the Documents folder. 

### Bash Shell
1. Create a function inside of your bashrc file.
    ```
    function ane(){
      cd Documents/
      python autonote.py $1 $2 $3
    }
2. To set this up to your need change the line cd Documents/ to where you want to have your notes created and stored
3. Store autonote.py inside the directory we are going to cd into. For this example I want my notes to be stored inside of Documents. So I will be placing autonote.py inside the Documents folder. 
