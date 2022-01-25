#!/usr/bin/python3

import sys

def help(exitCode = 0):
    print ("Usage : ./script.py [path_to_file] (path_to_new_file)")
    print ("\nIf no path_to_new_file, path_to_file will be updated\n")
    exit(exitCode)

def title (msg):
    '''
    return tuple (size,title) or (0,None) if isn't a title
    '''

    title = ""
    tab = msg.split(" ")
    level = 0

    for char in tab[0]:
        if char != "#": 
            break
        level+=1

    for word in tab[1:]:
        title += word + " "

    return (level,title)

####################################################
def main():
    '''Fonction principale'''
    # print(len(sys.argv))
    if (len(sys.argv) <= 1) or (len(sys.argv) > 3):
        print("Bad Usage\n")
        help(1)
    elif len(sys.argv) == 3:
        pathin = sys.argv[1]
        pathout = sys.argv[2]
    elif len(sys.argv) == 2:
        pathin = sys.argv[1]
        pathout = sys.argv[1]

    file_in = open(pathin, "r")
    # content is array of string where each string is a line
    content = file_in.readlines()

    #file_out = open("modified "+file_in.name,"w")
    content_out = ""

    begin = 0 #On commence a trier a partir de la ligne 0

    #On met le titre si il y en a un
    level, msg = title(content[0]) 

    if level == 1:
        #file_out.write('# ' + msg + "\n")
        content_out += '# ' + msg + "\n"
        begin = 1

    #Tant que l'on a pas de titre, on suppose que cela fait partie de la description
    while (level != 2):
        content_out += content[begin]
        begin += 1
        level, msg = title(content[begin])

    #Si il y a déjà un sommaire, on le supprime
    level, msg = title(content[2])
    if (level == 2 and msg == "Sommaire"):
        begin = 3
        level, msg = title(content[begin])
        while level != 2:
            begin += 1
            level, msg = title(content[begin])


    #On etabli le sommaire
    #file_out.write('## Sommaire\n')
    content_out += '## Sommaire\n'
    numline = begin

    while numline < len(content):
        #print(content[numline], title(content)[0])
        if content[numline][0] == '#':
            level, msg = title(content[numline]) 
            #file_out.write("\n")
            content_out += "\n"
            for i in range(2,level):
                #file_out.write("  ")
                content_out += "  "
            #file_out.write('- ' + msg )
            content_out += "- " + msg
        numline += 1
    content_out += "\n"

    #On rajoute la suite
    for line in content[begin:]:
        #file_out.write(line)
        content_out += line

    file_in.close()
    file_out = open(pathout,"w")
    file_out.write(content_out)
    file_out.close()

# if script is main
if __name__ == '__main__':
    main()