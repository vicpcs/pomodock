import argparse
import sys
import time

from inkyController import draw_jjk_image, draw_demon_slayer_image, draw_mha_image

parser = argparse.ArgumentParser()
parser.add_argument("--duration", type=int, help="Duration of the timer in minutes")

SECONDS_IN_A_MINUTE = 60

def start_timer(duration_minutes):
    print(f"Starting timer for {duration_minutes} minutes")
    duration_seconds = duration_minutes * SECONDS_IN_A_MINUTE
    # Capture the timestamp the timer was started 
    start_time = time.time()
    displayed_minutes_left = duration_minutes
    # While the current time - start_time (AKA the time elapsed) is less than the duration,
    # print the time remaining in minutes and change the image on the display
    imageMethods = [draw_jjk_image, draw_demon_slayer_image, draw_mha_image]
    imageMethods.pop(0)()  # Show the first image immediately
    while (time.time() - start_time) < duration_seconds:
        # Change the image every minute
        whole_minutes_left = int(duration_minutes - ((time.time() - start_time) // 60))
        
        if whole_minutes_left < displayed_minutes_left:
            displayed_minutes_left = whole_minutes_left
            print(f"{displayed_minutes_left} minutes left")
            # Change the image on the display
            if imageMethods:
                image_method = imageMethods.pop(0)
                image_method()
            else:
                print("No more images to display. Skipping image change.")
            


        time.sleep(1)
    print("time is up!")

# Parse command line arguments, discard unknown args
args, _ = parser.parse_known_args()
duration = args.duration

if not args.duration:
    print(f"""Usage:
    {sys.argv[0]} --duration 3""")
    sys.exit(1)

# Start timer to track 3 minutes for dev
start_timer(duration)