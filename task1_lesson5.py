def validation_int(func):
    def validation(*a):
        l = (int(i) for i in a)
        # l = (float(i) for i in a) for def validation_float(func)
        func(*l)
        print('hello')
    return validation

def validation_str(func):
    def validation(*a):
        l = (str(i) for i in a)
        func(*l)
        print('hello')
    return validation

def validation_list(func):
    def validation(*a):
        l = (list(i) for i in a)
        # l = (tuple(i) for i in a) for def validation_tuple(func)
        func(*a)
        print('hello')
    return validation

@validation_int
def data(*x):
    print(f'My data {x}')
   
data(356.678, 345)

