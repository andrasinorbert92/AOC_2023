def openFile(filename: str)->list:
    _file=open(filename, "r")
    _rows= _file.readlines()
    _file.close()
    return _rows

def stripInputRows(filename: str)->list:
    _rows=openFile(filename)
    _rows=[_rows[i].strip() for i in range(len(_rows)) ]
    return _rows

def roundWrapper(round:str)->bool:
    def validCubes(red:int, green:int, blue:int)->bool:
        if red>12: return False
        if green>13: return False
        if blue>14: return False
        return True
    def is_integer(num_str: str)->bool:
        try:
            float(num_str)
        except ValueError:
            return False
        else:
            return float(num_str).is_integer()
    def getBallNums(round:str, color:str)->int:
        index=round.find(color)
        if index!=-1:
            if is_integer(round[index-3]):
                return int(round[index-3:index-1])
            return int(round[index-2])
        return -1
    
    _cubes=["red", "green", "blue"]
    _balls=[]
    for color in _cubes:
        _balls.append(getBallNums(round, color))
    return validCubes(_balls[0], _balls[1], _balls[2])

def rowWrapper(row:str)->int:
    _row=row.split(":")
    _id=int(_row[0].split()[1])
    _rounds=_row[1].split(";")
    i=0
    while i<len(_rounds) and roundWrapper(_rounds[i]):
        i+=1
    if i<len(_rounds): return 0
    return _id

def wrapAllRow(rows:list)->list:
    idList=[]
    for i in range(len(rows)):
        idList.append(rowWrapper(rows[i]))
    return idList

rows=stripInputRows("input")

ids=wrapAllRow(rows)
print(sum(ids))