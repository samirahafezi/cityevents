from django.test import TestCase

class AnimalTestCase(TestCase):
    def test_animals_can_walk(self):
        assert sum([1, 2, 3]) == 8, "Should be 6"
