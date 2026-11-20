function go_forward (speed: number) {
    init()
    TinkerBott.motors(ltrim * speed, rtrim * speed)
}
function go_backward (speed2: number) {
    init()
    TinkerBott.motors((0 - ltrim) * speed2, (0 - rtrim) * speed2)
}
function init () {
    rtrim = 1
    ltrim = 1
}
let rtrim = 0
let ltrim = 0
go_forward(100)
basic.pause(5000)
TinkerBott.stopcar()
basic.forever(function () {
	
})
