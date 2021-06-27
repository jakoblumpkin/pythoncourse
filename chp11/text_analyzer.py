import unittest
import os


def analyze_text(filename):
    """Calculate the number of lines and characters in a file.
    
    Args:
       filename: The name of the file analyze.
    
    Raises:
        I0Error: If ''filename'' does not exist or can't be read.
        
    Returns: A tuple where the first element is the number od lines in
       the file and the second element is the number of charactors.
    """
    lines = 0
    chars = 0
    with open(filename, 'r') as f:
        for line in f:
            lines += 1
            chars += len(line)
    return (lines, chars)

class TestAnalysisTests(unittest.TestCase):
    """Tests for the ''analyze_text'' function"""

    def setUp(self):
        """Fixture that creates a file for the text methods to use."""
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('Now we are engaged in a great civil war.\n'
                     'testing wether that nation,\n'
                     'or any nation so conceived and so dedicated,\n'
                     'can long endure')
    def tearDown(self):
        """Fixture that deletes the files used by the test methods."""
        try:
            os.remove(self.filename)
        except:
            pass

    def test_function_runs(self):
        """Basic smoke test: does the function run."""
        analyze_text(self.filename)

    def test_line_count(self):
        """Check that the line count is correct"""
        self.assertEqual(analyze_text(self.filename)[0], 4)
    
    def test_charactor_count(self):
        """Check that the character count is correct."""
        self.assertEqual(analyze_text(self.filename)[1], 131)
    
    def test_no_such_file(self):
        """Check proper exception is thrown for missing file."""
        with self.assertRaises(I0Error):
           analyze_text('foobar')
        
if __name__ == '__main__':
    unittest.main()