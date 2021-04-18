import glob
from tqdm import tqdm
file_list = []

file_list = glob.glob("*.txt")

for x in tqdm(file_list):
    with open(x, "r", encoding="utf-8-sig") as f:
        buff = f.readline()

        with open("E:\\AI\\GPT2\\slogan\\type2\\total.txt", "a", encoding="utf-8-sig") as f2:

            while buff:
                tmp = []
                
                buff = buff.split("-")       

                if buff[0]:
                    buff[0] = buff[0].rstrip().lstrip()
                    f2.write(buff[0] + "\n")
                    #print(buff[0])

                buff = f.readline()
