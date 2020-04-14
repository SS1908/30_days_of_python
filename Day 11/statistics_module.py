"""
mean() function :- The mean() function is used to calculate the arithmetic mean of the numbers in the list.
"""
import statistics as st

#list o positive integer
data = [5,2,87,3,6,2,8]
#print mean
mean = st.mean(data)
print(mean)

# median() function :- The median() function is used to return the middle value of the numeric data in the list.
data = [5,2,87,3,6,2,8]
median = st.median(data)
print(median)

#mode() function :- The mode() function returns the most common data that occurs in the list.
data = [5,2,87,3,6,2,8]
mode = st.mode(data)
print(mode)

#stdev() function :- The stdev() function is used to calculate the standard deviation on a given sample which is available in the form of the list.
data = [5,2,87,3,6,2,8]
stddev = st.stdev(data)
print(stddev)

#median_low() :- The median_low function is used to return the low median of numeric data in the list.
data = [5,2,87,3,6,2,8]
low_median = st.median_low(data)
print(low_median)

#median_high() :- The median_high function is used to return the high median of numeric data in the list.
data = [5,2,87,3,6,2,8]
high_median = st.median_high(data)
print(high_median)