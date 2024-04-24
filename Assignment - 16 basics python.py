#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''1. Create a list called years_list, starting with the year of your birth, and each year thereafter until
the year of your fifth birthday. For example, if you were born in 1980. the list would be years_list =
[1980, 1981, 1982, 1983, 1984, 1985].'''

birth_year = 2000  # Replace this with your birth year
years_list = [birth_year + i for i in range(5)]
print(years_list)


# In[2]:


'''
2. In which year in years_list was your third birthday? Remember, you were 0 years of age for your
first year.
'''

birth_year = 2000  # Replace this with your birth year
years_list = [birth_year + i for i in range(5)]

# Your third birthday occurred when you were 2 years old
year_of_third_birthday = years_list[2]
print(year_of_third_birthday)


# In[3]:


'''3.In the years list, which year were you the oldest?'''

birth_year = 2000  # Replace this with your birth year
years_list = [birth_year + i for i in range(5)]

oldest_year = years_list[-1]
print(oldest_year)


# In[4]:


'''
4. Make a list called things with these three strings as elements: &quot;mozzarella&quot;, &quot;cinderella&quot;,
&quot;salmonella&quot;.
'''
things = ["mozzarella", "cinderella", "salmonella"]
print(things)



# In[5]:


'''
5. Capitalize the element in things that refers to a person and then print the list. Did it change the
element in the list?
'''
things = ["mozzarella", "cinderella", "salmonella"]
things[1] = things[1].capitalize()
print(things)



# In[6]:


'''
6. Make a surprise list with the elements &quot;Groucho,&quot;
&quot;Chico,&quot; and &quot;Harpo.&quot;
'''

surprise = ["Groucho", "Chico", "Harpo"]
print(surprise)



# In[7]:


'''
7. Lowercase the last element of the surprise list, reverse 
it, and then capitalize it.
'''
surprise = ["Groucho", "Chico", "Harpo"]

# Lowercase the last element
last_element_lower = surprise[-1].lower()

# Reverse the string
reversed_last_element = last_element_lower[::-1]

# Capitalize it
capitalized_reversed_last_element = reversed_last_element.capitalize()

print(capitalized_reversed_last_element)



# In[8]:


'''
8. Make an English-to-French dictionary called e2f and print it. Here are your starter words: dog is
chien, cat is chat, and walrus is morse.

'''
e2f = {
    "dog": "chien",
    "cat": "chat",
    "walrus": "morse"
}

print(e2f)



# In[9]:


'''
9. Write the French word for walrus in your three-word dictionary e2f.
'''
e2f = {
    "dog": "chien",
    "cat": "chat",
    "walrus": "morse"
}

french_word_for_walrus = e2f["walrus"]
print(french_word_for_walrus)



# In[10]:


'''
10. Make a French-to-English dictionary called f2e from e2f. Use the
items method.
'''
e2f = {
    "dog": "chien",
    "cat": "chat",
    "walrus": "morse"
}

f2e = {french: english for english, french in e2f.items()}
print(f2e)



# In[11]:


'''
11. Print the English version of the French word chien using f2e.
'''
e2f = {
    "dog": "chien",
    "cat": "chat",
    "walrus": "morse"
}

f2e = {french: english for english, french in e2f.items()}

english_word_for_chien = f2e["chien"]
print(english_word_for_chien)



# In[12]:


'''
12. Make and print a set of English words from the keys in e2f.
'''

e2f = {
    "dog": "chien",
    "cat": "chat",
    "walrus": "morse"
}

english_words_set = set(e2f.keys())
print(english_words_set)


# In[13]:


'''
14. Print the top-level keys of life.
'''
life = {
    "animals": {
        "cats": ["Henri", "Grumpy", "Lucy"],
        "octopi": {},
        "emus": {}
    },
    "plants": {},
    "other": {}
}

top_level_keys = life.keys()
print(top_level_keys)



# In[14]:


'''
15. Print the keys for life[&#39;animals&#39;].
'''
life = {
    "animals": {
        "cats": ["Henri", "Grumpy", "Lucy"],
        "octopi": {},
        "emus": {}
    },
    "plants": {},
    "other": {}
}

animals_keys = life['animals'].keys()
print(animals_keys)



# In[15]:


'''
16. Print the values for life[&#39;animals&#39;][&#39;cats&#39;]

'''
life = {
    "animals": {
        "cats": ["Henri", "Grumpy", "Lucy"],
        "octopi": {},
        "emus": {}
    },
    "plants": {},
    "other": {}
}

cats_values = life['animals']['cats']
print(cats_values)


# In[ ]:




