import os 
import time
import shutil

def main():
    path = "/Users/sj/Desktop/hello"
    days = 1

    seconds = time.time()-(days*24*60*60)

    deletedfolderscount = 0
    deltedfilescount = 0

    if os.path.exists(path):
        for rootfolder, folders, files in os.walk(path):
            if seconds>=getFileOrFolderTime(rootfolder):
                removeFolder(rootfolder)
                deletedfolderscount = deletedfolderscount+1
                break
            else:
                for folder in folders:
                    folderpath = os.path.join(rootfolder, folder)
                    if seconds>=getFileOrFolderTime(folderpath):
                        removeFolder(folderpath)
                        deletedfolderscount = deletedfolderscount+1
                for file in files:
                    filepath = os.path.join(rootfolder, file)
                    if seconds>=getFileOrFolderTime(filepath):
                        removeFile(filepath)
                        deltedfilescount = deltedfilescount+1
        else:
            if seconds>=getFileOrFolderTime(path):
                removeFile(path)
                deltedfilescount = deltedfilescount+1
    else:
        print('"{path}" not found, please try again')
        deltedfilescount = deltedfilescount+1

    print('Total files deleted:')
    print(deltedfilescount)
    print('Total folders deleted')
    print(deletedfolderscount)

def removeFolder(path):
    if not shutil.rmtree(path):
        print("{path} is removed succesfully")
    else:
        print('Unable to delete the'+path)

def removeFile(path):
    if not os.remove(path):
        print("{path} is removed successfully")
    else:
        print('Unable to delete the '+path)

def getFileOrFolderTime(path):
    ctime = os.stat(path).st_ctime
    return ctime

if __name__ == '__main__':
    main()
