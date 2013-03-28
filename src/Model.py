data_file = open('data.txt', 'r')
data_file2 = data_file.read()
data_file2 = data_file2.split("\n")
data_file.close()

num_lines = len([l for l in data_file2 if l.strip(' \n') != ''])

i = 0
subject = [] 
tag = []
group = []
student = []

while i < num_lines:
    if data_file2[i] == "<subject>":
        subject.append([data_file2[i+1],data_file2[i+2],data_file2[i+3]])
        i=i+1
    elif data_file2[i] == "<tag>":
        tag.append([data_file2[i+1],data_file2[i+2]])
        i=i+1
    elif data_file2[i] == "<group>":
        group.append([data_file2[i+1]])
        i=i+1
    elif data_file2[i] == "<student>":
        student.append([data_file2[i+1],data_file2[i+2]])
        i=i+1
    else:
        i=i+1
print(subject)
print("---------------------------------------------------")
print(tag)
print("---------------------------------------------------")
print(group)
print("---------------------------------------------------")
print(student)
print("---------------------------------------------------")  
