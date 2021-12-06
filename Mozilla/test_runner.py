import unittest
import test1
import test2
import test3

YandexTestSuite = unittest.TestSuite()
YandexTestSuite.addTest(unittest.makeSuite(test1.YandexMailNoPass))
YandexTestSuite.addTest(unittest.makeSuite(test2.YandexMailWrongPass))
YandexTestSuite.addTest(unittest.makeSuite(test3.YandexMailRightPass))
print("count of tests: " + str(YandexTestSuite.countTestCases()) + "\n")

runner = unittest.TextTestRunner(verbosity=2)
runner.run(YandexTestSuite)