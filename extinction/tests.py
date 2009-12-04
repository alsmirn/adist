'''
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
'''
import sys
import unittest
from unittest import TestCase

try:
    from arenou import *
except ImportError:
    print "Cannot import arenou module, check existence!"
    sys.exit(True)

class ArenouTestCase(TestCase):
    """
    Arenou module test case.
    @author: Alexey Smirnov
    """
    def test_negative_result(self):
        """Arenou function _must_ return only positive result"""
        self.assert_(av_arenou(100.0, 110.0, 30.0) >= 0.0) 
        
    def test_factors_is_all(self):
        """Test integrity of ARENOU_FACTORS data"""
        self.assert_(len(ARENOU_FACTORS) == 4)
        
        for elem in xrange(len(ARENOU_FACTORS)):
            self.assert_(len(ARENOU_FACTORS[elem]) == 200)    
    
    def test_plates_is_all(self):
        """Test integrity of PLATES_DESCRIPTION data"""
        current_seq, origin_seq = [], set(xrange(1, 200))

        for plates_set in PLATES_DESCRIPTION.values():
            for elem in plates_set:
                current_seq.append(elem[1])
        
        current_seq = set(current_seq) 
        self.assert_(current_seq==origin_seq)
    
    def test_plates_coverage(self):
        """Test whole coverage of plates"""
        try:
            [av_arenou(10.0, l, b) for b in (-90, 90+1) for l in xrange(360+1)]
        except TestCase.failureException, e:
            print e
            
if __name__ == '__main__':
    unittest.main()

