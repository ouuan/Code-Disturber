# -*- coding: utf-8 -*-

import sys
import random
import shlex

def isVar(x):
    for i in range(len(x)):
        if not (x[i:i+1].isalnum() or x[i]=='_'):
            return False
    return True

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
        if line[0] != "#":
            lex = shlex.shlex(line)
            words = list(lex)
            for i in words:
                if isVar(i):
                    x = random.randint(19968,40869)
                    while x in st:
                        x = random.randint(19968,40869)
                    disturbname[i] = chr(x)
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

    for i in keys:
        disturb.write("#define " + disturbname[i] + " " + i + "\n")

    for line in source:
        if line[0] != "#":
            lex = shlex.shlex(line)
            words = list(lex)
            for i in words:
                disturb.write(disturbname[i])
                if i != disturbname[i]:
                    disturb.write(' ')
        else:
            disturb.write('\n')
            disturb.write(line)
