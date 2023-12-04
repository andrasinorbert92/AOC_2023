def openFile(filename: str)->list:
    _file=open(filename, "r")
    _rows= _file.readlines()
    _file.close()
    return _rows

def stripInputRows(filename: str)->list:
    _rows=openFile(filename)
    _rows=[_rows[i].strip() for i in range(len(_rows)) ]
    return _rows

def rowWrapper(currRow:str, lastRow:str, nextRow:str)->int:
    def checkCharIsSymbol(char: str)->bool:
        if isinstance(char, int) or char==".": return False
        return True
        
    def checkNeighbourRowsOnIndexIsSymbol(index:int, row1:str, row2:str)->bool:
        _isSymbol=None
        if row1 is not None:
            _isSymbol= checkCharIsSymbol(row1[index])
            if _isSymbol: return True
        if row2 is not None:
            return checkCharIsSymbol(row2[index])
        return False
        
    print("------------------------------------")
    print(lastRow)
    print(currRow)
    print(nextRow)
    print("----------------")
    currNum_str=""
    sum=0
    isNum=False
    hasSymbol=False
    for i in range(len(currRow)):
        if currRow[i].isnumeric(): # number
            if hasSymbol: continue
            if len(currNum_str) == 0 and i > 0: # i>0 and number start
                hasSymbol|=checkCharIsSymbol(currRow[i-1])
                hasSymbol|=checkNeighbourRowsOnIndexIsSymbol(i-1, lastRow, nextRow)                
            
            hasSymbol|=checkNeighbourRowsOnIndexIsSymbol(i, lastRow, nextRow)
            if not hasSymbol: currNum_str+=currRow[i] # add curr char to currNum_str
            else: # has symbol
                isNum=False
                continue
            
            if i == len(currRow)-1: # last char in row
                print(currNum_str)
                sum+=int(currNum_str)
                currNum_str=""
                isNum=False
            isNum=True
        elif isNum and not hasSymbol:
            # Then i-1 char was num and dont have symbol
            hasSymbol=checkCharIsSymbol(currRow[i])
            hasSymbol|=checkNeighbourRowsOnIndexIsSymbol(i, lastRow, nextRow)
            if not hasSymbol:
                sum+=int(currNum_str) # end of the number
                print(currNum_str)
                currNum_str=""
                isNum=False
            else: isNum=False
        elif hasSymbol:
            isNum=False
            hasSymbol=False
            currNum_str=""
    print(sum)
    print("------------------------------------")
    return sum

def wrapAllRow(rows:list)->list:
    sum=0
    for i in range(len(rows)):
        currRow=rows[i]
        nextRow=None
        lastRow=None
        if i<len(rows)-1:
            nextRow=rows[i+1]
        if i>0:
            lastRow=rows[i-1]
        
        sum+=rowWrapper(currRow, lastRow, nextRow)
    
    return sum

rows=stripInputRows("day03/input")

sum=wrapAllRow(rows)
print(sum)
#print(sum(nums))