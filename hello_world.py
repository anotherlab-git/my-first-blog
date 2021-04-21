#これは文法確認です。
def hello(name):
    if name == 'jango':
       print("I'm jango")
    elif name == 'django':
        print("Hello, Django girls!")
    else:
        print('Oops! who are you!')

#hello('django')
#hello('jango')
#hello('ango')

def repHi(name):
    print('Hi ' + name)

boys = ['kan', 'wata', 'go']
for name in boys:
    repHi(name)
    print('Next!')

