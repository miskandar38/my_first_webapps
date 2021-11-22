%%writefile myfirstapp.py
import streamlit as st
import numpy as np
import pandas as pd

st.header("Incidence Rate For Dengue And Dengue Haemorrhagic Fever")

st.write("""This dataset shows the Incidence Rate For Dengue And Dengue Haemorrhagic Fever, Malaysia, 2000 - 2019""")

st.write(pd.DataFrame({
    'Year': [2000,2000,2001,2001,2002,2002,2003,2003,2004,2004,2005,2005,2006,2006,2007,2007,2008,2008,2009,2009,2010,2010,2011,2011,2012,2012,2013,2013,2014,2014,2015,2015,2016,2016,2017,2017,2018,2018,2019,2019],
    'Diseases': ['Dengue', 'Dengue H','Dengue','Dengue H','Dengue','Dengue H','Dengue','Dengue H','Dengue','Dengue H','Dengue','Dengue H','Dengue','Dengue H','Dengue','Dengue H','Dengue','Dengue H','Dengue','Dengue H','Dengue','Dengue H','Dengue','Dengue H','Dengue','Dengue H','Dengue','Dengue H','Dengue','Dengue H','Dengue','Dengue H','Dengue','Dengue H','Dengue','Dengue H','Dengue','Dengue H' ,'Dengue','Dengue H'],
    'Incidence Rate(Per 100,000 Population)' :[28.9,1.7,64.3,3.8,63.2,8,58.9,2.7,49.9,2.6,60.7,3.8,64.4,4.1,85.8,4.9,167.8,10.2,136.9,9.7,148.7,14.2,63.8,4.9,72.2,2.5,143.3,2.6,357.5,3.7,393,3.4,318.1,2,318.3,2,244.1,1.2,397.7,1.6]
}))

st.write("""**Randomized data on line chart**""")

chart_data = pd.DataFrame(
np.random.randn(100, 3),
columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.write("""**Randomized data on bar chart**""")

chart_data = pd.DataFrame(
np.random.randn(50, 3),
columns=['a', 'b', 'c'])

st.bar_chart(chart_data)
