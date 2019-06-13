

# This adds the directory above to our Python path
#   This is so that we can add import our custom python module code into this script
import sys
sys.path.append('../')

# Imports
from my_module.functions import personality_test


# Import five unique lists of questions from a separate file
from questions import *

# This will allow each prompt to disappear after an input has been entered
from IPython.display import clear_output

# Run the function personality_test for each of 5 unique list of strings (questions)
extroversion_score = personality_test(extroversion_questions)
conscientiousness_score = personality_test(conscientiousness_questions)
agreeableness_score = personality_test(agreeableness_questions)
openness_score = personality_test(openness_questions)
neuroticism_score = personality_test(neuroticism_questions)


# Create a string that will be added to below
result = "All done! "

# Add an introversion section to result
# Change the adverb according to score
if extroversion_score <= 5:
    result += "You are very introverted, "
elif extroversion_score > 5 and extroversion_score <=10:
    result += "You are fairly introverted, "
elif extroversion_score >10 and extroversion_score <=15:
    result += "You are fairly extroverted, "
else:
    result += "You are very extroverted, "

# Add a conscientiousness section to result
# Change the adverb according to score
if conscientiousness_score <= 5:
    result += "not very conscientious, "
elif conscientiousness_score > 5 and conscientiousness_score <= 10:
    result += "fairly conscientous, "
elif conscientiousness_score >10 and conscientiousness_score <=15:
    result += "quite conscientious, "
else:
    result += "extraordinarily conscientious, "

# Add an agreeableness section to result
# Change the adverb according to score
if agreeableness_score <= 5:
    result += "not very agreeable, \n"
elif agreeableness_score > 5 and agreeableness_score <= 10:
    result += "pretty agreeable, \n"
elif agreeableness_score >10 and agreeableness_score <= 15:
    result += "quite agreeable, \n"
else:
    result += "super agreeable, \n"
    
# Add an openness section to result
# Change the adverb according to score
if openness_score <= 5:
    result += "not very open, "
elif openness_score > 5 and openness_score <= 10:
    result += "somewhat open, "
elif openness_score > 10 and openness_score <= 15:
    result += "very open, "
else:
    result += "incredibly open, "
    
# Add a neuroticism section to result
# Change the adverb according to score
if neuroticism_score <= 5:
    result += "and not very neurotic! See you next time :)"
elif neuroticism_score > 5 and neuroticism_score <= 10:
    result += "and fairly neurotic! See you next time :)"
elif neuroticism_score >10 and neuroticism_score <= 15:
    result += "and very neurotic! See you next time :)"
else:
    result += "and neurotic beyond belief! See you next time :)"

# Print the final string
print(result)



# Import matplotlib in order to provide a bar graph
from matplotlib.ticker import FuncFormatter
# Display graphs in Jupyter Notebooks
%matplotlib inline
# Make pyplot callable as plt
import matplotlib.pyplot as plt
# Make numpy callable as np
import numpy as np

# Use numpy to specify spacing on bar graph
y = np.arange(0, 10, 2)

# Feed in list of traits
trait_list = [extroversion_score, conscientiousness_score, agreeableness_score, openness_score, neuroticism_score]


# Define a function that takes two inputs, x value and position
# matplotlib defaults to x values going up/down and y values going left/right
def trait_percentage(x, pos):
    return '%1.1f%%' % (x / 20 * 100)


# Formats vertical axis labels
formatter = FuncFormatter(trait_percentage)

# Create a graph of size 10x5
fig, ax = plt.subplots(figsize = (10, 5))
ax.yaxis.set_major_formatter(formatter)
# Plot the data into a bar graph
plt.bar(y, trait_list)
# Label horizontal axis with appropriate labels
plt.xticks(y, ('Extroverted', 'Conscientious', 'Agreeable', 'Open', 'Neurotic'))

# Display the graph
plt.show()








pass
