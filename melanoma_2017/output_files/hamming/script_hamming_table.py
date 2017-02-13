def hammdist2(str1, str2):
    return sum(a != b for (a,b) in zip(str1, str2))

TRB_cdr3_aa = []
with open("melanoma.txt", "r") as f:
    next(f)
    for line in f.readlines():
        line_split = line.split("\t")
        if line.find("TRB")!= -1:
            cdr3_aa = line_split[6]
            TRB_cdr3_aa.append(cdr3_aa)

hamming_table = open("hamming_table_out.txt", "w")


for i,x in enumerate(TRB_cdr3_aa):
    for j,y in enumerate(TRB_cdr3_aa):
        if i != j:
            if len(x) == len(y):
                if hammdist2(x, y) <= 3:
                    string = x+"\t"+y+"\t"+str(hammdist2(x, y))+"\n"
                    hamming_table.write(string)
