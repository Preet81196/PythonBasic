"""
Write a Python program to get a new string from a given string where "Is" has been added to the front. 
If the given string already begins with "Is" then return the string unchanged
"""

given_st = " it Sunday Today?"
given_st = given_st.strip()

if given_st.startswith('Is'):
    print(given_st)
else:
    print("Is", given_st)