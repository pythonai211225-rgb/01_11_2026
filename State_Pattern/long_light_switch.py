
class LightSwitch:
    def __init__(self, state):
        self._state = state

    @property
    def state(self):
        return self._state

    def light_on(self):
        if self._state == 'broken':
            print('Switch already broken')
            return
        if self._state == 'on':
            print('Switch is already on...')
            return
        if self._state == 'off':
            self._state = 'on'
            print('Switch On')

    def light_off(self):
        if self._state == 'broken':
            print('Switch already broken')
            return
        if self._state == 'off':
            self._state = 'broken'
            print('Switch is now broken')
            return
        if self._state == 'on':
            self._state = 'off'
            print('Switch On')

    def light_fix(self):
        if self._state == 'broken':
            print('Switch fix, now off')
            self._state = 'off'
        else:
            print('Switch is already fixed!')



