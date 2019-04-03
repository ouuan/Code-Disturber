# -*- coding: utf-8 -*-

import sys
import random
import shlex
import json

def isVar(x):
    for i in range(len(x)):
        if not (x[i:i+1].isalnum() or x[i]=='_'):
            return False
    return True

def getVar():
    global characterset
    global repeat
    res = ''
    for i in range(repeat):
        res += chr(random.choice(characterset))
    return res

if len(sys.argv) < 3 or len(sys.argv) > 5:
    print("disturb.py <sourcefile> <characterset> [repeat=1 [RLO=1]]")
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

    global characterset
    with open(sys.argv[2], "r") as charaterset_file:
        characterset = json.load(charaterset_file)

    if len(sys.argv) > 3:
        repeat = int(sys.argv[3])
    else:
        repeat = 1

    if len(sys.argv) >4:
        RLO = int(sys.argv[4])
    else:
        RLO = 1
    
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

    if RLO > 0:
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
