def chicken_prices_before(wing_number, day):
  if day.capitalize() == "Wednesday":
    return str(wing_number* 0.75)
  else:
    return str(wing_number* 1) 
  
def chicken_prices_after(wing_number, day):
  if day.capitalize() == "Wednesday":
    return str(wing_number*1.33)
  else:
    return str(wing_number*1.58)

# def difference ():
