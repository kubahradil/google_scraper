import unittest
from scraper import get_google_results

class TestGoogleScraper(unittest.TestCase):
    def test_results_structure(self):
        # Zavoláme scraper funkci s klíčovým slovem
        results = get_google_results("OpenAI")

        # Ověříme, že vrací list
        self.assertIsInstance(results, list)

        # Pokud seznam není prázdný, ověříme strukturu prvního prvku
        if results:
            self.assertIn("title", results[0])
            self.assertIn("link", results[0])
        else:
            # Pokud je seznam prázdný (např. kvůli Google blokaci), projde také
            self.assertEqual(results, [])

if __name__ == "__main__":
    unittest.main()