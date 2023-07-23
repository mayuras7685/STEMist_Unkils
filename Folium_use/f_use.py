import folium
import streamlit as st
from streamlit_folium import st_folium
from folium.plugins import Draw
from streamlit_image_comparison import image_comparison
import time

st.title("Wild Animal Tracking System Dashboard")


f1, f2 = st.columns(2)
with f1:
    global pred
    stream_files1 = st.file_uploader("CAM 1", type=['mp4', 'mpv', 'avi'], key=1, accept_multiple_files=True)
    st.text("Location: 21.091501, 70.749633")
    for stream in stream_files1:
        bytes_d1 = stream.read()
        st.write("filename:", stream.name)
    pred = 1
    

with f2:
    stream_files2 = st.file_uploader("CAM 2", type=['mp4', 'mpv', 'avi'], key=2, accept_multiple_files=True)
    st.text("Location: 21.095087, 70.737875")
    for stream in stream_files2:
        bytes_d2 = stream.read()
        st.write("filename:", stream.name)




if stream_files1 or stream_files2:
    time.sleep(10)
    st.header("Animal Location")
    # center on Liberty Bell, add marker
    m = folium.Map(location=[21.091501, 70.749633], zoom_start=15)
    folium.Marker(
    [21.091501, 70.749633], popup="Tiger", tooltip="Tiger"
).add_to(m)

    # call to render Folium map in Streamlit
    st_data = st_folium(m, width=700, height=250)



    st.header("Detection Proof")

    image_comparison(
        img1="../Uploaded/1.jpg",
        img2="../Detected/1.jpg",
        label1="Original",
        label2="Predication",
        width=500,
    )

    st.warning('Tiger going towards X Village', icon="⚠️")

    #Alert areas
    st.header("Alert Areas")
    m = folium.Map(location=[21.091501, 70.749633], zoom_start=15)
    folium.Marker(
        [21.091501, 70.749633], popup="Tiger", tooltip="Tiger"
    ).add_to(m)
    Draw(export=True).add_to(m)

    c1= st.columns(1)
    output = st_folium(m, width=700, height=400)

elif stream_files1 and stream_files2:
    time.sleep(10)
    st.header("Animal Location")
    # center on Liberty Bell, add marker
    m = folium.Map(location=[21.091501, 70.749633], zoom_start=15)
    folium.Marker(
    [21.091501, 70.749633], popup="Tiger", tooltip="Tiger"
).add_to(m)
    folium.Marker(
    [21.095087, 70.737875], popup="Lion", tooltip="Lion"
).add_to(m)

    # call to render Folium map in Streamlit
    st_data = st_folium(m, width=700, height=250)




    st.header("Detection Proof")

    image_comparison(
        img1="../Uploaded/1.jpg",
        img2="../Detected/1.jpg",
        label1="Original",
        label2="Predication",
        width=500,
    )

    st.warning('Tiger going towards X Village ', icon="⚠️")
    st.warning('Lion going towards Y Village', icon="⚠️")

    #Alert areas
    st.header("Alert Areas")
    m = folium.Map(location=[21.091501, 70.749633], zoom_start=15)
    folium.Marker(
        [21.091501, 70.749633], popup="Tiger", tooltip="Tiger"
    ).add_to(m)
    folium.Marker(
    [21.095087, 70.737875], popup="Lion", tooltip="Lion"
).add_to(m)
    Draw(export=True).add_to(m)

    c1= st.columns(1)
    output = st_folium(m, width=700, height=400)




st.divider()
st.header("Animal Detected Till now (Day by day)")
col1, col2, col3 = st.columns(3)
col1.metric("Lions", "15", "3")
col2.metric("Tiger", "8", "-5")
col3.metric("Hyena", "23", "12")


st.divider()


    

    



