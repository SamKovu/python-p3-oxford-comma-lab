def oxford_comma(items):
    
    if len(items)==2:
           return " and ".join(items) 
    elif len(items)>2:
         lastItem=items.pop()
         sentence=", ".join(items)
         return sentence+", and "+ lastItem
    else:
         return "".join(items)

   
