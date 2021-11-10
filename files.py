txt = "Which language do you like?"
with open('myfile.txt','a') as f:
    f.write(txt)
print(f.closed) #checks if file is closed and returns true or false


