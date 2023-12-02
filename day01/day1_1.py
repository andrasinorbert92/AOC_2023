def is_integer(num_str: str)->bool:
    try:
        float(num_str)
    except ValueError:
        return False
    else:
        return float(num_str).is_integer()
    
def getFirstNumber(row:str)->int:
    i=0
    while i<len(row):
        if is_integer( row[i]):
            return int(row[i])
        i+=1
        
def getLastNumber(row:str)->int:
    i=len(row)-1
    while i>=0:
        if is_integer( row[i]):
            return int(row[i])
        i-=1

def rowWrapper(row:str)->int:
    """Investigate one row.
    
    Args:
        row (string): raw row
    Returns:
        int: first and last number of row
    """
    first=getFirstNumber(row)
    last=getLastNumber(row)
    return first*10+last

def wrapAllRow(rows:list)->list:
    numsList=[]
    for i in range(len(rows)):
        numsList.append(rowWrapper(rows[i]))
    return numsList

def openFile(filename: str)->list:
    _file=open(filename, "r")
    _rows= _file.readlines()
    _file.close()
    return _rows

def stripInputRows(filename: str)->list:
    _rows=openFile(filename)
    _rows=[_rows[i].strip() for i in range(len(_rows)) ]
    return _rows

def sumNums(rows:list)->list:
    s=0
    for i in rows:
        s+=i
    return s

rows=stripInputRows("AOC_2023\day01\input")
rowsNums=wrapAllRow(rows)
sum=sumNums(rowsNums)
print(sum)