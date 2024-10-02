from unittest import TestCase

from shared.utils import modeling


class TestModeling(TestCase):
    def test_generate_uuid(self):
        self.assertEqual(len(modeling.generate_uuid()), 36)
