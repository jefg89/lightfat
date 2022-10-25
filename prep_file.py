import sys

filename = sys.argv[1]
f = open(filename, "r")
data = f.readlines()
f.close
f = open(filename[:-3]+ "log", "w")

cache = False
if (filename[-9:] == "cache.out"):
    cache = True

saved = []
if (cache):
    for line in data:
        fixed = line[25:34].replace('.', '')
        saved.append(int(fixed))
        f.write(str(int(fixed)) + '\n')
else:
    for line in data:
        fixed = line[72:75].replace(",", ".")
        print(fixed)
        saved.append(float(fixed))
        f.write(fixed + "\n")
