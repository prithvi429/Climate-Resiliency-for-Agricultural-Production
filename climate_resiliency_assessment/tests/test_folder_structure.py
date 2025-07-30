import os
import unittest

class TestFolderStructure(unittest.TestCase):
    def setUp(self):
        # Set project root assuming this script is in climate_resiliency_assessment/tests
        self.project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        self.base = os.path.join(self.project_root, 'climate_resiliency_assessment')

    def test_directory_structure(self):
        expected_directories = [
            os.path.join(self.project_root, 'climate_resiliency_assessment', 'src'),
            os.path.join(self.project_root, 'climate_resiliency_assessment', 'tests'),
            os.path.join(self.project_root, 'climate_resiliency_assessment', 'data'),
            os.path.join(self.project_root, 'climate_resiliency_assessment', 'data', 'raw'),
            os.path.join(self.project_root, 'climate_resiliency_assessment', 'data', 'processed')
        ]
        for directory in expected_directories:
            with self.subTest(directory=directory):
                self.assertTrue(os.path.isdir(directory), f"Directory {directory} does not exist.")

    def test_file_existence(self):
        expected_files = [
            os.path.join(self.project_root, 'README.md'),
            os.path.join(self.project_root, 'requirements.txt')
        ]
        for file in expected_files:
            with self.subTest(file=file):
                self.assertTrue(os.path.isfile(file), f"File {file} does not exist.")

if __name__ == '__main__':
    unittest.main()
