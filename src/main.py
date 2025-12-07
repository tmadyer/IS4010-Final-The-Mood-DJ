import argparse
from . import logic
import pandas as pd

def main():
    """
    Main function to run the CLI application.
    """
    parser = argparse.ArgumentParser(description="Analyzes your mood from a picture and suggests a playlist.")
    parser.add_argument("--image-path", required=True, help="Path to the image file for emotion analysis.")
    parser.add_argument("--dev-mode", action="store_true", help="Use mock data for development.")
    
    args = parser.parse_args()

    print("Analyzing your mood...")
    emotion = logic.analyze_emotion(args.image_path, dev_mode=args.dev_mode)
    
    if emotion:
        print(f"We think you're feeling: {emotion.capitalize()}")
        print("\nGenerating your playlist...")
        playlist_df = logic.get_playlist(emotion)
        
        print("Here are a few songs for you:\n")
        print(playlist_df.to_string(index=False))
    else:
        print("Could not determine the mood from the image.")

if __name__ == "__main__":
    main()