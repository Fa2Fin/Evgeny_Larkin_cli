import os
import unittest
import shutil
from unittest.mock import patch, MagicMock
import func
class TestFileManager(unittest.TestCase):

    def setUp(self):
        self.test_dir = 'test_dir'
        self.test_file = 'test_file.txt'
        os.mkdir(self.test_dir)
        with open(self.test_file, 'w') as f:
            f.write('Hello, world!')

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_list_directory(self):
        with patch('os.listdir', return_value=[self.test_file, self.test_dir]):
            with patch('builtins.print') as mocked_print:
                func.list_directory()
                mocked_print.assert_called()

    def test_change_directory_success(self):
        with patch('os.chdir') as mocked_chdir:
            func.change_directory(self.test_dir)
            mocked_chdir.assert_called_with(self.test_dir)

    def test_change_directory_file_not_found(self):
        with patch('os.chdir', side_effect=FileNotFoundError):
            with patch('builtins.print') as mocked_print:
                func.change_directory('non_existent_dir')
                mocked_print.assert_called_with("Ошибка: Указанный путь не найден.")

    def test_copy_file_success(self):
        dest_file = 'test_file_copy.txt'
        func.copy_file(self.test_file, dest_file)
        self.assertTrue(os.path.exists(dest_file))
        os.remove(dest_file)

    def test_copy_file_not_found(self):
        with patch('shutil.copy', side_effect=FileNotFoundError):
            with patch('builtins.print') as mocked_print:
                func.copy_file('non_existent_file.txt', 'dest.txt')
                mocked_print.assert_called_with("Ошибка: Исходный файл не найден.")

    def test_move_file_success(self):
        dest_file = 'test_file_moved.txt'
        func.move_file(self.test_file, dest_file)
        self.assertFalse(os.path.exists(self.test_file))
        self.assertTrue(os.path.exists(dest_file))
        os.remove(dest_file)

    def test_remove_file_success(self):
        func.remove_file(self.test_file)
        self.assertFalse(os.path.exists(self.test_file))

    def test_remove_directory_success(self):
        os.mkdir('test_sub_dir')
        func.remove_file('test_sub_dir')
        self.assertFalse(os.path.exists('test_sub_dir'))

if __name__ == '__main__':
    unittest.main()