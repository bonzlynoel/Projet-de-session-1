import unittest
import coordonnees_clou as cc


def test_calculer_reflexion_point_1():
    assert cc.calculer_reflexion_point((2,4),'x')==(2,-4)

def test_calculer_reflexion_point_2():
    assert cc.calculer_reflexion_point((2,4),'y')==(-2,4)


def test_calculer_rotate_point():
    assert cc.calculer_rotate_point((2,4),30,(0,0))==(-0.27,4.46)


def test_calculer_inclinaison_point_1():
    assert cc.calculer_inclinaison_point((2,4),5,'x')==(2.35,4.0)

def test_calculer_inclinaison_point_2():
    assert cc.calculer_inclinaison_point((2,4),5,'y')==(2.0,4.17)


def test_calculer_coordonnees_clou():
    assert cc.calculer_coordonnees_clou(3,10,1,0.75,2)==[('pt_0', (-5.0, 0.5)), ('pt_1', (-5.0, -0.5)), ('pt_2',
 (-5.75, -1.5)), ('pt_3', (-5.75, 1.5)), ('pk_0', (7.0, 0)), ('pk_1', (5.0, -0.5)), ('pk_2', (5.0,0.5))]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
