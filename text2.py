import pandas as pd
hollys_tbl = pd.DataFrame(fesult, columns = ('store', 'sido-gu', 'address', 'phone'))
hollys_tbl.to_csv("./6장_data/hollys.csv", encoding = "cp949", mode = "w", index = True)
