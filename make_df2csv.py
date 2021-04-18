import pandas as pd

data = []

with open("E:\\AI\\slogan\\type2\\자동차.txt", "r", encoding="utf-8-sig") as f:
    buff = f.readline()

    while buff:
        tmp = []
        
        buff = buff.split("-")

        if buff[0]:
            buff[0] = buff[0].rstrip().lstrip()
            tmp.append(buff[0])
            print(buff[0])

        if len(buff) > 1:
            try:
                buff[1] = buff[1].rstrip().lstrip()
                tmp.append(buff[1])
                print(buff[1])
            except:
                print("buff1 error!")
        else:
            tmp.append("")

        data.append(tmp)
        buff = f.readline()

print("문장 수 : ", len(data))

# index 제거
df = pd.DataFrame(data, columns = ["copywrite", "product"])
df.to_excel("car.xlsx", header=True, index=False)

