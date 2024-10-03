# Carla
## Prerequisites
1. Make sure you have done the setup from the README at the root of the repository.
2. To run the CARLA environment you must first start the carla simulator.  
    To do so, you can run the script **at the root of the repository** :  
    ```shell
    bash start_carla_sim.sh
    ```  
3. Create carla environment in python :  
    Minimum Working Examples :  
 
    **Train Env**  
    ```python
    from wrappers.carla_wrapper import carla_make

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
    ```

    **Eval Env**  
    ```python
    from wrappers.carla_wrapper import carla_make_eval

    config = {
        "setting": {
            "weather": {
                "custom_hard_high_light": {
                    "cloudiness": 0,
                    "precipitation": 0,
                    "precipitation_deposits": 0,
                    "wind_intensity": 0,
                    "fog_density": 0,
                    "fog_distance": 0,
                    "wetness": 0,
                    "sun_azimuth_angle": 0,
                    "sun_altitude_angle": 90,
                },
                "custom_soft_high_light": {
                    "cloudiness": 20,
                    "precipitation": 0,
                    "precipitation_deposits": 0,
                    "wind_intensity": 0,
                    "fog_density": 20,
                    "fog_distance": 0,
                    "wetness": 0,
                    "sun_azimuth_angle": 0,
                    "sun_altitude_angle": 10,
                },
                "custom_soft_low_light": {
                    "cloudiness": 50,
                    "precipitation": 0,
                    "precipitation_deposits": 0,
                    "wind_intensity": 0,
                    "fog_density": 30,
                    "fog_distance": 0,
                    "wetness": 0,
                    "sun_azimuth_angle": 0,
                    "sun_altitude_angle": 5,
                },
                "custom_hard_low_light": {
                    "cloudiness": 100,
                    "precipitation": 0,
                    "precipitation_deposits": 0,
                    "wind_intensity": 0,
                    "fog_density": 100,
                    "fog_distance": 0,
                    "wetness": 0,
                    "sun_azimuth_angle": 0,
                    "sun_altitude_angle": -90,
                },
                "custom_soft_noisy_low_light": {
                    "cloudiness": 80,
                    "precipitation": 50,
                    "precipitation_deposits": 50,
                    "wind_intensity": 0,
                    "fog_density": 30,
                    "fog_distance": 0,
                    "wetness": 0,
                    "sun_azimuth_angle": 0,
                    "sun_altitude_angle": 20,
                },
                "custom_hard_noisy_low_light": {
                    "cloudiness": 100,
                    "precipitation": 100,
                    "precipitation_deposits": 100,
                    "wind_intensity": 100,
                    "fog_density": 100,
                    "fog_distance": 0,
                    "wetness": 0,
                    "sun_azimuth_angle": 0,
                    "sun_altitude_angle": -90,
                },
            },
            "scenario": {
                "train": {"map": "Town04"},
                "highway": {
                    "map": "Town04",
                    "ego_veh": {
                        "road_id": 47,
                        "lane_id": [-1, -2, -3, -4],
                        "start_pos": [65, 70],
                        "speed": 0,
                    },
                },
                "roundabout": {
                    "map": "Town03",
                    "ego_veh": {
                        "road_id": 1100,
                        "lane_id": [-4, -5],
                        "start_pos": [8, 12],
                        "speed": 0,
                    },
                },
                "narrow": {
                    "map": "Town01",
                    "ego_veh": {
                        "road_id": 12,
                        "lane_id": [-1],
                        "start_pos": [0.2, 2.2],
                        "speed": 10,
                    },
                },
                "tunnel": {
                    "map": "Town03",
                    "ego_veh": {
                        "road_id": 1166,
                        "lane_id": [2, 3],
                        "start_pos": [2, 5],
                        "speed": 0,
                    },
                },
            },
        },
        "ip": "localhost",
        "port": 2000,
        "traffic_manager_port": 8042,
        "max_episode_steps": 1000,
        "frame_skip": 2,
        "render_display": 0,
        "display_text": 0,
        "record_display_images": 0,
        "record_rl_images": 0,
        "rl_image_size": 84,
        "fov": 60,
        "cameras": ["foresight0"],
        "scenario": "train",
        "map": "Town04",
        "vehicle_spawn_point_id": "random",
        "weather": "Default",
        "changing_weather_speed": 0,
        "vehicle": "vehicle.lincoln.mkz_2017",
        "num_other_cars": 40,
        "num_other_cars_nearby": 8,
    }

    action_repeat=2 # Feel free to change this

    env = carla_make_eval(config, action_repeat=action_repeat)
    ```
