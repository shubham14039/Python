
class ArrayStack:

    def __init__(self) -> None:
        self._data = []

    def __str__(self):
        return str(self._data)

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self,e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Exception('The stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Exception('The stack is empty')
        return self._data.pop()




# Reversing a data using stacks:
#     The LIFO principle of stacks is very useful in reversing the order of a data.  Let us see how:
#
# def reverse(data):
#     S = ArrayStack()
#     for i in data:
#         S.push(i)
#     reversed = []
#     while S:
#         reversed.append(S.pop())
#     return reversed 
# # This method has O(n) time complexity
#
# ls = [1,2,3,4,5,6,7,8,9]
# print(reverse(ls))
#
# We can also use these methods to get revrsed data:
#
# reversed_data = []
# for i in range(len(data) - 1, -1, -1):
#     reversed_data.append(data[i])
# This method has O(n) time complexity
#
#
# And, Using built in methods for reversing:
# list.reversed(data) 
# which is more efficient than any of the above
#
#
# NOTE: Now any of these methods can be used at any place. But we use either of them based on specific use case contexts.




# Check for valid palindrome:
#     TEST: If the rverse of a data is equal to the original data, then its a valid palindrome. 

# def palindrome(data):
#     S = ArrayStack()
#     n = len(data)
#     if n == 0:
#         return "The data is empty"
#     elif n == 1:
#         return "It is a valid palindrome (ex code: 00)"
#     elif n%2 == 0:
#         for i in range(n):
#             S.push(data[i])
#         for k in data[:n+1]:
#             if k != S.pop():
#                 return "Not a valid palindrome (ex code: 01)"
#         return "It is a valid palindrome (ex code: 01)"
#     else:
#         for i in range(n//2):
#             S.push(data[i])
#         for k in data[:n+2]:
#             if k != S.pop():
#                 return "Not a valid palindrome (ex code: 02)"
#             # break
#         return "It is a valid palindrome  (ex code: 02)"
#
# data = [None] #define more data variables
# print(palindrome(data))





# OPTIMIZE: Here's a more better sollution for checking for palindrome

# def palindrome(data):
#     S = ArrayStack()
#     n = len(data)
#
#     if n == 0:
#         return "The data is empty"
#     elif n == 1:
#         return "It is a valid palindrome (It's just one fu**ing digit)"
#
#     for i in range(n//2):
#         S.push(data[i])
#
#     start = (n//2) if n%2 == 0 else ((n//2)+1)
#
#     for j in range(start, n):
#         if data[j] != S.pop():
#             return "It is not a palindrome"
#     return "It is a palindrome"

# data = [None] #Define more data variables
# print(palindrome(data))



# HACK: We can also reverse the entire number and check if teh reversed number is equal to the input number

# def palindrome_using_reverse(data: int):
#     y = [i for i in str(data)]
#     if y == list(reversed(y)):
#         return True
#     else:
#         return False
# data = Nne # Define more data varialbles
# print(palindrome_using_reverse(data))
# NOTE: THIS IS THE BEST SOLUTION, with time complexity O(1)




# Using stacks to check for delimiters:
# stacks can also be used for checking whether correct delimiters are being used at correct place. 

# def delim(par: str):
#     S = ArrayStack()
#     lefty = "({["
#     righty = ")}]"
#     for i in par:
#         if i in lefty:
#             S.push(i)
#         elif i in righty:
#             if S.is_empty():
#                 return False
#             if lefty.index(S.pop()) != righty.index(i):
#                 return False
#     return S.is_empty()
#
# NOTE: The time complexity of this code is O(2n**2)




# Matching HTML tags:
# Doesnot works when attributes are present in the tags, 
# def matched_html(raw):
#     S = ArrayStack()
#     while raw:
#         j = raw.find('<')
#         if j == -1:
#             break
#         else:
#             k = raw.find('>', j+1)
#             if k:
#                 tag = raw[j+1:k]
#                 if not tag.startswith('/'):
#                     S.push(tag)
#                 else:
#                     if S.is_empty():
#                         return False
#                     if tag[1:] != S.pop():
#                         return False
#     raw = raw[k+1:]
#     return S.is_empty()
#
# FIXME: this functions runs indefinitely
# FIXME: Doesnot work whne attributes are present in the tags

#
# def is_matched(raw):
#     S = ArrayStack()
#     j = raw.find('<')
#     while j != -1:
#         k = raw.find('>')
#         if k == -1:
#             return False
#         tag = raw[j+1:k]
#         if not tag.startswith('/'):
#             S.push(tag)
#         else:
#             if S.is_empty():
#                 return False
#             if tag[1:] != S.pop():
#                 return False
#         j = raw.find('<', k+1)
#     return S.is_empty()
#
# raw_file = "<head><title>Sample HTML Document</title></head><body><header><h1>Welcome to My Website</h1></header><main><p>This is a simple HTML document. Feel free to customize it!</p><a>Visit Example</a></main><footer><p>Your Name</p></footer></body></html>"
# print(matched_html(raw_file))





# Using stacks for Evaluating Arithmetic Expressions:

# Evaluating Infix expressions

def eval_infix(data):
    valStack = ArrayStack()
    oprStack = ArrayStack()

    lefty = '[{('
    righty = ')}]'

    for i in data:
        if type(i) == int or float:
            valStack.push(i)
        elif i in lefty:
            oprStack.push(i)
        elif i in righty:
            while 
            # Assigning values to operand variables 
            operand2 = valStack.pop()
            operand1 = valStack.pop()


            # Assuming the following is a valid code
            result = eval(f"{operand1} {oprStack.pop()} {operand2}")

            # Pussing the evaluated result to the value stack
            valStack.push(result)
