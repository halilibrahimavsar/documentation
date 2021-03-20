# PANDAS DOC

pandas' some subsection is Series and DataFrame.
Series is one dimensional and dataframe is two dimensional.
if we slice dataframe we obtain series, so this mean dataframe contains series.

differance between pd and np is Pandas can work with any type but numpy can not.
for an example;
You can give any python data type, csv, html, json... etc to the pandas. (take a look to pd.read_...)

```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

creating series :
```series = pd.Series(data)```

creating dataframe :
```df = pd.DataFrame(data)```


## INPUT AND OUTPUT

for reading data from any source look at ```pd.read_...```
and for save an data as an file look at ```pd.DataframeOrSeriesVeriable.to_....```

```
csv_path = "/home/mint/PycharmProjects/aiCodes/data/survey_results_public.csv"
df = pd.read_csv(csv_path, index_col="Respondent")  # we can read csv, xlsx xml... so on.
```
you can pass any column to the csv data as index which is in csv data with index_col parameter


## SERIES SECTION
waiting...


## DATAFRAME SECTION
```
def dataframe():
    print(df.head(6))  # firs six rows of data
    print(df.tail(6))  # last six rows of data
    print(df.shape)  # returning shape of dataframe or series
    print(df.info())  # brief info about dataframe's included type of columns
    print(df.index)  # return dataframe's indexes
    print(df.columns)  # return dataframe's columns
```

## DATA SELECTION

#### LOC ILOC
```
def loc_iloc():
    """
    if you wanna select rows you need use loc or iloc
    but if you wanna select columns you need use
    df["ColumnName"] or df.ColumnName (but the first way is better than second) 

    now lets talk a little bit about loc and iloc
    iloc is integerLocation, loc is Location.
    differance between them is loc accept string, iloc accept integer.

    so for an couple of example
    loc :
    df.loc[[ListOfRows], [ListOfColumns]] -> return given list of column and rows
    df.loc[FirstRows:LastRows, FirstColumns:LastColumns] -> return all of among the
    first and last given columns and rows.
    iloc is same as above but differance is, lets say again, loc accept string, iloc accept integer
    """
```

#### CONDDITIONAL SELECTION
```
def condition_selection():
    """
    Another info about selection data in dataframe is we can use conditional operations in loc.
    simple example about condition ;

    return all of even number in range of zero to ten
    """
    print(df.iloc[[i for i in range(10) if i % 2 == 0], [2, 3]])
```



## ANY OTHER SUBSECTIONS
```
def trying():
    # setting column as an index. to do so (also an another way to do so is pass an argument. see line 28)
    changed_index_in_df = df.set_index("Hobbyist", inplace=True)
    # but this is just silly sample that we did.
    # Because of index mean is normally need to be unique values but in hobbyist data just Yes or No is available...
    print("Changed index in df  : ")
    print(changed_index_in_df)
    # by the way  the inplace=True argument is using for change the actual dataframe object
    # You can use this argument almost in every functions

    print(df.loc[["Yes"], ["MainBranch", "Age", "Country"]])

    print("Reset index :")
    df.reset_index(inplace=True)
    print(df)
```






