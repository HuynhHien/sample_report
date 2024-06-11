severity_viz = st.container()

with severity_viz:
  st.header('Severity wise AccidentStats')
  st.text('A pie chart depicting the count of accident severity')

  severity_plot = px.pie(api_data_modified, values='id', names='severity')
  st.plotly_chart(severity_plot)