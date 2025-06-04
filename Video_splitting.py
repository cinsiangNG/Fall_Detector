import subprocess
import math
import os


def get_video_duration(input_path):
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            input_path,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return float(result.stdout)


def split_video(input_path, output_prefix="output", segment_length=2):
    total_duration = get_video_duration(input_path)
    num_segments = math.ceil(total_duration / segment_length)
    for i in range(num_segments):
        start_time = i * segment_length
        output_filename = f"{output_prefix}_{i+1}.mp4"
        command = [
            "ffmpeg",
            "-ss",
            str(start_time),
            "-i",
            input_path,
            "-t",
            str(segment_length),
            "-c",
            "copy",
            output_filename,
        ]
        print(f"Exporting segment {i+1}: {output_filename}")
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("✅ All segments have been successfully exported!")


if __name__ == "__main__":
    video_folder = "input_folder"
    output_dir = "output_videos"
    os.makedirs(output_dir, exist_ok=True)

    for video in os.listdir(video_folder):
        if not video.lower().endswith(".mp4"):
            continue
        input_path = os.path.join(video_folder, video)
        base_name = os.path.splitext(video)[0]
        output_prefix = os.path.join(output_dir, base_name + "_segment")
        split_video(input_path, output_prefix=output_prefix)
