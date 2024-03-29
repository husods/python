import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,3,4])
y = np.array([4,3,2,1])
# =============================================================================
# plt.figure()
# plt.plot(x, y, color="red",alpha = 0.7, label = "line")
# plt.scatter(x,y,color = "blue",alpha= 0.4, label = "scatter")
# plt.title("Matplotlib")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.grid(1)
# plt.xticks([0,1,2,3,4,5])
# plt.legend()
# plt.show()
# =============================================================================

# =============================================================================
# fig, axes = plt.subplots(2,1, figsize=(9,7))
# fig.subplots_adjust(hspace = 0.5)

# x = [1,2,3,4,5,6,7,8,9,10]
# y = [10,9,8,7,6,5,4,3,2,1]


# axes[0].scatter(x,y)
# axes[0].set_title("sub-1")
# axes[0].set_ylabel("sub-1 y")
# axes[0].set_xlabel("sub-1 x")

# axes[1].scatter(y,x)
# axes[1].set_title("sub-2")
# axes[1].set_ylabel("sub-2 y")
# axes[1].set_xlabel("sub-2 x")
# =============================================================================
# fig, axs = plt.subplots(1, 2)
# fig.suptitle('Vertically stacked subplots')
# axs[0].plot(x, y)
# axs[1].plot(x, -y)
# =============================================================================
# fig, axs = plt.subplots(2, 2)
# fig.subplots_adjust(hspace = 0.5)
# axs[0, 0].plot(x, y)
# axs[0, 0].set_title('Axis [0, 0]')
# axs[0, 1].plot(x, y, 'tab:orange')
# axs[0, 1].set_title('Axis [0, 1]')
# axs[1, 0].plot(x, -y, 'tab:green')
# axs[1, 0].set_title('Axis [1, 0]')
# axs[1, 1].plot(x, -y, 'tab:red')
# axs[1, 1].set_title('Axis [1, 1]')

# for ax in axs.flat:
#     ax.set(xlabel='x-label', ylabel='y-label')

# # Hide x labels and tick labels for top plots and y ticks for right plots.
# for ax in axs.flat:
#     ax.label_outer()
# =============================================================================
# tuple-unpacking
# fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
# fig.suptitle('Sharing x per column, y per row')
# ax1.plot(x, y)
# ax2.plot(x, y**2, 'tab:orange')
# ax3.plot(x, -y, 'tab:green')
# ax4.plot(x, -y**2, 'tab:red')
# 
# for ax in fig.get_axes():
#     ax.label_outer()
# =============================================================================
# fig = plt.figure()
# gs = fig.add_gridspec(3, hspace=0)
# axs = gs.subplots(sharex=True, sharey=True)
# fig.suptitle('Sharing both axes')
# axs[0].plot(x, y ** 2)
# axs[1].plot(x, 0.3 * y, 'o')
# axs[2].plot(x, y, '+')

# # Hide x labels and tick labels for all but bottom plot.
# for ax in axs:
#     ax.label_outer()
# =============================================================================
# fig = plt.figure()
# gs = fig.add_gridspec(2, 2, hspace=0, wspace=0)
# (ax1, ax2), (ax3, ax4) = gs.subplots(sharex='col', sharey='row')
# fig.suptitle('Sharing x per column, y per row')
# ax1.plot(x, y)
# ax2.plot(x, y**2, 'tab:orange')
# ax3.plot(x + 1, -y, 'tab:green')
# ax4.plot(x + 2, -y**2, 'tab:red')
# 
# for ax in fig.get_axes():
#     ax.label_outer()
# =============================================================================
# fig, axs = plt.subplots(2, 2)
# axs[0, 0].plot(x, y)
# axs[0, 0].set_title("main")
# axs[1, 0].plot(x, y**2)
# axs[1, 0].set_title("shares x with main")
# axs[1, 0].sharex(axs[0, 0])
# axs[0, 1].plot(x + 1, y + 1)
# axs[0, 1].set_title("unrelated")
# axs[1, 1].plot(x + 2, y + 2)
# axs[1, 1].set_title("also unrelated")
# axs[0, 1].sharey(axs[1, 1])
# fig.tight_layout()
fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw=dict(projection='polar'))
ax1.plot(x, y)
ax2.plot(x, y ** 2)

plt.show()

