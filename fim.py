import hashlib
import json
import os


TARGET_FILE ="target.txt"
BASELINE_FILE = "baseline.json"

def calculate_file_hash(filepath):
    """Calculate and return the SHA-256 hash of a given file. """
    if not os.path.exists(filepath):
        print(f"[ERROR] Target file '{filepath}' does not exist.")
        return None

    hasher = hashlib.sha256()
    with open (filepath, 'rb') as file:
        content = file.read()
        hasher.update(content)
    return hasher.hexdigest()

def create_baseline():
    """Create baseline.json and returns status object."""
    current_hash = calculate_file_hash(TARGET_FILE)
    if current_hash is None:
        return {"status" : "error", "message": f"Target file '{TARGET_FILE}' not found."}
    
    baseline_data = {
        "file": TARGET_FILE,
        "hash": current_hash

    }
    
    with open(BASELINE_FILE, 'w') as file:
        json.dump(basline_data, file, indent=4)
        
        return{
            "status" : "success",
            "message": "Baseline created successfully.",
            "hash" : current_hash,
            "file" : TARGET_FILE

        }

    def check_integirity():
        """Compare the current hash with the baseline hash and return status object."""
        if not os.path.exists(BASELINE_FILE):
            return{"status" : "error", "message" : "no baseline"}
    