"""
plc主轴间距配置
"""
import qte.processdata
import stone_cnc.parameter.parameter as parameter
from hy_four_channels.hal.runtime.processdata import write_process_data

def _get_x_y_min_max_distance():
    x_min = parameter.write_spindle_distance_parameter("x_min_distance")
    x_max = parameter.write_spindle_distance_parameter("x_max_distance")

    y_min = parameter.write_spindle_distance_parameter("y_min_distance")
    y_max = parameter.write_spindle_distance_parameter("y_max_distance")

    return (x_min, x_max, y_min, y_max)

def _build_send_struct(x_min, x_max, y_min, y_max):
    result = {
        "ttt": {
            "XMIN":x_min, 
            "XMAX":x_max,
            "YMIN":y_min, 
            "YMAX":y_max,
            }
        }
    return result


def set_plc_spindle_distance():
    x_min, x_max, y_min, y_max = _get_x_y_min_max_distance()

    write_process_data("spindle_distance_check_config", _build_send_struct(x_min, x_max, y_min, y_max))


qte.processdata.ready.connect(set_plc_spindle_distance)