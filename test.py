from pettingzoo.sisl.oddoneout import pursuit
env = pursuit.env(render_mode="human", max_cycles=100)

env.reset()
for agent in env.agent_iter():
    observation, reward, termination, truncation, info = env.last()
    action = None if termination or truncation else env.action_space(
        agent).sample()  # this is where you would insert your policy
    print(agent, action)
    env.step(action)

env.close()
