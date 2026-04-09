class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        cnt = {
            0: 0,
            1: 0
        }

        for i in students:
            if i not in cnt:
                cnt[i] = 0
            cnt[i] += 1

        for s in sandwiches:
            if cnt[s] > 0:
                res -= 1
                cnt[s] -= 1
            else:
                return res
        return res
        


        