import matplotlib.pyplot as plt
import pandas as pd

print("Reading data from CSV and generating visualization...")

csv_filename = "illusion_results.csv"

try:
    # Load the CSV data
    df = pd.read_csv(csv_filename)
    
    # We don't need 'Other' if it's 0, but we'll include it just in case it exists in your data
    df.set_index("Model", inplace=True)
    
    # Plotting
    colors = ["#2ecc71", "#e74c3c", "#f1c40f", "#95a5a6"]
    
    # Create the stacked bar chart
    ax = df.plot(kind="bar", stacked=True, color=colors[:len(df.columns)], figsize=(12, 6), edgecolor='black')

    plt.title("AI Susceptibility to Multi-Type Optical Illusions", fontsize=16, pad=15)
    plt.ylabel("Number of Responses (out of 30)", fontsize=12)
    plt.xlabel("Model Architecture", fontsize=12)
    plt.xticks(rotation=15, ha='right')
    
    plt.legend(title="AI Perception Response", bbox_to_anchor=(1.05, 1), loc='upper left')

    # Reference line for total test cases (30 now, instead of 20)
    plt.axhline(30, color='black', linestyle='--', linewidth=1)

    plt.tight_layout()
    output_filename = "illusion_results_expanded.png"
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')

    print(f"Success! Graph saved as {output_filename}")

except FileNotFoundError:
    print(f"Error: Could not find '{csv_filename}'. Ensure you run the test script first.")