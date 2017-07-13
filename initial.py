#https://github.com/data-8/datascience

import matplotlib
matplotlib.use('Agg')
from datascience import Table
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('fivethirtyeight')


Table.read_table("~/Documents/Comp312/hw1/CDPH_Environmental_Inspections.csv")

