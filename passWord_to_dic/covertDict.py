import json
userinfo = dict()
with open('test.txt',mode="r") as f:
    for line in f:
        (key,value) = line.strip().split(':')
        userinfo[key] = value

# with open('res.txt',mode="w") as fr:
#     fr.write(str(userinfo))

# for key,value in userinfo.items():
#     print(key+" "+value)

out_file = open('userinfo.json','w')
json.dump(userinfo,out_file,indent=4,sort_keys=False)
out_file.close()

with open('userinfo.json','r') as f:
    data = json.load(f)

print(data)