import random, sys

textOut=str("")

#people:number

dct_name = {}
sfile = open("sfile.txt", "r")
sfile_name_number = int(sfile.readline())
for i in range(sfile_name_number):
    name_get = sfile.readline().split("\n")
    name = name_get[0]
    number = random.randint(1, 10000)
    dct_name.update({name:number})
sfile.close()

#number:name

dct_index = {}
sfileIndex = open("sfile.txt", "r")
sfile_name_number_index = int(sfileIndex.readline())
for i in range(sfile_name_number_index):
    name_get = sfileIndex.readline().split("\n")
    name = name_get[0]
    dct_index.update({dct_name[name]:name})
sfileIndex.close()



#lowers the score of some people

# for _ in range(1, len(dct_name)):
#     if dct_index[dct_name["Jakub"]] == "Jakub":
#         lower_val = dct_name["Jakub"] * 0.76
#         dct_name.update({"Jakub":lower_val})
#     elif dct_index[dct_name["Dano"]] == "Dano":
#         lower_val = dct_name["Dano"] * 0.76


#main definition

def Roll():
    wwchd = 0
    for name in dct_name:
        if int(dct_name[name]) > wwchd:
            wwchd = int(dct_name[name])
        elif int(dct_name[name]) <= wwchd:
            pass
    str(wwchd)
    winner = dct_index.get(wwchd)
    textOut = "Dnes pôjde odpovedať " + winner + ", veľa štastia!"


#bottom definitions(add people, remove people)
"""
def AddPeople():
    name = entry1.get()
    num = random.randint(1, 10000)
    dct_name.update({name:num})

def Exit():
    sys.Exit(0)

def RemPerson():
    name = entry1.get()
    dct_name.pop(name)
"""


Roll()
