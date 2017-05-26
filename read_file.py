def read_txt():
    with open("<filename>", "r") as f:
        for l in f:
            l = l.strip().split(",")
            yield l
