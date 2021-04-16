import glob


output = glob.glob('*.txt')

for file in output:

    new_file = file.split('.')[0] + "_1." + file.split('.')[-1] 

    f2 = open(new_file, "w")

    with open(file, "r") as f:
        buff = f.readline()

        while buff:

            if buff[0] == "-" :
                buff = buff[2:]
            #buff = buff.replace("{", "[").replace("}", "]")
            print(buff)
            f2.write(buff)
            buff = f.readline()
            
    f2.close()