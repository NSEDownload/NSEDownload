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
Close 	1 Day Returns 	1 Week Returns 	2 Week Returns 	1 Month Returns 	2 Month Returns 	3 Month Returns 	6 Month Returns 	9 Month Returns 	1 Year Returns 	2 Year Returns
Date 											
2021-10-14 	18338.55 	0.0097 	0.0308 	0.0409 	0.0552 	0.1095 	0.1516 	0.2577 	0.2564 	0.5319 	0.6047
2021-10-13 	18161.75 	0.0094 	0.0292 	0.0254 	0.0465 	0.0988 	0.1456 	0.2521 	0.247 	0.5218 	0.6014
2021-10-12 	17991.95 	0.0026 	0.0095 	0.0137 	0.0359 	0.0995 	0.1378 	0.2404 	0.2354 	0.508 	0.5915
2021-10-11 	17945.95 	0.0028 	0.0144 	0.0051 	0.0332 	0.1022 	0.1436 	0.254 	0.239 	0.5063 	0.5874
2021-10-08 	17895.20 	0.0059 	0.0207 	0.0024 	0.0312 	0.102 	0.1406 	0.2063 	0.2473 	0.5121 	0.5818
... 	... 	... 	... 	... 	... 	... 	... 	... 	... 	... 	...
2016-12-19 	8104.35 	-0.0043 	- 	- 	- 	- 	- 	- 	- 	- 	-
2016-12-16 	8139.45 	-0.0017 	- 	- 	- 	- 	- 	- 	- 	- 	-
2016-12-15 	8153.60 	-0.0035 	- 	- 	- 	- 	- 	- 	- 	- 	-
2016-12-14 	8182.45 	-0.0048 	- 	- 	- 	- 	- 	- 	- 	- 	-
2016-12-13 	8221.80 	- 	- 	- 	- 	- 	- 	- 	- 	- 	-
```