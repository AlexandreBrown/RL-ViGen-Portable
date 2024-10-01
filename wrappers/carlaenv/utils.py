from wrappers.carlaenv.carla_env_10 import CarlaEnv10
from wrappers.carlaenv.carla_env_10_eval import CarlaEnv10_eval


def make_env_10(cfg_dict, action_repeat):
    cfg_dict['frame_skip'] = action_repeat
    env = CarlaEnv10(cfg_dict)
    return env


def make_env_10_eval(cfg_dict, action_repeat):
    cfg_dict['frame_skip'] = action_repeat
    if cfg_dict['scenario'] == 'tunnel':
        cfg_dict['num_other_cars'] = 5
        cfg_dict['num_other_cars_nearby'] = 2
    elif cfg_dict['scenario'] == 'narrow' or cfg_dict['scenario'] == 'roundabout':
        cfg_dict['num_other_cars'] = 5
        cfg_dict['num_other_cars_nearby'] = 0
    env = CarlaEnv10_eval(cfg_dict)
    return env
