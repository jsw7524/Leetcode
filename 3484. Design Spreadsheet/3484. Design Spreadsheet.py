class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows
        self.dictSheet = {}

    def setCell(self, cell: str, value: int) -> None:
        self.dictSheet[cell] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)    

    def getValue(self, formula: str) -> int:
        cell1, cell2 = formula.split('+')
        cell1 = cell1.replace('=', '')
        result1, result2 = 0, 0  # Fixed typo: rsult2 -> result2
        
        if cell1.isdigit():  # Using isdigit() instead of str.isnumeric()
            result1 = int(cell1)
        else:
            result1 = self.dictSheet[cell1] if cell1 in self.dictSheet else 0
        
        if cell2.isdigit():
            result2 = int(cell2)
        else:
            result2 = self.dictSheet[cell2] if cell2 in self.dictSheet else 0
        
        return result1 + result2

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)