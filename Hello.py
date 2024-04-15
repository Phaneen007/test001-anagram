# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# my_app.py
import streamlit as st
import pandas as pd

st.title("Phanee's Ride App\n Hello Guys")
data = {
    'Miles': ['0-4 miles', '5-9 miles', '10-20 miles', 'More than 20 miles!'],
    'Price': ['1$/mile', '85¢/mile', '80¢/mile', 'To be negotiated'],
}

st.write("Check out these offers:")
df = pd.DataFrame(data)
st.table(df)

whatsapp_location_link = "https://maps.app.goo.gl/oVkHUtHeYceGWuRG6"

# Create a clickable link in Markdown
st.markdown(f"[See my location]({whatsapp_location_link})")

if st.button("Click here to chat in whatsapp"):
    st.markdown(
        f'https://wa.me/+13162101527',
        unsafe_allow_html=True
    )

##########################################
data = {
    'Time': ['8-9 AM', '9-10 AM', '10-11 AM', '11-11:59 AM', '12-1 PM','12-1 PM', '1-2 PM','2 -3 PM', '4-5 PM', '5-6 PM', '6-7 PM', '7-8 PM', '8-9 PM', '9-10 PM'],
    'Status': ['Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active', 'Active']
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Create a sidebar to update the status
st.sidebar.header('Update Status')
selected_name = st.sidebar.selectbox('Select a Time:', df['Time'])
new_status = st.sidebar.selectbox('Select Status:', ['Active', 'Inactive','Done'])

# Update the status in the DataFrame
df.loc[df['Time'] == selected_name, 'Status'] = new_status

# Display the updated table
st.table(df)

