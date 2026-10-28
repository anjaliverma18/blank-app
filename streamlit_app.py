import streamlit as st
st.title('BMI calculator')
name= st.text_input('enter your name')
weight= st.number_input("enter your weight(kg)",min_value=1.00, max_value=200,value=60)
height= st.number_input('enter your height(m)',min_value= 0.5, max_value=2.5,value=1.65)
if st.button('calculate BMI'):
    bmi=weight/(height **2)
    st.write(f"hello",{name})
    st.metric('your BMI',round(bmi,2))
    if bmi<18.5:
        st.warning('underweight')
    if bmi <25:
        st.success('normal')
    else:
        st.warning('overweight')
