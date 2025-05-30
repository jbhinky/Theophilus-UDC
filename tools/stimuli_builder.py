
import json
import time
import argparse
from datetime import datetime

def build_stimuli(inputs):
    timestamped = []
    base_time = int(time.time())
    for i, item in enumerate(inputs):
        entry = {
            "timestamp": base_time + i * 2,  # 2-second intervals for delay simulation
            "input": item.strip()
        }
        timestamped.append(entry)
    return timestamped

def main():
    parser = argparse.ArgumentParser(description="Create timestamped stimuli for Theophilus.")
    parser.add_argument('--inputs', nargs='+', required=True, help='List of stimuli (e.g. "What are you?" "Sound cue")')
    parser.add_argument('--output', default='stimuli_built.json', help='Output JSON file name')

    args = parser.parse_args()
    stimuli = build_stimuli(args.inputs)

    with open(args.output, 'w') as f:
        json.dump(stimuli, f, indent=4)

    print(f"[✓] Created {args.output} with {len(stimuli)} entries.")

if __name__ == '__main__':
    main()
