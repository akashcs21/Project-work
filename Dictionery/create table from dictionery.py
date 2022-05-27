# creating table from dictionery
d={"Akash":[70,80,90,68,59],"Bhoomi":[70,80,90,68,59],"Anshika":[70,80,90,68,59],"Soumya":[70,80,90,68,59],"Neha":[70,80,90,68,59]}
for row in zip(*([k]+(v) for k,v in sorted(d.items()))):
    print(*row,sep="\t")
