"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 20/05/20
* @decription: Write a Python program to determine profiling of Python programs
    A profile is a set of statistics that describes how often and for how long various parts of the program executed.
    These statistics can be formatted into reports via the pstats module.
"""
import profile


def explore_a_list():
    for each in range(100):
        pass


profile.run('explore_a_list()')
