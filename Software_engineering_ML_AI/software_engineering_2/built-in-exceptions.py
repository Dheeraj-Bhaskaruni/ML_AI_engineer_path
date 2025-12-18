sale_instruments = ['Violin', 'Conga', 'Clavinet']

print('The following ' + str(len(sale_instruments)) + 'instruments are on sale:')
print(TypeError.__bases__)
print(sale_instruments[0])
print(sale_instruments[1])
print(sale_instruments[2])


"""
Built-in Exceptions
8 min
In the previous exercise (and probably many times before), we saw one type of exception called the NameError. The NameError is just one of the many built-in exceptions — exceptions that are built into the Python language. Other built-in exceptions cover fields ranging from mathematical errors all the way to operating system errors. We don’t need to memorize them all, but it’s helpful to be familiar with some common ones and, more importantly, understand where they come from inside Python.

Exceptions are objects just like anything else. Most exceptions inherit directly from a class called Exception; however, they all are derived directly or indirectly from the BaseException class. We can examine the base classes by using the __bases__ attribute on any specific exception:

print(NameError.__bases__)

Copy to Clipboard

Will output:

<class 'Exception'>

Copy to Clipboard

We can even call __bases__ on the Exception class to see its origins:

print(Exception.__bases__)

Copy to Clipboard

Will output:

<class 'BaseException'>

Copy to Clipboard

The full hierarchy of built-in exceptions is the following:

BaseException
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError

Copy to Clipboard

Note that there are a lot of exceptions built into the language of Python. Again, we don’t need to memorize all of them, but at some point, we may see them pop up in our programs. We can find details on each of the exceptions listed above in the Python documentation.

Later in this lesson, we’ll be using the Exception base class to create custom exceptions. For now, let’s get some practice encountering built-in exceptions and reading their tracebacks.
"""