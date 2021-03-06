#!/usr/bin/env python

import unittest

import fracttypes
import absyn

class Test(unittest.TestCase):
    def testNumber(self):
        n = absyn.Number("1",None)
        self.assertEqual(fracttypes.Int, n.datatype)
        self.assertEqual(1, n.leaf)
        
        n = absyn.Number("1.0",None)
        self.assertEqual(fracttypes.Float, n.datatype)
        self.assertEqual(1.0,n.leaf)

        n = absyn.Number("1e0", None)
        self.assertEqual(fracttypes.Float, n.datatype)
        self.assertEqual(1.0,n.leaf)

        n = absyn.Number("1.", None)
        self.assertEqual(fracttypes.Float, n.datatype)
        self.assertEqual(1.0,n.leaf)

        n = absyn.Number("10000000000000.0", None)
        self.assertEqual(fracttypes.Float, n.datatype)
        self.assertEqual(10000000000000.0,n.leaf)

def suite():
    return unittest.makeSuite(Test,'test')

if __name__ == '__main__':
    unittest.main(defaultTest='suite')

