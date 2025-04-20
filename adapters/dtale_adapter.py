# adapters/dtale_adapter.py

from ports.dtale_port import DtalePort
import dtale
import pandas as pd

class DtaleAdapter(DtalePort):
    def open_in_dtale(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Launch Dtale at a specific host & port in a CLI scenario.
        
        - host="localhost": ensures we bind to localhost
        - port=40000: forces Dtale to run on port 40000 (change if needed)
        - open_browser=False: doesn't auto-launch a browser tab
        - subprocess=False: keep process inline

        Returning the same df for simplicity. 
        In practice, you'd use dtale APIs to retrieve the updated dataset.
        """
        d = dtale.show(
            df, 
            subprocess=False, 
            host="localhost", 
            port=40000, 
            open_browser=False
        )

        # Print out the local Dtale URL so user can open it manually
        print(f"Dtale is running at {d._main_url}")
        print("Open the above URL in your browser to explore or edit the data.")
        print("Returning the original DataFrame (no changes in this example).")

        # In a real-world scenario, you might fetch updates from Dtale
        # or call `d.data` after editing. For now, we just return the original df.
        return df
