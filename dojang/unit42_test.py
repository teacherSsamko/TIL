def html_tag(a):
    def wrapper(func):
        def processor():
            r = func()

            return f'<{a}>{r}</{a}>'
        return processor
    return wrapper

a, b = input().split()
 
@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello, world!'
 
print(hello())