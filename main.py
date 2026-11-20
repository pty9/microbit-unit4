def go_forward(speed: number):
    init()
    TinkerBott.motors(ltrim * speed, rtrim * speed)
def go_backward(speed2: number):
    init()
    TinkerBott.motors((0 - ltrim) * speed2, (0 - rtrim) * speed2)
def init():
    global rtrim, ltrim
    rtrim = 1
    ltrim = 1
rtrim = 0
ltrim = 0
go_forward(100)
basic.pause(5000)
TinkerBott.stopcar()

def on_forever():
    pass
basic.forever(on_forever)
