def under(s):
    dl=len (s)
    flip_line = str()
    for x in range(dl):
        flip_line += s[dl-1-x]
    return flip_line

mass = ("hello, world")
print(under(mass))

