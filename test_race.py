from unittest import TestCase
import Car

from driver import raceTimeOneKm
#this test case is to make sure each of these fucntions
# work correctly and make it through the entire code without pooping itself
class Test(TestCase):
    def test_sim(self):

        assert raceTimeOneKm()==True
        assert raceTimeOneKm() == True
