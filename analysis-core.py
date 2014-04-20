__author__ = 'raymond'
import os
import magic
import hashlib
import re
DEBUG = 0
FILEDIR = '/Users/raymond/malware'
PROCESSEDFILEDIR = '/Users/raymond/complete'
def hashfile(tempfile):
#Purpose: hash a file
    #hachlblocksize limits how many bytes to read in at once
    hashblocksize = 81960
    #set the hashing algorithm to use
    hash = hashlib.sha1()
    #open the file to hash as stream
    filetohash = open(tempfile, 'rb')

    #hash the file
    while True:
        buffer = filetohash.read(hashblocksize)
        hash.update(buffer)
        if not buffer:
            hash_result = hash.hexdigest()
            break

    filetohash.close()
    return hash_result

def filepathcheck (directory):
    """

    :rtype :
    """
    if os.path.exists(directory):
        if DEBUGFLAG == 1:
            print("Path exists")
        if os.path.isdir(directory):
            if DEBUGFLAG == 1:
                print("Path is directory")
                return 'true';
        else:
             if DEBUGFLAG == 1:
                print("path is not a directory")
                return 'false'
    else:
         print("Path does not exist")
         return '1'
#Test if file path exists
try:
    filepathcheck(FILEDIR)
    filepathcheck(PROCESSEDFILEDIR)

except:
    print("Go ahead caller")

#walk through the directory and sub-directories specified in FILEDIR
for subdir, directories, filenames in os.walk(FILEDIR):
             for filename in filenames:
                    stringsInfile = "none"
                    #Create the full file path to pass into libmagic (via python-magic)
                    tempfile = os.path.join(subdir,filename)
                    filehash = hashfile(tempfile)
                    filetype = magic.from_file(tempfile)
                    filetypestring = filetype.decode(encoding='UTF-8')

                    #If the file is a executable run strings on it
                    if re.search("executable", filetypestring):
                        filetostring = open(tempfile, 'rb')
                        stringsInfile = filetostring.readline()
                        filetostring.close()

                    #output the detect filetype.
                    print("Filename:",tempfile)
                    print("File type: ",filetypestring)
                    print("Hash: ",filehash)
                    print("Strings: ", stringsInfile,'\n')
                    #to do:
                    #seen before?, submit to cuckoobox, VT

