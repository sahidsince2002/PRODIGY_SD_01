# User input     
def repeat():  
    print("\n\t TEMPERATURE CONVERTER ")
    temp = int(input("\n\t Enter the temperature : "))
    print("\n\t Input Temperature Scale ")
    print("\n\t 1. Celcius ")
    print("\n\t 2. Farhenheit")
    print("\n\t 3. Kelvin")
    val = int(input("\n\t Choose from (1-3) : "))
    converter(val,temp)

# Converter Function
def converter(val,temp):
    if(val==1):
        farh = (1.8 * temp) + 32 
        kel = temp + 273.15
        print("\n\t The converted temperature to Farhenheit is ", round(farh,2),"deg F")
        print("\n\t The converted temperature to kelvin is ", round(kel,2),"deg K")
        repeat()
   
    elif(val==2):
        cel = (temp - 32) * 0.55
        kel = ((temp -32) * 0.55) + 273.15
        print("\n\t The converted temperature to Celcius is ", round(cel,2),"deg C")
        print("\n\t The converted temperature to kelvin is ", round(kel,2),"deg K")
        repeat()
        
    elif(val==3):
        cel = (temp - 273.15)
        farh = ((temp -273.15) * 1.8) + 32
        print("\n\t The converted temperature to Celcius is ", round(cel,2),"deg C")
        print("\n\t The converted temperature to Farhenheit is ", round(farh,2),"deg F")  
        repeat()
        
    else:
        print("\n\t Error check the input ")    
       
repeat()
    

    
           
           
