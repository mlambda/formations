fig = plt.figure()

# ... #
fig.savefig(
    "mon_plot",
    # --Optional--
    # Image resolution,
    # fig value is ignored if specified
    dpi=150,
    # png,pdf,jpg...
    # can be provided with the filepath
    format="png",
    # Plot background is transparent,
    # fig value is ignored if specified
    transparent=True,
)
