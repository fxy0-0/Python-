def printTable(table):
    colWidth = [0]*len(table)
    for i in range(len(table)):  
        print(i)
        for k in range(len(table[0])):
            if colWidth[i] < len(table[i][k]):
                colWidth[i] = len(table[i][k])
    #print(colWidth)
    for i in range(len(table[0])):  
        for k in range(len(table)):
            #print(table[k][i].ljust(colWidth[k]+5),end="")         
            if k == 0:
                print(table[k][i].rjust(colWidth[k]+5),end="\t")
            else:
                print(table[k][i].ljust(colWidth[k]+5),end="")       
        print()
tableData = [['apples', 'oranges', 'cherries', 'banana','last1'],
['Alice', 'Bob', 'Carol', 'David','last2'],
['dogs', 'cats', 'moose', 'goose','last3']]
printTable(tableData)