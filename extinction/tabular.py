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
import os

STD_V = {}
STD_BV = {}

# Table of values from: 
# http://vizier.cfa.harvard.edu/viz-bin/Cat?J/PAZh/34/21#sRM2.1

__file_with_standards = os.path.join("extinction", "standards.dat")

try:
    file = open(__file_with_standards, 'r')
except IOError:
    import sys
    print "File %s does not exists." % __file_with_standards
    print __file_with_standards
    sys.exit(True)

for row in [line.split()[1:] for line in file]:
    do_key = lambda lumin: "%s%d" % (row[0], lumin) 
    
    for lumin in (1, 3, 5):
        key = do_key(lumin)
        STD_V[key], STD_BV[key] = map(float, (row[lumin], row[lumin+1]))

def av_tabular(t_class, s_class, l_class, b_v):
    """
    @param t_class: Temperature class, from list 'OBAFGKM'.
    @type t_class: string.
    @param s_class: Temperature subclass, from 0 to 9.
    @type s_class: onteger.
    @param l_class: Luminosity class, like 1, 3 or 5.
    @type l_class: integer.
    @param b_v: B-V value.
    @type b_v: float.
    
    @return a_v: full extinction value in visual band.
    @type a_v: float.
    
    @author: Alexey Smirnov
    @note: computations are based on next paper results: "Inaccuracies in the 
    spectral classification of stars from the Tycho-2 Spectral Type Catalogue", 
    Tsvetkov, A. S.; Popov, A. V.; Smirnov, A. A., 
    Astronomy Letters, Volume 34, Issue 1, pp.17-27
    """

    t_class_basis = tuple('OBAFGKM')
    s_class_basis = range(10)
    l_class_basis = (1, 3, 5)

    if t_class not in t_class_basis:
        raise NameError("Temperature class %s is not in range %s" % 
                        (t_class, t_class_basis))
    if s_class not in s_class_basis:
        raise NameError("Temperature subclass %s is not in range %s" % 
                        (s_class, s_class_basis))
    if l_class not in l_class_basis:
        raise NameError("Luminosity class %s is not in range %s" % 
                        (l_class, l_class_basis))

    do_key = lambda *args: "%s%d%d" % args
    key = do_key(t_class, s_class, l_class)
    
    e_b_v = b_v - STD_BV[key]
    r_const = 3.30 + 0.28 * STD_BV[key] + 0.4 * e_b_v
    a_v = r_const * e_b_v 
    
    return a_v    
