import sys
import os

# Add modules folder to path FIRST
sys.path.append(os.path.join(os.path.dirname(__file__), "modules"))

from script_generator import generate_script
from scene_splitter import split_scenes
from voice_generator import generate_voice_sync
from visual_fetcher import fetch_image
from video_builder import build_video


def main():
    if len(sys.argv) < 2:
        print('Usage: python main.py "Your Topic"')
        return

    topic = sys.argv[1]
    print(f"\nGenerating script for: {topic}\n")

    # Step 1: Generate Script
    script = generate_script(topic)

    with open("output/script.txt", "w", encoding="utf-8") as f:
        f.write(script)

    # Step 2: Split into Scenes
    scenes = split_scenes(script)

    print(f"{len(scenes)} scenes created.\n")

    # Step 3: Generate Voice
    for i, scene in enumerate(scenes):
        audio_path = f"output/scene_{i+1}.mp3"
        print(f"Generating voice for Scene {i+1}...")
        generate_voice_sync(scene, audio_path)

    print("Voice files generated.\n")

    # Step 4: Fetch Different Images Per Scene
    for i, scene in enumerate(scenes):
        print(f"Fetching image for Scene {i+1}...")
        image_path = f"output/scene_{i+1}.jpg"

        if i == 0:
            search_query = "recruiter reviewing resumes office hiring process"
        elif i == 1:
            search_query = "AI resume screening recruitment analytics dashboard"
        elif i == 2:
            search_query = "video interview AI facial recognition recruitment software"
        else:
            search_query = topic + " AI hiring technology"

        fetch_image(search_query, image_path)

    print("Images fetched.\n")

    # Step 5: Build Final Video
    print("Building final video...")
    build_video()

    print("\n🚀 Pipeline complete! Video ready in output folder.\n")


if __name__ == "__main__":
    main()
