import cv2
import json
import os


# Load and Extract Frames

def main(video_path, output_dir):
    # Open the video file for reading
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    frame_number = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break  # Reached the end of the video

        # Get the timestamp of the frame (in milliseconds)
        timestamp_ms = int(cap.get(cv2.CAP_PROP_POS_MSEC))

        # Convert the frame to a list of pixel values
        frame_data = frame.tolist()

        # Create a dictionary to store frame information
        frame_info = {
            "frame_number": frame_number,
            "timestamp_ms": timestamp_ms,
            "frame_data": frame_data
        }

        # Save the frame data as a JSON file
        frame_json_path = os.path.join(output_dir, f"frame_{frame_number}.json")
        with open(frame_json_path, "w") as json_file:
            json.dump(frame_info, json_file, indent=4)

        frame_number += 1

    # Release the video capture object and close the video file
    cap.release()
    cv2.destroyAllWindows()

    print(f"Frames saved as JSON files in {output_dir}")


if __name__ == "__main__":
    video_path = "your_video.mp4"  # Replace with your video file path
    output_dir = "frames_json"  # Directory to save JSON files
    main(video_path, output_dir)
