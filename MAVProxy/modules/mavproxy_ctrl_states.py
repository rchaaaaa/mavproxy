 #!/usr/bin/env python
'''CtrlStates'''

import time, os

from MAVProxy.modules.lib import mp_module
from pymavlink import mavutil
import sys, traceback
import rospy
from swarm_traj_msgs.msg import ControlState

# print(mavutil.__file__)

class CtrlStatesModule(mp_module.MPModule):
    def __init__(self, mpstate):
        super(CtrlStatesModule, self).__init__(mpstate, "CtrlStates", "CtrlStates module")
        self.pub=rospy.Publisher('control_state',ControlState,queue_size=10)
        print("control state name: ",self.pub.resolved_name)
        '''initialisation code'''

    def mavlink_packet(self, m):
        'handle a mavlink packet'''
        # print(m.get_type())
        # print(m.get_msgId())
        if m.get_type() == 'CTRL_STATES':
            # print("got control state msg, x_target: %(x).2f" %m.x_target)
            control_state_=ControlState()
            control_state_.pos.x=m.x
            control_state_.pos.y=m.y
            control_state_.pos.z=m.z
            control_state_.vel.x=m.vx
            control_state_.vel.y=m.vy
            control_state_.vel.z=m.vz
            control_state_.att.x=m.roll
            control_state_.att.y=m.pitch
            control_state_.att.z=m.yaw
            control_state_.rate.x=m.roll_speed
            control_state_.rate.y=m.pitch_speed
            control_state_.rate.z=m.yaw_speed

            control_state_.pos_target.x=m.x_target
            control_state_.pos_target.y=m.y_target
            control_state_.pos_target.z=m.z_target
            control_state_.vel_target.x=m.vx_target
            control_state_.vel_target.y=m.vy_target
            control_state_.vel_target.z=m.vz_target
            control_state_.att_target.x=m.roll_target
            control_state_.att_target.y=m.pitch_target
            control_state_.att_target.z=m.yaw_target
            control_state_.rate_target.x=m.roll_speed_target
            control_state_.rate_target.y=m.pitch_speed_target
            control_state_.rate_target.z=m.yaw_speed_target
            
            self.pub.publish(control_state_)

            

def init(mpstate):
    '''initialise module'''
    return CtrlStatesModule(mpstate)