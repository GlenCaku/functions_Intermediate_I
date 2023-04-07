x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)

#2. Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students)

#3. In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

#4. Change the value 20 in z to 30
z[0]['y'] = 30
print(z)



students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
 
    for dct in some_list:
        str = ""
        
        for key, value in dct.items():
            str += f"{key} - {value}, "
        print(str[:-2])


iterateDictionary(students)




def iterateDictionary2(key_name, some_list):
   
    for dct in some_list:
        print(dct[key_name])


students = [
  {'first_name': 'Michael', 'last_name': 'Jordan'},
  {'first_name': 'John', 'last_name': 'Rosales'},
  {'first_name': 'Mark', 'last_name': 'Guillen'},
  {'first_name': 'KB', 'last_name': 'Tonel'}
]


iterateDictionary2('first_name', students)

iterateDictionary2('last_name', students)





def printInfo(some_dict):
   
    for key in some_dict:
      
        print(f"{len(some_dict[key])} {key.upper()}")
      
        for value in some_dict[key]:
            print(value)


dojo = {
  'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
  'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)




