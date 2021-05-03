#!/usr/bin/python3

import sys

def help():
    print ("Usage : ./script.py [path_to_file] (path_to_new_file)")
    print ("If no path_to_new_file, path_to_new_file = path_to_file")
    exit(0)

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
        title += word + " "

    return (level,title)

####################################################
def main():
  '''Fonction principale'''
  if 1 > len(sys.argv) > 3:
      help()
  elif len(sys.argv) == 3:
    pathin = sys.argv[1]
    pathout = sys.argv[2]
  elif len(sys.argv) == 2:
      pathin = sys.argv[1]
      pathout = sys.argv[1]
      
  file_in = open(pathin, "r")
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

#Si il y a déjà un sommaire, on le supprime
  level, msg = title(content[2])
  if (level == 2 and msg == "Sommaire\n "):
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


  #On rajoute la suite
  for line in content[begin:]:
      #file_out.write(line)
      content_out += line

  
  file_in.close()
  file_out = open(pathout,"w")
  file_out.write(content_out)
  file_out.close()


main()
