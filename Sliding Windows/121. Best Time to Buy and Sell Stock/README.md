# 121. Best Time to Buy and Sell Stock

#### EASY

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

## Solution

Given a point/price in the input array, the max profit you could make at that point would be the current price - the minimum price of all the points to the left. So, you can iterate the array and continously update the minimum price encountered and continously update the answer by taking the max of the current answer and the current price - minimum price.
