# Plotly express works with column-oriented, matrix or geographical data
# Plotly express works with long-, wide-, and mixed form data

# Functions like- px.bar, px.scatter expect to operate on column-oriented data
# of the type stored in a Pandas DataFrame (long- or wide- format).
# px.imshow operates on matrix-like data stored in a numpy or xarray array.
# px.imshow operates only on wide-form input
# px.choropleth_mapbox can operate on geographic data stored in a GeoPandas GeoDataFrame.

# Every Plotly Express function can operate on long-form (tidy data) data (other than px.imshow which operates
# only on wide-form input), and in addition, the following 2D-Cartesian functions can operate on
# wide-form and mixed-form data: px.scatter, px.line, px.area, px.bar, px.histogram, px.violin,
# px.box, px.strip, px.funnel, px.density_heatmap and px.density_contour.

# long-form data has one row per observation, and one column per variable.
# This is suitable for storing and displaying multivariate data i.e. with dimension greater than 2.
# This format is sometimes called "tidy".

# wide-form data has one row per value of one of the first variable, and one column per value of the second variable.
# This is suitable for storing and displaying 2-dimensional data.

# mixed-form data is a hybrid of long-form and wide-form data, with one row per value of one variable,
# and some columns representing values of another, and some columns representing more variables.
# ------------------------------------------------------------------------------------------------------------------
# Dependency: orca


import plotly.express as px
import pandas as pd
import numpy as np
import os
from varname import nameof


class Plot:
    """Class Plot for producing bar plot,
    horizontal bar plot, grouped bar plot, stacked barplot, scatter plot, histograms,
    ...
    """
    def __init__(self):
        self.df = None

    def bar(self, df=None, x=None, y=None, color=None, title=None, labels={}, update_title={}, update_xaxes={}, update_yaxes={},
            xtickangle=None, ytickangle=None, xtickformat=None, ytickformat=None, update_legend={}, update_font={}, hover_name=None,
            hover_data=None, barmode="relative", bargap=0.15, bargroupgap=0.1, color_discrete_sequence=None, fig_width=None, fig_height=None,
            color_continuous_scale=None, plot_bgcolor=None, paper_bgcolor=None, uniformtext_minsize=8, uniformtext_mode="hide",
            marker={}, selector={}, trace_name=None, update_trace_text=False, trace_text=None, texttemplate='%{text:.2s}', textangle=None, textposition="outside",
            textfont={}, bar_width=None, hoverinfo=None, hoverlabel=None, hovertemplate=None, hovertext=None,
            file_path=None, file_type=None, show=True):
        """
        Generate basic bar plot.
        :param df: (DataFrame or array-like or dict) – This argument needs to be passed for column names (and not keyword names) to be used.
                    Array-like and dict are transformed internally to a pandas DataFrame.
                    Optional: if missing, a DataFrame gets constructed under the hood using the other arguments.
        :param x: (str or int or Series or array-like) – Either a name of a column in data_frame, or a pandas Series or array_like object.
                    Values from this column or array_like are used to position marks along the x axis in cartesian coordinates.
                    Either x or y can optionally be a list of column references or array_likes, in which case the data will be treated
                    as if it were ‘wide’ rather than ‘long’.
        :param y: (str or int or Series or array-like) – Either a name of a column in data_frame, or a pandas Series or array_like object.
                    Values from this column or array_like are used to position marks along the y axis in cartesian coordinates.
                    Either x or y can optionally be a list of column references or array_likes, in which case the data will be treated
                    as if it were ‘wide’ rather than ‘long’.
        :param color: (str or int or Series or array-like) – Either a name of a column in data_frame, or a pandas Series or array_like object.
                    Values from this column or array_like are used to assign color to marks.
        :param labels: (dict with str keys and str values (default {})) – By default, column names are used in the figure for axis titles,
                    legend entries and hovers. This parameter allows this to be overridden. The keys of this dict should correspond to
                    column names, and the values should correspond to the desired label to be displayed.
        :param xtickangle: (int) tick angle
        :param ytickangle: (int) tick angle
        :param title: (str) – The figure title.
        :param update_title: {} - Update title, dict()
        :param update_xaxes: {} - Update xaxes, dict()
        :param update_yaxes: {} - Update yaxes, dict()
        :param xtickformat: (str) - formatting xaxes ticks (e.g., date formatting)
        :param ytickformat: (str) - formatting yaxes ticks (e.g., "$" for dollar, "%" for percentage)
        :param update_legend: {} - Update legend, dict()
        :param update_font: {} - Update font, {}
        :param file_path: (str) - The path of the saved figure.
        :param file_type: (str) - The type of the file format ("png","jpeg","webp", "svg", "pdf", or "eps").
        :param show: (Bool) - If True, show current figures, else does not show (default True).
        :param barmode: (str (default 'relative')) – One of 'group', 'overlay' or 'relative' In 'relative' mode,
                    bars are stacked above zero for positive values and below zero for negative values.
                    In 'overlay' mode, bars are drawn on top of one another.
                    In 'group' mode, bars are placed beside each other.
        :param bargap: (float) - gap between bars of adjacent location coordinates.
        :param bargroupgap: (float) - gap between bars of the same location coordinate.
        :param uniformtext_minsize: (int) - If you want all the text labels to have the same size, you can use the uniformtext layout
                    parameter. The minsize attribute sets the font size.
        :param uniformtext_mode: (str) - the mode attribute sets what happens for labels which cannot fit with the desired fontsize:
                    either hide them or show them with overflow.
        :param hover_name: (str or int or Series or array-like) – Either a name of a column in data_frame,
                    or a pandas Series or array_like object. Values from this column or array_like appear in bold in the hover tooltip.
        :param hover_data: (list of str or int, or Series or array-like, or dict) – Either a list of names of columns in data_frame,
                    or pandas Series, or array_like objects or a dict with column names as keys, with values True (for default formatting)
                    False (in order to remove this column from hover information), or a formatting string,
                    for example ‘:.3f’ or ‘|%a’ or list-like data to appear in the hover tooltip or tuples with a bool or formatting string
                    as first element, and list-like data to appear in hover as second element Values from these columns appear
                    as extra data in the hover tooltip.
        :param color_discrete_sequence: (list of str) – Strings should define valid CSS-colors. When color is set and the values
                    in the corresponding column are not numeric, values in that column are assigned colors by cycling through
                    color_discrete_sequence in the order described in category_orders, unless the value of color is a key in
                    color_discrete_map. Various useful color sequences are available in the plotly.express.colors submodules,
                    specifically plotly.express.colors.qualitative.
        :param color_continuous_scale: (list of str) – Strings should define valid CSS-colors This list is used to build a
                    continuous color scale when the column denoted by color contains numeric data. Various useful color scales are
                    available in the plotly.express.colors submodules, specifically plotly.express.colors.sequential,
                    plotly.express.colors.diverging and plotly.express.colors.cyclical.
        :param plot_bgcolor: (str) - plot background color
        :param paper_bgcolor: (str) - paper background color
        :param marker_colors: (List of str) - individual bar color
        :param update_trace: {} - update trace (bar- text, text position, color etc.)
        """

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

            if update_trace_text:
                if trace_text is None:
                    fig.update_traces(
                        text=y,
                        texttemplate=texttemplate,
                        textangle=textangle,
                        textposition=textposition,
                        textfont=textfont)
                elif trace_text is not None:
                    text = trace_text
                    fig.update_traces(
                        text=text,
                        texttemplate=texttemplate,
                        textangle=textangle,
                        textposition=textposition,
                        textfont=textfont)
                else:
                    fig.update_traces(
                        text=None,
                        texttemplate=None,
                        textangle=None,
                        textposition=None,
                        textfont=None)
            
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

    def barh(self, df=None, x=None, y=None, color=None, title=None, labels={}, update_title={}, update_xaxes={}, update_yaxes={},
            xtickangle=None, ytickangle=None, xtickformat=None, ytickformat=None, orientation='h', legend=False, update_legend={},
            update_font={}, hover_name=None, hover_data=None, barmode="relative", bargap=0.15, bargroupgap=0.1, color_discrete_sequence=None,
            fig_width=None, fig_height=None, color_continuous_scale=None, plot_bgcolor=None, paper_bgcolor=None, uniformtext_minsize=8,
            uniformtext_mode="hide", marker={}, selector={}, trace_name=None, update_trace_text=False, trace_text=None, texttemplate='%{text:.2s}',
            textangle=None, textposition="outside", textfont={}, bar_width=None, hoverinfo=None, hoverlabel=None, hovertemplate=None,
            hovertext=None, file_path=None, file_type=None, show=True):
        """
        Generate horizontal bar plot.
        :param df: (DataFrame or array-like or dict) – This argument needs to be passed for column names (and not keyword names) to be used.
                    Array-like and dict are transformed internally to a pandas DataFrame.
                    Optional: if missing, a DataFrame gets constructed under the hood using the other arguments.
        :param x: (str or int or Series or array-like) – Either a name of a column in data_frame, or a pandas Series or array_like object.
                    Values from this column or array_like are used to position marks along the x axis in cartesian coordinates.
                    Either x or y can optionally be a list of column references or array_likes, in which case the data will be treated
                    as if it were ‘wide’ rather than ‘long’.
        :param y: (str or int or Series or array-like) – Either a name of a column in data_frame, or a pandas Series or array_like object.
                    Values from this column or array_like are used to position marks along the y axis in cartesian coordinates.
                    Either x or y can optionally be a list of column references or array_likes, in which case the data will be treated
                    as if it were ‘wide’ rather than ‘long’.
        :param color: (str or int or Series or array-like) – Either a name of a column in data_frame, or a pandas Series or array_like object.
                    Values from this column or array_like are used to assign color to marks.
        :param labels: (dict with str keys and str values (default {})) – By default, column names are used in the figure for axis titles,
                    legend entries and hovers. This parameter allows this to be overridden. The keys of this dict should correspond to
                    column names, and the values should correspond to the desired label to be displayed.
        :param xtickangle: (int) tick angle
        :param ytickangle: (int) tick angle
        :param title: (str) – The figure title.
        :param update_title: {} - Update title, dict()
        :param update_xaxes: {} - Update xaxes, dict()
        :param update_yaxes: {} - Update yaxes, dict()
        :param xtickformat: (str) - formatting xaxes ticks (e.g., date formatting)
        :param ytickformat: (str) - formatting yaxes ticks (e.g., "$" for dollar, "%" for percentage)
        :param update_legend: {} - Update legend, dict()
        :param update_font: {} - Update font, {}
        :param file_path: (str) - The path of the saved figure.
        :param file_type: (str) - The type of the file format ("png","jpeg","webp", "svg", "pdf", or "eps").
        :param show: (Bool) - If True, show current figures, else does not show (default True).
        :param barmode: (str (default 'relative')) – One of 'group', 'overlay' or 'relative' In 'relative' mode,
                    bars are stacked above zero for positive values and below zero for negative values.
                    In 'overlay' mode, bars are drawn on top of one another.
                    In 'group' mode, bars are placed beside each other.
        :param bargap: (float) - gap between bars of adjacent location coordinates.
        :param bargroupgap: (float) - gap between bars of the same location coordinate.
        :param uniformtext_minsize: (int) - If you want all the text labels to have the same size, you can use the uniformtext layout
                    parameter. The minsize attribute sets the font size.
        :param uniformtext_mode: (str) - the mode attribute sets what happens for labels which cannot fit with the desired fontsize:
                    either hide them or show them with overflow.
        :param hover_name: (str or int or Series or array-like) – Either a name of a column in data_frame,
                    or a pandas Series or array_like object. Values from this column or array_like appear in bold in the hover tooltip.
        :param hover_data: (list of str or int, or Series or array-like, or dict) – Either a list of names of columns in data_frame,
                    or pandas Series, or array_like objects or a dict with column names as keys, with values True (for default formatting)
                    False (in order to remove this column from hover information), or a formatting string,
                    for example ‘:.3f’ or ‘|%a’ or list-like data to appear in the hover tooltip or tuples with a bool or formatting string
                    as first element, and list-like data to appear in hover as second element Values from these columns appear
                    as extra data in the hover tooltip.
        :param color_discrete_sequence: (list of str) – Strings should define valid CSS-colors. When color is set and the values
                    in the corresponding column are not numeric, values in that column are assigned colors by cycling through
                    color_discrete_sequence in the order described in category_orders, unless the value of color is a key in
                    color_discrete_map. Various useful color sequences are available in the plotly.express.colors submodules,
                    specifically plotly.express.colors.qualitative.
        :param color_continuous_scale: (list of str) – Strings should define valid CSS-colors This list is used to build a
                    continuous color scale when the column denoted by color contains numeric data. Various useful color scales are
                    available in the plotly.express.colors submodules, specifically plotly.express.colors.sequential,
                    plotly.express.colors.diverging and plotly.express.colors.cyclical.
        :param plot_bgcolor: (str) - plot background color
        :param paper_bgcolor: (str) - paper background color
        :param marker_colors: (List of str) - individual bar color
        :param update_trace: {} - update trace (bar- text, text position, color etc.)
        """

        try:

            # print(df.head(5))
            # # xaxis_title = "{}".format(nameof(x))
            # # yaxis_title = "{}".format(nameof(y))
            # original_x = x
            # df["sort_var"] = x
            # df.sort_values(x, ascending=True, inplace=True)
            # x = original_x
            # print([x, y])
            # print(tmdb[["popularity", "title"]])
            # print(df.head(5))
            fig = px.bar(df, x, y, color=color, labels=labels, title=title, orientation='h', hover_data=hover_data, hover_name=hover_name,
                         color_discrete_sequence=color_discrete_sequence, color_continuous_scale=color_continuous_scale)

            fig.update_layout(
                xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False))

            # fig.update_layout(
            #     xaxis_title=dict(text=xaxis_title),
            #     yaxis_title=dict(text=yaxis_title))

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
            print(y)
            if update_trace_text:
                if trace_text is None:
                    fig.update_traces(
                        text=x,
                        texttemplate=texttemplate,
                        textposition=textposition)
                elif trace_text is not None:
                    text = trace_text
                    fig.update_traces(
                        text=text,
                        texttemplate=texttemplate,
                        textangle=textangle,
                        textposition=textposition,
                        textfont=textfont)
                else:
                    fig.update_traces(
                        text=None,
                        texttemplate=None,
                        textangle=None,
                        textposition=None,
                        textfont=None)

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

    plot = Plot()

    # case-1: Long-form data
    # long_df = pd.read_csv("tips.csv")
    # print(long_df.head(3))
    # plot.bar(long_df, x="sex", y="total_bill", color="smoker", title="Total Bill by Sex", file_path="images/", file_type="webp", show=True)

    # case-2: Wide-form data
    # wide_df = pd.read_csv("billboard.csv")
    # print(wide_df.head(3))
    # plot.bar(wide_df, x="artist", y=["wk1", "wk2", "wk3"], title="Artist By Weeks", labels={"value": "count", "variable": "weeks"}, file_path="images/", file_type="png", show=True)

    # case-3: Input Data as Pandas DataFrames
    # Arguments can either be passed as dataframe columns, or as column names if the data_frame argument is provided

    # case-3a: Passing columns as arguments
    # tips_df = pd.read_csv("tips.csv")
    # print(tips_df.head(3))
    # plot.bar(tips_df, x=tips_df.sex, y=tips_df.total_bill, color=tips_df.smoker,
    #               title="Total Bill by Sex", file_path="images/", file_type="png", show=True)

    # col_names = ['Sepal_length', 'Sepal_width', 'Petal_length', 'Petal_width', 'Species']
    # iris_df = pd.read_csv('iris.csv', names=col_names)
    # print(iris_df.head(3))

    # case-3b: Passing name strings as arguments
    # tips_df = pd.read_csv("tips.csv")
    # print(tips_df.head(3))
    # plot.bar(tips_df, x="time", y="size", color="sex",
    #               title="Total Bill by Sex",
    #               # plot_bgcolor="rgba(0, 0, 0, 0)",
    #               plot_bgcolor="whitesmoke",
    #               paper_bgcolor="rgba(0, 0, 0, 0)",
    #               file_path="images/", file_type="png", show=True)

    # case-4: Using the index of a DataFrame
    # In addition to columns, it is also possible to pass the index of a DataFrame as argument.
    # In the example below the index is displayed in the hover data.
    # tips_df = pd.read_csv("tips.csv")
    # print(tips_df.head(3))
    # plot.bar(tips_df, x=tips_df.sex, y=tips_df.total_bill, hover_data=[tips_df.index],
    #          title="Total Bill by Sex", color_continuous_scale='Bluered_b', file_path="images/", file_type="png", show=True)

    # case-5: Columns not in the data_frame argument
    # In the addition to columns from the data_frame argument, one may also pass columns from a different DataFrame,
    # as long as all columns have the same length. It is also possible to pass columns without passing the data_frame argument.
    # However, column names are used only if they correspond to columns in the data_frame argument,
    # in other cases, the name of the keyword argument is used. As explained below, the labels argument can be used to set names.

    # df1 = pd.DataFrame(dict(time=[10, 20, 30], sales=[10, 8, 30]))
    # print(df1)
    # df2 = pd.DataFrame(dict(market=[4, 2, 5]))
    # print(df2)
    # plot.bar(df1, x=df1.time, y=df2.market, color=df1.sales, labels={'y': 'market'},
    #               title="Market vs Time", file_path="images/", file_type="png", show=True)

    # case-6: Input Data as array-like columns: NumPy arrays, lists...
    # px arguments can also be array-like objects such as lists, NumPy arrays,
    # in both long-form or wide-form (for certain functions).

    # case-6a-1: List arguments for bar()
    # organization = ['Microsoft', 'Apple Inc.', 'Alphabet', 'Intel', 'Nvidia']
    # market_cap = [334.39, 619.76, 432.15, 132.06, 11.69]
    # market_cap.sort(reverse=True)
    # colors = ['lightgreen', ] * len(organization)
    # # for i in range(len(organization)):
    # #     if organization[i] == "Apple Inc.":
    # #         colors[i] = 'crimson'
    # for i in range(len(market_cap)):
    #     if market_cap[i] == min(market_cap):
    #         colors[i] = 'crimson'
    # plot.bar(x=organization, y=market_cap, labels={'x': 'Organizations', 'y': 'Market Cap (Billions of US $)'},
    #          title="Market Capitalization", color_discrete_sequence=["seagreen"],
    #          update_title={'y': 0.94, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
    #          update_legend=dict(x=0, y=1, title=dict(text="Legend"), orientation="h", traceorder="reversed", title_font_family="Times New Roman",
    #                             font=dict(family="Courier", size=12, color="black")),
    #          # trace_text=market_cap,
    #          # texttemplate='%{text:.2s}',
    #          # textposition="inside",
    #          # textfont=dict(family='Courier'),
    #          # bar_width=.8,
    #          # marker=dict(color=colors, opacity=0.8),
    #          # plot_bgcolor="rgba(0, 0, 0, 0)",
    #          # paper_bgcolor="rgba(0, 0, 0, 0)",
    #          # fig_height=400,
    #          update_xaxes=dict(showline=True, linewidth=1, linecolor='blue', mirror=True, showgrid=False),
    #          update_yaxes=dict(tickprefix="$", ticksuffix="B", showline=True, linewidth=1, linecolor='blue', mirror=True, showgrid=False),
    #          update_trace_text=True,
    #          # sort=True,
    #          # reverse=True,
    #          file_path="images/", file_type="png", show=True)

    # case-6a-2: List arguments for barh() -  horaizontal bar
    # organization = ['Microsoft', 'Apple Inc.', 'Alphabet', 'Intel', 'Nvidia']
    # market_cap = [334.39, 619.76, 432.15, 132.06, 11.69]
    # market_cap.sort(reverse=True)
    # colors = ['green', ] * len(organization)
    # # for i in range(len(organization)):
    # #     if organization[i] == "Apple Inc.":
    # #         colors[i] = 'crimson'
    # for i in range(len(market_cap)):
    #     if market_cap[i] == min(market_cap):
    #         colors[i] = 'crimson'
    # plot.barh(x=market_cap, y=organization,
    #           title="Market Capitalization", color_discrete_sequence=["rgb(50, 171, 96)"],
    #           update_title={'y': 0.94, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
    #           update_legend=dict(x=0, y=1, title=dict(text="Legend"), orientation="h", traceorder="reversed", title_font_family="Times New Roman",
    #                              font=dict(family="Courier", size=16, color="black")),
    #           # trace_text=market_cap,
    #           # texttemplate='%{text:.2s}',
    #           # textposition="inside",
    #           # textfont=dict(family='Courier'),
    #           # marker=dict(color=colors, opacity=0.8),
    #           # plot_bgcolor="rgba(0, 0, 0, 0)",
    #           # paper_bgcolor="rgba(0, 0, 0, 0)",
    #           # fig_height=400,
    #           # update_yaxes=dict(showline=False, linewidth=1, linecolor='blue', mirror=True, showgrid=False),
    #           # update_xaxes=dict(tickprefix="$", ticksuffix="B", showline=False, linewidth=1, linecolor='blue', mirror=True, showgrid=False),
    #           file_path="images/", file_type="png", show=True)

    # case-6b: NumPy arrays arguments
    # time = np.array([10, 20, 30])
    # sales = np.array([10, 8, 30])
    # market = np.array([4, 2, 5])
    # plot.bar(x=time, y=market, color=sales, labels={'x': 'time', 'y': 'market'}, title="Market vs Time", file_path="images/", file_type="png", show=True)

    # =====================================================================
    # case-6c: List arguments in wide form
    # List arguments can also be passed in as a list of lists, which triggers wide-form data processing,
    # with the downside that the resulting traces will need to be manually renamed via fig.data[<n>].name = "name".

    # series1 = [3, 5, 4, 8]
    # series2 = [5, 4, 8, 3]
    # plot.line(x=[1, 2, 3, 4], y=[series1, series2])

    # case-7: Passing dictionaries or array-likes as the data_frame argument
    # The column-based argument data_frame can also be passed with a dict or array.
    # Using a dictionary can be a convenient way to pass column names used in axis titles,
    # legend entries and hovers without creating a pandas DataFrame.

    # N = 10000
    # np.random.seed(0)
    # plot.density_contour(dict(effect_size=5 + np.random.randn(N),
    #                           waiting_time=np.random.poisson(size=N)),
    #                      x="effect_size", y="waiting_time")

    # case-8: Integer column names
    # When the data_frame argument is a NumPy array, column names are integer corresponding
    # to the columns of the array. In this case, keyword names are used in axis, legend and hovers.
    # This is also the case for a pandas DataFrame with integer column names.
    # Use the labels argument to override these names.
    # ar = np.arange(100).reshape((10, 10))
    # plot.scatter(ar, x=2, y=6, size=1, color=5)
    # =====================================================================

    # case-9: Mixing dataframes and other types
    # It is possible to mix DataFrame columns, NumPy arrays and lists as arguments.
    # Remember that the only column names to be used correspond to columns in the data_frame argument,
    # use labels to override names displayed in axis titles, legend entries or hovers.

    # df = px.data.gapminder()
    # gdp = np.log(df['pop'] * df['gdpPercap'])  # NumPy array
    # plot.bar(df, x='year', y=gdp, color='continent', labels={'y': 'log gdp'},
    #          update_legend=dict(x=1, y=1, title=dict(text="Continent", font=dict(size=20, color="red")),
    #                             traceorder="reversed", title_font_family="Times New Roman",
    #                             font=dict(family="Times New Roman", size=18, color="blue")),
    #          barmode="group", hover_data=['country'], trace_name="Asia",
    #          title='Evolution of world GDP', file_path="images/", file_type="png", show=True)
# ==============================================================================================

    # tmdb data
    tmdb = pd.read_csv("/Users/santanusarma/Dropbox/Jagriti/Programming/Data Analysis/data_integration_middleware/dataware/tests/test_result/tmdb_results.csv")
    # tmdb.sort_values(by="popularity", ascending=True, inplace=True)
    # print(tmdb[["popularity", "title"]])
    # print(tmdb.head(5))
    plot.barh(tmdb, x=tmdb.popularity, y=tmdb.title, title="TMDB Movies Popularity",
              update_title={'y': 0.94, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
              # trace_text=tmdb.popularity,
              # texttemplate='%{text:.2s}',
              # textposition="outside",
              # textfont=dict(family='Courier'),
              # marker=dict(color=colors, opacity=0.8),
              plot_bgcolor="rgba(0, 0, 0, 0)",
              paper_bgcolor="rgba(0, 0, 0, 0)",
              # fig_height=400,
              update_xaxes=dict(ticksuffix="%"),
              update_trace_text=True,
              # sort=True,
              # reverse=False,
              file_path="images/", file_type="png", show=True)

    # plot.bar(tmdb, x=tmdb.title, y=tmdb.popularity, title="TMDB Movies Popularity",
    #           update_title={'y': 0.94, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
    #           # trace_text=tmdb.popularity,
    #           # texttemplate='%{text:.2s}',
    #           # textposition="outside",
    #           # textfont=dict(family='Courier'),
    #           # marker=dict(color=colors, opacity=0.8),
    #           plot_bgcolor="rgba(0, 0, 0, 0)",
    #           # plot_bgcolor="whitesmoke",
    #           # paper_bgcolor="rgba(0, 0, 0, 0)",
    #           # fig_height=400,
    #           # update_yaxes=dict(ticksuffix="%", showgrid=True),
    #           # update_xaxes=dict(showgrid=True),
    #           update_trace_text=True,
    #           fig_height=800,
    #           file_path="images/", file_type="png", show=True)

