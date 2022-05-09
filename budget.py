class Category:

#ATTRIBUTES     
    def __init__(self, name: str):
        self.name = name
        self.ledger = []
        self._balance = 0
        
#PRINTS THE LIST 

    def __str__(self):
        def sorter(self, string, test1):
            return_string = string.center(30, '*') + '\n'
            listA = []
            listB = []
            for object in test1:
                for value in object.values():
                    if type(value) == str:
                        listA.append(value[0:23].ljust(23))
                    else:
                        temp = float(value)
                        temp = str("{:.2f}".format(temp))
                        temp1 = temp[0:7].rjust(7)
                        listB.append(temp1)
    
            for string in range(len(listA)):
                return_string += listA[string] + listB[string] + '\n'
            
            return_string += 'Total: ' + str("{:.2f}".format(self._balance))
            return return_string
          
        self.printer = sorter(self, self.name, self.ledger)
        return self.printer

#GET BALANCE
    def get_balance(self):
            return self._balance
#CHECHK FUNDS

    def check_funds(self, amount):
        return amount <= self._balance
      
#DEPOSIT METHOD      
    def deposit(self, amount, description = ''):
        self._balance += amount
        self.ledger.append({"amount": amount, "description": description})

#WITHDRAW METHOD   
    def withdraw(self, amount: float, description = ''):
        checked = self.check_funds(amount)
        if checked:
            self._balance -= amount
            self.ledger.append({"amount": -abs(amount), "description": description})
            return True 
        else:
            return False
           

#TRANSFER METHOD
    def transfer(self, amount, budget_class):
        checked = self.check_funds(amount)
        if checked:
            self.withdraw(amount, f'Transfer to {budget_class.name}')
            budget_class.deposit(amount, f'Transfer from {self.name}')
            return True 
        else:
            return False

          
#SPEND CHART FUNCTION 
def create_spend_chart(categories):

#DETERMINE PERCENTAGES AND BARS' LENGTHS

 #WITHDRAWS PER CATEGORY      
    cat_withdraws = []
    for category in categories:
        temp_withdraws = []
        for entry in category.ledger:
            for value in entry.values():
                if type(value) == float and value < 0:
                    temp_withdraws.append(value)
        temp2_withdraws = sum(temp_withdraws)
        cat_withdraws.append(temp2_withdraws)

  #MAX PERCENTAGE AND CAT PERCENTAGES
    max_percentage = sum(cat_withdraws)
    cat_percentages = []
  
    for value in cat_withdraws:
        temp1 = round((value / max_percentage) * 100)
        if temp1 < 10:
            cat_percentages.append(0)
        else:
            counts = 0
            while temp1 >= 10:
                temp1 -= 10
                counts += 1
            cat_percentages.append(counts)

  #NAMES OF CATEGORYS AND LENGTH
          
    category_list = []
    categories_len = []
    for category in categories:
        category_list.append(category.name)
        categories_len.append(len(category.name))

    columns = 5 + (len(category_list) * 3)

  #WORKING ON THE FINAL STRING
      
    lines = 'Percentage spent by category' + '\n'
    y_axis = ['100| ', ' 90| ', ' 80| ', ' 70| ', ' 60| ', ' 50| ', ' 40| ', ' 30| ', ' 20| ', ' 10| ', '  0| ']
    linecount = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
  
    count = 0
  
  #WHILE THAT SUMS THE Y AXIS
    while count <= 10:
        lines += str(y_axis[count])
        catcount = 0
      
  #WHILE THAT CHECKS THE CATEGORY AND PRINTS A '0' IF IT MATCHS  
        while catcount < len(category_list):
            if cat_percentages[catcount] >= linecount[count]:
                lines += 'o  '
            else:
                lines += '   '
            catcount += 1
        lines += '\n'
        count += 1

    #X AXIS
    x_axis = ''
    for i in range(columns - 4):
        x_axis += '-'
    lines += '    ' + x_axis + '\n'
  
  #WHILE THAT PRINTS THE CATEGORIES' NAME

    cat_rows = max(categories_len)
    lettersCount = 0
    
  
    while lettersCount < cat_rows:
        lines += '     '
        catCount2 = 0
        while catCount2 < len(category_list):
            if len(category_list[catCount2]) - lettersCount > 0:
                lines += category_list[catCount2][lettersCount] + '  '
            else:
                lines += '   '
            catCount2 += 1
        if lettersCount < (cat_rows -1):
            lines += '\n'
        lettersCount += 1

    return lines
