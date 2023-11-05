from tello import *

def set_speed(speed):
    """sets the speed of the drone 10cm/s-100cm/s"""
    assert (speed >= 10), "Speed is less than 10cm/s (valid range is 10cm/s-100cm/s)."
    assert (speed <= 100), "Speed is more than 100cm/s (valid range is 10cm/s-100cm/s)."
    response = send_and_wait('speed %d' % (speed))

def curve(xi, yi, zi, xf, yf, zf, speed):
    """moves in a curve, (x1, y1, z1, x2, y2, z2, speed) x, y and z are between -500-500"""
    assert (xi >= -500), "The value is not good."
    assert (xi <= 500), "The value is not good."
    assert (xf >= -500), "The value is not good."
    assert (xf <= 500), "The value is not good."
    assert (yi >= -500), "The value is not good."
    assert (yi <= 500), "The value is not good."
    assert (yf >= -500), "The value is not good."
    assert (yf <= 500), "The value is not good."
    assert (zi >= -500), "The value is not good."
    assert (zi <= 500), "The value is not good."
    assert (zf >= -500), "The value is not good."
    assert (zf <= 500), "The value is not good."
    assert (speed >= 10), "Speed is less than 10cm/s (valid range is 10cm/s-100cm/s)."
    assert (speed <= 100), "Speed is more than 100cm/s (valid range is 10cm/s-100cm/s)."
    response = send_and_wait('curve %d %d %d %d %d %d %d' % (xi, yi, zi, xf, yf, zf, speed))

start()

start_video()

power = get_battery()
print("Power Level: ", power, "%")
print(send_and_wait("sdk?"))

takeoff()
set_speed(100)
clockwise(90)
up(50)
anticlockwise(90)
curve(10, 0, -50, 0, -50, 0, 100)


land()

