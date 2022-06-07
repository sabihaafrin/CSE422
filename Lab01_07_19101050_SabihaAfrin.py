# Question no 01

dfs_sample1 = []
file = open('txt1.txt', 'r')
read = file.readline()
for line in file:
    dfs_sample1.append(line.split())

dfs_sample2 = []
file = open('txt2.txt', 'r')
read = file.readline()
for line in file:
    dfs_sample2.append(line.split())


def dfs(i, j, graph, level = 0):
    graph[i][j] = level
    level = level + 1
    if i > 0 and j > 0 and graph[i][j] == "Y":
        level = dfs(i, j, graph, level)

    if i > 0 and graph[i - 1][j] == 'Y':
        level = dfs(i - 1, j, graph, level)

    if i > 0 and j < len(graph[0]) - 1 and graph[i - 1][j + 1] == 'Y':
        level = dfs(i - 1, j + 1, graph, level)

    if j < len(graph[0]) - 1 and graph[i][j + 1] == 'Y':
        level = dfs(i, j + 1, graph, level)

    if i < len(graph) - 1 and j < len(graph[0]) - 1 and graph[i + 1][j + 1] == 'Y':
        level = dfs(i + 1, j + 1, graph, level)

    if i < len(graph) - 1 and graph[i + 1][j] == 'Y':
        level = dfs(i + 1, j, graph, level)

    if i < len(graph) - 1 and j > 0 and graph[i + 1][j - 1] == 'Y':
        level = dfs(i + 1, j - 1, graph, level)

    if j > 0 and graph[i][j - 1] == 'Y':
        level = dfs(i, j - 1, graph, level)

    if i < len(graph) - 1 and j < 0 and graph[i - 1][j - 1] == 'Y':
        level = dfs(i - 1, j - 1, graph, level)

    return level


def main():
    maximum_level = 0

    for i, row in enumerate(dfs_sample1):
        for j, col in enumerate(row):
            if col != 'N' and col == 'Y':
                iterate = dfs(i, j, dfs_sample1)

                if maximum_level < iterate:
                    maximum_level = iterate

    print(maximum_level)

    maximum_level = 0

    for i, row in enumerate(dfs_sample2):
        for j, col in enumerate(row):
            if col == 'Y':
                iterate = dfs(i, j, dfs_sample2)

                if maximum_level < iterate:
                    maximum_level = iterate

    print(maximum_level)


# question 2 with BFS

noofRow1 = 5
noofCol1 = 4
bfs_sample1 = []
file = open('txt3.txt', 'r')
read = file.readline()
for line in file:
    bfs_sample1.append(line.split())

noofRow2 = 3
noofCol2 = 3
bfs_sample2 = []
file = open('txt4.txt', 'r')
read = file.readline()
for line in file:
    bfs_sample2.append(line.split())


def bfs(col_run, row_run, visited_num, level=0):
    maximum_level = level
    graph = []
    allien = False

    for i, row in enumerate(visited_num):
        for j, col in enumerate(row):
            if col == 'A':
                graph.append([i, j])
                visited_num[i][j] = level

    for i, j in graph:
        if j > 0 and visited_num[i][j - 1] == 'H':
            visited_num[i][j - 1] = 'A'
            allien = True

        if i < row_run - 1 and visited_num[i + 1][j] == 'H':
            visited_num[i + 1][j] = 'A'
            allien = True

        if j < col_run - 1 and visited_num[i][j + 1] == 'H':
            visited_num[i][j + 1] = 'A'
            allien = True

        if i > 0 and visited_num[i - 1][j] == 'H':
            visited_num[i - 1][j] = 'A'
            allien = True

    if allien:
        maximum_level = bfs(col_run, row_run, visited_num, level + 1)

    return maximum_level


human_survived = 0
time_round = bfs(noofCol1, noofRow1, bfs_sample1)
for row in bfs_sample1:
    for col in row:
        if col == 'H':
            human_survived = human_survived + 1

    print(f'Time: {time_round}\n'
          f'{"No one " if human_survived == 0 else human_survived}  survived')

human_safe = 0
total_time = bfs(noofCol2, noofRow2, bfs_sample2)
for rows in bfs_sample2:
    for cols in row:
        if cols == 'H':
            human_safe = human_safe + 1

    print(f'Time: {total_time}\n'
          f'{"" if human_safe == 0 else human_safe} survived')
