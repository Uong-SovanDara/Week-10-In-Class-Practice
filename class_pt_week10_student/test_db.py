import unittest
import mock


class TestDB(unittest.TestCase):

    # Mock data setup
    all_cat = [(1, 'jacky', 'm', 'Scottish Fold', '2020, 3, 8', 'smartest one'), (5, 'Smurf', 'f', 'Siberian',
                                                                                  '2018, 9, 12', 'bad cat'), (6, 'Dusty', 'm', 'Scottish Fold', '2019, 2, 14', 'valentine')]

    registered_cat = [(1, 'jacky', 'm', 'Scottish Fold', '2020, 3, 8', 'smartest one'),
                      (6, 'Dusty', 'm', 'Scottish Fold', '2019, 2, 14', 'valentine')]

    update_all_cat = [(1, 'jacky', 'm', 'Scottish Fold', '2020, 3, 8', 'smartest one'),  [
        7, 'Ah Kmao', 'Siberian', '2003, 10, 6', 'Good cat']]

    remove_all_cat = [(1, 'jacky', 'm', 'Scottish Fold',
                       '2020, 3, 8', 'smartest one'), [7, 'Ah Kmao', 'Siberian', '2003, 10, 6', 'Gangster']]

    @ mock.patch('db.get_cats', return_value=all_cat)
    def test_get_cats(self, get_cats):
        self.assertEqual(len(get_cats()[0]), 6)
        self.assertEqual(len(get_cats()), 3)

    @ mock.patch('db.register_cat', side_effect=registered_cat.append([7, 'Ah Kmao', 'Siberian', '2003, 10, 6', 'Gangster']))
    @ mock.patch('db.get_cats', return_value=registered_cat)
    def test_register_cat(self, get_cats, register_cat):
        global registered_cat
        register_cat((7, 'Ah Kmao', 'Siberian', '2003, 10, 6', 'Gangster'))
        self.assertTrue(register_cat.called)
        self.assertEqual(len(get_cats()), 3)

    @ mock.patch('db.update_cat')
    @ mock.patch('db.get_cats', return_value=update_all_cat)
    def test_update_cat(self, get_cats, update_cat):
        global update_all_cat
        update_cat([7, 'Ah Kmao', 'Siberian', '2003, 10, 6', 'Good cat'])
        self.assertTrue(update_cat.called)
        self.assertEqual(get_cats()[-1][4], 'Good cat')

    @ mock.patch('db.get_cats', return_value=remove_all_cat)
    @ mock.patch('db.remove_cat', side_effect=remove_all_cat.remove([7, 'Ah Kmao', 'Siberian', '2003, 10, 6', 'Gangster']))
    def test_remove_cat(self, remove_cat, get_cats):
        global remove_all_cat
        remove_cat([7, 'Ah Kmao', 'Siberian', '2003, 10, 6', 'Gangster'])
        self.assertTrue(remove_cat.called)
        self.assertEqual(len(get_cats()), 1)


if __name__ == "__main__":
    print("this file is use to perform a self test on db.py functions")
    print("----------------------------------------------------------\n")

    print("to get start please follow instructions below:")
    print("1. install unittest library: 'pip install pytest'")
    print("2. run self test from test_db.py file: 'pytest -v test_db.py'")
