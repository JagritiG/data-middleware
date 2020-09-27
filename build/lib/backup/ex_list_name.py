from varname import nameof

my_list = [1, 2]
# my_var_name = [k for k,v in locals().items() if v == my_list][0]
# print(my_var_name)

print(nameof(my_list))
