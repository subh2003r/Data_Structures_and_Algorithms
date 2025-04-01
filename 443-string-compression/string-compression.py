from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        c = 1
        n = len(chars)
        write_index = 0  # Position to write compressed characters

        for i in range(1, n + 1):  # Extend loop to ensure last char is processed
            if i < n and chars[i - 1] == chars[i]:
                c += 1  # Increase count for repeating chars
            else:
                # Write character
                chars[write_index] = chars[i - 1]
                write_index += 1
                # Write count if greater than 1
                if c > 1:
                    for digit in str(c):  # Split multi-digit count
                        chars[write_index] = digit
                        write_index += 1
                c = 1  # Reset count
        
        # Remove extra elements beyond `write_index`
        while len(chars) > write_index:
            chars.pop()

        return write_index  # Return new length


        # c = 1
        # for i in range(1, len(chars)):
        #     if chars[i-1] == chars[i]:
        #         c += 1
        #         chars[i-1] = c
        #     # print(c)
        #     else:
        #         c = 1
        # print(chars)

        # k = 0
        # p = 0
        # while k != len(chars):
        #     if str(chars[k]).isdigit() and str(chars[k+1]).isalpha():
        #         chars[k], chars[k+1] = chars[k+1], str(chars[k])
        #         if int(chars[k+1]) >= 10:
        #             temp = chars[k+1]
        #             for i in range(len(temp)):
        #                 if int(chars[k+1]) >= 10:
        #                     chars[k+1] = str(temp)[i]
        #                 else:
        #                     print(i, temp)
        #                     chars.insert(int(chars[k+1+i]), str(temp)[i])
        #         k += 2
        #         continue
        #     elif str(chars[k]).isdigit() and str(chars[k+1]).isdigit():
        #         chars.pop(k) 
        #         continue
        #     k+=1
        # print(chars)









        # lst = Counter(chars)
        # # lst = sorted(lst)
        # for i, j in lst.items():
        #     if j == 1:
        #         sol.append(i)
        #     else:
        #         sol.append(i)
        #         if j >= 10:
        #             for l in range(len(str(j))):
        #                 sol.append(str(j)[l])
        #         else:
        #             sol.append(str(j))
        # lst = sol
        # print(sol)