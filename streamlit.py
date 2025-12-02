import streamlit as st
import pandas as pd
from datetime import datetime
from geopy.distance import geodesic

@st.cache_data
def load_data():
    return pd.read_csv("./dubai_cold_coffee_spots_clean.csv")

df = load_data()


st.set_page_config(page_title="Dubai Cold Coffee Finder")

st.title("☕︎ Dubai Cold Coffee Finder")
st.caption("Find cold coffee spots near you — filter, sort, and view on map")

st.sidebar.title("Search & Filters")

with st.sidebar:
    st.subheader("Your location(manual)")

    user_lat = st.number_input("Latitude:",25.20)
    user_lng = st.number_input("Longitude:",55.29)

    st.subheader("Spot filters")

    spot_type = st.selectbox("Spots type",["all", "cart", "cafe", "truck"])

    max_dis = st.slider("Max distance(km)", 1,50,10)
    rating = st.slider("Minimum rating", 0.0, 5.0, 0.0, step=0.1)

    is_open_spot = st.checkbox("Only currently open", True)

    top_n = st.slider("Show top N result", 5, 100, 5)

    sort_by = st.selectbox("Sort by", ["distance", "rating", "name"])

   
@st.cache_data
def compute_distance(lat, lng, df):
    df["distance"] = df.apply(lambda r: round(geodesic((lat, lng), (r["lat"], r["lng"])).km, 2), axis=1)
    return df

df = compute_distance(user_lat, user_lng, df)

df["rating"] = pd.to_numeric(df["rating"], errors="coerce").fillna(0)

def is_open(row):
    now = datetime.now().time()
    try:
        open_t = datetime.strptime(row["opening_time"], "%H:%M").time()
        close_t = datetime.strptime(row["closing_time"], "%H:%M").time()
        return open_t <= now <= close_t
    except:
        return False


df["is_open_spot"] = df.apply(is_open, axis=1)

if is_open_spot:
    df = df[df["is_open_spot"] == True]
  
if spot_type != "all":
    df = df[df["type"] == spot_type]

df = df[df["distance"] <= max_dis]
df = df[df["rating"] >= rating]

df = df.head(top_n)
if sort_by == "distance":
    df = df.sort_values(by="distance", ascending=True, ignore_index=True)
elif sort_by == "rating":
    df = df.sort_values(by="rating", ascending=False, ignore_index=True)
else:
    df = df.sort_values(by="name", ascending=True, ignore_index=True)

st.metric("Results", f"{len(df)} spots found within {max_dis} km")
st.dataframe(df)
st.info("Tips: try moving the location, widening max distance, or lowering min rating to see more spots.")