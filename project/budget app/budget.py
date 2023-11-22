class Category:
  def __init__(self,name):
    self.name = name
    self.ledger = []
  def deposit(self,amount,description=""):
    x = {"amount": amount, "description": description}
    self.ledger.append(x)
  def withdraw(self,amount,description=""):
    if self.checkfunds((amount)) is True:
      y = y={"amount": -amount, "description": description}
      self.ledger.append(y)
      return True
    else:
      return False
  def get_balance(self):
    current_balance = 0
    if len(self.ledger) > 0:
      for item in self.ledger:
        current_balance = current_balance + item["amount"]
    return current_balance
  def transfer(self,amount,category):
      if self.check_funds(amount) is True:
        self.withdraw(amount,"Transfer to " + category.name)
        category.deposit(amount,"Transfer from " + self.name)
        return True
      else:
        return False
  def check_funds(self,amount):
      if amount> self.get_balance():
        return False
      return True
  
def create_spend_chart(categories):
  # /// step 1 put category names into a padded list. 
  names_list = []
  withdrawl_list = []
  for category in categories:
    names = category.name
    names_list = names_list.append(names)
    height = (len(max(names_list, key = len)))
    padded = []
    for word in names_list:
      padded.append(word.ljust(height))

# /// step 2 get percentage and put into a list 
      w_total = 0
      for item in category.ledger:
        amount = item['amount']
        if amount<0:
          w_total += amount
      withdrawl_list.append(w_total)
  
  total = int(round(sum(withdrawl_list)))
  percentage = []
  for x in withdrawl_list:
    per = (x * 100)/ total
    # /// rounding up in multiple of ten at floor value i.e 67.7 == 60
    per = round(per//10) * 10
    percentage.append(per)
  
# /// step 3 creat the final chart 
  chart = "Percentage spent by category\n"
  for i in reversed(range(0,110,10)):
    chart += f"{str(i) + '|':>4}"
    for percent in percentage:
        if percent>=i:
            chart += " o "
        else:
            chart+="   "
    chart += '\n'
  chart += "    " + "-"*10 + ' \n'

  for name in zip(*padded):
    # print(' '.join(name),end="\n")
    chart += "     "
    chart += ('  '.join(name)) + '  \n'

  return chart.rstrip('\n')