import pandas as pd

dataset = {
    'cars':["volvo", "honda", "corolla"],
    'code':[5, 2, 8]
}

result = pd.DataFrame(dataset)

print(result)