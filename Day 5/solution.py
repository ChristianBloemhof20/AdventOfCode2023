seeds = []
sts = {}
stf = {}
ftw = {}
wtl = {}
ltt = {}
tth = {}
htl = {}
currMap = None

#Parse Input
with open('input1.txt', 'r') as file:
    for line in file:
        line = line.replace('\n', '').split(' ')
        
        if line[0] == 'seeds:':
            for i in range(1, len(line)):
                seeds.append(int(line[i]))
        elif len(line) == 3:
            currMap[(int(line[1]), int(line[1])+int(line[2])-1)] = int(line[0]) - int(line[1])
        elif len(line) == 2:
            if line[0] == 'seed-to-soil': currMap = sts
            if line[0] == 'soil-to-fertilizer': currMap = stf
            if line[0] == 'fertilizer-to-water': currMap = ftw
            if line[0] == 'water-to-light': currMap = wtl
            if line[0] == 'light-to-temperature': currMap = ltt
            if line[0] == 'temperature-to-humidity': currMap = tth
            if line[0] == 'humidity-to-location': currMap = htl


order = [sts, stf, ftw, wtl, ltt, tth, htl, None]

#Part 1
part1 = float("inf")
for s in seeds:
    currMap = 0
    currVal = s
    while order[currMap] != None:
        for i in order[currMap]:
            if currVal >= i[0] and currVal <= i[1]:
                currVal += order[currMap][i]
                break
        currMap += 1
    part1 = min(part1, currVal)

print('Part 1:', part1)


#Part 2
currRanges = []
for s in range(0, len(seeds), 2):
    currRanges.append([seeds[s], seeds[s]+seeds[s+1]-1])

#Split ranges into every subrange
sr = 0
for s in currRanges:
    adds = [0] * len(currRanges)
    currMap = 0
    while order[currMap] != None:
        for m in order[currMap]:
            #seeds inside map
            if s[0] >= m[0] and s[1] <= m[1]:
                s[0] += order[currMap][m]
                s[1] += order[currMap][m]
                adds[sr] += order[currMap][m]
                break
            #map inside seeds
            elif m[0] >= s[0] and m[1] <= s[1]:
                adds += [0,0]
                currRanges.append([s[0]-adds[sr], m[0]-1-adds[sr]])
                currRanges.append([m[1]+1-adds[sr], s[1]-adds[sr]])
                s[0] = m[0] + order[currMap][m]
                s[1] = m[1] + order[currMap][m]
                adds[sr] += order[currMap][m]
                break
            #overlap with seeds first
            elif s[0] < m[0] and s[1] >= m[0] and s[1] <= m[1]:
                adds += [0]
                currRanges.append([s[0]-adds[sr], m[0]-1-adds[sr]])
                s[0] = m[0] + order[currMap][m]
                s[1] += order[currMap][m]
                adds[sr] += order[currMap][m]
                break
            #overlap with map first
            elif m[0] < s[0] and m[1] >= s[0] and m[1] <= s[1]:
                adds += [0]
                currRanges.append([m[1]+1-adds[sr], s[1]-adds[sr]])
                s[0] += order[currMap][m]
                s[1] = m[1] + order[currMap][m]
                adds[sr] += order[currMap][m]
                break
        currMap += 1
    sr += 1

part2 = float("inf")
currRanges.sort()
for c in currRanges:
    part2 = min(part2, c[0])

print('Part 2:', part2)