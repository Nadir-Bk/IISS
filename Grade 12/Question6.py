# Consider a file, SPORT.DAT, containing records of the following structure: [SportName, TeamName, No_Players] 
# Write a function copyData(), that reads contents from the file SPORT.DAT and copies the records with Sport name as
# “Basket Ball” to the file named BASKET.DAT. The function should return the total number of records copied
# to the file BASKET.DAT.

import pickle
def copyData():
    copyrecord = []
    for i in records:
        if i[0] == "Basketball":
            copyrecord.append(i)
    with open("Basket.dat", 'wb+') as g:
        pickle.dump(copyrecord, g)
        g.seek(0)
        print(pickle.load(g))
        
with open("Sport.dat", 'wb+') as f:
    n = int(input("Enter No: of Records to input: "))
    records = []
    for i in range(n):
        SportName = input("Enter Sport Name: ")
        TeamName = input("Enter team Name: ")
        No_Players = int(input("Enter No: of Players: "))
        Data = [SportName, TeamName, No_Players]
        records.append(Data)
    pickle.dump(records, f)
    f.seek(0)
    print(pickle.load(f))
    copyData()