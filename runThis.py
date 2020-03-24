import glob, os, os.path, time
os.chdir("C:\\Users\\guvin\\Desktop\\pythonDrill\\")
for file in glob.glob("*.txt"):
    print(file)
    print("last modified: %s" % time.ctime(os.path.getmtime(file)))
    print("created: %s" % time.ctime(os.path.getctime(file)))
