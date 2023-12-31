from tello import *

def inchesToCm(inches):
    return inches*2.54

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

power = get_battery()
print("Power Level: ", power, "%")

takeoff()
set_speed(100)
up(120)
forward(inchesToCm(115))
right(inchesToCm(10))
flip_forward()
#clockwise(180)
backward(inchesToCm(130))
#left(inchesToCm(10))

land()