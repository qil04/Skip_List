import random
from typing import Tuple
import operator


class Node:
    """
    Node of skip list
    """

    __slots__ = "key", "value", "forward"

    def __init__(self, key, value, level) -> None:
        """
        Construct a node with key as key and value as value
        :param key: node key
        :param value: the value of the node
        :param level: The number of levels of the node
        """
        self.key = key
        self.value = value
        self.forward = [None] * (level + 1)

    def __str__(self) -> str:
        """
        Represent the node
        : return: the string representing the node
        """
        return '(' + str(self.key) + ',' + str(self.value) + ')'

    def __repr__(self) -> str:
        """
        Represent the node
        :return: the string representing the node
        """
        return self.__str__()


class SkipList:
    """
    Class Skip List
    """

    __slots__ = "MAX_LEVEL", "portion","header", "level", "n"

    def __init__(self, max_level, portion) -> None:
        """
        Create a empty skip list
        :param max_level: the highest level that all nodes may reference
        :param portion: the proportion of node references \
            with i-1 order and i-order references
        """
        self.MAX_LEVEL = max_level
        self.portion = portion
        self.header = self._make_node(self.MAX_LEVEL, None, None)
        self.level = 0  # the current referencing level
        self.n = 0

    def __len__(self) -> int:
        """
        return the number of node of skip list
        :return: number of node
        """
        return self.n

    def skip_display(self) -> None:
        """
        represent the skip list
        :return: None
        """
        print("\n*****SkipList*****")
        header = self.header
        for lvl in range(self.level + 1):
            print("Level {}: ".format(lvl), end=' ')
            node = header.forward[lvl]
            while node is not None:
                print(node.key, end=' ')
                node = node.forward[lvl]
            print('')

    def empty(self) -> bool:
        """
        Determine whether the skip table is empty
        :return: return True if it is empty, return False if it is not empty
        """
        if self.n == 0:
            return True
        return False

    def _make_node(self, lvl, key, value) -> Node:
        """
        Create a new skip list node
        :param lvl: The highest reference order the new node
        :param key: the key of the new node
        :param value: the value of the new node
        :return: created new node
        """
        node = Node(key, value, lvl)
        return node

    def _rand_lvl(self) -> int:
        """
        Randomly generate the highest reference order of new nodes
        :return: the highest reference order of the new node
        """
        lvl = 0
        while random.random() < self.portion and lvl < self.MAX_LEVEL:
            lvl += 1
        return lvl

    def _utility_search(self, key2search) -> Tuple:
        """
        Find node (non-public method)
        :param key2search: the key of the node to be searched
        :return: the found node and the forward array of the node
        """
        cursor = [None] * (self.MAX_LEVEL + 1)
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key2search:
                current = current.forward[i]
            cursor[i] = current
        current = current.forward[0]
        return current, cursor

    def get_level_node(self, level) -> list:
        """
        Return every element
        :param level: the number of levels to search
        :return: a list containing all elements of this layer
        """
        level_list = []
        node = self.header.forward[level]
        while node is not None:
            level_list.append(node)
            node = node.forward[level]
        return level_list

    def skip_search(self, key2search) -> Node:
        """
        Find the node whose key is the key
        :param key2search: the key of the node to be searched
        :return: The found node, if it does not exist, return None
        """
        current, _ = self._utility_search(key2search)
        if current and current.key == key2search:
            return current
        else:
            return None

    def skip_insert(self, key2search, value2insert) -> None:
        """
        Insert node
        :param key2search: The key to insert the node
        :param value2insert: the value of the node to be inserted
        :return: None
        """
        current, cursor = self._utility_search(key2search)
        if current and current.key == key2search:
            current.value = value2insert
        else:
            lvl = self._rand_lvl()
            if lvl > self.level:
                for i in range(self.level + 1, lvl + 1):
                    cursor[i] = self.header
                self.level = lvl
            node = self._make_node(lvl, key2search, value2insert)
            for i in range(lvl + 1):
                node.forward[i] = cursor[i].forward[i]
                cursor[i].forward[i] = node
            self.n += 1

    def skip_delete(self, key2search) -> Node:
        """
        Delete node
        :param key2search: The key of the node to be deleted
        :return: the deleted node
        """
        current, cursor = self._utility_search(key2search)
        if current is not None and current.key == key2search:
            ret = current
            for i in range(self.level + 1):
                if cursor[i].forward[i] != current:
                    break
                cursor[i].forward[i] = current.forward[i]
            while self.level > 0 and self.header.forward[self.level] is None:
                self.level -= 1
            self.n -= 1
            return ret

def music_ranking(music_list):
    """
    Quickly sort and select the most played songs according to the list of songs
    :param music_list: Playlist to be sorted
    :return: The top 1
    """
    music_list_ranked = SkipList(10, 0.5)
    for music in music_list:
        music_list_ranked.skip_insert(music[0], music[1])
    layer0 = music_list_ranked.get_level_node(0)
    top1 = layer0[-1]
    return top1