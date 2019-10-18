import os
import sys

def runFiles( directoryPassed ):
    for filename in os.listdir(directoryPassed,):
            fullName = directoryPassed + "\\" + filename;
            if os.path.isfile(fullName):
                readfile = open(fullName, "r", encoding='UTF8', errors='ignore');
                for x in readfile.readlines():
                    if x.find(myText) >= 0:
                        print (fullName + " >> " + x[1:10]);
                        

if len(sys.argv) < 3:
    raise SyntaxError("Not enough arguments: searchText startDirectory findText");

if len(sys.argv) > 3:
    raise SyntaxError("Too many arguments provided: searchText startDirectory findText");


directoryStart = str(sys.argv[1])
myText = str(sys.argv[2])


for root, dirs, files in os.walk(directoryStart, topdown=False):
    if not dirs:
        runFiles(directoryStart);
    else:
        for name in dirs:
            directoryIn = os.path.join(root, name);
            runFiles(directoryIn);



                

        
        