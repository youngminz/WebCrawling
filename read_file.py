def read_txt(filename):
    with open(filename, "r") as f:
        for l in f:
            l = l.strip().split(",")
            yield l

            
def read_txt(filename):
    with open(filename, "r") as f:
        for l in f:
            l = l.strip()
            yield l
