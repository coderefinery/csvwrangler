import unittest

try:
    from io import StringIO
    from unittest.mock import patch
except ImportError:
    from StringIO import StringIO
    from mock import patch


class TestBaseFunctions(unittest.TestCase):

    @patch("csvwrangler.base_functions.extract_csv_column_by_name")
    def test_read_base(self, patched_function):
        from csvwrangler.base_functions import extract_csv_column
        val = extract_csv_column("something", "idx")
        assert patched_function.called

    def test_extract_csv_column_by_index(self):
        from csvwrangler.base_functions import extract_csv_column_by_index
        file_contents = (
                        "1,2,3\n"
                        "1, 2, 3"
                        )
        input_ = StringIO(file_contents)
        column = extract_csv_column_by_index(input_, 1)
        # indexing starts from 0 so result can be unintuitive
        self.assertEqual(column, [2.0, 2.0])

if __name__ == "__main__":
    unittest.main()
