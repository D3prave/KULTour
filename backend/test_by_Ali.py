import os
import pandas as pd
from ydata_profiling import ProfileReport
from IPython.display import IFrame
from IPython.core.display import display_html


data = pd.read_csv("prepared_data.csv")

columns = [""]

print(data)
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