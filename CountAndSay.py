class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return str(1)
        if n > 1:
            number = self.countAndSay(n-1)
            num_string = number
            length = len(num_string)
            count = 1
            num = num_string[0]
            return_str = ''
            if length == 1:
                return str(count) + num
            else:
                for i in range(1, len(num_string)):
                    if num_string[i] == num:
                        count += 1
                        continue
                    else:
                        return_str += str(count) + num
                        num = num_string[i]
                        count = 1
                return_str += str(count) + num
                return return_str

if __name__ == '__main__':
    solution = Solution()
    print(solution.countAndSay(1))
    print(solution.countAndSay(4))
    print(solution.countAndSay(5))
    print(solution.countAndSay(10))
