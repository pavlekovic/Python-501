# Python Fundamentals

## Variables
Variables are building blocks of any program. They are containers used to store values that can be referenced and manipulated later in a program. When initializing a variable, Python will automatically assign type to that variable based on the value being stored.

Python built-in data types include:
- Numbers: Integers (e.g. 1, 55), and floating point numbers (e.g. 5.47, 88.55)
- Strings: Anything that involves characters or text
- Boolean: Either True or False

To check the type of a variable, `type(<variable>)` can be used.

## Numbers
Numbers are a fundamental data type used for numerical computations. Python supports various numeric types to handle different types of numbers, such as integers and floating-point numbers.
<br>Python supports a range of math operators when it comes to numbers:
- Add (+)
- Subtract (-)
- Multiply (*)
- Divide (/)
- Modulo (%) - operator that returns remainder of division

## Strings
Strings are a sequence of characters used to store and manipulate text. To store strings, single, double, or triple quotation marks are used. Some of the built-in functions Python uses to work with strings:
- `concatenate` -> Used to combine multiple strings.
- `capitalize` -> Used to capitalize the first letter of a string.
- `find(sub, start, end)` -> Used when searching for a particular letter or string within a larger string.

- And many more  available on the official [Python website](https://docs.python.org/3/library/stdtypes.html#string-methods).

## Booleans and equality operators
Booleans represent one of two values: True or False. Booleans are used to evaluate conditions, control the flow of programs, and perform logical operations.
<br> Most commonly used operators are:
- `==` -> Equal to
- `!=` -> Not equal to
- `>` -> Greater than
- `<` -> Less than
- `>=` -> Greater than or equal to
- `<=` -> Less than or equal to

## Control Flow
We control the flow of the program by including if statements that are used to execute a block of code based on a condition. By using them, we make sure that the program is making the right decisions and taking different actions depending on whether a condition is True or False.

In Python, the following conditional statements are used:
- `if` -> Conditional statement which makes a portion of code executable only when the statement is True.
- `elif` -> Conditional statement that follows `if` to provide an alternative scenario, but also contains a condition which must be True for the code to execute.
- `else` -> Statement that provides "the last" alternative to the program which is executed when none of the conditions before it are met.

## Collections
Python supports data types beyond just variables. Collections are used to store and manage groups of related data. Two of the most commonly used collection types are lists and dictionaries.

### Lists
A list is an ordered, mutable collection of items. It allows duplicate elements and can hold items of any data type (e.g., integers, strings, objects).

Key features of lists:
- Ordered: Items maintain the order in which they are added.
- Mutable: Items in a list can be changed after the list is created.
- Can contain duplicates: The same value can appear multiple times.

Commonly used commands with lists:
- `my_list = []` -> Creates an empty list.
- `my_list.append(<item>)` -> Adds to the end of the list.
- `my_list.insert(1, <item>)` -> Inserts <item> at index 1.
- `my_list.remove(<item>)` -> Removes the first occurrence of <item>.
- `my_list.pop()` -> Removes and returns the last item.

### Dictionaries
A dictionary is an unordered, mutable collection of key-value pairs. Keys are unique, but values can be duplicated.

Key features of dictionaries:
- Unordered (Python 3.6+ maintains insertion order, but this is not guaranteed for earlier versions).
- Keys must be immutable (e.g., strings, numbers); values can be any data type.
- Highly efficient for lookups based on keys.

Commonly used commands with dictionaries:
- `my_dict = {}` -> Creates an empty dictionary.
- `my_dict = {"name": "Alice", "age": 30, "city": "London"}` -> Creates a dictionary with elements.
- `my_dict["country"] = "UK"` -> Adds a new key-value pair.
- `my_dict["age"] = 31` -> Updates the value of age.
- `del my_dict["city"]` -> Removes the key "city" and its value.

#### Comparison between lists and dictionaries
| Feature                | **List**                           | **Dictionary**                      |
|------------------------|-------------------------------------|--------------------------------------|
| Structure              | Ordered collection of elements     | Unordered collection of key-value pairs |
| Access Method          | By index (`list[0]`)              | By key (`dict['key']`)              |
| Duplicates             | Allows duplicate values            | Keys must be unique                 |
| Mutability             | Mutable (can be changed)           | Mutable (can add, remove, or update key-value pairs) |
| Example Use Cases      | Ordered data like a list of names  | Data with labels, like user profiles |

## Loops
In Python, loops are used to execute a block of code repeatedly as long as a certain condition is met or for a specific range of values. Python provides two main types of loops: for loops and while loops.

Example: <br>
`for item in sequence:` <br>
&nbsp; &nbsp; &nbsp; &nbsp; `# Code block to execute`

### For loops
A for loop iterates over a sequence (e.g., a list, string, or range) and executes the loop body for each element in the sequence.

### While loops
A while loop runs as long as a condition is True. It’s useful when the number of iterations is not predetermined.

Example: <br>
`while condition:` <br>
&nbsp; &nbsp; &nbsp; &nbsp; `# Code block to execute`

## Functions
Functions are reusable blocks of code that perform a specific task. They make it possible to organize the code and make it more readable. Importantly, they make possible to avoid repetition by calling the same block of code whenever needed.

They are created using the keyword `def` which is followed by the function name, parentheses, and a colon. All code inside the function is indented.

### Defining a function
Example: <br>
`def function_name(parameters):` <br>
&nbsp; &nbsp; &nbsp; &nbsp;`# Code block`


### Calling a function
Example: <br>
`def function_name(parameters):` <br>
&nbsp; &nbsp; &nbsp; &nbsp;`# Code block`

`function_name()`

### Function components
There are different components to any function:
- Parameters -> Variables listed in the function definition. 
- Arguments -> Values passed on when the function is called.
- Return statement -> Sends a value back to the caller.
- Default parameters -> Used when no argument is provided.
- Keyword arguments -> Arguments that are explicitly specified.
