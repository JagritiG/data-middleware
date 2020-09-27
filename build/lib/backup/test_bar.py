

#
#     plot = BarChart()
#
#     tmdb = pd.read_csv("tmdb_results.csv")
    # tmdb.sort_values(by="popularity", ascending=True, inplace=True)
    # print(tmdb[["popularity", "title"]])
    # print(tmdb.head(5))
    # x_pos = tmdb.columns.get_loc("title")
    # y_pos = tmdb.columns.get_loc("popularity")
    # print([x_pos, y_pos])

    # Basic bar chart
    # plot.bar(tmdb, x='title', y='popularity', xcol_pos=tmdb.columns.get_loc("title"), ycol_pos=tmdb.columns.get_loc("popularity"),
    #           title="TMDB Movies Popularity",
    #           # update_title={'y': 0.94, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
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
    #           # set_col_color="Ava",
    #           # fig_height=600,
    #           # sort_asc=True,
    #           # sort_desc=True,
    #           # N_largest=10,
    #           # N_smallest=10,
    #           file_path="image/",
    #           # file_type="png",
    #           show=True)

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
    #           set_col_color="Ava",
    #           # fig_height=1200,
    #           # fig_width=1000,
    #           # sort_asc=True,
    #           # sort_desc=True,
    #           # N_largest=10,
    #           # N_smallest=10,
    #           file_path="image/",
    #           # file_type="png",
    #           show=True)
