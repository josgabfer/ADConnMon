import mmap
errors = ['Exception', 'Failed to sync!', "duck", 'ADSync CheckDiff error']

with open (r"C:\Users\dgonzal4\OneDrive - Cisco\Documents\Full-Stack\Full-Stack Django\Python\sample.txt", 'rb', 0) as file:
    s = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
    for error in errors:
        location = s.find(bytes(error, 'utf-8'))
        if location != -1:
            print ("yes", location)
            
        else:
            print("No")

    
            