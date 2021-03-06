import unittest
from SkipList import Node, SkipList, music_ranking
import random
from string import ascii_lowercase
import time


class TestSkipList(unittest.TestCase):
    def test_list_insert(self):
        """
        Tests SkipList.skip_insert method
        """

        # Dataset
        skip_list = SkipList(10, 0.5)

        skip_list.skip_insert(3, 5)
        skip_list.skip_insert(12, 9)
        skip_list.skip_insert(26, 7)
        skip_list.skip_insert(7, 13)
        skip_list.skip_insert(21, 3)
        skip_list.skip_insert(25, 4)
        skip_list.skip_insert(6, 6)
        skip_list.skip_insert(17, 8)
        skip_list.skip_insert(19, 10)
        skip_list.skip_insert(9, 14)

        self.assertEqual(10, len(skip_list))

        for lvl in range(skip_list.level):
            level = skip_list.get_level_node(lvl)
            for i in range(len(level) - 1):
                self.assertLess(level[i].key, level[i + 1].key)

        # Alphabets
        skip_list_alpha = SkipList(10, 0.5)

        skip_list_alpha.skip_insert('a', 'a')
        skip_list_alpha.skip_insert('a', 'b')
        skip_list_alpha.skip_insert('b', 'e')
        skip_list_alpha.skip_insert('g', 'a')
        skip_list_alpha.skip_insert('c', 'f')
        skip_list_alpha.skip_insert('h', 'r')

        self.assertEqual(5, len(skip_list_alpha))

        for lvl in range(skip_list_alpha.level):
            level = skip_list_alpha.get_level_node(lvl)
            for i in range(len(level) - 1):
                self.assertLess(level[i].key, level[i + 1].key)

    def test_list_empty(self):
        """
        Tests SkipList.empty method
        """

        # empty list
        skip_list = SkipList(10, 0.5)
        self.assertTrue(skip_list.empty())

        # nonempty list
        skip_list.skip_insert(1, 1)
        self.assertFalse(skip_list.empty())

    def test_list_search(self):
        """
        Tests SkipList.search method
        """

        # Dateset
        skip_list = SkipList(10, 0.5)
        skip_list.skip_insert(3, 5)
        skip_list.skip_insert(12, 9)
        skip_list.skip_insert(26, 7)
        skip_list.skip_insert(7, 13)
        skip_list.skip_insert(21, 3)
        skip_list.skip_insert(25, 4)
        skip_list.skip_insert(6, 6)
        skip_list.skip_insert(17, 8)
        skip_list.skip_insert(19, 10)
        skip_list.skip_insert(9, 14)

        # Node that be searched is (3,5)
        result = skip_list.skip_search(3)
        self.assertTrue(isinstance(result, Node))
        self.assertEqual(result.key, 3)
        self.assertEqual(result.value, 5)

        # Searching an empty list gets nothing
        result = skip_list.skip_search(8)
        self.assertIsNone(result)
        # Searching operation doesn't change its length
        self.assertEqual(10, len(skip_list))

        # Alphabets
        skip_list_alpha = SkipList(10, 0.5)

        skip_list_alpha.skip_insert('a', 'a')
        skip_list_alpha.skip_insert('a', 'b')
        skip_list_alpha.skip_insert('b', 'e')
        skip_list_alpha.skip_insert('g', 'a')
        skip_list_alpha.skip_insert('c', 'f')
        skip_list_alpha.skip_insert('h', 'r')

        # Node that be searched is (b,e)
        result = skip_list_alpha.skip_search('b')
        self.assertTrue(isinstance(result, Node))
        self.assertEqual(result.key, 'b')
        self.assertEqual(result.value, 'e')

        # Searching an empty list gets nothing
        result = skip_list_alpha.skip_search('i')
        self.assertIsNone(result)

    def test_list_delete(self):
        """
        Tests SkipList.skip_delete method
        """

        # Dateset
        skip_list = SkipList(10, 0.5)

        # Deleting an empty list gets nothing
        self.assertIsNone(skip_list.skip_search(6))

        # Insert elements
        skip_list.skip_insert(3, 5)
        skip_list.skip_insert(12, 9)
        skip_list.skip_insert(26, 7)
        skip_list.skip_insert(7, 13)
        skip_list.skip_insert(21, 3)
        skip_list.skip_insert(25, 4)
        skip_list.skip_insert(6, 6)
        skip_list.skip_insert(17, 8)
        skip_list.skip_insert(19, 10)
        skip_list.skip_insert(9, 14)

        result = skip_list.skip_delete(19)
        self.assertTrue(isinstance(result, Node))

        # Node that should be deleted is (19,10)
        self.assertEqual(result.key, 19)
        self.assertEqual(result.value, 10)
        self.assertEqual(9, len(skip_list))

        # Deleting an nonexistent element gets nothing
        result = skip_list.skip_delete(8)
        self.assertIsNone(result)

        # Alphabets
        skip_list_alpha = SkipList(10, 0.5)

        skip_list_alpha.skip_insert('a', 'a')
        skip_list_alpha.skip_insert('a', 'b')
        skip_list_alpha.skip_insert('b', 'e')
        skip_list_alpha.skip_insert('g', 'a')
        skip_list_alpha.skip_insert('c', 'f')
        skip_list_alpha.skip_insert('h', 'r')

        result = skip_list_alpha.skip_delete('g')
        self.assertTrue(isinstance(result, Node))

        # Node that should be deleted is (g,a)
        self.assertEqual(result.key, 'g')
        self.assertEqual(result.value, 'a')
        self.assertEqual(4, len(skip_list_alpha))

        # Deleting an nonexistent element gets nothing
        result = skip_list_alpha.skip_search('i')
        self.assertIsNone(result)

    def test_list_insert_advanced(self):
        """
        More complicated insert cases
        """

        # Large dataset
        skip_list = SkipList(10, 0.5)
        for i in range(1000):
            ele = random.randint(0, 1000)
            skip_list.skip_insert(ele, ele)

        # elements are ordered in each level
        for lvl in range(skip_list.level):
            level = skip_list.get_level_node(lvl)
            for i in range(len(level) - 1):
                self.assertLess(level[i].key, level[i + 1].key)

        # Large dataset, same key should sort by value
        skip_list = SkipList(10, 0.5)

        for i in range(500):
            ele = random.randint(0, 100)
            skip_list.skip_insert(6, ele)

        # elements are ordered in each level
        for lvl in range(skip_list.level):
            level = skip_list.get_level_node(lvl)
            for i in range(len(level) - 1):
                self.assertLess(level[i].value, level[i + 1].value)

        # Non-numeric values
        skip_list_alpha = SkipList(10, 0.5)

        for letter in ascii_lowercase:
            skip_list_alpha.skip_insert(letter, letter)

        self.assertEqual(26, len(skip_list_alpha))

        # elements are ordered in each level
        for lvl in range(skip_list.level):
            level = skip_list.get_level_node(lvl)
            for i in range(len(level) - 1):
                self.assertLess(level[i].key, level[i + 1].key)

    def test_list_delete_advanced(self):
        """
        More complicated delete cases
        """
        # Large dataset
        skip_list = SkipList(10, 0.5)
        for i in range(1000):
            skip_list.skip_insert(i, i)
        correct = [i for i in range(1000)]
        student = list()
        for _ in range(1000):
            student.append(skip_list.skip_delete(_).key)
        self.assertEqual(correct, student)

        # Non-numeric values
        skip_list_alpha = SkipList(10, 0.5)
        correct = list()
        student = list()
        for _ in ascii_lowercase:
            correct.append(_)
            skip_list_alpha.skip_insert(_, _)
        for i in ascii_lowercase:
            student.append(skip_list_alpha.skip_delete(i).key)
        self.assertEqual(correct, student)

    def test_music_ranking_application(self):

        music_list = [[162511, 'Love Is Gone'], [272266, 'MELANCHOLY'], [15815, 'Monster']]
        top1 = music_ranking(music_list)
        built_in_sort_list = sorted(music_list, key=lambda x: x[0])
        self.assertEqual(top1.value, built_in_sort_list[-1][1])

        music_list = [[162511, 'Love Is Gone'], [9407, 'Lovefool'], [272266, 'MELANCHOLY'], [15815, 'Monster'],
                      [104747, 'Sold Out'], [47573, 'Walk Thru Fire'], [4122, 'Salt'], [14187, 'Astronomia'],
                      [12029, 'Love Story'], [121560, 'One Day'], [374203, 'Something Just Like This'],
                      [5896, 'Tonight'], [10400, 'Not Angry'], [40170, 'Unstoppable'], [140399, 'All Falls Down'],
                      [67293, 'Fractures'], [190709, 'Nevada'], [89922, 'Send It'], [143673, 'bad guy'],
                      [125451, 'Closer'], [36784, 'Move Up'], [30087, '50 Feet'], [150252, 'Counting Stars']]
        top1 = music_ranking(music_list)
        built_in_sort_list = sorted(music_list, key=lambda x: x[0])
        self.assertEqual(top1.value, built_in_sort_list[-1][1])

        update_data = [[157831, 'Love Is Gone'], [9524, 'Lovefool'], [22892, 'MELANCHOLY'], [15457, 'Monster'],
                       [158522, 'Sold Out'], [47573, 'Walk Thru Fire'], [4122, 'Salt'], [15473, 'Astronomia'],
                       [12029, 'Love Story'], [121560, 'One Day'], [5642, 'Something Just Like This'],
                       [5896, 'Tonight'], [10400, 'Not Angry'], [40170, 'Unstoppable'], [157303, 'All Falls Down'],
                       [689653, 'Fractures'], [5689, 'Nevada'], [89922, 'Send It'], [124824, 'bad guy'],
                       [15683, 'Closer'], [57893, 'Move Up'], [24834, '50 Feet'], [245972, 'Counting Stars'],
                       [635885, 'Reality'], [137808, 'NUMB'], [26618, 'Wrap Me In Plastic'], [18222, 'Warm'],
                       [4908, 'Is It Just Me?'], [313024, 'See You Again'], [13198, 'Teeth'], [271432, 'Faded'],
                       [323122, 'You'], [23835, 'Let Me Down Slowly'], [221602, 'That Girl'], [135642, 'There For You'],
                       [256727, 'Hall of Fame'], [87108, 'Psycho, Pt. 2'], [77847, 'East of Eden'],
                       [53266, 'This Is What You Came For'], [39111, 'By Your Side'], [32502, 'Once Upon a Time'],
                       [158705, 'Please Don''t Go'], [10467, 'Therefore I Am'], [39077, 'Outside'], [64427, 'Fire'],
                       [66188, 'Dance Monkey'], [58960, 'We Can''t Stop'], [49510, '2 Soon'], [63633, 'Wolves'],
                       [63225, 'Dancin'], [59463, 'Because of You'], [30063, 'End of The Night'], [27425, 'Steady Me']]
        top1 = music_ranking(update_data)
        built_in_sort_list = sorted(update_data, key= lambda x: x[0])
        self.assertEqual(top1.value, built_in_sort_list[-1][1])


if __name__ == '__main__':
    unittest.main()
