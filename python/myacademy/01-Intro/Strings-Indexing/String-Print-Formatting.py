my_name = "Sathyavelrajan"
print("My name is " + my_name)

# formatting using .format() method
# String can be inserted based on their indices
my_last_name = "Avudaiappan"
print("My name is {}".format(my_last_name))
my_frn_name = "Prabha"
# Key word arguments
print("My name is {}, and my friend's name is {}".format(my_name, my_frn_name))
print("My name is {0}  {1}, and my friends name is {2}".format(my_name,my_last_name, my_frn_name))
print("My name is {1} {1}, and my friends name is {1}".format(my_name,my_last_name, my_frn_name))
print("My name is {fn} {zn} and my friend's name is {frn})".format(fn="Raj", zn="A", frn="Prabha"))
