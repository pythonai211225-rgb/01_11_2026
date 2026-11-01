from State_Pattern.switch_state import SwitchState
from typing import override

class BrokenState(SwitchState):
    def __init__(self):
        super().__init__('Broken')

    @override
    def turn_on(self):
        print('Switch is broken!')
        return self

    @override
    def turn_off(self):
        print('Switch is broken!')
        return self

    @override
    def fix(self):
        from State_Pattern.off_state import OffState
        print('Switch is Fixed now!')
        return OffState()
