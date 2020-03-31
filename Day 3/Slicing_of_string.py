"""
SYNTAX :
            x = any string
            print( x[ starting index : ending index])
                        (included)       (not included)

"""
       #123456789.......   positive indexing
name = "Sagar Chodavadiya"
       #          ....-2-1 negative indexing

print("only starting index name[2:]")
print(name[2:])
print()

print("only ending index name[:4]")
print(name[:4])
print()

print("using Both index name[2:8]")
print(name[2:8])
print()

print("without pass any index name[:]")
print(name[:])
