#if we don't pass an argument function will take default argument

def function1(name="USER"):
    print("hello "+name)

function1("sagar")
function1("nayan")
function1()
function1("dallu")