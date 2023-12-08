
st.tutle('USA college admission rate prrediction')

image = Image.open('college admission.jpg')
st.image(image)

input = open('lr_admit.pkl', 'rb')
model = pkl.load(input)
st.header('Input admission information')
gre = st.number_input('Insert GRE Score')
