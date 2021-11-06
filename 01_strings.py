my_str = str('Python is great!')            # using the str() class constructor

s1 = 'hello'
s2 = b'goodbye'
print(type(s1))					            # <class 'str'>
print(type(s2)) 					        # <class 'bytes'>
print(type(s1) is str)				        # True
print(isinstance(s1, str)) 		            # True
print(isinstance(s2, str))			        # False


s5 = 'Python is fun'
sl1 = s5[0:4]
print(sl1)


s6 = '{lang} is over {0:0.2f} {date} old.'.format(20, date='years', lang='Python')
print(s6)


# format() examples:
print('{:>8}'.format('101.55'))                 # right-justify in a field-width of 8
print('{:-^20}'.format('hello'))                # center in a field-width of 20


# example of using f-strings (Note: you must be using Py 3.6 or higher.  If you are not,
# comment the next 3 lines out).
name, age = 'Tom', 42
s = f'Hello {name}.  Ten years ago, you were \
{age - 10} years old.'
print(s)
