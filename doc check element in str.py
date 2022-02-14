# check wheather list element in string or not. question38 in doc-
list=[".com",".edu",".tv"]
string="https://www.w3resource.com/python-exercises/list/"
i=0
while i<len(list):
    if list[i] in string:
        print("true-",list[i])
    else:
        print("false")
    i+=1