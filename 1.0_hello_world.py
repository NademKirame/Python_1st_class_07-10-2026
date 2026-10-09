"""Exercise 1.0: Hello World

WHAT THE PROGRAM MUST DO
    Display a message of your choice, five times, with each line numbered.

ANSWER THESE FIRST, in comments at the top of your file, before any code
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What message did you choose, and why that one?

WHAT THE AI CANNOT KNOW
    The message is yours. Choose something you would actually want a program to say,
    not "Hello, World!". Your comment has to justify it.

CHECK IT YOURSELF
    Count the lines your program produced. Five, not four and not six.
    Then change the number to 3 and run it again. If you had to rewrite more than one
    character, your program is not built the way it should be.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: my code 
# 2. Process: First drafting a code, then press run. The result should display my message 5 times.
# 3. Out: my message displayed 5 times, each line numbered 
# 4. My message, and why: "Welcome to the team" new joiners should receive this text when added in a DL


# Your code below

message = "Welcome to the team"
repetitions = 5

for number in range (1, repetitions +1):
    print(f"{number}. {message}")