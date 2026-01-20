#!/usr/bin/env python3
# Configuration
import sys
from pathlib import Path
EXAMPLE_DIR_ROOT = Path(__file__).resolve().parent.parent.parent
IMAGE_DIR = EXAMPLE_DIR_ROOT / "images"
sys.path.append(str(EXAMPLE_DIR_ROOT / "service"))
STATE_FILE = Path.home() / ".eink_display_state.json"

import json
import random
from datetime import date
from inkyController import draw_image

assetList = sorted([
    str(img) for img in IMAGE_DIR.glob("*")
    if img.suffix.lower() in ['.png', '.jpg', '.jpeg', '.bmp']
])

def load_state():
    """Load the current state from file."""
    if STATE_FILE.exists():
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    return None

def save_state(state):
    """Save the current state to file."""
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f)

def get_next_image():
    """Get the next random non-repeating image for today."""
    today = str(date.today())
    state = load_state()
    
    # Check if we need to start a new day
    if state is None or state.get('date') != today:
        # New day - create a shuffled list of all indices
        indices = list(range(len(assetList)))
        random.shuffle(indices)
        state = {
            'date': today,
            'remaining_indices': indices,
            'current_index': 0
        }
    
    # Get the next index
    current_idx = state['current_index']
    remaining = state['remaining_indices']
    
    # If we've used all images today, wrap around
    if current_idx >= len(remaining):
        current_idx = 0
    
    image_index = remaining[current_idx]
    
    # Update state for next run
    state['current_index'] = current_idx + 1
    save_state(state)
    
    return assetList[image_index]

def doSomething(image_path):
    """Display the image on your e-ink display."""
    print(f"Displaying: {image_path}")
    # Your e-ink display code goes here
    draw_image(image_path)

if __name__ == "__main__":
    image_path = get_next_image()
    doSomething(image_path)
