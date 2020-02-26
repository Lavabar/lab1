import gym
env = gym.make('CartPole-v0')
env.reset()
for _ in range(1000):
    env.render()
    obs, rew, done, _ = env.step(env.action_space.sample()) # take a random action
    print(obs)
    print(rew)
    print()
    #if done:
    #    env.reset()