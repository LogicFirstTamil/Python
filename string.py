#method,function - performs a specified task
message = "happybirthday"
print(message * 10)
print(len(message))
print(message.find("#"))
print(message.count("a"))
print(message.replace("a", "r"))
print(message.isdigit())
name = 'Ram'
quote = '"peace"'
msg = message + name
print(quote)
print(name.upper()) #invoking a method
print(name.lower())
print(message.title())
print(message + " " + name)
print("hello \t world") #escape sequence

str_in = "white,green,blue,orange"
color_list = str_in.split(',')
print(color_list)

#delimit by ,
str_ip = "34,5,2,8,9"
num_list = []
next_num = True
str2 = ''
for i in str_ip:
    if next_num:
        str2 = ''
        next_num=False
    if i == ',':
        num_list.append(int(str2))
        next_num=True
        continue
    str2 += i
num_list.append(int(str2))
print(num_list)

split and join in strings
str_in = "abc def ghi jkl"
split_list = str_in.split(' ')
print(split_list)

str_joined = '-'.join(split_list)
print(str_joined)

























