#Q1
print("__________________________________________________________________________________________________________________________________________________________________")

s = 'qwerty'

print(s.replace('q', ''))
#if the q was capital it sholde be capital in the replace
print("__________________________________________________________________________________________________________________________________________________________________")

Q2

num = int(input("Enter a number: "))

flag = False

if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
    
    print("__________________________________________________________________________________________________________________________________________________________________")

#Q3

string = "qwerty";
    
print("Duplicate characters in a given string: ");  
for i in range(0, len(string)):  
    count = 1;  
    for j in range(i+1, len(string)):  
        if(string[i] == string[j] and string[i] != ' '):  
            count = count + 1;  
            string = string[:j] + '0' + string[j+1:];  
    
    if(count > 1 and string[i] != '0'):  
        print(string[i]," - ",count);
