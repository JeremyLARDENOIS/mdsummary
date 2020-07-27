#!/usr/bin/python3

import sys

def help():
    print ("Usage : ./script.py [path_to_file]")

def title (msg):
    '''
    return tuple (size,title) or nothing if isn't a title
    '''

    title = ""
    tab = msg.split(" ")
    level = 0

    for char in tab[0]:
        if char != "#": 
            break
        level+=1


    for word in tab[1:]:
        title += word

    return (level,title)

####################################################

if len(sys.argv) > 2:
    help()
    exit(0)
elif len(sys.argv) == 2:
    path = sys.argv[1]
else:
    path = input("Chemin du fichier à traiter : ")

file_in = open(path, "r")
content = file_in.readlines()

file_out = open(file_in.name+" modified","w")
for line in content:
    file_out.write(line)


file_out.close()



file_in.close()
