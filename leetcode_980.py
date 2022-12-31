class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def getNextPoint(newPathArr, path, nextPoint, grid):
            if(nextPoint not in path and grid[nextPoint[0]][nextPoint[1]] != -1):
                tempPath = path.copy()
                tempPath.append(nextPoint)
                newPathArr.append(tempPath)
            return newPathArr

        def find_path(pathArr, end, blocked, grid):
            if(len(pathArr) == 0):
                return len(pathArr)
            newPathArr = []
            for path in pathArr:
                start = path[-1]
                hello = len(grid)*len(grid[0]) - blocked
                if(len(path) == (len(grid))*(len(grid[0])) - blocked):
                    return len(pathArr)
                if(start == end):
                    continue
                if(start[0] < len(grid)-1):
                    nextPoint = [start[0]+1, start[1]]
                    newPathArr = getNextPoint(newPathArr, path, nextPoint, grid)
                if(start[0] > 0):
                    nextPoint = [start[0]-1, start[1]]
                    newPathArr = getNextPoint(newPathArr, path, nextPoint, grid)
                if(start[1] < len(grid[0])-1):
                    nextPoint = [start[0], start[1]+1]
                    newPathArr = getNextPoint(newPathArr, path, nextPoint, grid)
                if(start[1] > 0):
                    nextPoint = [start[0], start[1]-1]
                    newPathArr = getNextPoint(newPathArr, path, nextPoint, grid)
            finalArr = find_path(newPathArr, end, blocked, grid)
            return finalArr

        def findStartEnd(grid):
            values = {1: "start", 2: "end"}
            position = {}
            blocked = 0
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if(grid[row][col] != 0):
                        if(grid[row][col] == -1):
                            blocked += 1
                        else:
                            position[values[grid[row][col]]] = [row, col]
            position['blocked'] = blocked
            return position

        position = findStartEnd(grid)
        return find_path([[position['start']]], position['end'], position['blocked'], grid)
