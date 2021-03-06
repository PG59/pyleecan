# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from numpy import where, argmin, abs, squeeze, split
from itertools import repeat
from ...Functions.init_fig import init_subplot, init_fig
from ...definitions import config_dict

FONT_NAME = config_dict["PLOT"]["FONT_NAME"]


def plot_A_2D(
    Xdata,
    Ydatas,
    legend_list=[""],
    color_list=[(0, 0, 1, 0.5)],
    linestyle_list=["-"],
    linewidth_list=[3],
    title="",
    xlabel="",
    ylabel="",
    fig=None,
    subplot_index=None,
    is_logscale_x=False,
    is_logscale_y=False,
    is_disp_title=True,
    is_grid=True,
    type="curve",
    is_fund=False,
    fund_harm=None,
    y_min=None,
    y_max=None,
    xticks=None,
    save_path=None,
):
    """Plots a 2D graph (curve, bargraph or barchart) comparing fields in Ydatas

    Parameters
    ----------
    Xdata : ndarray
        array of x-axis values
    Ydatas : list
        list of y-axes values
    legend_list : list
        list of legends
    color_list : list
        list of colors to use for each curve
    linewidth_list : list
        list of line width to use for each curve
    title : str
        title of the graph
    xlabel : str
        label for the x-axis
    ylabel : str
        label for the y-axis
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    subplot_index : int
        index of subplot in which to plot
    is_logscale_x : bool
        boolean indicating if the x-axis must be set in logarithmic scale
    is_logscale_y : bool
        boolean indicating if the y-axis must be set in logarithmic scale
    is_disp_title : bool
        boolean indicating if the title must be displayed
    is_grid : bool
        boolean indicating if the grid must be displayed
    type : str
        type of 2D graph : "curve", "bargraph", "barchart" or "quiver"
    is_fund : bool
        boolean indicating if the bar corresponding to the fundamental must be displayed in red
    fund_harm : float
        frequency of the fundamental harmonic
    y_min : float
        minimum value for the y-axis
    y_max : float
        maximum value for the y-axis
    xticks : list
        list of ticks to use for the x-axis
    """

    # Set figure/subplot
    is_show_fig = True if fig is None else False
    if fig is None:
        (fig, axes, patch_leg, label_leg) = init_fig(None, shape="rectangle")

    fig, ax = init_subplot(fig=fig, subplot_index=subplot_index)

    # Number of curves on a axe
    ndatas = len(Ydatas)

    # Expend default argument
    if 1 == len(color_list) < ndatas:
        # Set the same color for all curves
        color_list = list(repeat(color_list[0], ndatas))
    if 1 == len(linewidth_list) < ndatas:
        # Set the same color for all curves
        linewidth_list = list(repeat(linewidth_list[0], ndatas))
    if 1 == len(linestyle_list) < ndatas:
        # Set the same linestyles for all curves
        linestyle_list = list(repeat(linestyle_list[0], ndatas))
    if 1 == len(legend_list) < ndatas:
        # Set no legend for all curves
        legend_list = list(repeat("", ndatas))
        no_legend = True
    else:
        no_legend = False

    # Plot
    if type == "curve":
        for i in range(ndatas):
            ax.plot(
                Xdata,
                Ydatas[i],
                color=color_list[i],
                label=legend_list[i],
                linewidth=linewidth_list[i],
                ls=linestyle_list[i],
            )
        if xticks is not None:
            ax.xaxis.set_ticks(xticks)
    elif type == "bargraph":
        positions = range(-ndatas + 1, ndatas, 2)
        for i in range(ndatas):
            width = (Xdata[1] - Xdata[0]) / ndatas
            barlist = ax.bar(
                Xdata + positions[i] * width / (2 * ndatas),
                Ydatas[i],
                color=color_list[i],
                width=width,
                label=legend_list[i],
            )
            if is_fund:  # Find fundamental
                if fund_harm is None:
                    mag_max = max(Ydatas[i])
                    imax = int(where(Ydatas[i] == mag_max)[0])
                else:
                    imax = argmin(abs(Xdata - fund_harm))
                barlist[imax].set_edgecolor("k")
        if xticks is not None:
            ax.xaxis.set_ticks(xticks)
    elif type == "barchart":
        for i in range(ndatas):
            if i == 0:
                ax.bar(
                    range(len(Xdata)),
                    Ydatas[i],
                    color=color_list[i],
                    width=0.5,
                    label=legend_list[i],
                )
            else:
                ax.bar(
                    range(len(Xdata)),
                    Ydatas[i],
                    edgecolor=color_list[i],
                    width=0.5,
                    fc="None",
                    lw=1,
                    label=legend_list[i],
                )
        plt.xticks(range(len(Xdata)), [str(f) for f in Xdata], rotation=90)
    elif type == "quiver":
        for i in range(ndatas):
            x = [e[0] for e in Xdata]
            y = [e[1] for e in Xdata]
            vect_list = split(Ydatas[i], 2)
            ax.quiver(x, y, squeeze(vect_list[0]), squeeze(vect_list[1]))
            ax.axis("equal")

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_ylim([y_min, y_max])

    if is_logscale_x:
        ax.xscale("log")

    if is_logscale_y:
        ax.yscale("log")

    if is_disp_title:
        ax.set_title(title)

    if is_grid:
        ax.grid()

    if ndatas > 1 and not no_legend:
        ax.legend(prop={"family": FONT_NAME, "size": 22})

    plt.tight_layout()
    for item in (
        [ax.xaxis.label, ax.yaxis.label] + ax.get_xticklabels() + ax.get_yticklabels()
    ):
        item.set_fontname(FONT_NAME)
        item.set_fontsize(22)
    ax.title.set_fontname(FONT_NAME)
    ax.title.set_fontsize(24)

    if save_path is not None:
        fig.savefig(save_path)
        plt.close()

    if is_show_fig:
        fig.show()

    return ax
