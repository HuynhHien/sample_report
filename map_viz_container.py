map_con = st.container()

drop_cols = ['id', 'location', 'date', 'severity', 'borough', 'age', 'class', 'mode', 'ageBand', 'vehicles']
map_df = api_data_modified.drop(columns = drop_cols)

with map_con:
  st.header('A simple map of the accident zones in london')
  st.map(map_df, use_container_width =  True)