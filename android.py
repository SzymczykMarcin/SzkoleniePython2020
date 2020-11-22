class Android:

    def __init__(self):
        self.mode = 'Standard'
        self.body_parts = ['legs', 'arms', 'mouth']
        self.action = 'Idle'
        self._answere = ''

    def reset(self):
        self.mode = 'Standard'

    def listen(self, voice):
        if voice == 'What is your name?':
            self._answere = 'My name is C3PO'

    def set_mode(self, mode):
        self.mode = mode

    def jump(self):
        self.action = 'jump'

    def grab(self):
        self.action = 'grab'

    def speaking(self):
        return self._answere




