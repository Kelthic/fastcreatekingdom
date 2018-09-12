import time 
id_culture = " "
id_faction = " "
name_faction = " "
f = open('created_faction.py', 'w') 
id_culture = input("Укажите номер вашей культуры: (7\8\9 и т.д) \n")
f.write('  "culture_')
f.write(id_culture)
f.write('", ')
f.write('"{!}culture_')
f.write(id_culture)
f.write('", 0, 0.9, [], []),')
f.write("\n \n Вставьте это ниже чем: culture_6 \n \n")
print("Идёт коррекция файла, подождите.")
time.sleep(2)
f.write('("kingdom_')
f.write(id_culture)
f.write('",  "')
name_faction = input("Укажите имя вашего королевства на английском языке \n")
f.write(name_faction)
f.write('", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xEE7744),')
f.write(" \n \n Вставьте это ниже чем: kingdom_6")
f.close()
time.sleep(1)
print("Великолепно! Вся информация находится в created_faction.py")


 




