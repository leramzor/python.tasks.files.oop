def convertstr(f):
    def f1(str):
        str1 = int(str)
        return f(str1)
    return f1

@convertstr
def finalfun(str):
   return str

print(finalfun('12545'))