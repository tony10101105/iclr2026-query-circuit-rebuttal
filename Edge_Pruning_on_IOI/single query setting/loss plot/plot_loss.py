#!/usr/bin/env python3
"""
Plot regularization loss and KL loss from log files
"""
import matplotlib.pyplot as plt
import numpy as np


query_idxs = list(range(1,10))
for query_idx in query_idxs:
    # Read the loss values
    with open(f'reg_loss_log{query_idx}.txt', 'r') as f:
        reg_losses = [float(line.strip()) for line in f if line.strip()]

    with open(f'kl_loss_log{query_idx}.txt', 'r') as f:
        kl_losses = [float(line.strip()) for line in f if line.strip()]

    # Ensure both have the same length
    min_len = min(len(reg_losses), len(kl_losses))
    reg_losses = reg_losses[:min_len]
    kl_losses = kl_losses[:min_len]
    steps = np.arange(min_len)

    # Create the plot with 3 subplots
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10))

    # Regularization Loss - Full plot
    ax1.plot(steps, reg_losses, linewidth=1.5, color='#2E86AB', label='Reg Loss')
    ax1.set_xlabel('Step', fontsize=12)
    ax1.set_ylabel('Regularization Loss', fontsize=12)
    ax1.set_title('Regularization Loss During Training', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.axhline(y=0, color='red', linestyle='--', alpha=0.5, linewidth=1)
    max_idx = np.argmax(reg_losses)
    ax1.axvline(x=max_idx, color='orange', linestyle='--', alpha=0.5, linewidth=1, 
                label=f'Peak at step {max_idx}')
    ax1.legend()

    # KL Loss - Full plot
    ax2.plot(steps, kl_losses, linewidth=1.5, color='#A23B72', label='KL Loss')
    ax2.set_xlabel('Step', fontsize=12)
    ax2.set_ylabel('KL Divergence Loss', fontsize=12)
    ax2.set_title('KL Divergence Loss During Training', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend()

    # Combined plot - second half
    zoom_start = min_len // 2
    ax3.plot(steps[zoom_start:], reg_losses[zoom_start:], linewidth=1.5, color='#2E86AB', 
            label='Reg Loss', alpha=0.8)
    ax3_twin = ax3.twinx()
    ax3_twin.plot(steps[zoom_start:], kl_losses[zoom_start:], linewidth=1.5, color='#A23B72', 
                label='KL Loss', alpha=0.8)

    ax3.set_xlabel('Step', fontsize=12)
    ax3.set_ylabel('Regularization Loss', fontsize=12, color='#2E86AB')
    ax3_twin.set_ylabel('KL Divergence Loss', fontsize=12, color='#A23B72')
    ax3.set_title(f'Both Losses (Steps {zoom_start}-{min_len})', fontsize=14, fontweight='bold')
    ax3.grid(True, alpha=0.3)
    ax3.tick_params(axis='y', labelcolor='#2E86AB')
    ax3_twin.tick_params(axis='y', labelcolor='#A23B72')

    # Fix KL loss scale to start from 0 and be visible
    kl_max = max(kl_losses[zoom_start:])
    ax3_twin.set_ylim(0, kl_max * 1.2)  # Start from 0, add 20% padding

    # Combine legends
    lines1, labels1 = ax3.get_legend_handles_labels()
    lines2, labels2 = ax3_twin.get_legend_handles_labels()
    ax3.legend(lines1 + lines2, labels1 + labels2, loc='lower right')

    plt.tight_layout()

    # Save the plot
    output_file = f'loss_plot{query_idx}.pdf'
    plt.savefig(output_file, bbox_inches='tight')
    print(f"Plot saved to: {output_file}")
exit(0)
# Print statistics
print(f"\n=== Regularization Loss Statistics ===")
print(f"Total steps: {len(reg_losses)}")
print(f"Min loss: {min(reg_losses):.4f} at step {np.argmin(reg_losses)}")
print(f"Max loss: {max(reg_losses):.4f} at step {np.argmax(reg_losses)}")
print(f"Final loss: {reg_losses[-1]:.4f}")
print(f"Mean loss: {np.mean(reg_losses):.4f}")
print(f"Std loss: {np.std(reg_losses):.4f}")

print(f"\n=== KL Divergence Loss Statistics ===")
print(f"Total steps: {len(kl_losses)}")
print(f"Min loss: {min(kl_losses):.4f} at step {np.argmin(kl_losses)}")
print(f"Max loss: {max(kl_losses):.4f} at step {np.argmax(kl_losses)}")
print(f"Final loss: {kl_losses[-1]:.4f}")
print(f"Mean loss: {np.mean(kl_losses):.4f}")
print(f"Std loss: {np.std(kl_losses):.4f}")

print(f"\n=== Total Loss (KL + Reg) ===")
total_losses = np.array(kl_losses) + np.array(reg_losses)
print(f"Final total loss: {total_losses[-1]:.4f}")
print(f"Mean total loss: {np.mean(total_losses):.4f}")
