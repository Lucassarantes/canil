import json
from datetime import datetime
from canil.registers.models import Owner

animal_data = []
animals = []

with open('canil/utils/teste.txt', "r") as file:
    for line in file:
        data = line.split("- ")
        animal_data.append(data)
    
    for line in animal_data:
        dictionary = {}

        new_line = line[1].split(",")
        new_timestamp = (line[0].split("]"))
        # converted_date = datetime.strptime(str(new_timestamp[0]).replace("[", ""), '%Y-%m-%d %H:%M:%S')
        # print(converted_date)
        #print(new_line)
        #dictionary['id'] = 1
        dictionary['registered_at'] = str(new_timestamp[0]).replace("[", "")
        for value in range(0, len(new_line)):
            key_value = new_line[value].split(":")
            if key_value[0].lstrip() == 'Animal_age':
                dictionary['age'] = int(key_value[1].lstrip().replace("\n", "").replace(" years", "").replace(" year", ""))
            elif key_value[0].lstrip() == 'Sex_of_animal':
                dictionary['gender'] = key_value[1].lstrip().replace("\n", "")[0]
            elif key_value[0].lstrip() == 'Animal_condition':
                dictionary['status'] = key_value[1].lstrip().replace("\n", "")
            elif key_value[0].lstrip() == 'Size_of_animal':
                dictionary['size'] = key_value[1].lstrip().replace("\n", "")[0]
            elif key_value[0].lstrip() == 'Human_Owner':
                owner, created = Owner.objects.get_or_create(name = row["owner"],
                    phone='123456789',
                    email='owner@example.com',
                    cpf='12345678901',
                    zip='12345678',
                    address='123 Main St',
                    city='São Paulo',
                    state='SP'
                )
                dictionary['owner'] = owner
                #dictionary['owner'] = key_value[1].lstrip().replace("\n", "")
            elif key_value[0].lstrip() == 'Name':
                dictionary['name'] = key_value[1].lstrip().replace("\n", "")
            elif key_value[0].lstrip() == 'Breed':
                dictionary['breed'] = key_value[1].lstrip().replace("\n", "")
            elif key_value[0].lstrip() == 'Animal_type':
                dictionary['animal_type'] = key_value[1].lstrip().replace("\n", "")[0]
            else:
                dictionary[key_value[0].lstrip()] = key_value[1].lstrip().replace("\n", "")
            # end if
            
        animals.append(dictionary)
        print("")
        #print("Array ", animals)

#print(animal_data)

with open("animals.output.json", "w") as json_file:
    json.dump(animals, json_file, sort_keys = True, indent = 4)

# for animal in animals:
#     print(animal)
#print(animals)