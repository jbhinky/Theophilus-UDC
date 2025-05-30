
from core.theophilus_core import Theophilus
import json

def load_config():
    with open('core/config.json', 'r') as f:
        return json.load(f)

def load_stimuli():
    try:
        with open('run/stimuli_example.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return [{"timestamp": 0, "input": "initial boot"}]

def main():
    config = load_config()
    stimuli = load_stimuli()

    theo = Theophilus(config=config)
    theo.feed_stimuli(stimuli)
    theo.run()

if __name__ == "__main__":
    main()
