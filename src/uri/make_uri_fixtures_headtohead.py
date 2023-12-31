# MODULE IMPORT
import sys
from datetime import datetime, timedelta
sys.path.append('/Users/kimdohoon/git/football-data-pipeline/lib')
import football_lib as lib

# READ *
params_before = lib.read_Params("*", "pipe_round")

uri_list = []
for count in range(len(params_before)):
    # PARAMS : h2h, date, timezone
    params = {
        "h2h" : f"{params_before[count][3]}-{params_before[count][4]}",
        "date" : params_before[count][2][:params_before[count][2].index('T')],
        "timezone" : "Europe/London"
    }
    # MAKE URI
    uri = lib.make_uri("fixtures/headtohead", params)
    uri_list.append(uri)

# TEST
if __name__ == "__main__":
    print(params_before)
    print(uri_list[:5])