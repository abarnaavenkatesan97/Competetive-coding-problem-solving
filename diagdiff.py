class mye(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)
try:
    print("h")
    raise mye("oops")
except mye as e:
    print("err",e)