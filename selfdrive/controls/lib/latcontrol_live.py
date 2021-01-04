from common.op_params import opParams, ENABLE_LAT_PARAMS, WHICH_LAT_CTRL
from selfdrive.controls.lib.latcontrol_pid import LatControlPID
from selfdrive.controls.lib.latcontrol_indi import LatControlINDI
from selfdrive.controls.lib.latcontrol_lqr import LatControlLQR

class LatControlLive():
    def __init__(self, CP, OP=None):
        self.CP = CP

        if OP is None:
            OP = opParams()
        
        self.op_params = OP

        self.pid = LatControlPID(CP, OP=self.op_params)
        self.indi = LatControlINDI(CP, OP=self.op_params)
        self.lqr = LatControlLQR(CP, OP=self.op_params)

        self.ctrl_type = ''
        self.ctrl = None
        self._update_control()

    def _select_ctrl(self, ctrl_type):
        if ctrl_type == 'pid':
            self.ctrl_type = 'pid'
            self.ctrl = self.pid
        elif ctrl_type == 'indi':
            self.ctrl_type = 'indi'
            self.ctrl = self.indi
        elif ctrl_type == 'lqr':
            self.ctrl_type = 'lqr'
            self.ctrl = self.lqr

    def _update_control(self):
        if self.op_params.get(ENABLE_LAT_PARAMS):
            self._select_ctrl(self.op_params.get(WHICH_LAT_CTRL))
        else:
            self._select_ctrl(self.CP.lateralTuning.which())
    
    @property
    def angle_steers_des(self):
        return self.ctrl.angle_steers_des

    def reset(self):
        self.pid.reset()
        self.indi.reset()
        self.lqr.reset()

    def update(self, active, CS, CP, path_plan):
        self._update_control()
        return self.ctrl.update(active, CS, CP, path_plan)