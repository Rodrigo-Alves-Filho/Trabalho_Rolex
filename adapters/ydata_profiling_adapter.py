# adapters/ydata_profiling_adapter.py
from ydata_profiling import ProfileReport
from ports.profiling_port import ProfilingPort
import pandas as pd

class YDataProfilingAdapter(ProfilingPort):
    def generate_report(self, df: pd.DataFrame) -> None:
        profile = ProfileReport(df, title="Data Profiling Report", explorative=True)
        profile.to_file("profile_report.html")
        print("Report generated: profile_report.html")
