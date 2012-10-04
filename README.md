ABOUT
=====

"adist" is an astronomical library for photometric distances calculation. 

Implemented different extinction models: 

 - Arenou 3d model from Arenou F. et al. work "A tridimensional model of the 
 galactic interstellar extinction" published in Astronomy and Astrophysics 
 (ISSN 0004-6361), vol. 258, no. 1, p. 104-111.
 
 - Tabular model from Tsvetkov A. S. et al. work "Inaccuracies in the spectral 
 classification of stars from the Tycho-2 Spectral Type Catalogue", published 
 in Astronomy Letters, Volume 34, Issue 1, pp.17-27. 


USAGE
=====

>>> from adist import photo_dist
>>> v_mag = 10.0
>>> t_class, s_class, l_class = 'G', 5, 5

>>> # with no extinction
>>> photo_dist(v_mag, t_class, s_class, l_class)

>>> # Arenou scheme
>>> photo_dist(v_mag, t_class, s_class, l_class, extinction='arenou', 
		dist=240.5, l=240.0, b=30.4)
>>> # tabular scheme
>>> photo_dist(v_mag, t_class, s_class, l_class, extinction='tabular', 
		b_v=0.5)


VERSIONS
========

v0.1.1
------
 - fix photo_dist function interface (b_v parameter)

v0.1 - first release
--------------------

TODO
====

 - realize another extinction models.


AUTHOR/CONTACTS
===============

Alexey Smirnov is a postgraduate student in Saint-Petersburg State University, 
RUSSIA. Contact with: alsmirn@gmail.com.
