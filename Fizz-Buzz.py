# Write a program that outputs the string representation of numbers from 1 to n.

# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.


ans = []
        for i in range(1, n+1):
            if i % 5 == 0 and i % 3 == 0 : 
                ans.append("FizzBuzz")
            elif i % 3 == 0 : 
                ans.append("Fizz")
            elif i % 5 == 0 : 
                ans.append("Buzz")
            else: 
                ans.append(str(i))
        return ans