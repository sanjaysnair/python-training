import function_repeat_str

"""
This module will compile successfully even thoug we have called function 'repeeat' with typo
Only when it runs, it throws: NameError: name 'repeeat' is not defined
"""

name = input('Enter your company name: ')
if name == 'SG':
    print(repeeat(name)) # function name is called wrongly