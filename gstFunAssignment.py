def calc(price,gst):
    cgst=price+price*(gst/2)/100
    sgst=price+price*(gst/2)/100
    total=price+price*(gst)/100
    return(cgst,sgst,total)
price=int(input("enter the bare price: "))
gst=int(input("enter the gst price: "))

calcc=calc(price,gst)
print("Actual Price of the item =",price)
print("\nPrice after CGST=",calcc[0])
print("\nPrice after applying sgst=",calcc[1])
print("\nTotal price with gst",calcc[2])