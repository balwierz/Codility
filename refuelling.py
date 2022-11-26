import collections
def solution(fuel, pos):
    state = collections.defaultdict(int)
    for i in range(len(pos)):
        state[(i, True)] = fuel[i] # left position, 0/1 which end left/right we are at, value fuel in the tank
    width = -1
    while len(state):
        newState = collections.defaultdict(int)
        width += 1
        for [left, side], tank in state.items():
            if left:  # try to extend to the left
                val = tank - pos[left + width * side] + pos[left-1]
                if val >= 0:  # there is enough fuel to get to city left-1
                    key = (left-1, False)
                    newState[key] = max(newState[key], val + fuel[left-1])
            if left + width + 1 < len(pos):  # try extending to the right
                val = tank - pos[left + width + 1] + pos[left + width * side]
                if val >= 0: # there is enough fuel to get to city left + width + 1
                    key = (left, True)
                    newState[key] = max(newState[key], val + fuel[left + width + 1])
        state = newState
    return width + 1
