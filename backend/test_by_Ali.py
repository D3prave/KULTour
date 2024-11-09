import os
import pandas as pd
from ydata_profiling import ProfileReport
from IPython.display import IFrame
from IPython.core.display import display_html


#data = pd.read_csv("backend/original_data.csv", encoding='utf-16',low_memory=False)
data = pd.read_csv('original_data.csv', encoding='UTF-16')
columns_to_keep = ['eventName (actionDetails 1)', 'visitorType', 'visitCount', 'continent', 'country', 'visitorId']

data = data.loc[:, columns_to_keep]
print(data)

new_user_id = "asjfasjdkaskd"
user_country = "Belgien"

if "dcdde833cca8be02" in data["visitorId"].values:
    if user_country is None:
        raise ValueError("User has no country value.")

    print(data[data['country'].values == user_country])
    most_popular_event = (data[data['country'] == user_country]
                          .groupby('eventName (actionDetails 1)')['visitorId']
                          .count()
                          .idxmax())
    
    print(most_popular_event)
else:
    print("no")

#
#profile = ProfileReport(data, title="Profiling Report")
#
#report_file = 'general_report.html'
#dump_file_name = "general_report.pp"
#
#if not os.path.exists(report_file):
#    profile = ProfileReport(data, title = 'Mastercard Data - Report')
#
#    profile.to_file(report_file)
#    profile.dump(dump_file_name)
#
#profile = ProfileReport().load(dump_file_name)
#profile.to_notebook_iframe()