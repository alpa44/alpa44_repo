class DecoratorClass:
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('{} 함수가 호출되기전 입니다'
                .format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

@DecoratorClass
def display():
    print('display 함수가 실행됐습니다.')

@DecoratorClass
def display_info(name, age):
    print('display_info({},{}) 함수가 실행됐습니다.'.format(name, age))

display()
print
display_info('John', 25)
