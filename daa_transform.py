api_data_normal = get_data()

api_casualities = pd.json_normalize(api_data_normal['casualties'])
api_casualities_col  = pd.json_normalize(api_casualities[0])
#api_casualities_col['$type'][0]
api_casualities_col = api_casualities_col.drop(columns = '$type')
casuality_cols = api_casualities_col.columns
age = pd.Series(api_casualities_col['age'], name = 'age')
casualities_class = pd.Series(api_casualities_col['class'], name = 'class')
severity = pd.Series(api_casualities_col['severity'], name = 'severity')
mode = pd.Series(api_casualities_col['mode'], name = 'mode')
ageBand = pd.Series(api_casualities_col['ageBand'], name = 'ageBand')

api_vehicles = pd.json_normalize(api_data_normal['vehicles'])
api_vehicles_col = pd.json_normalize(api_vehicles[0])
api_vehicles_col = pd.Series(api_vehicles_col['type'], name = 'vehicles')

api_data_normal = api_data_normal.drop(columns = ['$type','casualties', 'vehicles'])
api_data_modified = pd.concat([api_data_normal,age, casualities_class, mode, ageBand, api_vehicles_col], axis=1)


class_dict = dict(api_data_modified['class'].value_counts())
class_df = pd.DataFrame(class_dict.items(), columns = ['class', 'count'])

mode_dict = dict(api_data_modified['mode'].value_counts())
mode_df = pd.DataFrame(mode_dict.items(), columns = ['mode', 'count'])

age_dict = dict(api_data_modified['age'].value_counts())
age_df = pd.DataFrame(age_dict.items(), columns = ['age', 'count'])

drop_cols = ['id', 'location', 'date', 'severity', 'borough', 'age', 'class', 'mode', 'ageBand', 'vehicles']
map_df = api_data_modified.drop(columns = drop_cols)