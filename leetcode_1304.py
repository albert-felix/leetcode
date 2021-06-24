def sumZero(self, n: int) -> List[int]:
        if n ==1:
            return [0]
        elif n % 2 == 0:
            result = []
            for i in range(1,n//2+1):
                result.extend([i, -i])
            return result
        else:
            result = []
            for i in range(1,n//2+1):
                result.extend([i, -i])
            result.append(0)
            return result
