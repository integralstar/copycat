with open("201205.txt", "r", encoding="utf-8-sig") as f:
    buff = f.readlines()

buff = filter(lambda x: not x.isspace(), buff)

with open("201205-1.txt", "w+", encoding="utf-8-sig") as f2:
    f2.writelines(buff)
    f2.close()