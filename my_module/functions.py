
# Import a function that will clear printed outputs
from IPython.display import clear_output

# Define a function that takes one parameter
def personality_test(question_list):
    
    # Set a counter equal to zero
    personalityscore = 0
    
    # Create a list of acceptable values
    list_of_acceptable_values = ['a', 'b', 'c', 'd', 'e']
    
    # Prompt a user for each question in the list of questions
    for question in question_list:
        response = input(question + "\nResponse: ")
        
        # Remind user to enter answers in list of acceptable values
        while response not in list_of_acceptable_values:
            print('Oops! Please enter a one letter answer a-e :)')
            response = input(question + "\nResponse: ") 
        
        # Clear prompt once input has been received
        clear_output()
            
        # Increment counter according to response
        if response == 'a':
            personalityscore += 4
        elif response == 'b':
            personalityscore += 3
        elif response == 'c':
            personalityscore += 2
        elif response == 'd':
            personalityscore += 1
        elif response == 'e':
            personalityscore += 0
            
    # Return result
    return personalityscore
