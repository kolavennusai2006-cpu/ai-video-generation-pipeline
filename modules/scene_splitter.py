import re

def split_scenes(script_text):
    scenes = re.split(r"### Scene \d+:", script_text)
    scenes = [scene.strip() for scene in scenes if scene.strip()]
    return scenes
