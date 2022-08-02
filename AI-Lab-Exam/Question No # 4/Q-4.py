import random

g = [[366, 0, 160, 242, 161],
[178, 77, 151, 226, 244],
[241, 234, 380, 98, 193],
[253, 329, 80, 199, 374],
[71, 75, 118, 111, 138]]

def beam_search_best(grid, k):
# loop to get k random states
random_states = []



for i in range(0,k):
s = []
r = random.randint(0,4)
c = random.randint(0,4)
s.append(r)
s.append(c)
if s not in random_states:
random_states.append(s)
else:
s = []
r = random.randint(0,4)
c = random.randint(0,4)
s.append(r)
s.append(c)
random_states.append(s)

print('Random states:',random_states)
# loop
while True:

# get all successors of all k states
successors = []
for i in random_states:
r = i[0]
c = i[1]
up = [r-1, c]
dwn = [r+1, c]
rgt = [r, c+1]
lft = [r, c-1]
if up[0] >= 0 and up[0] <= 4 and up[1] >= 0 and up[1] <= 4:
if up not in successors and up not in random_states:
successors.append(up)



if dwn[0] >= 0 and dwn[0] <= 4 and dwn[1] >= 0 and dwn[1] <= 4:
if dwn not in successors and dwn not in random_states:
successors.append(dwn)
if rgt[0] >= 0 and rgt[0] <= 4 and rgt[1] >= 0 and rgt[1] <= 4:
if rgt not in successors and rgt not in random_states:
successors.append(rgt)
if lft[0] >= 0 and lft[0] <= 4 and lft[1] >= 0 and lft[1] <= 4:
if lft not in successors and lft not in random_states:
successors.append(lft)
print('successors:',successors)

# finding sol: if any random state has greater value than all the
successors in the list
for i in random_states:
for j in successors:
if grid[i[0]][i[1]] > grid[j[0]][j[1]]:
flg = True
continue
else:
flg = False
break
if flg == True:
print('Solution:',i[0],i[1])
return (i[0],i[1])

# if solution not found
# get k best successors
succ_vals = []
succ = successors
for i in range(0,k):



max_val = 0
for j in succ:
val = grid[j[0]][j[1]]
print('Val:',val)
if val > max_val:
max_val = val
row = j[0]
col = j[1]
succ_vals.append([row,col])
print('Appending successor:',succ_vals)
print('max',max_val)
succ.remove([row,col])

print('succ_vals:',succ_vals)
random_states = succ_vals

#============================================================

def beam_search_random(grid, k):
# loop to get k random states
random_states = []
for i in range(0,k):
s = []
r = random.randint(0,4)
c = random.randint(0,4)
s.append(r)
s.append(c)
if s not in random_states:



random_states.append(s)
else:
s = []
r = random.randint(0,4)
c = random.randint(0,4)
s.append(r)
s.append(c)
random_states.append(s)

print('Random states:',random_states)
# loop
while True:

# get all successors of all k states
successors = []
for i in random_states:
r = i[0]
c = i[1]
up = [r-1, c]
dwn = [r+1, c]
rgt = [r, c+1]
lft = [r, c-1]
if up[0] >= 0 and up[0] <= 4 and up[1] >= 0 and up[1] <= 4:
if up not in successors and up not in random_states:
successors.append(up)
if dwn[0] >= 0 and dwn[0] <= 4 and dwn[1] >= 0 and dwn[1] <= 4:
if dwn not in successors and dwn not in random_states:
successors.append(dwn)
if rgt[0] >= 0 and rgt[0] <= 4 and rgt[1] >= 0 and rgt[1] <= 4:
if rgt not in successors and rgt not in random_states:
successors.append(rgt)
if lft[0] >= 0 and lft[0] <= 4 and lft[1] >= 0 and lft[1] <= 4:



if lft not in successors and lft not in random_states:
successors.append(lft)
print('successors:',successors)

# finding sol: if any random state has greater value than all the
successors in the list
for i in random_states:
for j in successors:
if grid[i[0]][i[1]] > grid[j[0]][j[1]]:
flg = True
continue
else:
flg = False
break
if flg == True:
print('Solution:',i[0],i[1])
return (i[0],i[1])

# if solution not found
# get k random successors
succ_vals = []
for i in range(0,k):
succ = random.choice(successors)
succ_vals.append(succ)
print('Randomly selected k successors:',succ_vals)
random_states = succ_vals

#======================================================================
if __name__ == '__main__':



result = beam_search_best(g, 4)
print('Beam Search (best k successors)',result,'\n')
print('-----------------\n')
result2 = beam_search_random(g, 4)
print('Beam Search (random k successors)',result2)