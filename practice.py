def make_pretty():
    def inner():
        print("i got decorated")
    return inner

pr = make_pretty()
pr()
#comment
