#Done by Carlos Amaral (31/07/2020)


#Try 17.3 - Testing python_repos.py

"""
n python_repos.py, we printed the value of
status_code to make sure the API call was successful. Write a program called
test_python_repos.py that uses unittest to assert that the value of status_code
is 200. Figure out some other assertions you can make—for example, that the
number of items returned is expected and that the total number of repositories
is greater than a certain amount.
"""

import unittest

import try_17_3 as tr

class TestPythonReposVisual(unittest.TestCase):
    """Tests for try_17.3.py."""

    def setUp(self):
        """Call all the functions and test all elements separately."""
        self.r = tr.get_response()
        self.repo_dicts = tr.get_repo_dicts()
        self.repo_links, self.stars, self.labels = tr.get_project_data(repo_dicts)

    def test_get_response(self):
        """Test if we get a valid response."""
        self.assertEqual(self.r.status_code, 200)

    def test_repo_dicts(self):
        """Test that we're getting the data we think we are."""
        self.assertEqual(len(self.repo_dicts), 20)

        # Repositories should have required keys.
        required_keys = ['name', 'owner', 'stargazers_count', 'html_url']
        for key in required_keys:
            self.assertTrue(key in self.repo_dict.keys())

if __name__ == '__main__':
    unittest.main()

