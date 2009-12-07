#!/usr/bin/env python
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

from extinction import arenou, tabular

def photo_dist(v_band, b_v, t_class, s_class, l_class, **kwargs):
    """
    @param v_band: visual magnitude. 
    @param b_v: B-V value. 
    @param t_class: Temperature class, from list 'OBAFGKM'.
    @param s_class: Temperature subclass, from 0 to 9. 
    @param l_class: Luminosity class, like 1, 3 or 5.
   
    @keyword extinction: use some extinction model or no, ('arenou', 'tabular')
    @keyword dist: some distance to star in parsecs.
    @keyword l: galactic longitude.
    @keyword b: galactic latitude.
    
    @return photo_dist: photometric distance in parsecs.
    @type photo_dist: float.
    
    @author: Alexey Smirnov
    """
    
    # full extinction
    a_v = float(0)
    
    # interstellar extinction mode detection
    try:
        extinction = kwargs.pop('extinction')
    except KeyError:
        extinction = str("No extinction models used.")
    
    # extinction model choice
    if extinction == 'arenou':
        try: 
            dist = kwargs.pop('dist')
            l = kwargs.pop('l')
            b = kwargs.pop('b')
        except KeyError:
            print "Not enough arguments to applying %s method." % extinction
            import sys
            sys.exit(True)
        a_v = arenou.av_arenou(dist, l, b)
    elif extinction == 'tabular':
        a_v = tabular.av_tabular(t_class, s_class, l_class, b_v)
    else:
        a_v = float(0)
        
    do_key = lambda *args: "%s%d%d" % args
    TSL = do_key(t_class, s_class, l_class)
    
    photo_dist = 10.0**(0.2 * (v_band - tabular.STD_V[TSL] - a_v + 5.0))
    
    return photo_dist  

def main():
    from time import time
    from random import randint
    beg = time()
    for i in xrange(100000):
        photo_dist(10, 4, 'O', 7, 5, extinction='arenou', 
                   dist=randint(0,1000), l=randint(0,361), b=randint(-90,91))
        #photo_dist(10, 4, 'O', 7, 5, extinction='tabular', )
    print time() - beg
    
main()
