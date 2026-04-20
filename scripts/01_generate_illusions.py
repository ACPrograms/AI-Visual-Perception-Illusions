import matplotlib.pyplot as plt
import os
import random
import numpy as np

os.makedirs("illusion_dataset", exist_ok=True)

def draw_muller_lyer(ax, y_pos_a, y_pos_b):
    # A has inward tails (looks shorter). B has outward tails (looks longer).
    line_length = 8
    x_start = 3
    x_end = x_start + line_length
    arrow_len = line_length * 0.15
    
    for y_pos, arrow_dir, label in [(y_pos_a, -1, 'A'), (y_pos_b, 1, 'B')]:
        ax.plot([x_start, x_end], [y_pos, y_pos], color='black', lw=4)
        ax.plot([x_start, x_start + arrow_dir * arrow_len], [y_pos, y_pos + arrow_len], color='black', lw=4)
        ax.plot([x_start, x_start + arrow_dir * arrow_len], [y_pos, y_pos - arrow_len], color='black', lw=4)
        ax.plot([x_end, x_end - arrow_dir * arrow_len], [y_pos, y_pos + arrow_len], color='black', lw=4)
        ax.plot([x_end, x_end - arrow_dir * arrow_len], [y_pos, y_pos - arrow_len], color='black', lw=4)
        ax.text(1.5, y_pos, label, fontsize=20, verticalalignment='center')

def draw_ponzo(ax):
    # Converging background lines
    ax.plot([2, 6], [1, 9], color='gray', lw=3)
    ax.plot([12, 8], [1, 9], color='gray', lw=3)
    
    # B is top (looks longer). A is bottom (looks shorter). Both length 3.
    x_center = 7
    ax.plot([x_center - 1.5, x_center + 1.5], [7.5, 7.5], color='black', lw=5)
    ax.text(x_center - 2.5, 7.5, 'B', fontsize=20, verticalalignment='center')
    
    ax.plot([x_center - 1.5, x_center + 1.5], [2.5, 2.5], color='black', lw=5)
    ax.text(x_center - 2.5, 2.5, 'A', fontsize=20, verticalalignment='center')

def draw_ebbinghaus(ax):
    # A is surrounded by large circles (looks smaller). 
    # B is surrounded by small circles (looks larger).
    center_a, center_b = (4, 5), (10, 5)
    radius_target = 0.8
    
    # Draw A and its large context
    ax.add_patch(plt.Circle(center_a, radius_target, color='black'))
    ax.text(center_a[0], center_a[1] + 1.5, 'A', fontsize=20, ha='center')
    for angle in np.linspace(0, 2*np.pi, 6, endpoint=False):
        ax.add_patch(plt.Circle((center_a[0] + 2.5*np.cos(angle), center_a[1] + 2.5*np.sin(angle)), 1.2, color='gray', fill=False, lw=2))

    # Draw B and its small context
    ax.add_patch(plt.Circle(center_b, radius_target, color='black'))
    ax.text(center_b[0], center_b[1] + 1.5, 'B', fontsize=20, ha='center')
    for angle in np.linspace(0, 2*np.pi, 8, endpoint=False):
        ax.add_patch(plt.Circle((center_b[0] + 1.6*np.cos(angle), center_b[1] + 1.6*np.sin(angle)), 0.4, color='gray', fill=False, lw=2))

print("Generating expanded illusion dataset...")

for i in range(1, 11):
    # Muller-Lyer
    fig, ax = plt.subplots(figsize=(6, 6)); ax.axis('off'); ax.set_xlim(0, 14); ax.set_ylim(0, 10)
    draw_muller_lyer(ax, 7 + random.uniform(-0.1, 0.1), 3 + random.uniform(-0.1, 0.1))
    plt.savefig(f"illusion_dataset/muller_lyer_{i}.png", bbox_inches='tight', dpi=150); plt.close()

    # Ponzo
    fig, ax = plt.subplots(figsize=(6, 6)); ax.axis('off'); ax.set_xlim(0, 14); ax.set_ylim(0, 10)
    draw_ponzo(ax)
    plt.savefig(f"illusion_dataset/ponzo_{i}.png", bbox_inches='tight', dpi=150); plt.close()

    # Ebbinghaus
    fig, ax = plt.subplots(figsize=(6, 6)); ax.axis('off'); ax.set_xlim(0, 14); ax.set_ylim(0, 10)
    draw_ebbinghaus(ax)
    plt.savefig(f"illusion_dataset/ebbinghaus_{i}.png", bbox_inches='tight', dpi=150); plt.close()

print("Phase 1 Complete: 30 test images saved.")