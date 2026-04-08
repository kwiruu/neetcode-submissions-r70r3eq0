class Solution:
    def calPoints(self, operations: List[str]) -> int:
        temp = []
        for i in range(len(operations)):
            match operations[i]:
                case 'D':
                    temp.append(int(temp[-1])*2)
                case '+':
                    temp.append(int(temp[-2])+int(temp[-1]))
                case 'C':
                    temp.pop()
                case _:
                    temp.append(int(operations[i]))

        return sum(temp)

            