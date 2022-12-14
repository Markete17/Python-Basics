# f = open("./DocumentoLeer.txt","w") # w=sobrescribir
# f = open("./DocumentoLeer.txt","a") # a=append
f = open("./DocumentoLeer2.txt","x") # x = crear
print(type(f))
f.write("This text has been updated\n")

f = open("./DocumentoLeer.txt") # open("./DocumentoLeer.txt","r") por defecto read
print(f.read())