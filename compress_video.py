import subprocess
import sys

def compress_video(input_path: str, output_path: str, crf: int = 23, preset: str = "slow"):
    """
    Compresses a video without noticeable quality loss using FFmpeg.
    
    :param input_path: Path to the input video file.
    :param output_path: Path to save the compressed output file.
    :param crf: Constant Rate Factor (default is 23, lower values mean higher quality).
    :param preset: Compression speed setting (ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow).
    """
    try:
        command = [
            "ffmpeg", "-i", input_path, "-vcodec", "libx264", "-crf", str(crf), "-preset", preset, "-y", output_path
        ]
        subprocess.run(command, check=True)
        print(f"✅ Compression successful! Output file: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during compression: {e}")

if __name__ == "__main__":
    # Check if enough arguments are provided
    if len(sys.argv) < 3:
        print("❌ Usage: python compress_video.py input.mp4 output.mp4 [crf] [preset]")
    else:
        # Parse command-line arguments
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        crf_value = int(sys.argv[3]) if len(sys.argv) > 3 else 23
        preset_value = sys.argv[4] if len(sys.argv) > 4 else "slow"

        # Call the compression function
        compress_video(input_file, output_file, crf_value, preset_value)
