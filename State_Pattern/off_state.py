from State_Pattern.switch_state import SwitchState
from typing import override

class OffState(SwitchState):
    def __init__(self):
        super().__init__('Off')

    @override
    def turn_on(self):
        from State_Pattern.on_state import OnState
        print('Switch is turned on!')
        return OnState()

    @override
    def turn_off(self):
        from State_Pattern.broken_state import BrokenState
        print('You broke the switch!')
        return BrokenState()

    @override
    def fix(self):
        print('Nothing to fix!')
        return self