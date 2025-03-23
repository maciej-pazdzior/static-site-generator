import unittest

from page_generator import extract_title

class TestPageGenerator(unittest.TestCase):
    def test_title_extraction(self):
        md = """
        # Heading 1

        ## Heading 2

        ### Heading 3

        #### Heading 4

        ##### Heading 5

        ###### Heading 6
            """
        title = extract_title(md)
        self.assertEqual(
            title,
            "Heading 1",
        )

if __name__ == "__main__":
    unittest.main()