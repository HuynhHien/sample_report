@st.cache
def get_data():
  api = r.get('https://api.tfl.gov.uk/AccidentStats/2019')
  api_status_code = api.status_code

  api_data = api.json()
  api_data_normal = pd.json_normalize(api_data)
  cols = api_data_normal.columns
  return api_data_normal