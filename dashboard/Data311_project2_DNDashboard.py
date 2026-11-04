import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
  from pathlib import Path

#page configuration
st.set_page_config(layout = "wide", page_title="Cal Poly Humboldt Regional Commute App")

#this session is a placeholder for performance, real data will come 
#when Track B is in
#@st.cache_data
#set title
st.title("Regional Commute & Car-Cost Calculator")
#map layout
map_container = st.container()
with map_container:
    st.header("Regional Map of Humboldt Area")

    #map_data from cleaned region routing table
      DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "cleaned" / "region_routing_table.csv"
  map_data = pd.read_csv(DATA_PATH) 
    map_df = pd.DataFrame(map_data)
    map_figure = px.scatter_map(map_df,  #these variable strings depend on map data variables in df
                                   lat= "lat",
                                   lon= "lon",
                                   hover_name="region",
                                   text="region",
                                   color= "population_count",
                                   size= "population_count",
                                   color_continuous_scale= px.colors.sequential.Darkmint,
                                   size_max=30,
                                   zoom= 9,
                                    center={"lat": 40.80, "lon": -124.10},
                                   height=400
                                )

    #this function sets the background of the mao using open-street-map
    map_figure.update_layout(map_style= "open-street-map")
    #this function strips the default margins for a clean looking map in hover
    map_figure.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    #plotly chart using map data from above DISPLAY LAST
    st.plotly_chart(map_figure, use_container_width=True)


regional_details_container = st.container()
with regional_details_container:
    #region panel
    st.header("Regional Details With Preferences") #fill in with group data
    #this will be a select box to check within each region and grabbing its row
    selected = st.selectbox("Select a region to view details: ", map_df["region"])
    selected_row = map_df[map_df["region"]==selected].iloc[0]
    #dynamic columns in the panel
    column1,column2 = st.columns(2)
    with column1:
        #dynamically sorts what user wants to see and their desired output
        st.metric(label=f"The population of {selected}",value=f"{selected_row["population_count"]:,}")
        # selected region's bar chart where selected_df = data most useful for the user in a dataframe
        selected_df = pd.DataFrame({
            "Preferred Transport":["Walking","Biking","Driving","Transit/Bus"],
            "Percentage": [selected_row["pct_walk"],selected_row["pct_bike"],selected_row["pct_drive"],selected_row["pct_bus"]]
        })
        #figure creation using the dataframe created
        selected_figure = px.bar(selected_df, x = "Preferred Transport", y = "Percentage", title = f" Desired Transportation Specification in {selected}")
        #design and cleanliness feature
    st.plotly_chart(selected_figure, use_container_width=True)

    with column2:
        #metrics data dictionary
        metrics = {
            "Measurements in": ["Time(Mins)","Distance(Miles)","CO2 Emissions (Kg)"],
            "Walking": [selected_row["walk_min"],selected_row["walk_mi"], selected_row["avg_co2e_walk"]],
            "Driving": [selected_row["drive_min"],selected_row["drive_mi"], selected_row["avg_co2e_drive"]]
        }
        if selected_row["bus_available"] == "False":
            metrics["Bus"] = ["No commute avaliable","No commute avaliable","No commute avaliable"]
            st.warning("No bus available")
        else:
            metrics["Bus"] =[selected_row["nearest_stop_name"],selected_row["nearest_stop_dist_mi"], selected_row["avg_co2e_bus"]]
    # creating the dataframe
    metrics_df = pd.DataFrame(metrics)
    st.table(metrics_df)

# CAR INFO and COST CALCULATOR
st.header("Cars' Cost and Emissions Calculator")
st.subheader("Commute Metrics in Time, Distance, and Emmissions?") #emissions maybe, it depends on the data received or a specific calculatioin using details forcommute

#online given permit prices for Cal Poly Humboldt
student_permit_pricing = {
    "Year Permit": 315.00,
    "Semester Permit (Fall or Spring)": 157.50,
    "Semester Evening Permit (Valid after 5 PM)": 58.00,
    "Semester Motorcycle Permit": 40.00,
    "Daily Permit": 5.0,
    "Meter Spaces (Hourly Rate)": 0.75,
    "Full Summer Permit (Valid June 1 - July 31)": 105.0,
    "Summer Motorcycle Permit": 16.0
} 
faculty_permit_pricing = {
    "Academic Year Permits":{
        "Non-Rep & MPP": 315.0,
        "Unit 1": 315.0,
        "Units 2, 5, 7, 9": 116.2,
        "Unit 3": 124.61,
        "Unit 4": 270.0,
        "Unit 6": 225.0,
        "Unit 8": 315.0,
        "Unit 11": 315.0
    },
    "Single Semester Permits":{
        "Non-Rep & MPP": 157.5,
        "Unit 1": 157.5,
        "Units 2, 5, 7, 9": 58.1,
        "Unit 3": 62.31,
        "Unit 4": 135.0,
        "Unit 6": 112.5,
        "Unit 8": 157.5,
        "Unit 11": 157.5        
    },
    "Academic Year Motorcycle Permits":{
        "Non-Rep & MPP": 80.0,
        "Unit 1": 80.0,
        "Units 2, 5, 7, 9": 29.04,
        "Unit 3": 31.16,
        "Unit 4": 68.0,
        "Unit 6": 57.0,
        "Unit 8": 80.0,
        "Unit 11": 80.0
    },
    "Single Semester Motorcycle Permits":{
        "Non-Rep & MPP": 40.0,
        "Unit 1": 40.0,
        "Units 2, 5, 7, 9": 14.52,
        "Unit 3": 15.58,
        "Unit 4": 34.0,
        "Unit 6": 28.5,
        "Unit 8": 40.0,
        "Unit 11": 40.0
    },
    "Single Semester Evening Permit":{
        "Non-Rep & MPP": 58.0,
        "Unit 1": 58.0,
        "Units 2, 5, 7, 9": 21.52,
        "Unit 3": 23.10,
        "Unit 4": 50.0,
        "Unit 6": 42.0,
        "Unit 8": 58.0,
        "Unit 11": 58.0
    },
    "Daily Permits":{
        "Non-Rep & MPP": 5.0,
        "Unit 1": 5.0,
        "Units 2, 5, 7, 9": 2.0,
        "Unit 3": 2.0,
        "Unit 4": 2.0,
        "Unit 6": 2.0,
        "Unit 8": 5.0,
        "Unit 11": 5.0
    },
    "Hourly Metered Spaces":{
        "Non-Rep & MPP": 0.75,
        "Unit 1": 0.75,
        "Units 2, 5, 7, 9": 0.75,
        "Unit 3": 0.75,
        "Unit 4": 0.75,
        "Unit 6": 0.75,
        "Unit 8": 0.75,
        "Unit 11": 0.75
    },
    "Summer Full":{
        "Non-Rep & MPP": 105.0,
        "Unit 1": 105.0,
        "Units 2, 5, 7, 9": 38.73,
        "Unit 3": 40.76,
        "Unit 4": 90.0,
        "Unit 6": 75.0,
        "Unit 8": 105.0,
        "Unit 11": 105.0
    },
    "Summer Motorcycle Permits":{
        "Non-Rep & MPP": 16.0,
        "Unit 1": 16.0,
        "Units 2, 5, 7, 9": 5.81,
        "Unit 3": 6.23,
        "Unit 4": 13.6,
        "Unit 6": 11.40,
        "Unit 8": 16.0,
        "Unit 11": 16.0
    }
}

#column containers
column_containers = st.container()
with column_containers:
    column_container1,column_container2,column_container3 = st.columns(3)
    with column_container1:
        days_per_wk_commuting = st.number_input("Days per week you plan to commute: ", min_value = 1, max_value = 7, value = 4)
        weeks_per_semester = st.number_input("Weeks per semester: ", min_value = 1, max_value = 20, value = 16)
    with column_container2:
        car_mpg = st.number_input("What is your car's Miles per Gallon(mpg): ", min_value = 1.0, max_value = 40.0)
        current_gas_price = st.number_input("Current gas price per gallon($): ", min_value = 1.0, max_value = 10.0)
    with column_container3:
        #this code assumes faculty/ staff and admin pay the same amount 
        #or the same amount applies to admins
        role = st.radio("Select Role for Parking:", ["Student"," Faculty, Staff/Admin"])
        if role == "Student":
            student_permit_type = st.selectbox("Select Permit Type: ", list(student_permit_pricing.keys()))
            student_permit_price = student_permit_pricing[student_permit_type]

            permit_type = student_permit_type
            permit_price = student_permit_price
        else:
            category_permit = st.selectbox("Select Permit Category: ", list(faculty_permit_pricing.keys()))
            category_unit_pricing = st.selectbox("Select Preffered Parking Permit Type: ", list(faculty_permit_pricing[category_permit].keys()))
            faculty_permit_price = faculty_permit_pricing[category_permit][category_unit_pricing]
            faculty_permit_type = f"{category_permit} ({category_unit_pricing})"

            permit_type = faculty_permit_type
            permit_price = faculty_permit_price
    st.write(f"Selected Permit Type: {permit_type}")
    st.metric(label = "Permit Price", value = f"${permit_price:.2f}")


# formula using inputs goes here
distance = selected_row["drive_mi"]

#from the user inputs from above
total_miles = distance * 2 * days_per_wk_commuting * weeks_per_semester
gallons_used = total_miles/car_mpg
calculated_commute_cost = (gallons_used * current_gas_price) + permit_price
# emission costs
driving_co2_emissions = 8.887 #in kg/gallon according to CO2e EPA factor 
#adding conversion to lbs
kg_to_lbs_converter = 2.20462262
co2e_emissions = gallons_used * driving_co2_emissions * kg_to_lbs_converter
#display results
result_conatiner = st.container()
with result_conatiner:
    st.subheader("Resulting Analysis")
    result_column1, result_column2 = st.columns(2)
    result_column1.metric("Calculated Commute Cost", f"${calculated_commute_cost:.2f}")
    result_column2.metric("Total CO2e Emissions",f"{co2e_emissions:.2f} lbs CO2e")

#method for calculation goes here if any

#survey can go here









