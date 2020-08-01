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
        title += word + " "

    return (level,title)

####################################################
def main():
  if len(sys.argv) > 2:
      help()
      exit(0)
  elif len(sys.argv) == 2:
      path = sys.argv[1]
  else:
      path = input("Chemin du fichier à traiter : ")

  file_in = open(path, "r")
  content = file_in.readlines()

  file_out = open("modified "+file_in.name,"w")

  begin = 0 #On commence a trier a partir de la ligne 0

  #On met le titre si il y en a un
  level, msg = title(content[0]) 

  if level == 1:
      file_out.write('# ' + msg + "\n")
      begin = 1


  #On etabli le sommaire
  file_out.write('## Sommaire\n')
  numline = begin
  while numline < len(content):
      if content[numline][0] == '#':
          level, msg = title(content[numline]) 
          file_out.write("\n")
          for i in range(2,level):
              file_out.write("  ")
          file_out.write('- ' + msg )
      numline += 1


  #On rajoute la suite
  for line in content[begin:]:
      file_out.write(line)


  file_out.close()
  file_in.close()

main()