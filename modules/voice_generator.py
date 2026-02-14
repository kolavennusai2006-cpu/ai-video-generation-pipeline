import asyncio
import edge_tts
import os

async def generate_voice(scene_text, output_path):
    communicate = edge_tts.Communicate(
        scene_text,
        voice="en-US-AriaNeural"   # Professional female voice
    )
    await communicate.save(output_path)

def generate_voice_sync(scene_text, output_path):
    asyncio.run(generate_voice(scene_text, output_path))
