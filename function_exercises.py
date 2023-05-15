#!/usr/bin/env python
# coding: utf-8

# ### 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[68]:


def is_two(num):
    if num in [2, '2']:
        return True
    else:
        return False


# In[73]:


list_of_nums = [2, 6, '4', 99, '2', '2', 4]
list_of_nums

for num in list_of_nums:
    print(f' {num} is 2: {is_two(num)}')


# ### 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# In[5]:


def is_vowel(string):
    if string.lower() in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False


# In[22]:


list_of_chars = ['r', 'w', 'i', 'h', 'a', 'a']

for char in list_of_chars:
    print(f'{char}: {is_vowel(char)}')


# ### 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# In[17]:


def is_consonant(str):
    if str.lower() not in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False


# In[21]:


list_of_chars = ['r', 'w', 'i', 'h', 'a', 'a']

for char in list_of_chars:
    print(f'{char}: {is_consonant(char)}')


# ### 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[23]:


def capitalize_if_consonant(word):
    if word[0] not in ['a', 'e', 'i', 'o', 'u']:
        word = word.capitalize()
    return word


# In[25]:


test_words = ['guacamole', 'anomaly', 'chartreuse', 'cowabunga', 'ukelele', 'tsunami', 'aardvark', ]

for word in test_words:
    print(capitalize_if_consonant(word))


# ### 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[54]:


def calculate_tip(bill, percent):
    return round(bill * (1 + percent), 2)


# In[30]:


sample_percents = [.04, .13, .18, .22]

for percent in sample_percents:
    print(calculate_tip(25, percent))


# ### 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[31]:


def apply_discount(price, disc_percentage):
    return price * (1 - disc_percentage)


# In[34]:


test_discounts = [.15, .20, .35, .70, .55]

for disc in test_discounts:
    print(round(apply_discount(150, disc), 2))


# ### 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[35]:


def handle_commas(numstr):
    numstr = numstr.replace(',', '')
    return numstr


# In[36]:


test_nstrings = ['1,000,000', '69,420', '55,555,555,555,555', '987,654,432']

for nstring in test_nstrings:
    print(handle_commas(nstring))


# ### 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# In[38]:


def get_letter_grade(grade):
    if grade > 89:
        return 'A'
    elif grade > 79:
        return 'B'
    elif grade > 69:
        return 'C'
    elif grade > 59:
        return 'D'
    else:
        return 'F'


# In[39]:


test_grades = [55, 67, 98, 33, 83, 79]

for grade in test_grades:
    print(get_letter_grade(grade))


# ### 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[45]:


def remove_vowels(str):
    for char in str:
        if char.lower() in ['a', 'e', 'i', 'o', 'u']:
            str = str.replace(char, '')
    return str


# In[46]:


test_strings = ['monkey', 'appalachia', 'kandahar', 'Abu Dhabi', 'kerfuffle']

for string in test_strings:
    print(remove_vowels(string))


# In[ ]:














# ### 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# * anything that is not a valid python identifier should be removed
# * leading and trailing whitespace should be removed
# * everything should be lowercase
# * spaces should be replaced with underscores
# * for example:
# ** Name will become name
# ** First Name will become first_name
# ** % Completed will become completed

# In[2]:


def normalize_name(str):
    str = str.strip()
    str = str.lower()
    str = str.replace(' ', '_')
    return str


# In[3]:


test_strings = ['TedBundy', 
                'R i c k y B o B B y', 
                'Prince Rogers Nelson', 
                'TYRIONLANNISTER', 
                'Jim', 
                'The Real Slim Shady', 
                'darkwingduck' ]

for string in test_strings:
    print(f"'{string}'{' ' * (20 - len(string))} --> '{normalize_name(string)}'")


# In[ ]:












# ### 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# * cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# * cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# In[65]:


def cumulative_sum(numlist):
    csum = []
    num_so_far = 0
    for num in numlist:
        num_so_far += num
        csum.append(num_so_far)
    return csum


# In[67]:


test_numlists = [[1,4,5,6,3,2], [1,1,1,1,1], [9,7,5,3,1], [3,3,3,3,3,3,3,3,3,3,3]]

for list in test_numlists:
    print(cumulative_sum(list))

