from State_Pattern import switch_state

class LightSwitch:
    def __init__(self, state: switch_state.SwitchState):
        self._state = state
        print(f'Creating switch- State is {self._state}')

    @property
    def state(self):
        return self._state

    def light_on(self):
        self._state = self._state.turn_on()

    def light_off(self):
        self._state = self._state.turn_off()

    def light_fix(self):
        self._state = self._state.fix()
