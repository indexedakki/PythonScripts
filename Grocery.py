while True:   
    budget = float(input("Enter your budget : ")) 
    temp = budget
    
    dict ={"name":[], "quantity":[], "price":[]} 
    
    t = list(dict.values()) 
    name = t[0]   
    quantity = t[1]  
    price = t[2] 

    while True: 
        try: 
            char = int(input("1.ADD \n 2.EXIT \n Enter your choice : ")) 
        except ValueError: 
            print("\n Enter 1 or 2") 
            continue
        else: 
            if char == 1 and temp>0:                      
                pname = input("Enter product name : ")  
                pquantity = input("Enter quantity : ") 
                pprice = float(input("Enter price of the product : "))   
                if pprice>temp: 
                  
                    print("\n Can't be added, budget is low")  
                    continue
    
                else: 
        
                    if pname in name:   
                    
                        ind = name.index(pname)    
                        quantity.remove(quantity[ind])  
                        price.remove(price[ind])   
                        quantity.insert(ind, pquantity)    
                        price.insert(ind, pprice)    
                        temp = budget-sum(price)    
    
                        print("\n Current budget", temp) 
                    else: 
 
                        name.append(pname)   

                        quantity.append(pquantity)    
    
                        price.append(pprice)     

                        temp = budget-sum(price)    
    
                        print("\n Current budget", temp) 
    
            elif char==2:
                break 
    
    print("\n Current budget", temp)  
    
    if temp in price:   
        print("\nAmount left can buy you a", name[price.index(temp)])   
    
    print("\n\n\nGROCERY LIST") 

    for i in range(len(name)):  
        print(name[i], quantity[i], price[i])