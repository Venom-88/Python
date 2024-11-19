my_dict = {'Дмитрий':1988, 'Андрей':'1986'}
print(my_dict)
existing_value = my_dict['Дмитрий']
print(existing_value)
not_existing_value = my_dict.get('Виктор')
print(not_existing_value)

my_set = {
    'Vasya',
    (234, 123),
    99.99,
    79,
    97,
    79,
    97,
    97,
    97
}
print(my_set)
my_set.add(111)
my_set.add(3.14)
my_set.remove((234, 123))
print(my_set)