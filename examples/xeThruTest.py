from utils.XeThru_utils.xeThruX4_interface import xeThruX4SensorInterface
from utils.XeThru_utils.xeThruX4_algorithm import *
import matplotlib.pyplot

if __name__ == '__main__':
    X4M300 = xeThruX4SensorInterface()

    X4M300.config_x4_sensor(device_name='COM8', min_range=0, max_range=0.15,
                            center_frequency=3, FPS=1, baseband=False)

    X4M300.clear_xep_buffer()
    counter = 0
    while 1:
        frame = X4M300.read_frame()
        if frame is not None:
            counter += 1
            print(counter)
            print(frame)
            plt.plot(frame)
            plt.title("fast time index example")
            plt.xlabel("fast time index")
            plt.ylabel("amplitude")

            plt.show()
            history = np.array(X4M300.frame_history)
