
class tag:
    def __init__(self, id, name, text):
        self.id = id
        self.name = name
        self.text = text

class subject:
    def __init__(self, id, name, shortcut, year):
        self.id = id
        self.name = name
        self.shortcut = shortcut
        self.year = year

class group:
    def __init__(self, id, group):
        self.id = id
        self.group = group
        
class student:
    def __init__(self, id, name, student_id):
        self.id = id
        self.name = name
        self.student_id = student_id
        
data_file = open('data.txt', 'r')
data_file2 = data_file.read()
data_file2 = data_file2.split("\n")
data_file.close()

num_lines = len([l for l in data_file2 if l.strip(' \n') != ''])

i = 0
tag_list = []
tag_number = 0
subject_list = [] 
subject_number = 0
group_list = []
group_number = 0
student_list = []
student_number = 0

while i < num_lines:
    if data_file2[i] == "<subject>":
        flag = i
        while data_file2[flag] != "</subject>":
            if data_file2[flag][0:6] == "<name>":
                subject_name = data_file2[flag][6:-7]
                flag = flag+1
            elif data_file2[flag][0:10] == "<shortcut>":
                subject_shortcut = data_file2[flag][10:-11]
                flag = flag+1
            elif data_file2[flag][0:6] == "<year>":
                subject_year = data_file2[flag][6:-7]
                flag = flag+1
            else:
                flag = flag+1
        subject_list.append(subject(subject_number, subject_name, subject_shortcut, subject_year))
        i = i+1
        subject_number = subject_number+1
    elif data_file2[i] == "<tag>":
        flag = i
        while data_file2[flag] != "</tag>":
            if data_file2[flag][0:6] == "<name>":
                tag_name = data_file2[flag][6:-7]
                flag = flag+1    
            elif data_file2[flag][0:6] == "<text>":
                tag_text = data_file2[flag][6:-7]
                flag = flag+1
            else:    
                flag = flag+1
        tag_list.append(tag(tag_number, tag_name, tag_text))
        i = i+1
        tag_number = tag_number+1
    elif data_file2[i][0:7] == "<group>":
        group_group = data_file2[i][7:-8]
        group_list.append(group(group_number, group_group))
        i = i+1
        group_number = group_number+1
    elif data_file2[i] == "<student>":
        flag = i
        while data_file2[flag] != "</student>":
            if data_file2[flag][0:6] == "<name>":
                student_name = data_file2[flag][6:-7]
                flag = flag+1    
            elif data_file2[flag][0:4] == "<id>":
                student_student_id = data_file2[flag][4:-5]
                flag = flag+1
            else:    
                flag = flag+1
        student_list.append(student(student_number, student_name, student_student_id))
        i = i+1
        student_number = student_number+1
    else:
        i = i+1
        

print(subject_list[0].name, subject_list[0].shortcut, subject_list[0].year)
print(student_list[1].name, student_list[1].student_id)
