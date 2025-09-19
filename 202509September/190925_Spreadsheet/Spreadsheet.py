class Spreadsheet:

    def __init__(self, rows: int):
        self.map = dict()        

    def setCell(self, cell: str, value: int) -> None:        
        self.map[cell] = value

    def resetCell(self, cell: str) -> None:
        if(cell in self.map):
            self.map.pop(cell)          

    def getValue(self, formula: str) -> int:
        
        formula = formula.replace("=", "")
        formula = formula.split("+")
        t1 = formula[0]
        t2 = formula[1]

        if(t1.isdigit()):
            t1 = int(t1)    
        else:
            if(t1 not in self.map):
                t1 = 0
            else:
                t1 = self.map[t1]
        
        if(t2.isdigit()):
            t2 = int(t2)    
        else:
            if(t2 not in self.map):
                t2 = 0
            else:
                t2 = self.map[t2]

        return t1 + t2


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
