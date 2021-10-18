---
layout: default
title: Returns
parent: Usage
nav_order: 3
---

# **Returns**
{: .no_toc }

Trailing returns over various periods ranging from days to years can be generated for stocks and indices using closing price.


### **Using start and end date** 
Here the date is specified in 'dd-mm-yyyy' format

```
from NSEDownload import returns
x = returns.calculate_returns(df, make_csv = True, name = "Returns")
```

```

```