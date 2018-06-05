def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)

# search = grep("pattern")
# next(search)
# search.send("First kattern")
# search.send("Second pattern")

# list_ob = [x-2 for x in range(-2,8)]
# gen_ob = (x-2 for x in range(-2,8))
#
# for i in list_ob:
#     print i
#
#
# next(gen_ob)
#
# print gen_ob
# for i in gen_ob:
#     print i
#
# print gen_ob
# for j in gen_ob:
#     print gen_ob
#     print "second time", j+10

import itertools

horses = [1, 2, 3, 4]
races = list(itertools.permutations(horses))
for i in races:
    print reduce(lambda x, y : x + y, (y for y in i))
print '####'
print races
