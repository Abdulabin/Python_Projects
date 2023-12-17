# # # 1.Craeating Flames Game

Name1=input("User1 Enter Name ").lower()
Name2=input("User2 Enter Name ").lower()
Name2=Name2.replace(" ","")
Name1=Name1.replace(" ","")
# Removing Duplicates

for x in Name1:
    for y  in Name2:
        if x==y:
            Name1=Name1.replace(x,"")
            Name2=Name2.replace(y,"")
            break
total=len(Name1+Name2)

# Finding Relation
if total>0:
    Flames=["Friends","Lovers","Affectionate","Marriage","Enemies","Siblings"]
    while len(Flames)>1:
        c=total%len(Flames)
        count=c-1
        if count>=0:
            Ltrim=Flames[:count]
            Rtrim=Flames[count+1:]
            Flames=Rtrim+Ltrim
        else:
            Flames=Flames[:len(Flames)-1]
    print(f"The Relation is {Flames[0]}")
else:
    print("NO Relation ")

