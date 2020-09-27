# Bar plot (vertical, horizontal, group, stack), unsorted, sorted (ascending, descending), NLargest, NSmallest
# from pandas DataFrame, List-Array likes, NumPy Array (long-, wide-, mix- from data)
# ===================================================================================
import plotly.express as px
import pandas as pd
import numpy as np
import os


class BarChart:
    """
    Bar Chart class.
    """
    def __init__(self):
        self.df = None

    # Basic bar chart
    def bar(self, df=None, x=None, y=None, xcol_pos=None, ycol_pos=None, color=None, title=None, orientation=None, labels={}, update_title={}, update_xaxes={}, update_yaxes={},
            xtickangle=None, ytickangle=None, xtickformat=None, ytickformat=None, update_legend={}, update_font={}, hover_name=None,
            hover_data=None, barmode="relative", bargap=0.15, bargroupgap=0.1, color_discrete_sequence=None, fig_width=1200, fig_height=800,
            color_continuous_scale=None, plot_bgcolor=None, paper_bgcolor=None, uniformtext_minsize=8, uniformtext_mode="hide",
            marker={}, selector={}, trace_name=None, update_trace_text=False, trace_text=None, texttemplate='%{text:.2s}', textangle=None, textposition="outside",
            textfont={}, bar_width=None, hoverinfo=None, hoverlabel=None, hovertemplate=None, hovertext=None, sort_asc=False, sort_desc=False,
            N_largest=None, N_smallest=None, file_path=None, file_type="png", show=True):

        if sort_asc:

            # print(df.head(3))
            df.sort_values(by=y, ascending=True, inplace=True)
            self._bar_sort_asc(df, x=x, y=y, color=color, title=title, orientation=orientation, labels={"y": df.columns[ycol_pos], "x": df.columns[xcol_pos]}, update_title=update_title, update_xaxes=update_xaxes,
                               update_yaxes=update_yaxes, xtickangle=xtickangle, ytickangle=ytickangle, xtickformat=xtickformat,
                               ytickformat=ytickformat, update_legend=update_legend, update_font=update_font, hover_name=hover_name,
                               hover_data=hover_data, barmode=barmode, bargap=bargap, bargroupgap=bargroupgap,
                               color_discrete_sequence=color_discrete_sequence, color_continuous_scale=color_continuous_scale,
                               fig_width=fig_width, fig_height=fig_height, plot_bgcolor=plot_bgcolor, paper_bgcolor=paper_bgcolor,
                               uniformtext_minsize=uniformtext_minsize, uniformtext_mode=uniformtext_mode, marker=marker, selector=selector,
                               trace_name=trace_name, update_trace_text=update_trace_text, trace_text=None, texttemplate=texttemplate,
                               textangle=textangle, textposition=textposition, textfont=textfont, bar_width=bar_width, hoverinfo=hoverinfo,
                               hoverlabel=hoverlabel, hovertemplate=hovertemplate, hovertext=hovertext, file_path=file_path,
                               file_type=file_type, show=show)

        elif sort_desc:

            df.sort_values(by=y, ascending=False, inplace=True)
            self._bar_sort_desc(df, x, y, color=color, title=title, orientation=orientation, labels=labels, update_title=update_title,
                                update_xaxes=update_xaxes, update_yaxes=update_yaxes, xtickangle=xtickangle, ytickangle=ytickangle,
                                xtickformat=xtickformat, ytickformat=ytickformat, update_legend=update_legend, update_font=update_font,
                                hover_name=hover_name, hover_data=hover_data, barmode=barmode, bargap=bargap, bargroupgap=bargroupgap,
                                color_discrete_sequence=color_discrete_sequence, color_continuous_scale=color_continuous_scale,
                                fig_width=fig_width, fig_height=fig_height, plot_bgcolor=plot_bgcolor, paper_bgcolor=paper_bgcolor,
                                uniformtext_minsize=uniformtext_minsize, uniformtext_mode=uniformtext_mode, marker=marker, selector=selector,
                                trace_name=trace_name, update_trace_text=update_trace_text, trace_text=trace_text, texttemplate=texttemplate,
                                textangle=textangle, textposition=textposition, textfont=textfont, bar_width=bar_width, hoverinfo=hoverinfo,
                                hoverlabel=hoverlabel, hovertemplate=hovertemplate, hovertext=hovertext, file_path=file_path,
                                file_type=file_type, show=show)

        elif N_largest:

            df = df.nlargest(N_largest, y)
            self._n_largest(df, x, y, color=color, title=title, orientation=orientation, labels=labels, update_title=update_title, update_xaxes=update_xaxes,
                            update_yaxes=update_yaxes, xtickangle=xtickangle, ytickangle=ytickangle, xtickformat=xtickformat,
                            ytickformat=ytickformat, update_legend=update_legend, update_font=update_font, hover_name=hover_name,
                            hover_data=hover_data, barmode=barmode, bargap=bargap, bargroupgap=bargroupgap,
                            color_discrete_sequence=color_discrete_sequence, color_continuous_scale=color_continuous_scale,
                            fig_width=fig_width, fig_height=fig_height, plot_bgcolor=plot_bgcolor, paper_bgcolor=paper_bgcolor,
                            uniformtext_minsize=uniformtext_minsize, uniformtext_mode=uniformtext_mode, marker=marker, selector=selector,
                            trace_name=trace_name, update_trace_text=update_trace_text, trace_text=trace_text, texttemplate=texttemplate,
                            textangle=textangle, textposition=textposition, textfont=textfont, bar_width=bar_width, hoverinfo=hoverinfo,
                            hoverlabel=hoverlabel, hovertemplate=hovertemplate, hovertext=hovertext, N_largest=N_largest, file_path=file_path,
                            file_type=file_type, show=show)

        elif N_smallest:

            df = df.nsmallest(N_smallest, y)
            df.sort_values(by=y, ascending=False, inplace=True)
            self._n_smallest(df, x, y, color=color, title=title, orientation=orientation, labels=labels, update_title=update_title, update_xaxes=update_xaxes,
                             update_yaxes=update_yaxes, xtickangle=xtickangle, ytickangle=ytickangle, xtickformat=xtickformat,
                             ytickformat=ytickformat, update_legend=update_legend, update_font=update_font, hover_name=hover_name,
                             hover_data=hover_data, barmode=barmode, bargap=bargap, bargroupgap=bargroupgap,
                             color_discrete_sequence=color_discrete_sequence, color_continuous_scale=color_continuous_scale,
                             fig_width=fig_width, fig_height=fig_height, plot_bgcolor=plot_bgcolor, paper_bgcolor=paper_bgcolor,
                             uniformtext_minsize=uniformtext_minsize, uniformtext_mode=uniformtext_mode, marker=marker, selector=selector,
                             trace_name=trace_name, update_trace_text=update_trace_text, trace_text=trace_text, texttemplate=texttemplate,
                             textangle=textangle, textposition=textposition, textfont=textfont, bar_width=bar_width, hoverinfo=hoverinfo,
                             hoverlabel=hoverlabel, hovertemplate=hovertemplate, hovertext=hovertext, N_smallest=N_smallest,
                             file_path=file_path, file_type=file_type, show=show)

        else:

            self._bar(df, x, y, color=color, title=title, orientation=orientation, labels=labels, update_title=update_title, update_xaxes=update_xaxes,
                      update_yaxes=update_yaxes, xtickangle=xtickangle, ytickangle=ytickangle, xtickformat=xtickformat,
                      ytickformat=ytickformat, update_legend=update_legend, update_font=update_font, hover_name=hover_name,
                      hover_data=hover_data, barmode=barmode, bargap=bargap, bargroupgap=bargroupgap,
                      color_discrete_sequence=color_discrete_sequence, color_continuous_scale=color_continuous_scale,
                      fig_width=fig_width, fig_height=fig_height, plot_bgcolor=plot_bgcolor, paper_bgcolor=paper_bgcolor,
                      uniformtext_minsize=uniformtext_minsize, uniformtext_mode=uniformtext_mode, marker=marker, selector=selector,
                      trace_name=trace_name, update_trace_text=update_trace_text, trace_text=trace_text, texttemplate=texttemplate,
                      textangle=textangle, textposition=textposition, textfont=textfont, bar_width=bar_width, hoverinfo=hoverinfo,
                      hoverlabel=hoverlabel, hovertemplate=hovertemplate, hovertext=hovertext, file_path=file_path,
                      file_type=file_type, show=show)

    # Horizontal Bar Chart
    def barh(self, df=None, x=None, y=None, xcol_pos=None, ycol_pos=None, color=None, title=None, orientation='h', labels={}, update_title={}, update_xaxes={}, update_yaxes={},
            xtickangle=None, ytickangle=None, xtickformat=None, ytickformat=None, update_legend={}, update_font={}, hover_name=None,
            hover_data=None, barmode="relative", bargap=0.15, bargroupgap=0.1, color_discrete_sequence=None, fig_width=1200, fig_height=800,
            color_continuous_scale=None, plot_bgcolor=None, paper_bgcolor=None, uniformtext_minsize=8, uniformtext_mode="hide",
            marker={}, selector={}, trace_name=None, update_trace_text=False, trace_text=None, texttemplate='%{text:.2s}', textangle=None, textposition="outside",
            textfont={}, bar_width=None, hoverinfo=None, hoverlabel=None, hovertemplate=None, hovertext=None, sort_asc=False, sort_desc=False,
            N_largest=None, N_smallest=None, file_path=None, file_type="png", show=True):

        if sort_asc:

            df.sort_values(by=x, ascending=True, inplace=True)
            self._bar_sort_asc(df, x, y, color=color, title=title, orientation=orientation, labels={"y": df.columns[ycol_pos], "x": df.columns[xcol_pos]}, update_title=update_title, update_xaxes=update_xaxes,
                               update_yaxes=update_yaxes, xtickangle=xtickangle, ytickangle=ytickangle, xtickformat=xtickformat,
                               ytickformat=ytickformat, update_legend=update_legend, update_font=update_font, hover_name=hover_name,
                               hover_data=hover_data, barmode=barmode, bargap=bargap, bargroupgap=bargroupgap,
                               color_discrete_sequence=color_discrete_sequence, color_continuous_scale=color_continuous_scale,
                               fig_width=fig_width, fig_height=fig_height, plot_bgcolor=plot_bgcolor, paper_bgcolor=paper_bgcolor,
                               uniformtext_minsize=uniformtext_minsize, uniformtext_mode=uniformtext_mode, marker=marker, selector=selector,
                               trace_name=trace_name, update_trace_text=update_trace_text, trace_text=None, texttemplate=texttemplate,
                               textangle=textangle, textposition=textposition, textfont=textfont, bar_width=bar_width, hoverinfo=hoverinfo,
                               hoverlabel=hoverlabel, hovertemplate=hovertemplate, hovertext=hovertext, file_path=file_path,
                               file_type=file_type, show=show)

        elif sort_desc:

            df.sort_values(by=x, ascending=False, inplace=True)
            self._bar_sort_desc(df, x, y, color=color, title=title, orientation=orientation, labels=labels, update_title=update_title, update_xaxes=update_xaxes,
                                update_yaxes=update_yaxes, xtickangle=xtickangle, ytickangle=ytickangle, xtickformat=xtickformat,
                                ytickformat=ytickformat, update_legend=update_legend, update_font=update_font, hover_name=hover_name,
                                hover_data=hover_data, barmode=barmode, bargap=bargap, bargroupgap=bargroupgap,
                                color_discrete_sequence=color_discrete_sequence, color_continuous_scale=color_continuous_scale,
                                fig_width=fig_width, fig_height=fig_height, plot_bgcolor=plot_bgcolor, paper_bgcolor=paper_bgcolor,
                                uniformtext_minsize=uniformtext_minsize, uniformtext_mode=uniformtext_mode, marker=marker, selector=selector,
                                trace_name=trace_name, update_trace_text=update_trace_text, trace_text=trace_text, texttemplate=texttemplate,
                                textangle=textangle, textposition=textposition, textfont=textfont, bar_width=bar_width, hoverinfo=hoverinfo,
                                hoverlabel=hoverlabel, hovertemplate=hovertemplate, hovertext=hovertext, file_path=file_path,
                                file_type=file_type, show=show)

        elif N_largest:

            df = df.nlargest(N_largest, x)
            df.sort_values(by=x, ascending=True, inplace=True)
            self._n_largest(df, x, y, color=color, title=title, orientation=orientation, labels=labels, update_title=update_title, update_xaxes=update_xaxes,
                            update_yaxes=update_yaxes, xtickangle=xtickangle, ytickangle=ytickangle, xtickformat=xtickformat,
                            ytickformat=ytickformat, update_legend=update_legend, update_font=update_font, hover_name=hover_name,
                            hover_data=hover_data, barmode=barmode, bargap=bargap, bargroupgap=bargroupgap,
                            color_discrete_sequence=color_discrete_sequence, color_continuous_scale=color_continuous_scale,
                            fig_width=fig_width, fig_height=fig_height, plot_bgcolor=plot_bgcolor, paper_bgcolor=paper_bgcolor,
                            uniformtext_minsize=uniformtext_minsize, uniformtext_mode=uniformtext_mode, marker=marker, selector=selector,
                            trace_name=trace_name, update_trace_text=update_trace_text, trace_text=trace_text, texttemplate=texttemplate,
                            textangle=textangle, textposition=textposition, textfont=textfont, bar_width=bar_width, hoverinfo=hoverinfo,
                            hoverlabel=hoverlabel, hovertemplate=hovertemplate, hovertext=hovertext, N_largest=N_largest, file_path=file_path,
                            file_type=file_type, show=show)

        elif N_smallest:

            df = df.nsmallest(N_smallest, x)
            self._n_smallest(df, x, y, color=color, title=title, orientation=orientation, labels=labels, update_title=update_title, update_xaxes=update_xaxes,
                             update_yaxes=update_yaxes, xtickangle=xtickangle, ytickangle=ytickangle, xtickformat=xtickformat,
                             ytickformat=ytickformat, update_legend=update_legend, update_font=update_font, hover_name=hover_name,
                             hover_data=hover_data, barmode=barmode, bargap=bargap, bargroupgap=bargroupgap,
                             color_discrete_sequence=color_discrete_sequence, color_continuous_scale=color_continuous_scale,
                             fig_width=fig_width, fig_height=fig_height, plot_bgcolor=plot_bgcolor, paper_bgcolor=paper_bgcolor,
                             uniformtext_minsize=uniformtext_minsize, uniformtext_mode=uniformtext_mode, marker=marker, selector=selector,
                             trace_name=trace_name, update_trace_text=update_trace_text, trace_text=trace_text, texttemplate=texttemplate,
                             textangle=textangle, textposition=textposition, textfont=textfont, bar_width=bar_width, hoverinfo=hoverinfo,
                             hoverlabel=hoverlabel, hovertemplate=hovertemplate, hovertext=hovertext, N_smallest=N_smallest,
                             file_path=file_path, file_type=file_type, show=show)

        else:

            self._bar(df, x, y, color=color, title=title, orientation=orientation, labels=labels, update_title=update_title, update_xaxes=update_xaxes,
                      update_yaxes=update_yaxes, xtickangle=xtickangle, ytickangle=ytickangle, xtickformat=xtickformat,
                      ytickformat=ytickformat, update_legend=update_legend, update_font=update_font, hover_name=hover_name,
                      hover_data=hover_data, barmode=barmode, bargap=bargap, bargroupgap=bargroupgap,
                      color_discrete_sequence=color_discrete_sequence, color_continuous_scale=color_continuous_scale,
                      fig_width=fig_width, fig_height=fig_height, plot_bgcolor=plot_bgcolor, paper_bgcolor=paper_bgcolor,
                      uniformtext_minsize=uniformtext_minsize, uniformtext_mode=uniformtext_mode, marker=marker, selector=selector,
                      trace_name=trace_name, update_trace_text=update_trace_text, trace_text=trace_text, texttemplate=texttemplate,
                      textangle=textangle, textposition=textposition, textfont=textfont, bar_width=bar_width, hoverinfo=hoverinfo,
                      hoverlabel=hoverlabel, hovertemplate=hovertemplate, hovertext=hovertext, file_path=file_path,
                      file_type=file_type, show=show)

    def _bar_sort_asc(self, df, x, y, color, title, orientation, labels, update_title, update_xaxes,
                      update_yaxes, xtickangle, ytickangle, xtickformat, ytickformat, update_legend, update_font, hover_name,
                      hover_data, barmode, bargap, bargroupgap, color_discrete_sequence, color_continuous_scale,
                      fig_width, fig_height, plot_bgcolor, paper_bgcolor, uniformtext_minsize, uniformtext_mode, marker, selector,
                      trace_name, update_trace_text, trace_text, texttemplate, textangle, textposition, textfont, bar_width, hoverinfo,
                      hoverlabel, hovertemplate, hovertext, file_path, file_type, show):
        try:

            fig = px.bar(df, x=x, y=y, color=color, labels=labels, title=title, hover_data=hover_data, hover_name=hover_name,
                         color_discrete_sequence=color_discrete_sequence, color_continuous_scale=color_continuous_scale)

            fig.update_layout(
                xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False)
            )

            fig.update_layout(
                title=update_title,
                xaxis=update_xaxes,
                yaxis=update_yaxes,
                legend=update_legend,
                xaxis_tickangle=xtickangle,
                yaxis_tickangle=ytickangle,
                xaxis_tickformat=xtickformat,
                yaxis_tickformat=ytickformat,
                width=fig_width,
                height=fig_height,
                font=update_font,
                barmode=barmode,
                bargap=bargap,
                bargroupgap=bargroupgap,
                uniformtext_minsize=uniformtext_minsize,
                uniformtext_mode=uniformtext_mode,
                plot_bgcolor=plot_bgcolor,
                paper_bgcolor=paper_bgcolor,
                )

            if orientation == "h":
                fig.update_layout(
                    xaxis=update_xaxes,
                    yaxis=update_yaxes,
                )

            if update_trace_text:
                if orientation == "h":
                    if trace_text:
                        text = trace_text
                        fig.update_traces(
                            text=text,
                            texttemplate=texttemplate,
                            textangle=textangle,
                            textposition=textposition,
                            textfont=textfont)
                    else:
                        fig.update_traces(
                            text=df[x],
                            texttemplate=texttemplate,
                            textangle=textangle,
                            textposition=textposition,
                            textfont=textfont)
                else:
                    if trace_text:
                        text = trace_text
                        fig.update_traces(
                            text=text,
                            texttemplate=texttemplate,
                            textangle=textangle,
                            textposition=textposition,
                            textfont=textfont)
                    else:
                        fig.update_traces(
                            text=df[y],
                            texttemplate=texttemplate,
                            textangle=textangle,
                            textposition=textposition,
                            textfont=textfont)

            fig.update_traces(
                width=bar_width,
                hoverinfo=hoverinfo,
                hoverlabel=hoverlabel,
                hovertemplate=hovertemplate,
                hovertext=hovertext,
                marker=marker,
                selector=selector
                )

            fig.for_each_trace(
                lambda trace: trace.update(marker_color="black") if trace.name == trace_name else ()
            )

            # right to png
            if file_type == "png":
                if os.path.exists('{}{}_asc'.format(file_path, title.lower().replace(' ', '_')) + ".png"):
                    old_file_name = '{}{}_asc.png'.format(file_path, title.lower().replace(' ', '_'))
                    new_file_name = '{}old_{}_asc.png'.format(file_path, title.lower().replace(' ', '_'))

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file_name = file_path + "{}_asc".format(title.lower().replace(' ', '_')) + ".png"
                fig.write_image(file_name)
                print('File, {}, has been created successfully'.format(file_name))

            # right to jpeg
            if file_type == "jpeg":
                if os.path.exists('{}{}_asc'.format(file_path, title.lower().replace(' ', '_')) + ".jpeg"):
                    old_file_name = '{}{}_asc.jpeg'.format(file_path, title.lower().replace(' ', '_'))
                    new_file_name = '{}old_{}_asc.jpeg'.format(file_path, title.lower().replace(' ', '_'))

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file_name = file_path + "{}_asc".format(title.lower().replace(' ', '_')) + ".jpeg"
                fig.write_image(file_name)
                print('File, {}, has been created successfully'.format(file_name))

            # right to svg
            if file_type == "svg":
                if os.path.exists('{}{}_asc'.format(file_path, title.lower().replace(' ', '_')) + ".svg"):
                    old_file_name = '{}{}_asc.svg'.format(file_path, title.lower().replace(' ', '_'))
                    new_file_name = '{}old_{}_asc.svg'.format(file_path, title.lower().replace(' ', '_'))

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file_name = file_path + "{}_asc".format(title.lower().replace(' ', '_')) + ".svg"
                fig.write_image(file_name)
                print('File, {}, has been created successfully'.format(file_name))

            # right to pdf
            if file_type == "pdf":
                if os.path.exists('{}{}_asc'.format(file_path, title.lower().replace(' ', '_')) + ".pdf"):
                    old_file_name = '{}{}_asc.pdf'.format(file_path, title.lower().replace(' ', '_'))
                    new_file_name = '{}old_{}_asc.pdf'.format(file_path, title.lower().replace(' ', '_'))

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file_name = file_path + "{}_asc".format(title.lower().replace(' ', '_')) + ".pdf"
                fig.write_image(file_name)
                print('File, {}, has been created successfully'.format(file_name))

            # right to eps
            if file_type == "eps":
                if os.path.exists('{}{}_asc'.format(file_path, title.lower().replace(' ', '_')) + ".eps"):
                    old_file_name = '{}{}_asc.eps'.format(file_path, title.lower().replace(' ', '_'))
                    new_file_name = '{}old_{}_asc.eps'.format(file_path, title.lower().replace(' ', '_'))

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file_name = file_path + "{}_asc".format(title.lower().replace(' ', '_')) + ".eps"
                fig.write_image(file_name)
                print('File, {}, has been created successfully'.format(file_name))

            # right to jpeg
            if file_type == "webp":
                if os.path.exists('{}{}_asc'.format(file_path, title.lower().replace(' ', '_')) + ".webp"):
                    old_file_name = '{}{}_asc.webp'.format(file_path, title.lower().replace(' ', '_'))
                    new_file_name = '{}old_{}_asc.webp'.format(file_path, title.lower().replace(' ', '_'))

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file_name = file_path + "{}_asc".format(title.lower().replace(' ', '_')) + ".webp"
                fig.write_image(file_name)
                print('File, {}, has been created successfully'.format(file_name))
            if show:
                fig.show()

        except Exception as e:
            print('Error: {}'.format(str(e)))

    def _bar_sort_desc(self, df, x, y, color, title, orientation, labels, update_title, update_xaxes,
                       update_yaxes, xtickangle, ytickangle, xtickformat, ytickformat, update_legend, update_font, hover_name,
                       hover_data, barmode, bargap, bargroupgap, color_discrete_sequence, color_continuous_scale,
                       fig_width, fig_height, plot_bgcolor, paper_bgcolor, uniformtext_minsize, uniformtext_mode, marker, selector,
                       trace_name, update_trace_text, trace_text, texttemplate, textangle, textposition, textfont, bar_width, hoverinfo,
                       hoverlabel, hovertemplate, hovertext, file_path, file_type, show):
        try:

            fig = px.bar(df, x=x, y=y, color=color, labels=labels, title=title, hover_data=hover_data, hover_name=hover_name,
                         color_discrete_sequence=color_discrete_sequence, color_continuous_scale=color_continuous_scale)

            fig.update_layout(
                xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False)
            )

            fig.update_layout(
                title=update_title,
                xaxis=update_xaxes,
                yaxis=update_yaxes,
                legend=update_legend,
                xaxis_tickangle=xtickangle,
                yaxis_tickangle=ytickangle,
                xaxis_tickformat=xtickformat,
                yaxis_tickformat=ytickformat,
                width=fig_width,
                height=fig_height,
                font=update_font,
                barmode=barmode,
                bargap=bargap,
                bargroupgap=bargroupgap,
                uniformtext_minsize=uniformtext_minsize,
                uniformtext_mode=uniformtext_mode,
                plot_bgcolor=plot_bgcolor,
                paper_bgcolor=paper_bgcolor,
                )

            if orientation == "h":
                fig.update_layout(
                    xaxis=update_xaxes,
                    yaxis=update_yaxes,
                )

            if update_trace_text:
                if orientation == "h":
                    if trace_text:
                        text = trace_text
                        fig.update_traces(
                            text=text,
                            texttemplate=texttemplate,
                            textangle=textangle,
                            textposition=textposition,
                            textfont=textfont)
                    else:
                        fig.update_traces(
                            text=df[x],
                            texttemplate=texttemplate,
                            textangle=textangle,
                            textposition=textposition,
                            textfont=textfont)
                else:
                    if trace_text:
                        text = trace_text
                        fig.update_traces(
                            text=text,
                            texttemplate=texttemplate,
                            textangle=textangle,
                            textposition=textposition,
                            textfont=textfont)
                    else:
                        fig.update_traces(
                            text=df[y],
                            texttemplate=texttemplate,
                            textangle=textangle,
                            textposition=textposition,
                            textfont=textfont)

            fig.update_traces(
                width=bar_width,
                hoverinfo=hoverinfo,
                hoverlabel=hoverlabel,
                hovertemplate=hovertemplate,
                hovertext=hovertext,
                marker=marker,
                selector=selector
                )

            fig.for_each_trace(
                lambda trace: trace.update(marker_color="black") if trace.name == trace_name else ()
            )

            # right to png
            if file_type == "png":
                if os.path.exists('{}{}_desc'.format(file_path, title.lower().replace(' ', '_')) + ".png"):
                    old_file_name = '{}{}_desc.png'.format(file_path, title.lower().replace(' ', '_'))
                    new_file_name = '{}old_{}_desc.png'.format(file_path, title.lower().replace(' ', '_'))

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file_name = file_path + "{}_desc".format(title.lower().replace(' ', '_')) + ".png"
                fig.write_image(file_name)
                print('File, {}, has been created successfully'.format(file_name))

            # right to jpeg
            if file_type == "jpeg":
                if os.path.exists('{}{}_desc'.format(file_path, title.lower().replace(' ', '_')) + ".jpeg"):
                    old_file_name = '{}{}_desc.jpeg'.format(file_path, title.lower().replace(' ', '_'))
                    new_file_name = '{}old_{}_desc.jpeg'.format(file_path, title.lower().replace(' ', '_'))

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file_name = file_path + "{}_desc".format(title.lower().replace(' ', '_')) + ".jpeg"
                fig.write_image(file_name)
                print('File, {}, has been created successfully'.format(file_name))

            # right to svg
            if file_type == "svg":
                if os.path.exists('{}{}_desc'.format(file_path, title.lower().replace(' ', '_')) + ".svg"):
                    old_file_name = '{}{}_desc.svg'.format(file_path, title.lower().replace(' ', '_'))
                    new_file_name = '{}old_{}_desc.svg'.format(file_path, title.lower().replace(' ', '_'))

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file_name = file_path + "{}_desc".format(title.lower().replace(' ', '_')) + ".svg"
                fig.write_image(file_name)
                print('File, {}, has been created successfully'.format(file_name))

            # right to pdf
            if file_type == "pdf":
                if os.path.exists('{}{}_desc'.format(file_path, title.lower().replace(' ', '_')) + ".pdf"):
                    old_file_name = '{}{}_desc.pdf'.format(file_path, title.lower().replace(' ', '_'))
                    new_file_name = '{}old_{}_desc.pdf'.format(file_path, title.lower().replace(' ', '_'))

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file_name = file_path + "{}_desc".format(title.lower().replace(' ', '_')) + ".pdf"
                fig.write_image(file_name)
                print('File, {}, has been created successfully'.format(file_name))

            # right to eps
            if file_type == "eps":
                if os.path.exists('{}{}_desc'.format(file_path, title.lower().replace(' ', '_')) + ".eps"):
                    old_file_name = '{}{}_desc.eps'.format(file_path, title.lower().replace(' ', '_'))
                    new_file_name = '{}old_{}_desc.eps'.format(file_path, title.lower().replace(' ', '_'))

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file_name = file_path + "{}_desc".format(title.lower().replace(' ', '_')) + ".eps"
                fig.write_image(file_name)
                print('File, {}, has been created successfully'.format(file_name))

            # right to jpeg
            if file_type == "webp":
                if os.path.exists('{}{}_desc'.format(file_path, title.lower().replace(' ', '_')) + ".webp"):
                    old_file_name = '{}{}_desc.webp'.format(file_path, title.lower().replace(' ', '_'))
                    new_file_name = '{}old_{}_desc.webp'.format(file_path, title.lower().replace(' ', '_'))

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file_name = file_path + "{}_desc".format(title.lower().replace(' ', '_')) + ".webp"
                fig.write_image(file_name)
                print('File, {}, has been created successfully'.format(file_name))
            if show:
                fig.show()

        except Exception as e:
            print('Error: {}'.format(str(e)))

    def _n_largest(self, df, x, y, color, title, orientation, labels, update_title, update_xaxes,
                   update_yaxes, xtickangle, ytickangle, xtickformat, ytickformat, update_legend, update_font, hover_name,
                   hover_data, barmode, bargap, bargroupgap, color_discrete_sequence, color_continuous_scale,
                   fig_width, fig_height, plot_bgcolor, paper_bgcolor, uniformtext_minsize, uniformtext_mode, marker, selector,
                   trace_name, update_trace_text, trace_text, texttemplate, textangle, textposition, textfont, bar_width, hoverinfo,
                   hoverlabel, hovertemplate, hovertext, N_largest, file_path, file_type, show):
        try:

            fig = px.bar(df, x=x, y=y, color=color, labels=labels, title=title, hover_data=hover_data, hover_name=hover_name,
                         color_discrete_sequence=color_discrete_sequence, color_continuous_scale=color_continuous_scale)

            fig.update_layout(
                xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False)
            )

            fig.update_layout(
                title=update_title,
                xaxis=update_xaxes,
                yaxis=update_yaxes,
                legend=update_legend,
                xaxis_tickangle=xtickangle,
                yaxis_tickangle=ytickangle,
                xaxis_tickformat=xtickformat,
                yaxis_tickformat=ytickformat,
                width=fig_width,
                height=fig_height,
                font=update_font,
                barmode=barmode,
                bargap=bargap,
                bargroupgap=bargroupgap,
                uniformtext_minsize=uniformtext_minsize,
                uniformtext_mode=uniformtext_mode,
                plot_bgcolor=plot_bgcolor,
                paper_bgcolor=paper_bgcolor,
                )

            if orientation == "h":
                fig.update_layout(
                    xaxis=update_xaxes,
                    yaxis=update_yaxes,
                )

            if update_trace_text:
                if orientation == "h":
                    if trace_text:
                        text = trace_text
                        fig.update_traces(
                            text=text,
                            texttemplate=texttemplate,
                            textangle=textangle,
                            textposition=textposition,
                            textfont=textfont)
                    else:
                        fig.update_traces(
                            text=df[x],
                            texttemplate=texttemplate,
                            textangle=textangle,
                            textposition=textposition,
                            textfont=textfont)
                else:
                    if trace_text:
                        text = trace_text
                        fig.update_traces(
                            text=text,
                            texttemplate=texttemplate,
                            textangle=textangle,
                            textposition=textposition,
                            textfont=textfont)
                    else:
                        fig.update_traces(
                            text=df[y],
                            texttemplate=texttemplate,
                            textangle=textangle,
                            textposition=textposition,
                            textfont=textfont)

            fig.update_traces(
                width=bar_width,
                hoverinfo=hoverinfo,
                hoverlabel=hoverlabel,
                hovertemplate=hovertemplate,
                hovertext=hovertext,
                marker=marker,
                selector=selector
                )

            fig.for_each_trace(
                lambda trace: trace.update(marker_color="black") if trace.name == trace_name else ()
            )

            # right to png
            if file_type == "png":
                if os.path.exists('{}{}_top_{}'.format(file_path, title.lower().replace(' ', '_'), N_largest) + ".png"):
                    old_file_name = '{}{}_top_{}.png'.format(file_path, title.lower().replace(' ', '_'), N_largest)
                    new_file_name = '{}old_{}_top_{}.png'.format(file_path, title.lower().replace(' ', '_'), N_largest)

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file_name = file_path + "{}_top_{}".format(title.lower().replace(' ', '_'), N_largest) + ".png"
                fig.write_image(file_name)
                print('File, {}, has been created successfully'.format(file_name))

            # right to jpeg
            if file_type == "jpeg":
                if os.path.exists('{}{}_top_{}'.format(file_path, title.lower().replace(' ', '_'), N_largest) + ".jpeg"):
                    old_file_name = '{}{}_top_{}.jpeg'.format(file_path, title.lower().replace(' ', '_'), N_largest)
                    new_file_name = '{}old_{}_top_{}.jpeg'.format(file_path, title.lower().replace(' ', '_'), N_largest)

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file_name = file_path + "{}_top_{}".format(title.lower().replace(' ', '_'), N_largest) + ".jpeg"
                fig.write_image(file_name)
                print('File, {}, has been created successfully'.format(file_name))

            # right to svg
            if file_type == "svg":
                if os.path.exists('{}{}_top_{}'.format(file_path, title.lower().replace(' ', '_'), N_largest) + ".svg"):
                    old_file_name = '{}{}_top_{}.svg'.format(file_path, title.lower().replace(' ', '_'), N_largest)
                    new_file_name = '{}old_{}_top_{}.svg'.format(file_path, title.lower().replace(' ', '_'), N_largest)

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file_name = file_path + "{}_top_{}".format(title.lower().replace(' ', '_'), N_largest) + ".svg"
                fig.write_image(file_name)
                print('File, {}, has been created successfully'.format(file_name))

            # right to pdf
            if file_type == "pdf":
                if os.path.exists('{}{}_top_{}'.format(file_path, title.lower().replace(' ', '_'), N_largest) + ".pdf"):
                    old_file_name = '{}{}_top_{}.pdf'.format(file_path, title.lower().replace(' ', '_'), N_largest)
                    new_file_name = '{}old_{}_top_{}.pdf'.format(file_path, title.lower().replace(' ', '_'), N_largest)

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file_name = file_path + "{}_top_{}".format(title.lower().replace(' ', '_'), N_largest) + ".pdf"
                fig.write_image(file_name)
                print('File, {}, has been created successfully'.format(file_name))

            # right to eps
            if file_type == "eps":
                if os.path.exists('{}{}_top_{}'.format(file_path, title.lower().replace(' ', '_'), N_largest) + ".eps"):
                    old_file_name = '{}{}_top_{}.eps'.format(file_path, title.lower().replace(' ', '_'), N_largest)
                    new_file_name = '{}old_{}_top_{}.eps'.format(file_path, title.lower().replace(' ', '_'), N_largest)

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file_name = file_path + "{}_top_{}".format(title.lower().replace(' ', '_'), N_largest) + ".eps"
                fig.write_image(file_name)
                print('File, {}, has been created successfully'.format(file_name))

            # right to jpeg
            if file_type == "webp":
                if os.path.exists('{}{}_top_{}'.format(file_path, title.lower().replace(' ', '_'), N_largest) + ".webp"):
                    old_file_name = '{}{}_top_{}.webp'.format(file_path, title.lower().replace(' ', '_'), N_largest)
                    new_file_name = '{}old_{}_top_{}.webp'.format(file_path, title.lower().replace(' ', '_'), N_largest)

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file_name = file_path + "{}_top_{}".format(title.lower().replace(' ', '_'), N_largest) + ".webp"
                fig.write_image(file_name)
                print('File, {}, has been created successfully'.format(file_name))
            if show:
                fig.show()

        except Exception as e:
            print('Error: {}'.format(str(e)))

    def _n_smallest(self, df, x, y, color, title, orientation, labels, update_title, update_xaxes,
                    update_yaxes, xtickangle, ytickangle, xtickformat, ytickformat, update_legend, update_font, hover_name,
                    hover_data, barmode, bargap, bargroupgap, color_discrete_sequence, color_continuous_scale,
                    fig_width, fig_height, plot_bgcolor, paper_bgcolor, uniformtext_minsize, uniformtext_mode, marker, selector,
                    trace_name, update_trace_text, trace_text, texttemplate, textangle, textposition, textfont, bar_width, hoverinfo,
                    hoverlabel, hovertemplate, hovertext, N_smallest, file_path, file_type, show):
        try:

            fig = px.bar(df, x=x, y=y, color=color, labels=labels, title=title, hover_data=hover_data, hover_name=hover_name,
                         color_discrete_sequence=color_discrete_sequence, color_continuous_scale=color_continuous_scale)

            fig.update_layout(
                xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False)
            )

            fig.update_layout(
                title=update_title,
                xaxis=update_xaxes,
                yaxis=update_yaxes,
                legend=update_legend,
                xaxis_tickangle=xtickangle,
                yaxis_tickangle=ytickangle,
                xaxis_tickformat=xtickformat,
                yaxis_tickformat=ytickformat,
                width=fig_width,
                height=fig_height,
                font=update_font,
                barmode=barmode,
                bargap=bargap,
                bargroupgap=bargroupgap,
                uniformtext_minsize=uniformtext_minsize,
                uniformtext_mode=uniformtext_mode,
                plot_bgcolor=plot_bgcolor,
                paper_bgcolor=paper_bgcolor,
                )

            if orientation == "h":
                fig.update_layout(
                    xaxis=update_xaxes,
                    yaxis=update_yaxes,
                )

            if update_trace_text:
                if orientation == "h":
                    if trace_text:
                        text = trace_text
                        fig.update_traces(
                            text=text,
                            texttemplate=texttemplate,
                            textangle=textangle,
                            textposition=textposition,
                            textfont=textfont)
                    else:
                        fig.update_traces(
                            text=df[x],
                            texttemplate=texttemplate,
                            textangle=textangle,
                            textposition=textposition,
                            textfont=textfont)
                else:
                    if trace_text:
                        text = trace_text
                        fig.update_traces(
                            text=text,
                            texttemplate=texttemplate,
                            textangle=textangle,
                            textposition=textposition,
                            textfont=textfont)
                    else:
                        fig.update_traces(
                            text=df[y],
                            texttemplate=texttemplate,
                            textangle=textangle,
                            textposition=textposition,
                            textfont=textfont)

            fig.update_traces(
                width=bar_width,
                hoverinfo=hoverinfo,
                hoverlabel=hoverlabel,
                hovertemplate=hovertemplate,
                hovertext=hovertext,
                marker=marker,
                selector=selector
                )

            fig.for_each_trace(
                lambda trace: trace.update(marker_color="black") if trace.name == trace_name else ()
            )

            # right to png
            if file_type == "png":
                if os.path.exists('{}{}_bottom_{}'.format(file_path, title.lower().replace(' ', '_'), N_smallest) + ".png"):
                    old_file_name = '{}{}_bottom_{}.png'.format(file_path, title.lower().replace(' ', '_'), N_smallest)
                    new_file_name = '{}old_{}_bottom_{}.png'.format(file_path, title.lower().replace(' ', '_'), N_smallest)

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file_name = file_path + "{}_bottom_{}".format(title.lower().replace(' ', '_'), N_smallest) + ".png"
                fig.write_image(file_name)
                print('File, {}, has been created successfully'.format(file_name))

            # right to jpeg
            if file_type == "jpeg":
                if os.path.exists('{}{}_bottom_{}'.format(file_path, title.lower().replace(' ', '_'), N_smallest) + ".jpeg"):
                    old_file_name = '{}{}_bottom_{}.jpeg'.format(file_path, title.lower().replace(' ', '_'), N_smallest)
                    new_file_name = '{}old_{}_bottom_{}.jpeg'.format(file_path, title.lower().replace(' ', '_'), N_smallest)

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file_name = file_path + "{}_bottom_{}".format(title.lower().replace(' ', '_'), N_smallest) + ".jpeg"
                fig.write_image(file_name)
                print('File, {}, has been created successfully'.format(file_name))

            # right to svg
            if file_type == "svg":
                if os.path.exists('{}{}_bottom_{}'.format(file_path, title.lower().replace(' ', '_'), N_smallest) + ".svg"):
                    old_file_name = '{}{}_bottom_{}.svg'.format(file_path, title.lower().replace(' ', '_'), N_smallest)
                    new_file_name = '{}old_{}_bottom_{}.svg'.format(file_path, title.lower().replace(' ', '_'), N_smallest)

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file_name = file_path + "{}_bottom_{}".format(title.lower().replace(' ', '_'), N_smallest) + ".svg"
                fig.write_image(file_name)
                print('File, {}, has been created successfully'.format(file_name))

            # right to pdf
            if file_type == "pdf":
                if os.path.exists('{}{}_bottom_{}'.format(file_path, title.lower().replace(' ', '_'), N_smallest) + ".pdf"):
                    old_file_name = '{}{}_bottom_{}.pdf'.format(file_path, title.lower().replace(' ', '_'), N_smallest)
                    new_file_name = '{}old_{}_bottom_{}.pdf'.format(file_path, title.lower().replace(' ', '_'), N_smallest)

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file_name = file_path + "{}_bottom_{}".format(title.lower().replace(' ', '_'), N_smallest) + ".pdf"
                fig.write_image(file_name)
                print('File, {}, has been created successfully'.format(file_name))

            # right to eps
            if file_type == "eps":
                if os.path.exists('{}{}_bottom_{}'.format(file_path, title.lower().replace(' ', '_'), N_smallest) + ".eps"):
                    old_file_name = '{}{}_bottom_{}.eps'.format(file_path, title.lower().replace(' ', '_'), N_smallest)
                    new_file_name = '{}old_{}_bottom_{}.eps'.format(file_path, title.lower().replace(' ', '_'), N_smallest)

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file_name = file_path + "{}_bottom_{}".format(title.lower().replace(' ', '_'), N_smallest) + ".eps"
                fig.write_image(file_name)
                print('File, {}, has been created successfully'.format(file_name))

            # right to jpeg
            if file_type == "webp":
                if os.path.exists('{}{}_bottom_{}'.format(file_path, title.lower().replace(' ', '_'), N_smallest) + ".webp"):
                    old_file_name = '{}{}_bottom_{}.webp'.format(file_path, title.lower().replace(' ', '_'), N_smallest)
                    new_file_name = '{}old_{}_bottom_{}.webp'.format(file_path, title.lower().replace(' ', '_'), N_smallest)

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file_name = file_path + "{}_bottom_{}".format(title.lower().replace(' ', '_'), N_smallest) + ".webp"
                fig.write_image(file_name)
                print('File, {}, has been created successfully'.format(file_name))
            if show:
                fig.show()

        except Exception as e:
            print('Error: {}'.format(str(e)))

    def _bar(self, df, x, y, color, title, orientation, labels, update_title, update_xaxes,
             update_yaxes, xtickangle, ytickangle, xtickformat, ytickformat, update_legend, update_font, hover_name,
             hover_data, barmode, bargap, bargroupgap, color_discrete_sequence, color_continuous_scale,
             fig_width, fig_height, plot_bgcolor, paper_bgcolor, uniformtext_minsize, uniformtext_mode, marker, selector,
             trace_name, update_trace_text, trace_text, texttemplate, textangle, textposition, textfont, bar_width, hoverinfo,
             hoverlabel, hovertemplate, hovertext, file_path, file_type, show):

        try:

            fig = px.bar(df, x, y, color=color, labels=labels, title=title, hover_data=hover_data, hover_name=hover_name,
                         color_discrete_sequence=color_discrete_sequence, color_continuous_scale=color_continuous_scale)

            fig.update_layout(
                xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False)
            )

            fig.update_layout(
                title=update_title,
                xaxis=update_xaxes,
                yaxis=update_yaxes,
                legend=update_legend,
                xaxis_tickangle=xtickangle,
                yaxis_tickangle=ytickangle,
                xaxis_tickformat=xtickformat,
                yaxis_tickformat=ytickformat,
                width=fig_width,
                height=fig_height,
                font=update_font,
                barmode=barmode,
                bargap=bargap,
                bargroupgap=bargroupgap,
                uniformtext_minsize=uniformtext_minsize,
                uniformtext_mode=uniformtext_mode,
                plot_bgcolor=plot_bgcolor,
                paper_bgcolor=paper_bgcolor,
                )

            if orientation == "h":
                fig.update_layout(
                    xaxis=update_xaxes,
                    yaxis=update_yaxes,

                )

            if update_trace_text:
                if orientation == "h":
                    if trace_text:
                        text = trace_text
                        fig.update_traces(
                            text=text,
                            texttemplate=texttemplate,
                            textangle=textangle,
                            textposition=textposition,
                            textfont=textfont)
                    else:
                        fig.update_traces(
                            text=df[x],
                            texttemplate=texttemplate,
                            textangle=textangle,
                            textposition=textposition,
                            textfont=textfont)
                else:
                    if trace_text:
                        text = trace_text
                        fig.update_traces(
                            text=text,
                            texttemplate=texttemplate,
                            textangle=textangle,
                            textposition=textposition,
                            textfont=textfont)
                    else:
                        fig.update_traces(
                            text=df[y],
                            texttemplate=texttemplate,
                            textangle=textangle,
                            textposition=textposition,
                            textfont=textfont)

            fig.update_traces(
                width=bar_width,
                hoverinfo=hoverinfo,
                hoverlabel=hoverlabel,
                hovertemplate=hovertemplate,
                hovertext=hovertext,
                marker=marker,
                selector=selector
                )

            fig.for_each_trace(
                lambda trace: trace.update(marker_color="black") if trace.name == trace_name else ()
            )

            # right to png
            if file_type == "png":
                if os.path.exists('{}{}'.format(file_path, title.lower().replace(' ', '_')) + ".png"):
                    old_file_name = '{}{}.png'.format(file_path, title.lower().replace(' ', '_'))
                    new_file_name = '{}old_{}.png'.format(file_path, title.lower().replace(' ', '_'))

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file_name = file_path + "{}".format(title.lower().replace(' ', '_')) + ".png"
                fig.write_image(file_name)
                print('File, {}, has been created successfully'.format(file_name))

            # right to jpeg
            if file_type == "jpeg":
                if os.path.exists('{}{}'.format(file_path, title.lower().replace(' ', '_')) + ".jpeg"):
                    old_file_name = '{}{}.jpeg'.format(file_path, title.lower().replace(' ', '_'))
                    new_file_name = '{}old_{}.jpeg'.format(file_path, title.lower().replace(' ', '_'))

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file_name = file_path + "{}".format(title.lower().replace(' ', '_')) + ".jpeg"
                fig.write_image(file_name)
                print('File, {}, has been created successfully'.format(file_name))

            # right to svg
            if file_type == "svg":
                if os.path.exists('{}{}'.format(file_path, title.lower().replace(' ', '_')) + ".svg"):
                    old_file_name = '{}{}.svg'.format(file_path, title.lower().replace(' ', '_'))
                    new_file_name = '{}old_{}.svg'.format(file_path, title.lower().replace(' ', '_'))

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file_name = file_path + "{}".format(title.lower().replace(' ', '_')) + ".svg"
                fig.write_image(file_name)
                print('File, {}, has been created successfully'.format(file_name))

            # right to pdf
            if file_type == "pdf":
                if os.path.exists('{}{}'.format(file_path, title.lower().replace(' ', '_')) + ".pdf"):
                    old_file_name = '{}{}.pdf'.format(file_path, title.lower().replace(' ', '_'))
                    new_file_name = '{}old_{}.pdf'.format(file_path, title.lower().replace(' ', '_'))

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file_name = file_path + "{}".format(title.lower().replace(' ', '_')) + ".pdf"
                fig.write_image(file_name)
                print('File, {}, has been created successfully'.format(file_name))

            # right to eps
            if file_type == "eps":
                if os.path.exists('{}{}'.format(file_path, title.lower().replace(' ', '_')) + ".eps"):
                    old_file_name = '{}{}.eps'.format(file_path, title.lower().replace(' ', '_'))
                    new_file_name = '{}old_{}.eps'.format(file_path, title.lower().replace(' ', '_'))

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file_name = file_path + "{}".format(title.lower().replace(' ', '_')) + ".eps"
                fig.write_image(file_name)
                print('File, {}, has been created successfully'.format(file_name))

            # right to jpeg
            if file_type == "webp":
                if os.path.exists('{}{}'.format(file_path, title.lower().replace(' ', '_')) + ".webp"):
                    old_file_name = '{}{}.webp'.format(file_path, title.lower().replace(' ', '_'))
                    new_file_name = '{}old_{}.webp'.format(file_path, title.lower().replace(' ', '_'))

                    os.rename(old_file_name, new_file_name)
                    print("File renamed!")

                file_name = file_path + "{}".format(title.lower().replace(' ', '_')) + ".webp"
                fig.write_image(file_name)
                print('File, {}, has been created successfully'.format(file_name))
            if show:
                fig.show()

        except Exception as e:
            print('Error: {}'.format(str(e)))


if __name__ == "__main__":

    plot = BarChart()

    tmdb = pd.read_csv("/Users/santanusarma/Dropbox/Jagriti/Programming/Data Analysis/data_integration_middleware/dataware/tests/test_result/tmdb_results.csv")
    # tmdb.sort_values(by="popularity", ascending=True, inplace=True)
    # print(tmdb[["popularity", "title"]])
    # print(tmdb.head(5))
    # x_pos = tmdb.columns.get_loc("title")
    # y_pos = tmdb.columns.get_loc("popularity")
    # print([x_pos, y_pos])

    # Basic bar chart
    plot.bar(tmdb, x='title', y='popularity', xcol_pos=tmdb.columns.get_loc("title"), ycol_pos=tmdb.columns.get_loc("popularity"),
              title="TMDB Movies Popularity",
              # update_title={'y': 0.94, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
              # trace_text=tmdb.popularity,
              # texttemplate='%{text:.2s}',
              # textposition="outside",
              # textfont=dict(family='Courier'),
              # marker=dict(color=colors, opacity=0.8),
              plot_bgcolor="rgba(0, 0, 0, 0)",
              # plot_bgcolor="whitesmoke",
              # paper_bgcolor="rgba(0, 0, 0, 0)",
              # fig_height=400,
              # update_yaxes=dict(ticksuffix="%", showgrid=True),
              # update_xaxes=dict(showgrid=True),
              update_trace_text=True,
              # fig_height=600,
              # sort_asc=True,
              # sort_desc=True,
              # N_largest=10,
              N_smallest=10,
              file_path="images/",
              # file_type="png",
              show=True)

    # Horizontal bar chart
    # plot.barh(tmdb, x='popularity', y='title', xcol_pos=tmdb.columns.get_loc("popularity"), ycol_pos=tmdb.columns.get_loc("title"),
    #           title="TMDB Movies Popularity",
    #           # update_title={'y': 0.94, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
    #           # trace_text=tmdb.popularity,
    #           # texttemplate='%{text:.2s}',
    #           # textposition="outside",
    #           # textfont=dict(family='Courier'),
    #           # marker=dict(color=colors, opacity=0.8),
    #           # plot_bgcolor="rgba(0, 0, 0, 0)",
    #           # paper_bgcolor="rgba(0, 0, 0, 0)",
    #           # update_xaxes=dict(ticksuffix="%"),
    #           update_trace_text=True,
    #           # fig_height=1200,
    #           # fig_width=1000,
    #           # sort_asc=True,
    #           # sort_desc=True,
    #           # N_largest=10,
    #           N_smallest=10,
    #           file_path="images/",
    #           # file_type="png",
    #           show=True)
