mydict={
    "engg mechanics"  : "beginner",
    "solid mechanics" : "moderate",
    "fluid mechanics" : "difficult"
}
mydict["fluid mechanics"]= "not so tough"
mydict["theory of machines"]= "so tough"
mydict["machine design"]= "ok"
print(mydict)
del mydict["solid mechanics"]
del mydict["engg mechanics"]
print(mydict)

