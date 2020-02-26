import gym
import numpy as np

n_steps = 5000

env_name = "BipedalWalker-v2"
env = gym.make(env_name)

num_deltas = 16
best_deltas = 8

#def gen_deltas(num_deltas):



state = env.reset()
env.render()

cur_step = 0
done = False

while not done or cur_step < n_steps:
    action = env.action_space.sample()
    new_state, reward, done, _ = env.step(action)
    env.render()

    state = new_state
    cur_step += 1
    if done:
        break