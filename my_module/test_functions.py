# Import my functions file
import functions as fnc

# Code for testing "random" inputs.
options = ["a", "b", "c", "d", "e"]
# List of "random" inputs to answers, including two inputs that will not work, and 25 that will work.
# These responses should add up to a score of 11 for extroversion_questions
user_in = ["shouldn't work", "also shouldn't work", "a", "b", "d", "e", "c", "a", "b", "d", "d", "c", "e", "b", "d", "e", "c", "c", "b", "d", "e", "c", "a", "a", "d", "e", "c"]
# Keep track of index.
user_index = 0

def simulate_user_input(arg):
    global user_index
    user_index += 1
    return user_in[user_index - 1]

# Override input
def test_personality_test():
    fnc.input = simulate_user_input

    extroversion_questions = ["You derive pleasure from conversations with others \n(a) always \n(b) often \n(c) sometimes \n(d) rarely \n(e) never",
                           "You would rather take a walk with a friend than by yourself \n(a) always \n(b) often \n(c) sometimes \n(d) rarely \n(e) never",
                           "You seek out high energy social situations such as parties \n(a) always \n(b) often \n(c) sometimes \n(d) rarely \n(e) never",
                           "You get bored if you spend more than a few mintues alone \n(a) always \n(b) often \n(c) sometimes \n(d) rarely \n(e) never",
                           "You spend time planning and worrying about future interactions \n(a) always \n(b) often \n(c) sometimes \n(d) rarely \n(e) never"
    ]

    # Test the function using one array with both valid and invalid input
    fnc.personality_test(extroversion_questions)
    return True

# Make sure the test is working properly, and that the "random" inputs produce an extroversion score of 11
if test_personality_test():
    assert extroversion_score == 11
    print("Passed Test!")