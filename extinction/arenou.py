"""
Copyright (c) 2009, Alexey Smirnov
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the Saint-Petersburg State University nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY ALEXEY SMIRNOV ''AS IS'' AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL ALEXEY SMIRNOV BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

#199, 4
ARENOU_FACTORS = (
    # Alpha coefficients
    (float(), # hack: fill zero position in list
    2.22534, 3.35436, 2.77637, 4.44190, 4.46685, 7.63699, 2.43412, 3.34481,
    1.40733, 1.64466, 2.12696, 2.34636, 2.77060, 1.96533, 1.93622, 1.05414,
    1.39990, 2.73481, 2.99784, 3.23802, 1.72679, 1.88890, 1.98973, 1.49901,
    0.90091, 1.94200,-0.37804,-0.15710, 3.20162, 1.95079, 1.91200, 2.50487,
    2.44394, 2.82440, 3.84362, 0.60365, 0.58307, 2.03861, 1.14271, 0.79908,
    0.94260, 1.66398, 1.08760, 1.20087, 1.13147, 1.97804, 1.40086, 2.06355,
    1.59260, 1.45589, 2.56438, 3.24095, 2.95627, 1.85158, 1.60770, 0.69920,
    1.36189, 0.33179, 1.70303, 1.97414, 1.07407, 1.69495, 1.51449, 1.87894,
    1.43670, 6.84802, 4.16321, 0.78135, 0.85535, 0.52521, 0.88376, 0.42228,
    0.71318, 0.99606, 0.91519, 0.85791, 1.44226, 2.55486, 3.18047, 2.11235,
    1.75884, 1.97257, 1.41497, 1.17795, 2.62556, 3.14461, 4.26624, 2.54447,
    2.27030, 1.34359, 1.76327, 2.20666, 1.50130, 2.43965, 3.35775, 2.60621,
    2.90112, 2.55377, 3.12598, 3.66930, 2.15465, 1.82465, 1.76269, 1.06085,
    1.21333, 0.58326, 0.74200, 0.67520, 0.62609, 0.61415, 0.58108, 0.68352,
    0.61747, 1.06827, 1.53631, 1.94300, 1.22185, 1.79429, 2.29545, 2.07408,
    2.94213, 3.04627, 3.78033, 2.18119, 1.45372, 1.05051, 0.48416, 0.61963,
    4.40348, 2.50938, 0.44180, 3.96084, 2.53335, 2.03760, 1.06946, 0.86348,
    0.30117, 0.75171, 1.97427, 1.25208, 0.89448, 0.81141, 0.83781, 1.10600,
    1.37040, 1.77590, 1.20865, 2.28830, 3.26278, 2.58100, 6.23279, 4.47693,
    1.22938, 0.84291, 0.23996, 0.40062, 0.56898,-0.95721,-0.19051, 2.31305,
    1.39169, 1.59418, 1.57082, 1.95998, 2.59567, 5.30273, 2.93960, 1.65864,
    1.71831, 1.33617,-0.31330, 1.51984,-0.50758, 1.25864, 1.54243, 2.72258,
    2.81545, 2.23818, 1.38587, 2.28570, 1.36385, 0.05943, 1.40171, 0.14718,
    0.57124, 3.69891, 1.19568, 0.69443, 1.11811, 1.10427,-0.42211, 0.87576,
    1.27477, 1.19512, 0.97581, 0.54379,-0.85054, 0.74347, 0.77310),
    
    # Beta coefficients
    (float(), # hack: fill zero position in list
    -6.00212,-14.74567, -9.62706,-19.92097,-26.07305,-46.10856,-8.69913, 
    -13.93228,-3.43418, -3.97380, -6.05682, -8.17784, -9.52310,-5.63251,
    -13.31757,-2.36540, -1.35325,-11.70266,-11.64272,-11.63810,-6.05085,
    -5.51861, -4.86206, -3.75837, -1.30459, -6.26833, 10.77372, 5.03190,
    -10.59297,-4.73280, -4.97640, -8.63106, -9.17612, -4.78217,-8.04690,
    0.07893,  -0.21053, -4.40843, -1.35635,  1.48074,  8.16346, 0.26775,
    -1.02443, -2.45407, -1.87916, -2.92838, -1.12403, -3.68278,-2.18754,
    -1.90598, -2.31586, -2.78217, -2.57422, -0.67716,  0.35279,-0.09146,
    -1.05290,  0.37629, -0.75246, -1.59784, -0.40066, -1.00071,-0.08441,
    -0.73314,  0.67706, -5.06864, -5.80016, -0.27826,  0.20848, 0.65726,
    -0.44519, -0.26304, -0.67229, -0.70103, -0.39690, -0.29115,-1.09775,
    -1.68293, -2.69796, -1.77506, -1.38574,  1.55545, -1.05722,-0.95012,
    -1.11097, -1.01140, -1.61242, -0.12771, -0.68720, -0.05416,-0.26407,
    -0.41651, -0.09855, -0.82128, -1.16400, -0.68687, -0.97988,-0.71214,
    -1.21437, -2.29731, -0.70690, -0.60223, -0.35945, -0.14211,-0.23225,
    -0.06097, -0.19293, -0.21041, -0.25312, -0.13788,  0.01195,-0.10743,
     0.02675, -0.26290, -0.36833, -0.71445, -0.40185, -0.48657,-0.84096,
    -0.64745, -2.09258,  7.71159, -3.91956, -2.4050,  -0.49522,-1.01704,
    -0.27182,  0.41697, -2.95611, -0.56541,  1.58923, -3.37374,-0.40541,
    -0.66317, -0.87395, -0.65870, -0.16136, -0.57143, -2.02654,-1.47763,
    -0.43870, -0.51001, -0.44138, -0.86263, -1.02779, -1.26951,-0.70679,
    -1.71890, -0.94181, -1.69237,-10.30384, -7.28366, -1.19030,-1.59338,
    0.06304,  -1.75628, -0.53331, 11.69217,  1.45670, -7.82531,-1.72984,
    -1.28296, -1.97295, -3.26159, -4.84133, -7.43033, -6.48049,-9.99317,
    -7.25286,-10.39799,  1.35622, -8.69502,  4.73320,-12.59627,-3.76065,
    -7.47806, -5.52139,  0.81772, -9.06536, -9.88812, -8.10127,-1.08126,
    -3.21783,  3.92670, -4.30242,-19.62204, -0.45043, -0.27600, 0.71179,
    -2.37654,  5.24037, -4.38033, -4.98307, -6.58464, -4.89869,-0.84403,
    13.01249, -1.39825, -4.4500),

    # r0
    (float(), # hack: fill zero position in list
    0.052, 0.035, 0.042, 0.025, 0.026, 0.014, 0.050, 0.035, 0.091, 0.074,
    0.056, 0.052, 0.145, 0.174, 0.073, 0.223, 0.252, 0.117, 0.129, 0.139,
    0.143, 0.171, 0.205, 0.199, 0.329, 0.155, 0.210, 0.294, 0.151, 0.206,
    0.192, 0.145, 0.133, 0.295, 0.239, 0.523, 0.523, 0.231, 0.421, 0.523,
    0.441, 0.523, 0.523, 0.245, 0.301, 0.338, 0.523, 0.280, 0.364, 0.382,
    0.554, 0.582, 0.574, 1.152, 0.661, 0.952, 0.647, 1.152, 1.132, 0.618,
    1.152, 0.847, 0.897, 1.152, 0.778, 0.676, 0.359, 1.152, 1.152, 1.152,
    0.993, 0.803, 0.530, 0.710, 1.152, 1.152, 0.657, 0.759, 0.589, 0.595,
    0.635, 0.634, 0.669, 0.620, 1.182, 1.555, 1.323, 1.300, 1.652, 2.000,
    2.000, 2.000, 1.475, 1.485, 0.841, 1.897, 1.480, 1.793, 1.287, 0.799,
    1.524, 1.515, 2.000, 2.000, 2.000, 2.000, 1.923, 1.604, 1.237, 2.000,
    2.000, 2.000, 2.000, 2.000, 2.000, 1.360, 1.520, 1.844, 1.365, 1.602,
    0.703, 0.355, 0.482, 0.453, 1.152, 0.516, 0.891, 1.152, 0.745, 1.152,
    0.949, 0.587, 1.152, 1.152, 0.612, 0.655, 0.933, 0.658, 0.487, 0.424,
    1.019, 0.795, 0.949, 0.641, 0.667, 0.699, 0.855, 0.666, 1.152, 0.763,
    0.302, 0.307, 0.516, 0.265, 0.523, 0.114, 0.523, 0.240, 0.376, 0.148,
    0.402, 0.523, 0.398, 0.300, 0.268, 0.357, 0.227, 0.083, 0.118, 0.064,
    0.329, 0.087, 0.250, 0.050, 0.205, 0.182, 0.255, 0.329, 0.076, 0.116,
    0.084, 0.027, 0.218, 0.252, 0.066, 0.094, 0.252, 0.153, 0.085, 0.123,
    0.184, 0.100, 0.128, 0.091, 0.100, 0.207, 0.126, 0.207, 0.08),
    
    # Gamma coefficients
    (float(), # hack: fill zero position in list
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,  0.08336, 0.0, 0.0,
    0.12839, 0.16258, 0.0, 0.0, 0.12847, 0.17698, 0.08567,0.0,0.0, 
    0.42624, 0.0, 0.60387, 0.0, 0.0, 0.0, 0.06013, 0.0, 0.20994, 0.01323,
    0.01961, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00043, 0.03264, 0.03339,
    0.00340, 0.0, 0.0, 0.0, 0.04928, 0.0, 0.0, 0.0, 0.0, 0.01959,0.00298,
    0.0, 0.0, 0.0, 0.15298, 0.33473, 0.14017, 0.20730, 0.08052, 0.0, 0.0,
    0.36962, 0.07459, 0.16602, 0.14437, 0.26859, 0.07661,  0.00849,  0.0,
    0.0, 0.02960, 0.15643, 0.07354, 0.0, 0.0, 0.12750, 0.05490, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.08639, 0.47171, 0.0, 0.0, 0.0,  0.34109,  0.0,  0.0,
    0.29230, 0.09089, 0.07495, 0.00534, 0.0, 0.31600, 0.0, 0.03505, 
    0.02820, 0.03402, 0.05608, 0.06972, 0.02902, 0.22887,  0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0))

PLATES_DESCRIPTION = {
    (-90, -60): (
        ( 29, 1), ( 57, 2), ( 85, 3), (110,  4), (150,  5), (180,  6), 
        (210, 7), (240, 8), (270, 9), (300, 10), (330, 11), (360, 12)),
    (-60, -45): (
        ( 30, 13), ( 60, 14), (110, 15), (180, 16), (210, 17), (240, 18), 
        (270, 19), (300, 20), (330, 21), (360, 22)),
    (-45, -30): (
        ( 30, 23), ( 60, 24), ( 90, 25), (120, 26), (160, 27), (200, 28),
        (235, 29), (265, 30), (300, 31), (330, 32), (360, 33)),
    (-30, -15): (
        ( 20, 34), ( 40, 35), ( 80, 36), (100, 37), (120, 38), (140, 39),
        (160, 40), (180, 41), (200, 42), (220, 43), (240, 44), (260, 45),
        (280, 46), (300, 47), (320, 48), (340, 49), (360, 50)),
    (-15, -5): (
        ( 10, 51), ( 20, 52), ( 30, 53), ( 40, 54), ( 50, 55), ( 60, 56),
        ( 80, 57), ( 90, 58), (100, 59), (110, 60), (120, 61), (130, 62),
        (140, 63), (150, 64), (160, 65), (180, 66), (190, 67), (200, 68),
        (210, 69), (220, 70), (230, 71), (240, 72), (250, 73), (260, 74),
        (270, 75), (280, 76), (290, 77), (300, 78), (310, 79), (320, 80),
        (330, 81), (340, 82), (350, 83), (360, 84)),
    (-5, 5): (
        ( 10,  85), ( 20,  86), ( 30,  87), ( 40,  88), ( 50,  89), ( 60,  90),
        ( 70,  91), ( 80,  92), ( 90,  93), (100,  94), (110,  95), (120,  96),
        (130,  97), (140,  98), (150,  99), (160, 100), (170, 101), (180, 102),
        (190, 103), (200, 104), (210, 105), (220, 106), (230, 107), (240, 108),
        (250, 109), (260, 110), (270, 111), (280, 112), (290, 113), (300, 114),
        (310, 115), (320, 116), (330, 117), (340, 118), (350, 119), 
        (360, 120)),
    (5, 15): (
        ( 10, 121), ( 30, 122), ( 40, 123), ( 50, 124), ( 60, 125), ( 70, 126),
        ( 80, 127), ( 90, 128), (100, 129), (120, 130), (130, 131), (140, 132),
        (160, 133), (170, 134), (200, 135), (210, 136), (230, 137), (240, 138),
        (250, 139), (260, 140), (270, 141), (280, 142), (290, 143), (300, 144),
        (310, 145), (320, 146), (330, 147), (340, 148), (350, 149), 
        (360, 150)),
    (15, 30): (
        ( 20, 151), ( 40, 152), ( 60, 153), ( 80, 154), (100, 155), (140, 156),
        (180, 157), (200, 158), (220, 159), (240, 160), (260, 161), (280, 162),
        (300, 163), (320, 164), (340, 165), (360, 166)),
    (30, 45):(
        ( 20, 167), ( 50, 168), ( 80, 169), (110, 170), (160, 171), (190, 172),
        (220, 173), (250, 174), (280, 175), (320, 176), (340, 177), 
        (360, 178)),
    (45, 60): (
        ( 60, 179), ( 90, 180), (110, 181), (170, 182), (200, 183), (230, 184),
        (290, 185), (330, 186), (360, 187)),
    (60, 90): (
        ( 30, 188), ( 60, 189), ( 90, 190), (120, 191), (150, 192), (180, 193),
        (210, 194), (240, 195), (270, 196), (300, 197), (330, 198), 
        (360, 199))}

def __get_plate_no(b, l):
    """
    @param l: galactic longitude.
    @type l: float.
    @param b: galactic latitude,
    @type b: float.
    
    @return plate_no: unique identifier of plate in (l, b) direction.
    @type plate_no: integer.
    
    @author: Alexey Smirnov
    """
    plate_no = int(0)

    for b_set, l_plate_no_set in PLATES_DESCRIPTION.items():

        b_left, b_right = b_set

        if b_left <= b < b_right:
            
            l_left = float(0)
            for l_plate_no in l_plate_no_set:

                l_right, plate_no = l_plate_no
                
                if l_left <= l < l_right:
                    return plate_no
                else:
                    l_left = l_right
            
    return plate_no

def av_arenou(r, l, b):
    """
    @param r: distance in parsecs.
    @param l: galactic longitude.
    @param b: galactic latitude.
    
    @return a_v: full extinction value in visual band.
    
    @author: Alexey Smirnov
    @note: computations are based on next paper results: "A tridimensional 
    model of the galactic interstellar extinction", 
    Arenou, F.; Grenon, M.; Gomez, A.,
    Astronomy and Astrophysics (ISSN 0004-6361), vol. 258, no. 1, p. 104-111.
    """
    a_v = float()
    plate_no = __get_plate_no(b, l)

    r /= 1000.0 # translate to kiloparsecs
    if r < 0.0: return 0.0

    if r < ARENOU_FACTORS[2][plate_no]:
        a_v = (
            ARENOU_FACTORS[0][plate_no] * r + 
            ARENOU_FACTORS[1][plate_no] * r**2)
    else:
        r0 = ARENOU_FACTORS[2][plate_no]
        a_v = (
            ARENOU_FACTORS[0][plate_no] * r0 + 
            ARENOU_FACTORS[1][plate_no] * r0**2 + 
            ARENOU_FACTORS[3][plate_no] * (r - r0))
       
    # If full extinction below zero then equate them with zero.
    # (Situation happens because some Beta coefficients from ARENOU_FACTORS 
    # are negative).
    a_v = 0.0 if a_v < 0.0 else a_v
    
    return a_v
