class Nonogram():
    def __init__(self, rows=None, columns=None):
        #sets class attributes
        if rows != None and columns != None:
            self.rows = rows
            self.columns = columns
        else: #create a random nonogram
            pass
        self.grid = [[0 for i in range(len(self.columns))] for j in range(len(self.rows))]
    
    def solve(self):
        #solves the nonogram
        while True:
            if self.check_solved():
                return
            else:
                for y in range(len(self.rows)):
                    if (self.grid[y]).count(1) == sum(self.rows[y]):
                        for x in range(len(self.grid[y])):
                            if self.grid[y][x] == 0:
                                self.grid[y][x] = -1
                    if (self.grid[y]).count(0) == sum(self.rows[y])-(self.grid[y]).count(1):
                        for x in range(len(self.grid[y])):
                            if self.grid[y][x] == 0:
                                self.grid[y][x] = 1
                    combos = self.check_combos(self.find_combos(len(self.rows)), self.rows, y)
                    final = [True for i in range(len(self.rows))]
                    pop_list = []
                    for i in range(len(combos)):
                        if self.binary_and(lst1 = combos[i], lst2 = self.num_to_bool(self.grid[y])) != self.num_to_bool(self.grid[y]):
                            pop_list.append(i)
                        for j in range(len(combos[i])):
                            var = 0
                            if self.grid[y][j] == -1 and combos[i][j]:
                                var += 1
                            if var != 0:
                                pop_list.append(i)
                    pop_list = list(set(pop_list))
                    pop_list.sort(reverse=True)
                    for i in pop_list:
                        combos.pop(i)
                    for combo in combos:
                        final = self.binary_and(final, combo)
                    self.grid[y] = final
                for x in range(len(self.columns)):
                    data = []
                    for y in range(len(self.grid)):
                        data.append(self.grid[y][x])
                    if (data).count(1) == sum(self.columns[x]):
                        for y in range(len(self.grid)):
                            if self.grid[y][x] == 0:
                                self.grid[y][x] = -1
                    if (data).count(0) == sum(self.columns[x])-(data).count(1):
                        for y in range(len(self.grid)):
                            if self.grid[y][x] == 0:
                                self.grid[y][x] = 1
                    combos = self.check_combos(self.find_combos(len(self.columns)), self.columns, x)
                    final = [True for i in range(len(self.columns))]
                    pop_list = []
                    for i in range(len(combos)):
                        if (self.binary_and(combos[i], self.num_to_bool(data)) != self.num_to_bool(data)):
                            pop_list.append(i)
                        for j in range(len(combos[i])):
                            var = 0
                            if data[j] == -1 and combos[i][j]:
                                var += 1
                            if var != 0:
                                pop_list.append(i)
                    pop_list.sort(reverse=True)
                    for i in pop_list:
                        combos.pop(i)
                    for combo in combos:
                        final = self.binary_and(final, combo)
                    for y in range(len(self.grid)):
                        self.grid[y][x] = final[y]
    
    def check_solved(self):
        #checks if the nonogram is solved
        count = 0
        for y in range(len(self.rows)):
            count += (self.grid[y]).count(1)
        total = 0
        for i in range(len(self.rows)):
            total += sum(self.rows[i])
        if count == total:
            return True
        else:
            return False

    def binary_and(self,lst1,lst2):
        #returns the binary AND of two lists
        result = []
        for i in range(len(lst1)):
            if lst1[i] and lst2[i]:
                result.append(True)
            else:
                result.append(False)
        return result
    
    def num_to_bool(self, lst):
        #converts a list of numbers to a list of booleans
        result = []
        for i in range(len(lst)):
            if lst[i] == 1:
                result.append(True)
            else:
                result.append(False)
        return result
    
    def check_combos(self, combo_list, line, pos):
        #checks if each combo in combo_list is valid and returns the valid ones
        new_combos = []
        for combo in combo_list:
            result = [0]
            current_pos = 0
            for val in combo:
                if val:
                    result[current_pos] += 1
                else:
                    if result[current_pos] != 0:
                        result.append(0)
                        current_pos += 1
            if result[-1] == 0:
                result.pop(-1)
            if result == line[pos]:
                new_combos.append(combo)
        return new_combos


    def find_combos(self, length):
        #finds all possible combinations of booleans of length 'length'
        if length == 0:
            return [[]]
        else:
            return [[False] + combo for combo in self.find_combos(length - 1)] + [[True] + combo for combo in self.find_combos(length - 1)]

    def __str__(self):
        #formats the nonogram to print
        filled = "■"
        unfilled = "□"
        xed = "⛝"
        grid = ""
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == 1:
                    grid += filled
                elif self.grid[y][x] == -1:
                    grid += xed
                else:
                    grid += unfilled
                grid += " "
            grid += "\n"
        return grid


test = Nonogram([[1],[1,1],[3,1],[1,3],[2]],[[4],[1],[2],[2],[4]])
test.solve()
print(test)