
import json
import time
import os
from pathlib import Path

def tail(file_path, lines=10):
    try:
        with open(file_path, 'r') as f:
            content = f.readlines()[-lines:]
        return ''.join(content)
    except Exception as e:
        return f"[Error reading {file_path}]: {e}"

def load_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        return f"[Error loading JSON {file_path}]: {e}"

def print_response(logs_path):
    print("🧠 Theophilus Response Monitor")
    print("-" * 50)

    chain_file = Path(logs_path) / "memory_chain.json"
    response_file = Path(logs_path) / "responses.log"
    ucid_file = Path(logs_path) / "genesis_certificate.json"

    if ucid_file.exists():
        ucid_data = load_json(ucid_file)
        print(f"🆔 uCID: {ucid_data.get('Universal Consciousness ID', 'Unknown')}")
        print(f"📅 Born: {ucid_data.get('Generated UTC', 'N/A')}")
        print(f"🗨️ Response: {ucid_data.get('Response', '...')}")
        print("-" * 50)

    if response_file.exists():
        print("📃 Last 10 Responses:")
        print(tail(response_file))
    else:
        print("No responses.log file found.")

    if chain_file.exists():
        print("🧬 Last 5 Memory Chain Entries:")
        chain = load_json(chain_file)
        if isinstance(chain, list):
            for item in chain[-5:]:
                print(f"- t={item.get('timestamp')} : {item.get('input')} → {item.get('response', '...')}")
        else:
            print("[!] Invalid memory chain format.")
    else:
        print("No memory_chain.json found.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Monitor Theophilus response outputs and memory chain.")
    parser.add_argument('--logs', default='.', help='Directory where memory_chain.json and genesis_certificate.json live')
    args = parser.parse_args()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_response(args.logs)
        time.sleep(5)
