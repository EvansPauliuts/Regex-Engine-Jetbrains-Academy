# Regex-Engine-Jetbrains-Academy
This project jetbrains academy https://hyperskill.org/projects/114

## Work on project. Stage 3/6: Working with strings of different length
### Objectives

Your improved regex engine should do the following:

- A new function is created as an entry point;
- It should repeatedly invoke the function that compares two equal length patterns;
- If that function returns ```True```, the new function should also return ```True```;
- If that function returns ```False```, the input string should be passed to the matching function with an incremented starting position, and the regex should be passed unmodified;
- The process goes on until the entire input string has been consumed.

A way to implement this is to use slicing like in the previous stages, but do it only to progress the input string.
The input string should be consumed character by character, and the regex should be checked against every position.

A loop can be used to take care of the changing starting characters, but you can also experiment more with recursion.

In case you choose to use a loop, keep in mind that the type of the loop you use is optional,
but in order to slice a string, integers should be passed as string indexes, and an index should not
be greater than the length of the input string. If the end of the string is reached, the input string
is consumed without a match, which should return ```False```.

If you prefer to stick to recursion, use the same logic you used earlier. However, keep in
mind that Python has a limit on recursion, and it might be reached if you're dealing with longer strings.
To counter this, the following lines should be added to your program if it throws an error message
about reaching the recursion limit:

```shell
import sys
sys.setrecursionlimit(10000)
```

#### Example
```shell
Input: 'apple|apple'     Output: True
Input:    'ap|apple'     Output: True
Input:    'le|apple'     Output: True
Input:     'a|apple'     Output: True
Input:     '.|apple'     Output: True
Input: 'apwle|apple'     Output: False
Input: 'peach|apple'     Output: False
```
