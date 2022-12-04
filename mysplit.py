def mysplit(string):
    arr = []
    tem = ""
    for ch in string:
        if ch != " ":
            tem += ch
        if ch == " ":
            if len(tem)>1:
                arr.append(tem)
                tem = ""

        
    return arr
