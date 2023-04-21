#!/usr/bin/env python
# coding: utf-8

# <img src="images/jupiter.png" width="200" height="200"/>

# # Using Jupyter

# ## Markdown cells
# 
# This is a Markdown (documentation) cell, for adding documentation and comments to a notebook. It uses Markdown, a text styling language, as well as HTML. When a Markdown cell is "run", it converts the contents of the cell into HTML, which is then rendered and displayed.
# 
# Double-click on a Markdown cell to see its source.
# 
# This is **more** _markdown_. Surround text with double asterisk for bold, or single underline for italic. 
# 
# See the Notebook named **JupyterMarkdownGuide** for details. 

# ###  Code Cells
# 
# Code cells contain Python (or other language) code. When a code cell is run, it executes the code, and shows the output below the cell. The output is retained unless you explicitly clear it. 

# In[1]:


x = 3


# In[2]:


for i in range(3):
    print(i)


# In[3]:


print("wombat")


# In[ ]:





# In[4]:


print(x)


# ## It's all one program
# 
# All code is run in the same instance of the Python interpreter, so that objects created in one cell are available to other cells, as long as the first cell has been run.

# In[5]:


from datetime import date as Date


# In[6]:


then = Date(2011,5,22)


# In[7]:


print(then.year)


# In[8]:


get_ipython().run_line_magic('pinfo', 'then')


# ## Getting help
# Putting a ? before (or after) any object displays help for that object. Using ?? will add more detailed help, if available. (The output will be in a separate pane at the bottom of the browser window).

# In[9]:


get_ipython().run_line_magic('pinfo', 'i')


# In[10]:


get_ipython().run_line_magic('pinfo2', 'Date')


# ## Using Python's scientific libraries
# For typical use of Python's scientific libraries, put the following at the top of the notebook in a code cell:
# 
# <pre>
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# </pre>
# 
# Other  modules and packages should be included as needed.
# 

# In[11]:


import pandas as pd
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns



# ## Inline plotting
# After matplotlib is imported, use the **%matplotlib inline** magic to display figures as part of the notebook. Otherwise, they are displayed in popup windows. 

# In[12]:


get_ipython().run_line_magic('matplotlib', 'inline')
values = np.random.randint(1, 100, 50)
plt.plot(values)


# ## Using HTML
# 
# Since Markdown is converted to HTML, any actual HTML in a Markdown cell is used. 
# 
# <ul><li>red</li><li>purple</li><li>orange</li></ul>
# <br/>
# <hr/>
# Hello
# <hr/>

# ## Magics
# 
# iPython and Jupyter notebooks have _line magics_, which are line-oriented. Many of them execute commands or turn iPython settings on and off. 
# 
# Jupyter has _cell magics_, which apply to the entire cell. 

# In[13]:


get_ipython().run_line_magic('lsmagic', '')


# In[14]:


get_ipython().system('hostname')
h = get_ipython().getoutput('hostname')
print(h)


# ## Running external Python scripts
# 
# Use the **%run** magic to launch an external Python script

# In[15]:


get_ipython().run_line_magic('run', '../EXAMPLES/my_vars.py')


# In[16]:


print(user_name)
print(animal)
print(snake)


# ## Loading scripts into cells
# 
# Use the **%load** magic to read a separate Python script into the current cell. After it's loaded, it can be run like any other cell.
# 
# Once the code is loaded into the cell, the **%load** command is commented out

# In[17]:


# %load ../EXAMPLES/read_tyger.py

with open("../DATA/tyger.txt", "r") as tyger_in:  # tyger_in is return value of open()
    for raw_line in tyger_in:  # tyger_in is iterable of lines in the file
        line = raw_line.rstrip()  # remove \n
        print(line)


# In[18]:


get_ipython().run_line_magic('load', 'imports.py')


# ## Using LaTeX
# 
# Markdown cells can render LaTeX via MathJax. Put the LaTeX code inside a pair of dollar signs: **\$\rho\$:**
# 
# $\rho$, $\rho$, $\rho$ your boat

# $\mathbf{V}_1 \times \mathbf{V}_2 =  \begin{vmatrix} \
# \mathbf{i} & \mathbf{j} & \mathbf{k}  \\
# \frac{\partial X}{\partial u} & \frac{\partial Y}{\partial u} & 0\\
# \frac{\partial X}{\partial v} & \frac{\partial Y}{\partial v} & 0\\
# \end{vmatrix}$ 
# 
# $\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$

# ### Can you read this limerick?

# 
# $\frac{12 + 144  + 20 + 3\sqrt{4}}{7} + (5 * 11) = 9^2 + 0$ <br/>
# 
# <i>See text of limerick at the bottom of this notebook</i>
# 
# 

# ## Getting info

# In[19]:


from scipy import stats
sp.info(stats)


# ## Benchmarking
# 
# The **%%timeit** cell magic will execute the code in the cell and report the average time it took to execute it. 

# In[20]:


fruits = ["pomegranate", "cherry", "apricot", "date", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE" ]


# #### Benchmark with *for* loop

# In[21]:


get_ipython().run_cell_magic('timeit', '100', 'f1 = []\nfor f in fruits:\n    f1.append(f[:3])\n')


# #### Benchmark with list comprehension

# In[22]:


get_ipython().run_cell_magic('timeit', '100', 'f2 = [f[:3] for f in fruits]\n')


# ## Images
# 
# You can insert images into doc cells using the Markdown image tag:
# 
# _The following uses a Markdown table to arrange the images._ 
# 
# | Guido        | Tim the Enchanter | Wombat  |
# | ------------- |:-------------:| -----:|
# | ![Guido](images/guido.png)|  ![Tim](images/tim.jpg) |![wombat](images/wombat.jpg) |
# 

# ### The limerick
# 
# A dozen, a gross, and a score<br/>
# Plus three times the square root of four<br/>
# Divided by seven<br/>
# Plus five times eleven<br/>
# Is nine squared and not a bit more.<br/>
# 

# In[ ]:




