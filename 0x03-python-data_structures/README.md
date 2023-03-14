<h1>0x03. Python - Data Structures: Lists, Tuples Task description
   </h1>

<h5>0. Print a list of integers
   
#!/usr/bin/python3

def print_list_integer(my_list=[]):
    
for i in range(len(my_list)):
        
print("{:d}".format(my_list[i]))</h5>

...................................................

<h5>1. Secure access to an element in a list

#!/usr/bin/python3

def element_at(my_list, idx):
    
if idx < 0 or idx > len(my_list) - 1:
        
return 'None'
    
else:
        
return my_list[idx]

................................................


2. Replace element 
..................................................

#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    
if idx < 0 or idx > len(my_list) - 1:
        
return my_list
    
else:
        
my_list[idx] = element
        
return my_list

........................................................


3. Print a list of integers... in reverse! 
.....................................................

#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    
if my_list:
        
my_list.reverse()
        
for i in range(len(my_list)):
            
print("{:d}".format(my_list[i]))
........................................................ii.i:
