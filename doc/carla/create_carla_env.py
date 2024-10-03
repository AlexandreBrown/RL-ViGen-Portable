import matplotlib.pyplot as plt
from wrappers.carla_wrapper import carla_make
from dm_env import StepType

if __name__ == "__main__":

    config = {
        "ip": "localhost",
        "port": 2000,
        "traffic_manager_port": 8018,
        "max_episode_steps": 1000,
        "frame_skip": 2,
        "render_display": 0,
        "display_text": 0,
        "record_display_images": 0,
        "record_rl_images": 0,
        "rl_image_size": 84,
        "fov": 60,
        "cameras": ["foresight0"],
        "map": "Town04",
        "weather": "Default",
        "changing_weather_speed": 0.1,
        "vehicle": "vehicle.lincoln.mkz_2017",
        "vehicle_spawn_point_id": "train",
        "num_other_cars": 40,
        "num_other_cars_nearby": 8,
    }

    action_repeat = 2  # Feel free to change this

    env = carla_make(config, action_repeat=action_repeat)

    timestep = env.reset()

    done = False
    total_reward = 0.0
    episode = 0
    max_nb_trajs_for_test = 2
    frame_id = 0

    obs_for_visualization_purposes = []
    try:
        while episode < max_nb_trajs_for_test:
            action = env.action_space.sample()

            timestep = env.step(action)[0]
            done = timestep.step_type == StepType.LAST
            step_reward = timestep.reward

            total_reward += step_reward

            print(
                f"Episode: {episode} Step Reward: {step_reward:.4f}, Total Reward: {total_reward:.4f}"
            )

            if frame_id % 20 == 0:
                latest_observation = timestep.observation[-3:].transpose(1, 2, 0)
                obs_for_visualization_purposes.append(
                    (latest_observation, episode, frame_id, step_reward)
                )

            if done:
                env.reset()
                episode += 1
                frame_id = 0
            else:
                frame_id += 1
    except:
        pass

    env.finish()

    for obs, episode, frame_id, step_reward in obs_for_visualization_purposes:
        fig, ax = plt.subplots()
        ax.set_title(
            f"Episode: {episode}, frame index: {frame_id}, step reward: {step_reward}"
        )
        plt.imshow(obs)
        plt.show()
        plt.close(fig)
