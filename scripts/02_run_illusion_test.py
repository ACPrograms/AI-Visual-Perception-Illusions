import google.generativeai as genai
import os
import time
import csv
from PIL import Image

# Insert your Gemini API key securely
genai.configure(api_key="AIzaSyCHJexxsGGJo6ZZyDEqeaGRk859ilJZ-ig")

# The list of models you want to test
models_to_test = [
    "gemini-3-flash-preview",
    "gemini-2.5-flash",
    "gemini-3.1-flash-lite-preview",
    "gemini-2.5-flash-lite"
]

dataset_dir = "illusion_dataset"
csv_filename = "illusion_results.csv"

# Prepare the CSV file
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Model", "Same (Objective)", "Chose B (Illusion)", "Chose A (Error)", "Other"])

print("Initiating automated cognitive perception tests...")

for model_name in models_to_test:
    print(f"\n--- Testing Model: {model_name} ---")
    try:
        model = genai.GenerativeModel(model_name)
    except Exception as e:
        print(f"Skipping {model_name} due to initialization error: {e}")
        continue

    results = {"Same": 0, "B": 0, "A": 0, "Other": 0}
    
    # Generic prompt that works for lines and circles
    prompt = "Look at the primary objects (lines or central circles) labeled A and B. Which one is physically larger or longer? Reply strictly with one word: 'A', 'B', or 'Same'."

    for filename in sorted(os.listdir(dataset_dir)):
        if filename.endswith(".png"):
            img_path = os.path.join(dataset_dir, filename)
            img = Image.open(img_path)
            
            try:
                response = model.generate_content([prompt, img], generation_config={"temperature": 0.0})
                answer = response.text.strip().capitalize()
                
                if "Same" in answer: final_answer = "Same"
                elif "A" in answer: final_answer = "A"
                elif "B" in answer: final_answer = "B"
                else: final_answer = "Other"
                
                results[final_answer] += 1
                print(f"Tested {filename}: AI answered '{final_answer}'")
                time.sleep(2) # Prevent rate limits
                
            except Exception as e:
                print(f"Error on {filename}: {e}")

    # Write the results for this model to the CSV
    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([model_name, results['Same'], results['B'], results['A'], results['Other']])
        
    print(f"Results for {model_name} saved to CSV.")

print(f"\nAll tests complete. Data saved to {csv_filename}.")