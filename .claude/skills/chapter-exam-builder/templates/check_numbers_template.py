# -*- coding: utf-8 -*-
"""Mau tinh dap so DOC LAP voi loi giai. Moi cau mot khoi; in ket qua de doi chieu bang mat va
dung assert de bao ve cac so lieu da dua vao de. Chay truoc khi viet loi giai.
"""
from math import pi, sqrt

R = {}
R['mcq1'] = 30 / 6                      # 5 m/s
R['ess1_t'] = 120 / (40 + 20)           # 2 h
R['ess1_x'] = 40 * R['ess1_t']          # 80 km

assert abs(R['mcq1'] - 5) < 1e-9 and abs(R['ess1_t'] - 2) < 1e-9 and abs(R['ess1_x'] - 80) < 1e-9
for k, v in R.items():
    print(k, v)
