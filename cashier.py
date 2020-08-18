def main():
    # write code here
   items=[]
   s=0
   
   name=input("Item enter \"done\" when finished:")
   
   while name != "done":
      dic={}

      price=input("Price:")
      Quantity=input("Quantity:")

      dic["name"]=name
      dic["price"]=float(price)
      dic["Quantity"]=int(Quantity)
      
      
      items.append(dic.copy())

      name=input("enter \"done\" when finished:")
      s=s+1
   


   print()
   print("-------------------")
   print("receipt")
   print("-------------------")
  
   for name,Quantity,price  in items.value():
    print("%d %s %f KD"%(Quantity,name,price))
  #  for key, value in items.items():
    
  #   # Again iterate over the nested dictionary
  #   for name,Quantity,price in value.items():
  #       print("%d %s %f KD"%(Quantity,name,price))

   print("-------------------") 
  #  price=0
  #  for x in items:
  #    price+=items[x]["price"]*items[x]["Quantity"]
  #  print("Total Price: %f KD"%(price))  
  #  for x in items:
  #    print("%d %s %f KD"%(items[x]["Quantity"],items[x]["name"],items[x]["price"]))
# -------------------
# receipt
# -------------------
# 4 apples 0.800KD
# 1 carrot 0.100KD
# 2 flour 2.600KD
# 10 water bottles 0.500KD
# -------------------
# Total Price: 4.000KD

if __name__ == '__main__':
    main()
