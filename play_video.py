import cv2
import os
from pathlib import Path

def play_video(video_path):
    """
    Load and play a video file using OpenCV.
    
    Args:
        video_path: Path to the video file
    """
    # Check if video file exists
    if not os.path.exists(video_path):
        print(f"Error: Video file not found at {video_path}")
        return
    
    # Open video file
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return
    
    # Get video properties
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    print(f"Video Info:")
    print(f"  Resolution: {width}x{height}")
    print(f"  FPS: {fps}")
    print(f"  Total frames: {frame_count}")
    print(f"\nPlaying video... (Press 'q' to quit)")
    
    # Play video
    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("End of video or failed to read frame")
            break
        
        # Display the frame
        cv2.imshow('Video Player', frame)
        
        # Wait for 'q' key to quit
        if cv2.waitKey(int(1000/fps)) & 0xFF == ord('q'):
            break
    
    # Release resources
    cap.release()
    cv2.destroyAllWindows()
    print("Video playback finished.")

if __name__ == "__main__":
    # Get the video file from data directory
    script_dir = Path(__file__).parent
    video_file = script_dir / "data" / "test_pendular_1.mp4"
    
    play_video(str(video_file))

