import json
import matplotlib.pyplot as plt

# 32491 edges in total
# nominal_sparsity = [0.96, 0.98, 1.01, 1.05, 1.1, 1.2]

sparsity = [0.962, 0.968, 0.974, 0.978, 0.981, 0.985]


logit_diff = [3.378, 3.649, 2.982, 2.722, 2.697, 2.182] # y
nfs = [0.693, 0.918, 0.618, 0.487, 0.164, 0.300] # y
ndf = [0.517, 0.481, 0.471, 0.439, 0.417, 0.384] # y
fig, axs = plt.subplots(1, 3, figsize=(15, 4), sharex=True)

axs[0].plot(sparsity, logit_diff, marker='o', linestyle='-', color='tab:blue')
axs[0].set_title('Logit Difference vs Sparsity')
axs[0].set_xlabel('Sparsity')
axs[0].set_ylabel('Logit difference')
axs[0].set_xticks(sparsity)
axs[0].grid(True)
axs[0].set_ylim(-0.5, 4)

axs[1].plot(sparsity, nfs, marker='s', linestyle='-', color='tab:green')
axs[1].set_title('NFS vs Sparsity')
axs[1].set_xlabel('Sparsity')
axs[1].set_ylabel('NFS')
axs[1].set_xticks(sparsity)
axs[1].grid(True)
axs[1].set_ylim(0, 1)

axs[2].plot(sparsity, ndf, marker='^', linestyle='-', color='tab:red')
axs[2].set_title('NDF vs Sparsity')
axs[2].set_xlabel('Sparsity')
axs[2].set_ylabel('NDF')
axs[2].set_xticks(sparsity)
axs[2].grid(True)
axs[2].set_ylim(0, 1)

plt.tight_layout()
plt.savefig('our_replication_result.pdf')