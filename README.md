# AI Video Generation Pipeline
I built a fully automated AI Video Generation Pipeline that converts a single topic input into a YouTube-ready video. The system follows a modular architecture where each stage is independently handled through Python modules.
The pipeline works as follows:
Gemini 2.5 Flash API generates a structured multi-scene script.
The script is automatically split into scenes.
Edge-TTS converts each scene into synchronized voiceover audio.
Pexels API dynamically fetches relevant royalty-free visuals per scene.
MoviePy combines images and audio to generate a final .mp4 video.
The biggest challenge was handling API compatibility issues and model deprecations while ensuring end-to-end automation without manual intervention. I solved this by listing available models via API and dynamically integrating a supported model.
If I improve this further, I would add dynamic subtitle generation, auto-thumbnail creation, YouTube upload automation, and scene-wise adaptive visual matching using keyword extraction instead of first-sentence mapping.
This project demonstrates my ability to design modular architectures, integrate multiple APIs, handle real-world debugging challenges, and build scalable AI workflows end-to-end.
