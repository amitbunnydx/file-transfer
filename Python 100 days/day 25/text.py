
import pandas as pd

s = pd.Series(['Hello', 'World', 'PYTHON'])
s = s.str.lower()

print(s)