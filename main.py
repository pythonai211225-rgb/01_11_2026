
'''
from Four_Sides.square import Square
from Rounded.circle import Circle

s1 = Square('my-square', 5)
print(s1)
c1 = Circle('my-circle', 7)
print(c1)
'''

from State_Pattern.light_switch import LightSwitch
from State_Pattern.on_state import OnState

my_switch = LightSwitch(OnState())
# print(my_switch.state)
my_switch.light_on()
my_switch.light_off()
my_switch.light_off()
my_switch.light_on()
my_switch.light_fix()
my_switch.light_on()

