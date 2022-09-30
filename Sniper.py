import cv2
import mss
from numpy import array

with mss.mss() as sct:
    # Part of the screen to capture
    monitor_number = -1
    mon = sct.monitors[monitor_number]
    monitor = {
        "top": mon["height"] // 2 - 100,  # 100px from the top
        "left": mon["width"] // 2 - 100,  # 100px from the left
        "width": 200,
        "height": 200,
        "mon": monitor_number,
    }
    while "not q":
        img = array(sct.grab(monitor))
        # Display the picture
        cv2.imshow("OpenCV/Numpy normal", cv2.resize(img, (400, 400), interpolation=cv2.INTER_AREA))
        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
