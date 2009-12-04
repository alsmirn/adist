#!/usr/bin/env python

from extinction import arenou, tabular
import extinction

def photo_dist(v_band, b_v, t_class, s_class, l_class, **kwargs):
    """
    Positional arguments:
    @param v_band: visual magnitude
    @param b_v: B-V value. Float. 
    @param t_class: Temperature class, from list 'OBAFGKM'. String.
    @param s_class: Temperature subclass, from 0 to 9. Integer.
    @param l_class: Luminosity class, like 1, 3 or 5. Integer.
   
    Keyword arguments:
    @param extinction: use some extinction model or no, ('arenou', 'tabular')  
    @param dist: some distance to star in parsecs. Float.
    @param l: galactic longitude. Float.
    @param b: galactic latitude. Float.
    
    @return photo_dist: photometric distance in parsecs.
    
    @author: Alexey Smirnov
    """
    #@TODO: params check!
    __params = ('extinction', 'dist', 'l', 'b', )
    
    # full extinction
    a_v = float(0)
    
    # interstellar extinction mode
    extinction = kwargs.pop('extinction')
    
    if extinction == 'arenou':
        dist = kwargs.pop('dist')
        l = kwargs.pop('l')
        b = kwargs.pop('b')
        
        a_v = arenou.av_arenou(dist, l, b)
        
    elif extinction == 'tabular':
        a_v = tabular.av_tabular(t_class, s_class, l_class, b_v)
        
    else:
        a_v = float(0)
        
    do_key = lambda *args: "%s%d%d" % args
    TSL = do_key(t_class, s_class, l_class)
    
    photo_dist = 10.0**(0.2*(v_band - tabular.STD_V[TSL] - a_v + 5.0))
        
    return photo_dist  

def main():
    from time import time
    from random import randint
    beg = time()
    for i in xrange(1000000):
        photo_dist(10, 4, 'O', 7, 5, extinction='arenou', 
                   dist=randint(0,1000), l=randint(0,361), b=randint(-90,91))
    print time() - beg
    
main()
