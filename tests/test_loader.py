import unittest
from loader import Loader


class Test_test_loader(unittest.TestCase):

    def test_lopad_stl(self):
        loader = Loader()
        unit = loader.load_stl("test.stl")

        self.assertEqual(12, len(unit.polygons))


if __name__ == '__main__':
    unittest.main()
