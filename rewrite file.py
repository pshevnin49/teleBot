citys = open("citys.txt", 'r', encoding='utf8')
new_list = []
for line in citys:
    string = line.lower()
    string = string.title()
    new_list.append(string)
citys.close()
print(new_list)

new_citys = open("citys.txt", 'w', encoding='utf8')
for element in new_list:
    new_citys.write(element)
new_citys.close()