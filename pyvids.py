#This script is used to help organize my two security camera's files
import shutil
import time
import zipfile
import datetime
import os

#initialize date
now = datetime.datetime.now()
date = now.strftime('%m-%d-%y')


print '-'*15
print 'creating archive'

#creates zipfile object and folder where files are to be store
zf = zipfile.ZipFile('/mnt/0AF4ABD23479F169/FILES/Motion/'+date+'_Lvideos.zip','w', allowZip64=True)

print '-'*15
print '\nadding LRoom'

#"walks" though the Living room camera's folder adding/printing each of the files
for folder, subfolder, files in os.walk('/mnt/0AF4ABD23479F169/FILES/Motion/Active_vids/LRoom'):
    for file in files:
        if file.endswith('.mp4'):
            zf.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), '/mnt/0AF4ABD23479F1691/FILES/Motion/Active_vids'), compress_type = zipfile.ZIP_DEFLATED)
            print file

zf.close()

print '\n\nL-room Complete'

#creates zipfile object (again) and folder where files are to be store
zf = zipfile.ZipFile('/mnt/0AF4ABD23479F169/FILES/Motion/'+date+'_Gvideos.zip','w', allowZip64=True)

print '-'*15
print '\nadding Garage'

#"walks" though the Garage camera's folder adding/printing each of the files
for folder, subfolder, files in os.walk('/mnt/0AF4ABD23479F169/FILES/Motion/Active_vids/Garage'):
    for file in files:
        if file.endswith('.mp4'):
            zf.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), '/mnt/0AF4ABD23479F1691/FILES/Motion/Active_vids'), compress_type = zipfile.ZIP_DEFLATED)
            print file

zf.close()

print '\n\nGarage Complete'
print '-'*15

print 'done'
print '-'*15
