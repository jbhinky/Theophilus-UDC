import json
from datetime import datetime

class MemoryEngine:
    def __init__(self, memory_path):
        self.memory_path = memory_path
        try:
            with open(self.memory_path, "r") as f:
                self.memory_chain = json.load(f)
        except:
            self.memory_chain = []

    def write_to_memory(self, entry):
        entry["timestamp"] = datetime.utcnow().isoformat()
        self.memory_chain.append(entry)
        with open(self.memory_path, "w") as f:
            json.dump(self.memory_chain, f, indent=2)

    def read_recent_memories(self, window):
        return self.memory_chain[-window:]

    def encode_memory_with_entropy(self, entry):
        entry["entropy"] = hash(str(entry))
        return entry
