# -*- coding: utf-8 -*-

import sys
import random
import shlex

def isVar(x):
    for i in range(len(x)):
        if not (x[i:i+1].isalnum() or x[i]=='_'):
            return False
    return True

def getVar():
	res = ''
	for i in range(5):
		res += chr(random.choice([8237, 8238, 8236, 8235]))
	return res

if len(sys.argv) < 2:
    print("disturb.py <sourcefile>")
else:
    source_file_name = sys.argv[1].split(".")
    source_name = source_file_name[0]
    for i in range(1,len(source_file_name) - 1):
        source_name = source_name + "." + source_file_name[i]
    source_suffix = source_file_name[len(source_file_name) - 1]
    
    with open(sys.argv[1], "r", encoding="utf-8") as source_file:
        source = source_file.readlines()
        source_file.close()

    disturb = open(source_name+"disturb."+source_suffix, "w", encoding="utf-8")

    disturbname = {}
    st = {}

    for line in source:
        pos = line.find("//")
        if pos != -1:
            line=line[:pos]
        if len(line)>0 and line[0] != "#":
            lex = shlex.shlex(line)
            words = list(lex)
            for i in words:
                if isVar(i):
                    while True:
                        x = getVar()
                        if x not in st: break
                    disturbname[i] = x
                    st[x] = True
                else:
                    disturbname[i]=i
        else:
            disturbname[line]=line

    keys=[]
    
    for i in disturbname.keys():
        if i != disturbname[i]:
            keys.append(i)
                
    random.shuffle(keys)

    disturbname[keys[random.randint(0,len(keys)-1)]]="\u202E"

    disturb.write("//https://github.com/ouuan/Code-Disturber\n\n")

    for i in keys:
        disturb.write("#define " + disturbname[i] + " " + i + "\n")

    for line in source:
        pos = line.find("//")
        if pos != -1:
            line=line[:pos]
        if len(line)>0 and line[0] != "#":
            lex = shlex.shlex(line)
            words = list(lex)
            for i in words:
                disturb.write(disturbname[i])
                if i != disturbname[i]:
                    disturb.write(' ')
        else:
            disturb.write('\n')
            disturb.write(line)
