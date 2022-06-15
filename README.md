# hypr
Data Ingestion into Tableau Hyperfile

## Goal

The goal of this repo is the repo is to demonstrate how to leverage `python` and `tableau hyperfiles` for data processing, storage, and transport, while staying below available computing ressources.

## Setup

Follow the example from `./markdown/test.Rmd` and make sure to have `tidyverse` and `reticulate` packages installed.

## Examples

Activate Virtual Environment

```{r}
library(reticulate)

env <- "test-venv"

use_virtualenv(virtualenv = env, required = TRUE)

```

Read and process data & generate hyperfile

```{python}
import pandas as pd
import tableauhyperio as hio

# Read and process data
flights = pd.read_csv("../Data/flights.csv")

flights = flights[flights["dest"] == "ORD"]
flights = flights[['carrier', 'dep_delay', 'arr_delay']]
flights = flights.dropna()

# Output file name 
output_file = "../Dataout/flights_output.hyper"

# Writing a regular hyper file
hio.to_hyper(flights, output_file)

# Writing a regular hyper file
df = hio.read_hyper(output_file)

df.head()

```

Access Pandas data frame through R
```{r}
head(py$df)
```

---

*Disclaimer: The findings, interpretation, and conclusions expressed herein are those of the authors and do not necessarily reflect the views of United States Agency for International Development. All errors remain our own.*