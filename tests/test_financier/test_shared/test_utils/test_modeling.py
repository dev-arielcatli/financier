from shared.utils import modeling
from unittest import TestCase

class TestModeling(TestCase):
    def test_generate_uuid(self):
        self.assertEqual(len(modeling.generate_uuid()), 36)