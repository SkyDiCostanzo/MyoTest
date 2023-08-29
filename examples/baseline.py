print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Running baseline.py")

import gym
import myosuite, deprl

env = gym.make('myoChallengeChaseTagP1-v0')
policy = deprl.load_baseline(env)

episodes = 10

for ep in range(episodes):
    print('Episode: {ep} of {episodes}')
    state = env.reset()
    while True:
        action = policy(state)
        
        # This is the line that renders the episodes. These episodes aren't training, just the policy doing it's best
        env.mj_render()
        
        next_state, reward, done, info = env.step(action)
        state = next_state
        if done: 
            break

    # If you want to print the reward for each episode, uncomment this. The reward is 0 until you define a reward function. This enviroment doesnt come with its own reward function
    # print("Reward: {}".format(reward))
