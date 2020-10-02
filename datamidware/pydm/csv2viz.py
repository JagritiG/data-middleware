"""
Implementation of csv2viz() function:
Visualize csv data

param filename: csv file name
param kind: plot kind (bar, horizontal bar, stacked bar, group bar, scatter, line, hist,
                       kde, pie and more..)
param file_path: file path to save figure
param x: x data; list or array-like data
param y: y data; list or array-like data
param title: title of the figure
param label: x-label, y-label
param show: If True, show the current figure; default=True
"""
# =====================================================================================
from __future__ import print_function
from __future__ import absolute_import
import pandas as pd
from datamidware.pyviz import bar


def csv2viz(filename=None, kind=None, x=None, y=None,
            color=None, title=None, labels={}, set_col_color=None,
            update_title={}, update_xaxes={}, update_yaxes={}, xtickangle=None, ytickangle=None,
            xtickformat=None, ytickformat=None, update_legend={}, update_font={}, hover_name=None,
            hover_data=None, barmode="relative", bargap=0.15, bargroupgap=0.1, color_discrete_sequence=None,
            fig_width=1200, fig_height=800, color_continuous_scale=None, plot_bgcolor=None, paper_bgcolor=None,
            uniformtext_minsize=8, uniformtext_mode="hide", marker={}, selector={}, trace_name=None,
            update_trace_text=False, trace_text=None, texttemplate='%{text:.2s}', textangle=None,
            textposition="outside",textfont={}, bar_width=None, hoverinfo=None, hoverlabel=None, hovertemplate=None,
            hovertext=None, sort_asc=False, sort_desc=False, N_largest=None, N_smallest=None,
            file_path=None, file_type="png", show=True):
    """

    :param filename:
    :param kind:
    :param x:
    :param y:
    :param color:
    :param title:
    :param orientation:
    :param labels:
    :param update_title:
    :param update_xaxes:
    :param update_yaxes:
    :param xtickangle:
    :param ytickangle:
    :param xtickformat:
    :param ytickformat:
    :param update_legend:
    :param update_font:
    :param hover_name:
    :param hover_data:
    :param barmode:
    :param bargap:
    :param bargroupgap:
    :param color_discrete_sequence:
    :param fig_width:
    :param fig_height:
    :param color_continuous_scale:
    :param plot_bgcolor:
    :param paper_bgcolor:
    :param uniformtext_minsize:
    :param uniformtext_mode:
    :param marker:
    :param selector:
    :param trace_name:
    :param update_trace_text:
    :param trace_text:
    :param texttemplate:
    :param textangle:
    :param textposition:
    :param textfont:
    :param bar_width:
    :param hoverinfo:
    :param hoverlabel:
    :param hovertemplate:
    :param hovertext:
    :param sort_asc:
    :param sort_desc:
    :param N_largest:
    :param N_smallest:
    :param file_path:
    :param file_type:
    :param show:
    :return: Figure
    """

    try:
        plot = bar.BarChart()

        # Read csv file in pandas DataFrame
        df = pd.read_csv(filename, delimiter=',')
        df.columns = df.columns.str.replace(' ', '')

        # plot bar chart
        if kind == "bar":
            plot.bar(df=df, x=x, y=y, color=color, title=title, labels=labels,
                     set_col_color=set_col_color, update_title=update_title, update_xaxes=update_xaxes, update_yaxes=update_yaxes,
                     xtickangle=xtickangle, ytickangle=ytickangle, xtickformat=xtickformat, ytickformat=ytickformat,
                     update_legend=update_legend, update_font=update_font, hover_name=hover_name,
                     hover_data=hover_data, barmode=barmode, bargap=bargap, bargroupgap=bargroupgap,
                     color_discrete_sequence=color_discrete_sequence, fig_width=fig_width, fig_height=fig_height,
                     color_continuous_scale=color_continuous_scale, plot_bgcolor="rgba(0, 0, 0, 0)", paper_bgcolor="rgba(0, 0, 0, 0)",
                     uniformtext_minsize=uniformtext_minsize, uniformtext_mode=uniformtext_mode,
                     marker=marker, selector=selector, trace_name=trace_name, update_trace_text=update_trace_text,
                     trace_text=trace_text, texttemplate=texttemplate, textangle=textangle, textposition=textposition,
                     textfont=textfont, bar_width=bar_width, hoverinfo=hoverinfo, hoverlabel=hoverlabel, hovertemplate=hovertemplate,
                     hovertext=hovertext, sort_asc=sort_asc, sort_desc=sort_desc,
                     N_largest=N_largest, N_smallest=N_smallest, file_path=file_path, file_type=file_type, show=show)

        # plot horizontal bar chart
        if kind == "barh":
            plot.barh(df=df, x=x, y=y, color=color, title=title, orientation="h", labels=labels,
                      set_col_color=set_col_color, update_title=update_title, update_xaxes=update_xaxes, update_yaxes=update_yaxes,
                      xtickangle=xtickangle, ytickangle=ytickangle, xtickformat=xtickformat, ytickformat=ytickformat,
                      update_legend=update_legend, update_font=update_font, hover_name=hover_name,
                      hover_data=hover_data, barmode=barmode, bargap=bargap, bargroupgap=bargroupgap,
                      color_discrete_sequence=color_discrete_sequence, fig_width=fig_width, fig_height=fig_height,
                      color_continuous_scale=color_continuous_scale, plot_bgcolor="rgba(0, 0, 0, 0)", paper_bgcolor="rgba(0, 0, 0, 0)",
                      uniformtext_minsize=uniformtext_minsize, uniformtext_mode=uniformtext_mode,
                      marker=marker, selector=selector, trace_name=trace_name, update_trace_text=update_trace_text,
                      trace_text=trace_text, texttemplate=texttemplate, textangle=textangle, textposition=textposition,
                      textfont=textfont, bar_width=bar_width, hoverinfo=hoverinfo, hoverlabel=hoverlabel, hovertemplate=hovertemplate,
                      hovertext=hovertext, sort_asc=sort_asc, sort_desc=sort_desc,
                      N_largest=N_largest, N_smallest=N_smallest, file_path=file_path, file_type=file_type, show=show)

        if kind == "line":
            pass

        if kind == "scatter":
            pass

        if kind == "hist":
            pass

        if kind == "kde":
            pass

        if kind == "box":
            pass

        if kind == "pie":
            pass

    except Exception as e:
        print('Error: {}'.format(str(e)))

