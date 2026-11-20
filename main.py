ltrim = 0
rtrim = 0
def go_forward(speed: number):
    TinkerBott.motors(ltrim * speed, rtrim * speed)
def go_backward(speed2: number):
    TinkerBott.motors(-ltrim * speed2, -rtrim * speed2)
def init():
    global rtrim, ltrim
    rtrim = 1
    ltrim = 1

def on_forever():
    pass
basic.forever(on_forever)
