# Project: Skip List

## Skip List

The full name of skip list is a data structure like linked list. The performance of the skip table is the same as the performance of the balanced tree. The time complexity of insertion, deletion, and search is O(n), which is a data structure that uses space for time.

If you want to quickly find the element 10 in the linked list above, you can only traverse the linked list from the beginning until you find the element we need to find. Search path: 1, 3, 4, 5, 7, 8, 9, 10. Such search efficiency is very low, and the average time complexity is very high O(n). By implementing the jump list, we extract every two elements from the linked list, add a first-level index, and the first-level index points to the original linked list, that is, the down pointer of the first-level index 7 can find the 7 of the original linked list.

First look for 1, 4, 7, 9 in the index. When traversing to 9 of the primary index, it is found that the successor node of 9 is 13, which is greater than 10, so instead of looking back, we find 9 of the original linked list through 9. Then we traverse back and find the 10 we are looking for, and the traversal ends. When the first-level index is added, the search path: 1, 4, 7, 9, 10. There are relatively few elements that need to be traversed to find the node. We do not need to traverse all the data before 10, and the search efficiency is improved.

Using "space for time" is the idea of ​​skipping list, and by indexing the linked list, the search efficiency is improved. When the amount of data is large enough, the efficiency will be greatly improved. If the ordered single chain has 10,000 elements, they are 0~9999. Now we have built many levels of index, the most advanced index is two elements 0, 5000, the next high index four elements 0, 2500, 5000, 7500, and so on, when we look for the element 7890, the search path is 0 , 5000, 7500 ... 7890, 5000 elements are directly skipped through the highest-level index, and 2500 elements are directly skipped through the second-level index, so that the linked list can realize binary search. It can be seen that when the number of elements is large, the efficiency of indexing is relatively large, which is similar to binary search.

### Search time complexity
Time complexity = index height * the number of elements traversed by each level of index.
Assuming that every two nodes will extract a node as the node of the upper level index, the original linked list has n elements, then the first level index has n/2 elements, the second level index has n/4 elements, k The level index has n/2k elements. The highest-level index generally has 2 elements, namely: the highest-level index h satisfies 2 = n/2h, that is, h = log2n-1, the highest-level index h is the height of the index layer plus the original data layer, and the total height of the jump table h = log2n.

### Space complexity
The skip list improves the efficiency of finding elements by establishing an index.
If the original linked list contains n elements, the number of primary index elements is n/2, the number of secondary index elements is n/4, the number of tertiary index elements is n/8, and so on. Therefore, the sum of index nodes is: n/2 + n/4 + n/8 +… + 8 + 4 + 2 = n-2, and the space complexity is O(n).


## class Node: 

*   **Attributes**
    *   **key**: node key
    *   **value:** value contained in the node
    *   **forward:** the number of levels of the node

*   **__init__**(self, key, value, level)

    *   **key**: node key
    *   **value:** value contained in the node
    *   **forward:** the number of levels of the node
    *   Construct a node with key as key and value as value
    *   return: **None**
    *   _Time Complexity: O(1)_

*   **__str__**(self)
    *   Representation of **key** and **value** as a string
    *   return: **str**
    *   _Time Complexity: O(1)

## class Skip List
*    **Reference SkipList.py file**

## Application Designning:
Compared with common linked lists, SkipList increases the space overhead, but its performance in search, insertion and other aspects is better than data structures such as red and black trees. Therefore, SkipList is often used in situations where the data scale is large and the change speed is fast, such as leaderboards. The title of this app is to quickly sort and select the most played songs according to the list of songs given - including the number of plays and the song name.
