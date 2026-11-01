
from State_Pattern.switch_state import SwitchState
from typing import override

class OnState(SwitchState):
    def __init__(self):
        super().__init__('On')

    @override
    def turn_on(self):
        print('Switch is already on!')
        return self

    @override
    def turn_off(self):
        from State_Pattern.off_state import OffState
        print('Switch is turned off!')
        return OffState()

    @override
    def fix(self):
        print('Nothing to fix!')
        return self
