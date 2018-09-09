Convert a linked list to a string

Preloaded for you is a class, struct or derived data type Node (depending on the language) used to construct linked lists in this Kata:

class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

Task
If you are attempting this Kata in NASM, the code examples shown below may not be relevant at all - please refer to the Sample Tests (written in C) for the exact requirements.

Create a function stringify which accepts an argument list/$list and returns a string representation of the list. The string representation of the list starts with the value of the current Node, specified by its data/$data/Data property, followed by a whitespace character, an arrow and another whitespace character (" -> "), followed by the rest of the list. The end of the string representation of a list must always end with null/NULL/None/nil/nullptr/null() (all caps or all lowercase depending on the language you are undertaking this Kata in). For example, given the following list:

Node(1, Node(2, Node(3)))
... its string representation would be:

"1 -> 2 -> 3 -> None"

Note that null/NULL/None/nil/nullptr/null() itself is also considered a valid linked list. In that case, its string representation would simply be "null"/"NULL"/"None"/"nil"/"nullptr"/@"NULL"/"null()" (again, depending on the language).

For the simplicity of this Kata, you may assume that any Node in this Kata may only contain non-negative integer values. For example, you will not encounter a Node whose data/$data/Data property is "Hello World".

# source: https://www.codewars.com/kata/convert-a-linked-list-to-a-string