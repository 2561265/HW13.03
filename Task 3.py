class_list = open('class_list.txt' , 'r+')
key_base = ['First name', 'Last name', 'Gender', 'Age']
student_info = []
student = class_list.readline()
student_list = student.split()
class_list.seek(0)
student_base = {}
stud = {}
count = 1

while True:
    if student_list == []:
         break
    student = class_list.readline()
    student_list = student.split()
    student_info.append(student_list)
student_info = list(filter(None, student_info))

for x in range(len(student_info)):
    stud[count] = dict(zip(key_base, student_info[x]))
    student_base.update(stud)
    count += 1

for stud_number, stud_info in stud.items():
    print('\nStudent number - ' + str(stud_number) + ':')
    full_name = stud_info['First name'] + ' ' + stud_info['Last name']
    gender = stud_info['Gender']
    age = stud_info['Age']
    print('\tFull name: ' + full_name.title())
    print('\tStudent gender: ' + gender.title())
    print('\tStudent age: ' + str(age))