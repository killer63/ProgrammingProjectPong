from functools import partial

class Input:
    keysPressed = []

    def __init__(self, upkey, downkey, paddle, window):
        self.upkey = upkey
        self.downkey = downkey
        self.paddle = paddle
        window.onkeypress(partial(self.handleInputs, self.upkey), self.upkey)
        window.onkeypress(partial(self.handleInputs, self.downkey), self.downkey)
        window.onkeyrelease(partial(self.resetInput, self.upkey), self.upkey)
        window.onkeyrelease(partial(self.resetInput, self.downkey), self.downkey)

    def run(self):
        if Input.keysPressed.count(self.upkey) == 1:
            self.paddle.up()
        elif Input.keysPressed.count(self.downkey) == 1:
            self.paddle.down()

    def handleInputs(self, key):
        if Input.keysPressed.count(key) == 0:
            Input.keysPressed.append(key)

    def resetInput(self, key):
        Input.keysPressed.remove(key)