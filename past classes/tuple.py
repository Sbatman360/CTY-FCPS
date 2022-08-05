people = [('Allen', 21, '123-45-6789', 'peaches', 30000), ('Beth', 36, '987-65-4321', 'oranges', 47000), ('Chuck', 13, '444-55-6666', 600, 'apples'), ('Darla', 47, '24-689-7531', 53000, 'pears'),('Edgar', 29, '000-88-4444', 38000, 'rocks')]
names = ['Allen', 'Beth', 'Chuck',  'Darla', 'Edgar']
ages = ['21','36', '13', '47', '29']
ids = ['123-45-6789', '987-65-4321', '444-55-6666', '24-689-7531', '000-88-4444']
salaries = [30000, 47000, 600, 53000, 38000]
fav_foods = ['peaches', 'oranges', 'apples', 'pears', 'rocks']
def print_data():
  for name, age, id, salary, fav_food in people:
    print (names + '(age'+str(age)+';id '+ id+')')
    print ('Favorite food:' + fav_food)
    print('Salary:' + str(salary))
    
print_data()