# *1 import shirt_printing
# *2 from shirt_printing import make_shirt
# *3 from shirt_printing import make_shirt as ms
#  *4import shirt_printing as sp
from shirt_printing import *

#1 
#shirt_printing.make_shirt()
#shirt_printing.make_shirt("M")
#shirt_printing.make_shirt("S","For the Horde!")
#shirt_printing.make_shirt(size="XL", text="Avengers Assemble!")

#2 ,5
make_shirt()
make_shirt("M")
make_shirt("S","For the Horde!")
make_shirt(size="XL", text="Avengers Assemble!")

#3
#ms()
#ms("M")
#ms("S","For the Horde!")
#ms(size="XL", text="Avengers Assemble!")

#4
#sp.make_shirt()
#sp.make_shirt("M")
#sp.make_shirt("S","For the Horde!")
#sp.make_shirt(size="XL", text="Avengers Assemble!")

