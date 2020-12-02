import unittest

from package1.login import login
from package1.signup import signup
from package2.payment1 import DebitCard
from package2.payment2 import CreditCard

test1 = unittest.TestLoader().loadTestsFromTestCase(login)
test2 = unittest.TestLoader().loadTestsFromTestCase(signup)
test3 = unittest.TestLoader().loadTestsFromTestCase(DebitCard)
test4 = unittest.TestLoader().loadTestsFromTestCase(CreditCard)

#Test suite

tsuite = unittest.TestSuite([test1,test3,test2,test4])

unittest.TextTestRunner().run(tsuite)

