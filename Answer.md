## Q1. What is the difference between list and tuples in Python?
    -List chứa một tập các giá trị, được phân tách nhau bằng dấu phẩy, List có thể chứa bất kỳ kiểu dữ liệu nào. Một List được tạo bởi cặp dấu [].
    -Tương tự như kiểu dữ liệu List tuy nhiên lại có một sự khác biệt với kiểu List đó là các phần tử trong Tuple không thể bị thay đổi sau khi gán chính vì vậy tốc độ của Tuple luôn luôn nhanh hơn so với List, Tuple chứa một tập các giá trị, được phân tách nhau bằng dấu phẩy, có thể chứa bất kỳ kiểu dữ liệu nào. Một tuple được tạo bởi cặp dấu ().

# Q2. What are the key features of Python?
    -Understandable And Easy
    -Meaningful programming language
    -Available For Anyone
    -Programmer-Friendly Language
    -Easily Movable Language
    -Object Oriented
    -Uncomplicated Code Running
    -Readily Extended
    -Great Standard Library
    -Data Specification
    -Crux

# Q3. What type of language is python?
    -Python is a dynamically typed interpreted language. These types of languages are typically referred to as “scripting” languages because code is not compiled to a binary form. By dynamically typed I mean that types do not need to be declared when coding, the interpreter figures them out at runtime.

# Q4. How is Python an interpreted language?
    -Python is called an interpreted language because it goes through an interpreter, which turns code you write into the language understood by your computer’s processor. Later on when you work on a project on your own computer, you will download and use the Python interpreter to be able to write Python code and execute it on your own!

# Q5. What is pep 8?
    PEP 8 is Python's style guide. It's a set of rules for how to format your Python code to maximize its readability. Writing code to a specification helps to make large code bases, with lots of writers, more uniform and predictable, too.

# Q6. How is memory managed in Python?
    -The Python memory manager manages chunks of memory called “Blocks”. A collection of blocks of the same size makes up the “Pool”. Pools are created on Arenas, chunks of 256kB memory allocated on heap=64 pools. If the objects get destroyed, the memory manager fills this space with a new object of the same size.

# Q7. What is name space in Python?
    -Namespace is a way to implement scope. In Python, each package, module, class, function and method function owns a "namespace" in which variable names are resolved. When a function,  module or package is evaluated (that is, starts execution), a namespace is created. Think of it as an "evaluation context". When a function, etc., finishes execution, the namespace is dropped. The variables are dropped. Plus there's a global namespace that's used if the name isn't in the local namespace.

    Each variable name is checked in the local namespace (the body of the function, the module, etc.), and then checked in the global namespace.

    Variables are generally created only in a local namespace. The global and nonlocal statements can create variables in other than the local namespace.

# Q8. What is PYTHON PATH?
    -PYTHONPATH is an environment variable which you can set to add additional directories where python will look for modules and packages. For most installations, you should not set these variables since they are not needed for Python to run. Python knows where to find its standard library.

# Q9. What are python modules?
    -A module allows you to logically organize your Python code. Grouping related code into a module makes the code easier to understand and use. A module is a Python object with arbitrarily named attributes that you can bind and reference.

    Simply, a module is a file consisting of Python code. A module can define functions, classes and variables. A module can also include runnable code.

# Q10. What are local variables and global variables in Python? Please give an exam
    -In general, a variable that is defined in a block is available in that block only. It is not accessible outside the block. Such a variable is called a local variable. Formal argument identifiers also behave as local variables.

    The following example will underline this point. An attempt to print a local variable outside its scope will result in a NameError.

    Example: Function with a Local Variable Copy
    def SayHello():
        user='John'
        print ("user = ", user)
        return

    Example: Function with a Global Variable Copy
    user='John'
    def SayHello():
        print ("user = ", user)
        return

# Q11. What is __init__?
    -__init__ is a special Python method that is automatically called when memory is allocated for a new object. The sole purpose of __init__ is to initialize the values of instance members for the new object. Using __init__ to return a value implies that a program is using __init__ to do something other than initialize the object. This logic should be moved to another instance method and called by the program later, after initialization.


# Q12. What is self in Python?
    In Python, the word self is the first parameter of methods that represents the instance of the class. Therefore, in order to call attributes and methods of a class, the programmer needs to use self.

