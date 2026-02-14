import os
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips


def build_video(output_folder="output", final_name="final_video.mp4"):

    scene_files = sorted(
        [f for f in os.listdir(output_folder) if f.startswith("scene_") and f.endswith(".mp3")]
    )

    clips = []

    for audio_file in scene_files:
        scene_number = audio_file.split("_")[1].split(".")[0]

        image_path = os.path.join(output_folder, f"scene_{scene_number}.jpg")
        audio_path = os.path.join(output_folder, audio_file)

        audio_clip = AudioFileClip(audio_path)
        image_clip = ImageClip(image_path).set_duration(audio_clip.duration)

        image_clip = image_clip.set_audio(audio_clip)

        clips.append(image_clip)

    final_video = concatenate_videoclips(clips, method="compose")

    final_path = os.path.join(output_folder, final_name)
    final_video.write_videofile(final_path, fps=24)

    print("Final video created:", final_path)
