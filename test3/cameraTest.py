from djitellopy import Tello
import cv2

my_drone = Tello()
my_drone.connect()
print(my_drone.get_battery())
my_drone.streamon()
while True:
    # Read a frame from the video stream
    img = my_drone.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    # Display the frame
    cv2.imshow("Image", img)
    # Check for key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
my_drone.streamoff()
my_drone.land()