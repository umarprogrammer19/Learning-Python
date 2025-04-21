# @Author: Arif Kasim Rozani - (Team Operation Badar)

# Useful Links:
# - Download Python
# - Python 3.13.2 documentation
# - www.w3schools.com
# - www.tutorialspoint.com
# - code.visualstudio.com
# - www.cursor.com

# Python: The Versatile and Powerful Programming Language
# Python is a high-level, interpreted, and versatile programming language 
# known for its simplicity and readability. It emphasizes code clarity and 
# supports multiple programming paradigms like procedural, object-oriented, 
# and functional programming. Its extensive standard library and community 
# support make it ideal for web development, data analysis, AI, automation, and more.

# Python in Agentic AI: Powering Autonomous Intelligence 🚀
# Python plays a crucial role in Agentic AI, enabling autonomous agents to 
# perceive, reason, and act. With frameworks like LangChain, CrewAI, Microsoft AutoGen, 
# Auto-GPT, and OpenAI's APIs, Python facilitates LLM-driven workflows, 
# decision-making, and self-improving AI. Its rich ecosystem supports seamless 
# integration of NLP, reinforcement learning, and automation for building intelligent, 
# agentic systems.

# Practical Applications of Python
# Python has numerous practical applications across various industries:
# - Data Science and Analytics: data analysis, machine learning, and visualization
# - Agentic AI: building autonomous agents, chatbots, and virtual assistants
# - Machine Learning: developing predictive models and recommender systems
# - Natural Language Processing (NLP): text analysis, sentiment analysis, and language translation
# - Computer Vision: image recognition, object detection, and facial recognition
# - Robotics: building and controlling robots, drones, and autonomous vehicles
# - Web Development: building web applications and frameworks
# - Artificial Intelligence and Machine Learning: AI, ML, and deep learning
# - Automation and Scripting: automating tasks and workflows
# - Scientific Computing: scientific simulations and data analysis
# - Cybersecurity: security testing and penetration testing
# - Internet of Things (IoT): building IoT applications and devices

# Python's simplicity and extensive libraries make it an ideal choice for building 
# Agentic AI applications that can interact, learn, and adapt to their environments.

# The Code Execution Continuum: A Comprehensive Exploration of Computer Languages
# from Code Writing to Runtime and Output
# Delve into the code execution continuum, exploring how computer languages transform 
# from source code to bytecode, runtime, and output. Discover the complex journey of code 
# compilation, interpretation, and execution.

# Introduction to Python Bytecode
# Python bytecode is the intermediate representation of Python code that is generated 
# by the Python compiler. When you write Python code, it is first compiled into bytecode, 
# which is then executed by the Python interpreter.

# Python Bytecode Process
# - Lexical Analysis: Breaks the Python code into individual tokens (keywords, identifiers, literals).
# - Syntax Analysis: Checks if the code follows the correct syntax.
# - Semantic Analysis: Ensures the code makes sense logically.
# - Bytecode Generation: The final compiled representation of the code in bytecode.

# Example of Python Bytecode:
# Let's use the dis module to inspect bytecode for the Person class.

import dis

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Let's create a Person object
person = Person("Arif Rozani", 20)
person.greet()

# Disassemble the Person class to see the bytecode
dis.dis(Person)

# Explanation of the bytecode:
# The bytecode shows the individual instructions that are executed when the Person 
# class object is created, and the __init__ and greet functions are called.

# Introduction to the dis Module
# The dis module in Python allows us to disassemble and inspect the bytecode of Python 
# functions, methods, and classes. This gives us a low-level representation of how the 
# Python interpreter executes the code.

# Why is Python Bytecode Important?
# - Platform Independence: Python bytecode can run on any platform with the Python interpreter.
# - Dynamic Typing: Python is dynamically typed, which means variables' types are determined at runtime.
# - Flexibility: Python bytecode can be easily modified or extended.
# - Python bytecode is stored in .pyc files, generated during import, and executed by the interpreter.

# Can You Run Python Bytecode Directly?
# Python bytecode requires the Python interpreter (CPython VM) to run it, unlike Java bytecode 
# which runs on the JVM. 

# Indentation in Python
# Indentation is crucial in Python as it defines code blocks for control structures, 
# functions, and classes. Incorrect indentation will lead to syntax errors.

# Rules of Indentation:
# - Use consistent indentation (4 spaces is the standard convention).
# - Indentation follows control structures (e.g., after `if`, `for`, function definitions).

# Example of correct and incorrect indentation:

# Correct indentation
if True:
    print("Hello, World!")

# Incorrect indentation
if True:
    print("Hello, World!")

# Python is a Dynamically-Typed Language with Optional Type Hinting
# Python does not enforce data types at compile time. Variables are dynamically typed at runtime. 
# Type hinting, introduced in Python 3.5, allows developers to specify the expected types of variables, 
# function parameters, and return types.

# Example:
age: int = input("Enter your age: ")
print(f"Your age is {age}")
print("type(age) = ", type(age))

# Output:
# Enter your age: 22
# Your age is 22
# type(age) =  <class 'str'>

# Object-Based vs Object-Oriented Languages
# - Object-Based Language: Supports objects but lacks full support for OOP features (inheritance, polymorphism).
# - Object-Oriented Language: Fully supports OOP features (encapsulation, inheritance, polymorphism).
# Examples of OOP languages: Python, Java, C++, Ruby.

# Duck Typing
# Duck typing allows developers to write flexible and dynamic code. It focuses on what an object can do, 
# rather than what type it is. If an object can respond to the required methods, it can be used, regardless 
# of its actual class.

# Example of Duck Typing:
class Human:
    def speak(self):
        print("Human: I'm good, thanks!")

class Parrot:
    def speak(self):
        print("Parrot: Polly wants a cracker!")

def have_conversation(person):
    print("\nHave conversation: Hello, how are you? ", type(person))
    person.speak()

# You can pass different objects, and if they implement the speak() method, 
# the function works as expected, demonstrating the power of duck typing.

human = Human()
parrot = Parrot()

have_conversation(human)  # Output: Human: I'm good, thanks!
have_conversation(parrot)  # Output: Parrot: Polly wants a cracker!
