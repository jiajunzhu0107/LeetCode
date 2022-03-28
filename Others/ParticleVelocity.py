# https://algo.monster/problems/particle_velocity
def particleVelocity(particles):
    # WRITE YOUR BRILLIANT CODE HERE
    res = 0
    if len(particles) < 3:
        return 0
    prev_v = particles[1] - particles[0]
    leng_period = 2
    for i in range(2,len(particles)):
        curr_v = particles[i] - particles[i-1]
        if curr_v == prev_v:
            res += leng_period - 1
            leng_period += 1
        else:
            prev_v = curr_v
            leng_period = 2
            continue
    
    if res > 10 ** 9:
        res = -1
    return res