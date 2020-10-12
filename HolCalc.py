#File: HolCalc.py



def flights(nights):
  nights = int(raw_input ("How many nights will you be staying on your holiday? "))
  return 140 * nights

def location(city):
  city = raw_input("Please select from one of the following locations: Charlotte, Tampa, Pittsbrugh or Los Angeles. ")
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

def car(days):
  days = int(raw_input("How many days will you require a hire car?: "))
  cost = days * 40
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost

def spend(cash):
  cash = int(raw_input("How much spending money will you take?: "))
  return cash
