# Create hierarchies of clusters
import plotly.figure_factory as ff

fig = ff.create_dendrogram(df, labels=['The Guardian', 'WSJ', 'NYT', 'The Washington Post',   'The Times of India', 'SMH', 'The Asahi Shimbun', 'Dawn', 'Zaman'])
fig.update_layout(width=800, height=500)
fig.show()