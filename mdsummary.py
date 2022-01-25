#!/usr/bin/python3

import sys

def help(exitCode = 0):
    print ("Usage : ./script.py [path_to_file] (path_to_new_file)")
    print ("\nIf no path_to_new_file, path_to_file will be updated\n")
    exit(exitCode)

def find_title_level (msg):
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

def extract_all_titles(content):
    '''
    Allow to extract all content
    return a list of title. A value can be another list or a string
    '''
    titles = []
    for line in content:
        level, text = find_title_level(line)
        if level != 0:
            # need a refactor
            i = 2 # we don't count the main title
            result = text.split('\n ')[0] # there is '\n ' to the end
            while i < level:
                result = [result]
                i+=1
            titles.append(result) 
    
    return titles

####################################################
def main():
    '''Main fonction'''
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

    # Init result
    content_out = ""

    begin = 0 # We begin from line 0

    # We put the title if exists
    level, msg = find_title_level(content[0]) 
    if level == 1:
        content_out += '# ' + msg + "\n"
        begin = 1

    # While no new title, we suppose that it's description
    while (level == 0):
        content_out += content[begin]
        begin += 1
        level, msg = find_title_level(content[begin])

    # if summary already exists, we delete it, and we stop to new title
    if (level == 2 and msg == "Sommaire"):
        begin += 1
        level, msg = find_title_level(content[begin])
        while level == 0:
            begin += 1
            level, msg = find_title_level(content[begin])


    # We etablish the summary
    content_out += '## Sommaire\n\n'

    # We create a list of all titles
    titles = extract_all_titles(content[begin:])
    
    # And we write the summary
    for title in titles:
        text=title
        while type(text) != type(str()):
            content_out += "  "
            text=text[0]
        content_out += "- [" + text + '](#' + text.replace(' ','_') + ')\n'
    content_out += '\n'

    # We add the rest of the file
    for line in content[begin:]:
        level, msg = find_title_level(line)
        if level == 0:
            content_out += line
        else:
            msg_raw = msg.replace("\n ","")
            content_out += '<div id="' + msg_raw.replace(' ','_')
            content_out += '"><h' + str(level) + '>'
            content_out += msg_raw
            content_out += '</h' + str(level) + '></div>\n'

            # for i in range(level):
            #     content_out
            # content_out += line

    file_in.close()
    file_out = open(pathout,"w")
    file_out.write(content_out)
    file_out.close()

# If script is main, execute main
if __name__ == '__main__':
    main()