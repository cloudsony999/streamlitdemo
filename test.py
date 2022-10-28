import streamlit as st
import pandas as pd
import numpy as np
st.write('i am amitava....')

st.title('My web Page')

df=pd.DataFrame([[11,22,33],[66,99,77],[111,222,333]],columns=['Physics','Maths','Chemistry'])
st.table(df)
st.dataframe(df)

st.latex(
    r'''
    S=\sum^{N}_{i=0}a_{n}
    '''
)

df=pd.DataFrame()

df['x']=np.arange(0,10)
df['y']=np.power(np.arange(0,10),2)


st.dataframe(df)

st.line_chart(data=df)

st.area_chart(data=df)

st.bar_chart(data=df)

if st.checkbox('Please Check here'):
    st.write('U have selected it')


l=['python','ML','Data Science','Java','C','Go','Jumla']
#r=st.selectbox('select any language U like!!!',l)
r=st.multiselect('select any no of language U like!!!',l)
st.write('U selected ',r)


food=['rice','polao','biriani','roti']
t=st.radio("Select your Lunch",food)
st.write("U selected for today's lunch",t)







