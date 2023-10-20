# Temperature to convert celuius to fahrenheite.
celcius = float(input("Put in your temperature in Celcius:\n"))
f=0
# function to convert celcius to fahrenheit
def convert_temp(f):
    
    f = (celcius * (9 / 5) + 32)
    print("The temparture in celius to fahrenheit is:\n" ,f )

convert_temp(f)   