import pandas as pd
import sys
import typing as T

if sys.version_info.micro >= 9:
    DictWithStrs = dict[str, str]
else:
    DictWithStrs = T.TypedDict[str, str]


# data = data.groupby(['type', 'status', 'name']).agg({
#     'one' : np.mean, 
#     'two' : lambda value: 100* ((value>32).sum() / reading.mean()), 
#     'test2': lambda value: 100* ((value > 45).sum() / value.mean())
# })

# df = pd.read_csv(
#     "my_file.csv", 
#     converters={'col1': func1, 'col2': func2},
#     dtype={'col1': int, 'col2': pd.StringDType()},
# )

DictWithStrs = T.TypedDict[str, str]

def foo(x: DictWithStrs):
    print("I am a foo")

wombat = foo

wombat({'a':'b'})

foo({1:2})


# "code-runner.executorMap": {
#     "python": "$pythonPath $fullFileName"
#   },