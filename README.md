# BMW Sales Analytics Dashboard

A professional data analytics dashboard built with Streamlit for analyzing BMW vehicle sales data.

## Features

- **Interactive Filters**: Filter by model, year range, and fuel type
- **Key Metrics**: Display of total vehicles, average price, mileage, MPG, and engine size
- **Data Visualizations**: 
  - Price distribution by model
  - Transmission type breakdown
  - Price vs Mileage analysis
  - Engine size vs MPG correlation
  - Yearly price trends
  - Model comparisons
  - Fuel type and transmission analysis
  - Tax, MPG, and engine size distributions

- **Data Summary**: Detailed statistics and filtered dataset preview
- **Export Functionality**: Download filtered data as CSV

## Installation

1. Clone or download this repository
2. Install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

The dashboard will open in your web browser at `http://localhost:8501`

## Data

The dashboard uses BMW sales data from `bmw.csv` with the following columns:
- model: BMW model name
- year: Year of manufacture
- price: Vehicle price in USD
- transmission: Transmission type (Automatic/Manual)
- mileage: Mileage in miles
- fuelType: Fuel type (Diesel/Petrol)
- tax: Tax amount
- mpg: Miles per gallon
- engineSize: Engine size in liters

## Technologies Used

- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive data visualizations

## Deployment

### Deploy on Streamlit Cloud

1. Push your repository to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app" and select your repository
4. Choose the main branch and specify `app.py` as the entry point
5. Deploy!

## Project Structure

```
dashboard/
├── app.py              # Main Streamlit application
├── bmw.csv             # BMW sales data
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
├── .gitignore          # Git ignore file
└── .streamlit/
    └── config.toml     # Streamlit configuration
```

## License

This project is open source and available under the MIT License.
