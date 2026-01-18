import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(page_title="BMW Sales Analytics", layout="wide", initial_sidebar_state="expanded", page_icon="🚗")

# Load data
df = pd.read_csv('bmw.csv')

# Clean data (remove leading spaces if any)
df.columns = df.columns.str.strip()

# ============================================================================
# SIDEBAR SECTION
# ============================================================================
st.sidebar.header("🎛️ Dashboard Filters")

# Filter by model
selected_models = st.sidebar.multiselect("Select Model(s)", df['model'].unique(), default=df['model'].unique())
df_filtered = df[df['model'].isin(selected_models)]

# Filter by year range
year_range = st.sidebar.slider("Year Range", int(df['year'].min()), int(df['year'].max()), 
                               (int(df['year'].min()), int(df['year'].max())))
df_filtered = df_filtered[(df_filtered['year'] >= year_range[0]) & (df_filtered['year'] <= year_range[1])]

# Filter by fuel type
selected_fuel = st.sidebar.multiselect("Fuel Type", df['fuelType'].unique(), default=df['fuelType'].unique())
df_filtered = df_filtered[df_filtered['fuelType'].isin(selected_fuel)]

# ============================================================================
# HEADER SECTION
# ============================================================================
st.title("🏎️ BMW Sales Analytics Dashboard")
st.markdown("---")

# Key metrics
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Total Vehicles", f"{len(df_filtered):,}")
with col2:
    avg_price = df_filtered['price'].mean()
    st.metric("Avg Price", f"${avg_price:,.0f}")
with col3:
    avg_mileage = df_filtered['mileage'].mean()
    st.metric("Avg Mileage", f"{avg_mileage:,.0f} mi")
with col4:
    avg_mpg = df_filtered['mpg'].mean()
    st.metric("Avg MPG", f"{avg_mpg:.1f}")
with col5:
    avg_engine = df_filtered['engineSize'].mean()
    st.metric("Avg Engine Size", f"{avg_engine:.2f}L")

st.markdown("---")

# ============================================================================
# MAIN DASHBOARD CONTENT
# ============================================================================

# Row 1: Distribution Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("Price Distribution by Model")
    fig_price = px.box(df_filtered, x='model', y='price', color='model', 
                       template="plotly_white", height=400)
    fig_price.update_layout(showlegend=False, xaxis_tickangle=-45)
    st.plotly_chart(fig_price, use_container_width=True)

with col2:
    st.subheader("Transmission Type Distribution")
    transmission_counts = df_filtered['transmission'].value_counts()
    fig_transmission = px.pie(values=transmission_counts.values, names=transmission_counts.index,
                              template="plotly_white", height=400)
    st.plotly_chart(fig_transmission, use_container_width=True)

# Row 2: Relationship Analysis
col1, col2 = st.columns(2)

with col1:
    st.subheader("Price vs Mileage")
    fig_scatter = px.scatter(df_filtered, x='mileage', y='price', color='fuelType',
                            size='engineSize', hover_data=['model', 'year'],
                            template="plotly_white", height=400)
    st.plotly_chart(fig_scatter, use_container_width=True)

with col2:
    st.subheader("Engine Size vs MPG")
    fig_engine = px.scatter(df_filtered, x='engineSize', y='mpg', color='fuelType',
                           size='price', hover_data=['model', 'year'],
                           template="plotly_white", height=400)
    st.plotly_chart(fig_engine, use_container_width=True)

# Row 3: Trend Analysis
st.subheader("Average Price Trend Over Years")
yearly_price = df_filtered.groupby('year')['price'].mean().reset_index()
fig_trend = px.line(yearly_price, x='year', y='price', markers=True, 
                    template="plotly_white", height=350)
fig_trend.update_traces(line=dict(color='#1f77b4', width=3))
st.plotly_chart(fig_trend, use_container_width=True)

# Row 4: Model Analytics
col1, col2 = st.columns(2)

with col1:
    st.subheader("Average Price by Model")
    model_price = df_filtered.groupby('model')['price'].mean().sort_values(ascending=False)
    fig_model = px.bar(x=model_price.values, y=model_price.index, 
                       template="plotly_white", orientation='h', height=400)
    fig_model.update_layout(xaxis_title="Average Price ($)", yaxis_title="Model")
    st.plotly_chart(fig_model, use_container_width=True)

with col2:
    st.subheader("Vehicle Count by Fuel Type & Transmission")
    fuel_trans = df_filtered.groupby(['fuelType', 'transmission']).size().reset_index(name='count')
    fig_fuel_trans = px.bar(fuel_trans, x='fuelType', y='count', color='transmission',
                           template="plotly_white", height=400, barmode='group')
    st.plotly_chart(fig_fuel_trans, use_container_width=True)

# Row 5: Advanced Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Tax Distribution")
    fig_tax = px.histogram(df_filtered, x='tax', nbins=30, template="plotly_white", height=350)
    st.plotly_chart(fig_tax, use_container_width=True)

with col2:
    st.subheader("Average MPG by Fuel Type")
    mpg_fuel = df_filtered.groupby('fuelType')['mpg'].mean().sort_values(ascending=False)
    fig_mpg = px.bar(x=mpg_fuel.index, y=mpg_fuel.values, template="plotly_white", height=350)
    fig_mpg.update_layout(xaxis_title="Fuel Type", yaxis_title="Average MPG")
    st.plotly_chart(fig_mpg, use_container_width=True)

with col3:
    st.subheader("Engine Size Distribution")
    fig_engine_dist = px.histogram(df_filtered, x='engineSize', nbins=25, template="plotly_white", height=350)
    st.plotly_chart(fig_engine_dist, use_container_width=True)

# ============================================================================
# DATA SUMMARY SECTION
# ============================================================================
st.markdown("---")
st.subheader("📊 Detailed Data Summary")

# Create summary statistics table
summary_stats = pd.DataFrame({
    'Metric': ['Count', 'Mean', 'Median', 'Std Dev', 'Min', 'Max'],
    'Price ($)': [
        f"{df_filtered['price'].count():,}",
        f"${df_filtered['price'].mean():,.2f}",
        f"${df_filtered['price'].median():,.2f}",
        f"${df_filtered['price'].std():,.2f}",
        f"${df_filtered['price'].min():,.2f}",
        f"${df_filtered['price'].max():,.2f}"
    ],
    'Mileage (mi)': [
        f"{df_filtered['mileage'].count():,}",
        f"{df_filtered['mileage'].mean():,.0f}",
        f"{df_filtered['mileage'].median():,.0f}",
        f"{df_filtered['mileage'].std():,.0f}",
        f"{df_filtered['mileage'].min():,.0f}",
        f"{df_filtered['mileage'].max():,.0f}"
    ],
    'MPG': [
        f"{df_filtered['mpg'].count():,}",
        f"{df_filtered['mpg'].mean():.2f}",
        f"{df_filtered['mpg'].median():.2f}",
        f"{df_filtered['mpg'].std():.2f}",
        f"{df_filtered['mpg'].min():.2f}",
        f"{df_filtered['mpg'].max():.2f}"
    ]
})

st.table(summary_stats)

# Data table
st.subheader("📋 Filtered Dataset Preview")
st.dataframe(df_filtered.head(50), use_container_width=True)

# Download data
st.subheader("⬇️ Export Data")
csv = df_filtered.to_csv(index=False)
st.download_button(label="Download filtered data as CSV", data=csv, file_name="bmw_data.csv", mime="text/csv")
