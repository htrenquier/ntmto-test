from django.test import TestCase
import mfalcon.r2d2

# Create your tests here.
class R2D2TestCase(TestCase):

    def test_r2d2(self):
        self.falcon_data = {
            "autonomy": 6,
            "departure": "Tatooine",
            "arrival": "Endor",
            "routes_db": 'universe.db'
        }
        self.empire_data = {
            "countdown": 23,
            "bounty_hunters": [
                {"planet": "Tatooine", "day": 1},
                {"planet": "Tatooine", "day": 2},
                {"planet": "Dagobah", "day": 7},
                {"planet": "Hoth", "day": 7},
                {"planet": "Hoth", "day": 8},
                {"planet": "Endor", "day": 8},
                {"planet": "Endor", "day": 9},

            ]
        }
        self.r2 = mfalcon.r2d2.R2D2(self.falcon_data, self.empire_data)
        print("Test R2D2", self.r2.get_journey(), self.r2.get_odds())
        self.assertEqual(self.r2.get_odds(), 100)
        self.assertEqual(self.r2.get_journey(), ([('Tatooine', ' (Departure)'), 
                                                  ('Dagobah', ''), ('Dagobah', ' (refuel)'), ('Tatooine', ''), 
                                                  ('Tatooine', ' (refuel)'), ('Dagobah', ''), ('Dagobah', ' (refuel)'), 
                                                  ('Hoth', ''), ('Endor', '')], 0))
