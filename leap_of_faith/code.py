# --------------
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']
new_class = (class_1 + class_2)
print(new_class)

# Append the list
new_class.append('Peter Warden')
print(new_class)
new_class.remove('Carla Gentry')
print(new_class)



# --------------
# Code starts here



# Code ends here
courses= {'Math' : 65,'English' : 70,'History': 80,'French': 70,'Science': 60}
math = courses['Math']
english = courses['English']
history = courses['History']
french = courses['French']
science = courses['Science']
total=math+english+history+french+science 
print(total)
percentage =(total * 100/500)
print(percentage)


# --------------
# Code starts here





# Code ends here  
mathematics = {'Geoffrey Hinton' : 78,'Andrew Ng' : 95,'Sebastian Raschka' :65,'Yoshua Benjio' :50,'Hilary mason' :70,'Corinna Cortes' :66,'Peter Warden' :75}

max_marks_scored = max(mathematics,key = mathematics.get)
print(max_marks_scored)
topper = max_marks_scored




# --------------
# Given string
topper = 'andrew ng'
first_name = (topper.split()[0])
print(first_name)
last_name = (topper.split()[1])
print(last_name)
full_name = last_name + ' ' + first_name
print(full_name)

certificate_name = full_name.upper()
print(certificate_name)



