import requests as r

def get_data(url):
  api = r.get(url)
  api_status_code = api.status_code #200

  api_data = api.json() #converting into json format
  api_data_normal = pd.json_normalize(api_data) #converting into dataframe
  
  return api_data_normal

get_data('https://api.tfl.gov.uk/AccidentStats/2019')