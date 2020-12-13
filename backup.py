import os      #import OS module
import zipfile #import zipfile module
import shutil #import shutil module to copy files from one location to another

#Define how we copy the folders/files for zip compression
#By utilizing the ZipFile class for reading and writing zip files
def zip_compression(home_folder, main_zip):
    readyzip = zipfile.ZipFile(r"C:\Users\User\Desktop\Project\backup_Homefolder\Backup.7z", 'w')
    readyzip.extractall(r"C:\Users\User\Desktop\Project")
    for folders, subfolders, files in os.walk(home_folder):
        for file in files:
            print (os.path.join(folders, file))
            readyzip.write(os.path.join(folders, file))

    readyzip.close()

    #Display the locatoin of where the compressed will be located
    print ("Create!", main_zip)

#How to Copy the files to your targeted folder
def copy(home_folder, targeted_folder):
    for subdir, dirs, files in os.walk(home_folder):
        for file in files:
            print (os.path.join(subdir, file))
            shutil.copy(os.path.join(subdir, file), targeted_folder)

if __name__=='__main__':
    print ('Starting Compressoin')

    #Compressing the file you choose
    home_folder = (r"C:\Users\User\Desktop\Project\backup_Homefolder")
    main_zip = (r"C:\Users\User\Desktop\Project")
    zip_compression(home_folder, main_zip)

    #Send the copy to backup folder!
    home_folder = (r"C:\Users\User\Desktop\Project\Home_Folder")
    targeted_folder =  (r"C:\Users\User\Downloads")
    copy(home_folder, targeted_folder)

    print('Complete!')
