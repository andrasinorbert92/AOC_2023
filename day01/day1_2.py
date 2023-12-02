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

def changeFirstAndLastSubstrToInt(row:str)->str:
    """
    two1nine -> 2wo1nin9
    
    eightwothree -> 8ightwothre3
    """
    def getmax(numslist:list)->int:
        index, value= 0, numslist[0]
        for i in range(len(numslist)):
            if numslist[i]>value:
                index= i
                value=numslist[i]
        return index,value
    def getmin(numslist:list)->int:
        index, value= 0, numslist[0]
        for i in range(len(numslist)):
            if numslist[i]<value:
                index= i
                value=numslist[i]
        return index,value
    def changeCharInStr(oldString:str, index:int, newChar:str)->str:
        _newString=oldString[:index]
        _newString+=newChar
        _newString+=oldString[index+1:]
        return _newString
    def find_all(row:str, sub_str:str):
        start = 0
        found=[]
        while True:
            start = row.find(sub_str, start)
            if start == -1: return found
            found.append(start)
            start += len(sub_str)
        
    nums=["one", "two", "three", "four", "five",
          "six", "seven", "eight", "nine"]
    indexList=[]
    numList=[]
    for i in range(len(nums)):
        index=find_all(row,nums[i])
        for j in range(len(index)):
            indexList.append(index[j])
            numList.append(i+1)
    if(len(indexList)!=0):
        last=getmax(indexList)
        first=getmin(indexList)

        if(last[1]!=first[1]):
            row=changeCharInStr(row, first[1],str(numList[first[0]]))
            row=changeCharInStr(row,
                                last[1]+len(nums[numList[last[0]]-1])-1,
                                str(numList[last[0]]))
        else:
            row=changeCharInStr(row, first[1],str(numList[first[0]]))

    return row

def rowWrapper(row:str)->int:
    """Investigate one row.
    
    Args:
        row (string): raw row
    Returns:
        int: first and last number of row
    """
    row=changeFirstAndLastSubstrToInt(row)
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