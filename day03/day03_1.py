def openFile(filename: str)->list:
    _file=open(filename, "r")
    _rows= _file.readlines()
    _file.close()
    return _rows

def stripInputRows(filename: str)->list:
    _rows=openFile(filename)
    _rows=[_rows[i].strip() for i in range(len(_rows)) ]
    return _rows

"""
class FoundNumber:
    def __init__(self, row:int, column:int, number_str:str) -> None:
        self.row=row
        self.column=column
        self.number_str=number_str
        self.number_int=int(number_str)
        self.number_len=len(number_str)
        self.environment=[]
        
    def __str__(self) -> str:
        return f"{self.number_str}\t\t{self.row}\t\t{self.column}\t\t{self.number_len}\t\t{self.hasSymbol}"
    def __repr__(self) -> str:
        return f"{self.number_str}\t\t{self.row}\t\t{self.column}\t\t{self.number_len}\t\t{self.hasSymbol}"
    def getNum(self):
        return self.number_int
    def setEnvironment(self, rows:list):
        if self.row==0:
            if self.column==0:
                # left top
                self.environment.append(rows[self.row][:self.column+len(self.number_str)+1])
                self.environment.append(rows[self.row+1][:self.column+len(self.number_str)+1])
            elif self.column+self.number_len-1==len(rows[self.row]):
                #right top
                self.environment.append(rows[self.row][self.column-1:])
                self.environment.append(rows[self.row+1][self.column-1:])
            else:
                #top
                self.environment.append(rows[self.row][self.column-1:self.column+len(self.number_str)+1])
                self.environment.append(rows[self.row+1][self.column-1:self.column+len(self.number_str)+1])
        elif self.row==len(rows)-1:
            if self.column==0:
                # left bottom
                self.environment.append(rows[self.row-1][:self.column+len(self.number_str)+1])
                self.environment.append(rows[self.row][:self.column+len(self.number_str)+1])
            elif self.column+self.number_len-1==len(rows[self.row]):
                #right bottom
                self.environment.append(rows[self.row-1][self.column-1:])
                self.environment.append(rows[self.row][self.column-1:])
            else:
                #bottom
                self.environment.append(rows[self.row-1 ][self.column-1:self.column+len(self.number_str)+1])
                self.environment.append(rows[self.row   ][self.column-1:self.column+len(self.number_str)+1])
        else:
            if self.column==0:
                # left
                self.environment.append(rows[self.row-1][:self.column+len(self.number_str)+1])
                self.environment.append(rows[self.row][:self.column+len(self.number_str)+1])
                self.environment.append(rows[self.row+1][:self.column+len(self.number_str)+1])
            elif self.column+self.number_len-1==len(rows[self.row]):
                #right
                self.environment.append(rows[self.row-1][self.column-1:])
                self.environment.append(rows[self.row][self.column-1:])
                self.environment.append(rows[self.row+1][self.column-1:])
            else:
                self.environment.append(rows[self.row-1 ][self.column-1:self.column+len(self.number_str)+1])
                self.environment.append(rows[self.row   ][self.column-1:self.column+len(self.number_str)+1])
                self.environment.append(rows[self.row+1 ][self.column-1:self.column+len(self.number_str)+1])
                
        self.hasSymbol=self.checkEnvironment()
                
    def printEnvironment(self):
        for i in range(len(self.environment)):
            print(self.environment[i])
    
    def checkEnvironment(self):
        i=0
        while i<len(self.environment):
            j=0
            while j<len(self.environment[i]):
                #if self.environment[i][j] != '.' and not self.environment[i][j].isnumeric(): return True
                if self.environment[i][j] not in "0123456789.": return True
                j+=1
            i+=1
        return False


class FoundNumberList:
    def __init__(self):
        self.numberList=[]
    
    def append(self, row:int, column:int, number_str:str):
        self.numberList.append(FoundNumber(row, column, number_str))
        
    def setEnvironment(self, rows:list):
        for i in self.numberList:
            i.setEnvironment(rows)
    def print(self):
        print("Number\t\trow\t\tcolumb\t\tlength\t\thasSymbol")
        for i in range(len(self.numberList)):
            print(f"{self.numberList[i]}")
            
    def sumIfHasSymbol(self)->int:
        sum=0
        for i in self.numberList:
            if i.hasSymbol:
                i.printEnvironment()
                print(i)
                sum+=i.getNum()
        return sum
    def sumAll(self):
        sum=0
        for i in self.numberList:
            sum+=i.getNum()
        return sum
"""
"""
def rowWrapper(currRow:str, lastRow:str, nextRow:str)->int:
    def checkCharIsSymbol(char: str)->bool:
        if isinstance(char, int) or char==".": return False
        #f=open("day03/output", "a")
        #f.write(char+" ")
        #f.close()
        return True
        
    def checkNeighbourRowsOnIndexIsSymbol(index:int, row1:str, row2:str)->bool:
        _isSymbol=None
        if row1 is not None:
            _isSymbol= checkCharIsSymbol(row1[index])
            if _isSymbol: return True
        if row2 is not None:
            return checkCharIsSymbol(row2[index])
        return False
    
    def sumAllNumber(row:str)->int:
        sum =0
        number_str=""
        for i in range(len(row)):
            if row[i].isnumeric():
                number_str+=row[i]
            else:
                if len(number_str)>0:
                    sum+=int(number_str)
                    number_str=""
        return sum
    
    sum_All_number=sumAllNumber(currRow)
    #print("------------------------------------")
    #print(lastRow)
    #print(currRow)
    #print(nextRow)
    #print("----------------")
    currNum_str=""
    sum_has_not_symbol=0
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
                #print(currNum_str)
                sum_has_not_symbol+=int(currNum_str)
                currNum_str=""
                isNum=False
            isNum=True
        elif isNum and not hasSymbol:
            # Then i-1 char was num and dont have symbol
            hasSymbol=checkCharIsSymbol(currRow[i])
            hasSymbol|=checkNeighbourRowsOnIndexIsSymbol(i, lastRow, nextRow)
            if not hasSymbol:
                sum_has_not_symbol+=int(currNum_str) # end of the number
                #print(currNum_str)
                currNum_str=""
                isNum=False
            else: isNum=False
        elif hasSymbol:
            isNum=False
            hasSymbol=False
            currNum_str=""
    #print(sum_has_not_symbol)
    #print("------------------------------------")
    #return sum_All_number-sum_has_not_symbol
    return sum_All_number

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
"""

class Symbol:
    def __init__(self, symbol, row, col) -> None:
        self.symbol=symbol
        self.row=int(row)
        self.column=int(col)
        self.numlist=[]
        self.environment=[]
        self.state=""
        
    def __str__(self) -> str:
        env=""
        for i in range(len(self.environment)):
            env+=self.environment[i]+"\n"
        return f"{self.symbol}\t\t{self.row}\t\t{self.column}\n{env}"
    def __repr__(self) -> str:
        env=""
        for i in range(len(self.environment)):
            env+=self.environment[i]
        return f"{self.symbol}\t\t{self.row}\t\t{self.column}\n{env}"
    def addNumberList(self, number:int):
        self.numlist.append(number)
    def getSum(self)->int:
        return sum(self.numlist)
    def findNums(self, rows:list):
        pass
    def printEnvironment(self):
        for i in range(len(self.environment)):
            print(self.environment[i])
    def setEnvironment(self, rows:list):
        if self.row==0: #first row
            if self.column==0:
                # left top
                self.state="TL"
                self.environment.append(rows[0][:2])
                self.environment.append(rows[1][:2])
            elif self.column==len(rows[0])-1:
                #right top
                self.state="TR"
                self.environment.append(rows[0][-2:])
                self.environment.append(rows[1][-2:])
            else:
                #top
                self.state="TO" # top other
                self.environment.append(rows[0][self.column-1:self.column+2])
                self.environment.append(rows[1][self.column-1:self.column+2])
        elif self.row==len(rows)-1: #last row
            if self.column==0:
                # left bottom
                self.state="BL"
                self.environment.append(rows[-2][:2])
                self.environment.append(rows[-1][:2])
            elif self.column==len(rows[-1])-1:
                #right bottom
                self.state="BR"
                self.environment.append(rows[-2][-2:])
                self.environment.append(rows[-1][-2:])
            else:
                #bottom
                self.state="BO"
                self.environment.append(rows[-2][self.column-1:self.column+2])
                self.environment.append(rows[-1][self.column-1:self.column+2])
        else:
            if self.column==0:
                # left
                self.state="OL"
                self.environment.append(rows[self.row-1][:2])
                self.environment.append(rows[self.row][:2])
                self.environment.append(rows[self.row+1][:2])
            elif self.column+1==len(rows[self.row]):
                #right
                self.state="OR"
                self.environment.append(rows[self.row-1][-2:])
                self.environment.append(rows[self.row][-2:])
                self.environment.append(rows[self.row+1][-2:])
            else:
                self.state="OO"
                self.environment.append(rows[self.row-1 ][self.column-1:self.column+2])
                self.environment.append(rows[self.row   ][self.column-1:self.column+2])
                self.environment.append(rows[self.row+1 ][self.column-1:self.column+2])
    
    def checkIsNum(char):
        return char in "0123456789"
    
    def setNumList(self, rows:list):
        # if self.state=="OO":
        # tehát nincs szimbolum a szélén
        # ergo 8 pozit kell megnézni
        if self.checkIsNum(self.environment[1][0]): # tehát szimbolumtol balra
            number=self.environment[1][0]
            i=self.column-2
            while self.checkIsNum(rows[self.row][i]):
                number=rows[self.row][i]+number
                i-=1
            self.numlist.append(int(number))
            number=""
            # amugy ha általánositani szeretném, akkár átadhatnám, hogy -1 akkor balra kell nézni, +1 esetén jobbra, 0 esetén mindkét irányba
        #meg lehetne számolni hány olyan eset van, hogy felül és alul a 2-2 sarokban van szám, de közte . van

class SymbolList:
    def __init__(self) -> None:
        self.symbolList=[]
    def append(self, symbol:str, row:int, column:int):
        self.symbolList.append(Symbol(symbol, row, column))
    def sumAll(self):
        sum=0
        for i in self.symbolList:
            sum+=i.getSum()
        return sum
    def setEnvironment(self, rows:list):
        for i in self.symbolList:
            i.setEnvironment(rows)
    def print(self):
        print("Symbol\t\trow\t\tcolumb")
        for i in range(len(self.symbolList)):
            print(f"{self.symbolList[i]}")
    def getSymbolTypes(self):
        #only "OO"
        types=set()
        for i in self.symbolList:
            types.add(i.state)
        return types

def rowWrapper(row:str, rowNumber:int, founds:SymbolList):
    for i in range(len(row)):
        if row[i] not in "1234567890.":
            founds.append(row[i], rowNumber, i)

def wrapAllRow(rows:list)->SymbolList:
    founds=SymbolList()
    for i in range(len(rows)):
        rowWrapper(rows[i], i, founds)
    founds.setEnvironment(rows)
    founds.print()
    print(founds.getSymbolTypes())
    return sum

rows=stripInputRows("day03/input")

sum=wrapAllRow(rows)
print(sum)

#print(founds)
#print(sum(nums))

#519345 too low

# {'*', '%', '&', '#', '-', '$', '/', '@', '=', '+'}