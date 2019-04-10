import json

out=[]

for i in range(0x4dc0,0x04dff):
    out.append(i)

with open("gua.json","w") as fil:
    fil.write(json.dumps(out))
