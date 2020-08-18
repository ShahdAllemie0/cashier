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
  
   for x in items:
    print("%d %s %.3f KD"%(x["Quantity"],x["name"],x["price"]*x["Quantity"]))
    

   print("-------------------") 
   price=0
   for x in items:
     price+=x["price"]*x["Quantity"]
   print("Total Price: %.3f KD"%(price)) 



if __name__ == '__main__':
    main()
