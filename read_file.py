def read_txt(filename):
    with open(filename, "r") as f:
        for l in f:
            yield l.strip().split(",")

            
def read_txt(filename):
    with open(filename, "r") as f:
        for l in f:
            yield l.strip()
