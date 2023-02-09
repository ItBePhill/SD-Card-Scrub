import os
import shutil
destdir = "C:/Users/phill/Desktop/desmume-win-x64/Roms"
filearray = os.listdir("E:/")
ndsarray = []
savarray = []
for i in filearray:
    if os.path.splitext(i)[1] == ".ndss":
        ndsarray.append(i)
    if os.path.splitext(i)[1] == ".sav":
        savarray.append(i)
for i in ndsarray:
    #shutil.copyfile(os.path.abspath(os.path.join("E:/", i)),os.path.join(destdir, i))
    #print(str(len(os.listdir(destdir)))+ "/" +str(len(ndsarray)))
    print(os.path.splitext(i)[0])
    