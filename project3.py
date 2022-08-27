import json
with open("task2.json","r") as f:
    year=json.load(f)
    def group_by_year():
        y=1950
        dic={}
        for i in range(1950,2022,10):
            b=[]
            for j in year:
                if y<int(j)and int(j)<(y+10):
                    b.append(year[j])
            dic[y]=b
            y+=10
            with open("task3.json","w") as f1:
                json.dump(dic,f1,indent=4)
    group_by_year()

















    