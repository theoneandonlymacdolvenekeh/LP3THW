# this one is likw your scripts with argv
def print_two(*args):
    arg1, arg2, args
    print(f"arg1: {arg1}, arg2 {arg2}")
    
# ok, taht *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg: {arg1}, arg2: {arg2}")
    
# thid just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")
    
# this one takes no arguments
def print_none():
    print("I got nothin'.")
    
print_two("zed", "show")
print_two_again("zed", "show")
print_one("first")
print_mone()

