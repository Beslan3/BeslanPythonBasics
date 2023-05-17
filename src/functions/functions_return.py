# chapter 8: The return statement takes a value
# from inside a function and sends it back to the line that called the function.
# Return values allow you to move much of your program’s grunt work into
# functions, which can simplify the body of your program.

# get data/info (getters): usually these kind of functions have return value, you can assign the function to a varialbe, treat as a value
# set data/info (setters): create/update data/infor in db,code, variable (applies logic in the functions)

def get_full_name(fistname: str, lastname: str, middlename: str = '') -> str:
    """
    Returns formatted full name
    :param fistname:
    :param lastname:
    :param middlename: this is optional parameter, default value is empty space
    :return:
    """
    if middlename != '':
        return f"{fistname} {middlename} {lastname}".title()
    else:
        return f"{fistname} {lastname}".title()


print("Executing the functions with Positional Arguments.")
print(get_full_name('john', 'doe'))  # third argument is optional
print(get_full_name('john', 'doe', 'brown'))
# arguments you pass are positional, which will be assigned to each parameter based on position you enter




def print_all_names(names):
    print("***** print_all_names **** ")
    for name in names:
        print(name)


