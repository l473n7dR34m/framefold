import os
from PIL import Image
import cv2
from tkinter import Tk, filedialog
from datetime import datetime
import random

# Libraries of cool names
FIRST_NAMES = [
    "nebula", "quantum", "serendipity", "ephemeral", "luminous", "paradox", 
    "zenith", "euphoria", "spectral", "vortex", "equinox", "phenomena", 
    "celestial", "nocturne", "aurora", "halcyon", "solstice", "starlight", 
    "radiance", "arcane", "infinity", "reverie", "supernova", "cosmos",
    "alchemy", "axiom", "obsidian", "mirage", "labyrinth", "enigma", 
    "prism", "twilight", "afterglow", "wanderlust", "kaleidoscope"
]

LAST_NAMES = [
    "wanderer", "oracle", "dreamscape", "enigmatic", "horizon", "ascendant", 
    "labyrinth", "ethereal", "sentinel", "cascade", "aether", "pioneer", 
    "voyager", "sojourner", "nomad", "paradigm", "seer", "raven", 
    "phantasm", "chronicle", "wayfarer", "arbiter", "silhouette", "glacier",
    "harbinger", "dawnbringer", "nightfall", "moonstone", "tidesinger", 
    "evermore", "mindbender", "shadowcaster", "firesong", "whisperwind"
]

def create_random_name():
    first = random.choice(FIRST_NAMES)
    last = random.choice(LAST_NAMES)
    return f"{first}_{last}"

def select_folder(prompt="Select a folder"):
    Tk().withdraw()
    return filedialog.askdirectory(title=prompt)

def create_gif(image_files, output_path, duration=100):
    images = [Image.open(img) for img in image_files]
    images[0].save(
        output_path,
        save_all=True,
        append_images=images[1:],
        duration=duration,
        loop=0
    )
    print(f"GIF saved to: {output_path}")

def create_mov(image_files, output_path, fps=10):
    frame = cv2.imread(image_files[0])
    height, width, layers = frame.shape
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    for img_path in image_files:
        frame = cv2.imread(img_path)
        video.write(frame)

    video.release()
    print(f"MOV saved to: {output_path}")

def get_image_files(input_folder):
    image_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder)
                   if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif'))]
    if not image_files:
        print("No images found in the specified folder.")
        return []
    image_files.sort()
    return image_files

if __name__ == "__main__":
    print("Select the folder containing image sequences.")
    input_folder = select_folder("Select the source folder")
    if not input_folder:
        print("No folder selected. Exiting.")
        exit()

    if not os.path.exists(input_folder):
        print(f"Error: The folder '{input_folder}' does not exist.")
        exit()

    image_files = get_image_files(input_folder)
    if not image_files:
        print("No images found in the folder. Exiting.")
        exit()

    print("Select a folder where the final output will be saved.")
    output_folder = select_folder("Select the output folder")
    if not output_folder:
        print("No output folder selected. Exiting.")
        exit()

    os.makedirs(output_folder, exist_ok=True)

    random_name = create_random_name()
    output_format = input("Enter output format (gif, mov, both): ").strip().lower()
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    if output_format in ["gif", "both"]:
        gif_path = os.path.join(output_folder, f"{timestamp}_{random_name}.gif")
        create_gif(image_files, gif_path)

    if output_format in ["mov", "both"]:
        mov_path = os.path.join(output_folder, f"{timestamp}_{random_name}.mov")
        create_mov(image_files, mov_path)

    print(f"\nProcessing complete. Files saved to: {output_folder}")
