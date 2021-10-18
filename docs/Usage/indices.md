---
layout: default
title: Indices
parent: Usage
nav_order: 2
---

# **Indices**
{: .no_toc }

Check out Installation first.  
Indices can be of historical type or total return index. By default, the index is assumed as historical.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## **Downloading Data**
{:toc}
You can specify the date range either using start and end date or using the full_data. 

### **Using start and end date** 
Here the date is specified in 'dd-mm-yyyy' format

```
from NSEDownload import indices
df = indices.get_data(indexName = "NIFTY Shariah 25",start_date="09-01-2017",end_date="14-08-2019")
```
Output Dataframe :
```
           Open High Low    Close    Shares Traded Turnover (Rs. Cr)   
Date                                                                   
2017-01-09    -    -   -  3281.54                -                 -   
2017-01-10    -    -   -  3295.08                -                 -   
2017-01-11    -    -   -  3327.22                -                 -   
2017-01-12    -    -   -  3323.66                -                 -   
2017-01-13    -    -   -  3306.55                -                 -   
...         ...  ...  ..      ...              ...               ... ..
2018-01-02    -    -   -  4279.85         48401645           2403.21   
2018-01-03    -    -   -  4277.67         46232696           3194.03   
2018-01-04    -    -   -  4323.68         50699017           3333.30   
2018-01-05    -    -   -  4354.23         56414034           3668.95   
2018-01-08    -    -   -  4382.23         42746996           2925.44   

[249 rows x 7 columns]
```
### **Using Full Data**
Full data gives data from the inception of stock to today.
```
from NSEDownload import indices
df = indices.get_data(indexName = "NIFTY 100", full_data=True)
```

Output Dataframe:
```
Open 	High 	Low 	Close 	Shares Traded 	Turnover (Rs. Cr) 	
Date 							
2003-01-01 	0.00 	0.00 	0.00 	1000.00 	- 	- 	
2003-01-02 	0.00 	0.00 	0.00 	1008.03 	- 	- 	
2003-01-03 	0.00 	0.00 	0.00 	1004.49 	- 	- 	
2003-01-06 	0.00 	0.00 	0.00 	999.85 	- 	- 	
2003-01-07 	0.00 	0.00 	0.00 	997.81 	- 	- 	
... 	... 	... 	... 	... 	... 	... 	...
2021-10-08 	18154.00 	18195.30 	18092.55 	18141.70 	689834891 	31536.6 	
2021-10-11 	18128.70 	18289.45 	18100.70 	18198.90 	683323566 	36616.7 	
2021-10-12 	18181.55 	18275.00 	18125.20 	18258.85 	724211945 	35552.7 	
2021-10-13 	18365.90 	18469.10 	18323.35 	18433.20 	901778939 	44813.4 	
2021-10-14 	18543.05 	18621.60 	18525.80 	18610.35 	976710994 	49481 	

[4671 rows × 7 columns]
```

## **Total Returns Index** 
{:toc}
Additional 'indextype' has to be set to 'TRI' to use this. The date range can be specified same as above.

```
from NSEDownload import indices
df = indices.get_data(indexName = "NIFTY 100",full_data=True, indextype="TRI")
```

Output Dataframe:
```
            Total Returns Index 	
Date 		
2003-01-01 	1000.00 	
2003-01-02 	1008.03 	
2003-01-03 	1004.49 	
2003-01-06 	999.85 	
2003-01-07 	997.81 	
... 	... 	...
2021-10-08 	23799.61 	
2021-10-11 	23874.63 	
2021-10-12 	23953.27 	
2021-10-13 	24181.99 	
2021-10-14 	24416.33 	

[4672 rows × 2 columns]
```
