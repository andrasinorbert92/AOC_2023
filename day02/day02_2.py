def openFile(filename: str)->list:
    _file=open(filename, "r")
    _rows= _file.readlines()
    _file.close()
    return _rows

def stripInputRows(filename: str)->list:
    _rows=openFile(filename)
    _rows=[_rows[i].strip() for i in range(len(_rows)) ]
    return _rows

def roundWrapper(round:str)->list:
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
    return _balls

def rowWrapper(row:str)->int:
    def calcPower(balls:list)->int:
        s=1
        for i in balls: s*=i
        return s
    _row=row.split(":")
    _id=int(_row[0].split()[1])
    _rounds=_row[1].split(";")
    
    maxBalls=[0,0,0]
    i=0
    while i<len(_rounds):
        _r=roundWrapper(_rounds[i])
        for j in range(len(_r)):
            if _r[j]>maxBalls[j]:
                maxBalls[j]=_r[j]
        i+=1
    return calcPower(maxBalls)

def wrapAllRow(rows:list)->list:
    idList=[]
    for i in range(len(rows)):
        idList.append(rowWrapper(rows[i]))
    return idList

rows=stripInputRows("input")

powers=wrapAllRow(rows)
print(sum(powers))