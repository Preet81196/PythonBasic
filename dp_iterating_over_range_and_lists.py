"""
 * @author Divyesh Patel
 * @email pateldivyesh009@gmail.com
 * @create date 18-05-2020 07:02:43
 * @modify date 18-05-2020 07:02:43
 * @desc Range Vs List Iteration Performace test using Python's Built-In module timeit, Attached link refers to the Plot of test outcomes
"""
# TODO: swapping x and y Axes with each other
#       generating more results with increase in iteration_cases using list comprehension
#       storing results in files and plotting them using matplot lib

# Notes
# The results are produced here at https://imgur.com/a/IO0Z6RX

# Results for Intel i5 DDR3 8 GB Ram, OS MacOs Catalina 10.15.3

import timeit

iteration_cases = [10, 100, 1000, 10000, 100000, 1000000, 2000000, 3000000, 6000000, 10000000, 12000000, 30000000, 50000000, 100000000] # upto 10 Cr

list_result = []
range_result = []


for each in iteration_cases:
    setup_for_list = 'alist = [str(each) for each in range(%s)]' % str(each)
    setup_for_range = 'for each in range(%s): pass' % str(each)

    list_result.append(timeit.timeit('for each in alist: pass', setup=setup_for_list, number=10))
    range_result.append(timeit.timeit(setup_for_range, number=10))

print(list_result) # [2.560000000002144e-06, 1.05640000000011e-05, 9.733499999999701e-05, 0.0009547130000000029, 0.011746447999999993, 0.12862854099999999, 0.24252997899999995, 0.3633072799999999, 1.2874315390000008, 1.6970225820000007, 1.7553785880000028, 3.6755533919999976, 7.821054337999996, 109.112779517]
print(range_result) # 5.899000000000182e-06, 1.6514000000002194e-05, 0.00022325399999999912, 0.002495780000000003, 0.025142051, 0.25421969899999997, 0.5049327350000001, 0.8119190670000003, 1.9548219190000005, 3.0123160769999995, 3.478548472, 7.541595660999995, 13.864057238000001, 25.636940737000003]

