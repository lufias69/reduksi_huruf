
def reduksi_huruf(kata):
#kata = 'siiiiiiapaaaa'
    nkata  = list()
    for i,k in enumerate(kata):
        if i>2:
            if kata[i]== kata[i-1] and kata[i] == kata[i-2]:
                continue
            else:
                nkata.append(k)
        else:
            nkata.append(k)
    return "".join(nkata)
