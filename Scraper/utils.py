import os
import json
sPathToConfig = 'config.json'




def readConfig(platform):
    if not  os.path.exists(sPathToConfig):
        print(f'Path: {sPathToConfig} does not exist')
        raise ValueError('Path config does not exist')
    with open(sPathToConfig) as f:
        config = json.load(f)

    if platform not in config:
        raise ValueError(f"Platform {platform} does not have config...")

    return config[platform]

