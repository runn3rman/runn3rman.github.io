"""
Utah Water Conservation Data Generator
Creates realistic datasets based on CUWCD 2024 Annual Report data
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_snowpack_data():
    """Generate snowpack data for Jordan & Lower Green River Basins"""
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    
    # Jordan River Basin - 135% of median
    jordan_swe = []
    jordan_percent = []
    
    # Lower Green River Basin - 131% of median  
    green_swe = []
    green_percent = []
    
    for date in dates:
        # Seasonal patterns with realistic variation
        day_of_year = date.timetuple().tm_yday
        
        # Peak snowpack in March-April
        if 60 <= day_of_year <= 120:  # Feb-May
            jordan_base = 15 + 10 * np.sin((day_of_year - 60) * np.pi / 60)
            green_base = 12 + 8 * np.sin((day_of_year - 60) * np.pi / 60)
        else:
            jordan_base = max(0, 5 + 3 * np.sin(day_of_year * np.pi / 180))
            green_base = max(0, 4 + 2 * np.sin(day_of_year * np.pi / 180))
        
        # Add realistic noise
        jordan_swe.append(jordan_base + np.random.normal(0, 1.5))
        green_swe.append(green_base + np.random.normal(0, 1.2))
        
        # Percent of median (135% and 131% respectively)
        jordan_percent.append(135 + np.random.normal(0, 8))
        green_percent.append(131 + np.random.normal(0, 6))
    
    snowpack_df = pd.DataFrame({
        'Date': dates,
        'Jordan_SWE_inches': jordan_swe,
        'Jordan_Percent_Median': jordan_percent,
        'Green_SWE_inches': green_swe,
        'Green_Percent_Median': green_percent
    })
    
    return snowpack_df

def generate_reservoir_data():
    """Generate reservoir levels and storage data"""
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    
    reservoirs = {
        'Strawberry': {'capacity_af': 1100000, 'current_af': 1050000, 'spill_events': 3},
        'Jordanelle': {'capacity_af': 320000, 'current_af': 310000, 'spill_events': 1},
        'Utah_Lake': {'capacity_af': 850000, 'current_af': 780000, 'spill_events': 0}
    }
    
    reservoir_data = []
    
    for date in dates:
        for reservoir, data in reservoirs.items():
            # Seasonal variation - higher in spring/summer
            day_of_year = date.timetuple().tm_yday
            
            # Spring runoff peak
            if 80 <= day_of_year <= 150:  # March-June
                seasonal_factor = 1.0 + 0.1 * np.sin((day_of_year - 80) * np.pi / 70)
            else:
                seasonal_factor = 0.95 + 0.05 * np.sin(day_of_year * np.pi / 180)
            
            current_storage = data['current_af'] * seasonal_factor + np.random.normal(0, 5000)
            current_storage = max(0, min(current_storage, data['capacity_af']))
            
            percent_capacity = (current_storage / data['capacity_af']) * 100
            
            reservoir_data.append({
                'Date': date,
                'Reservoir': reservoir,
                'Storage_AF': current_storage,
                'Capacity_AF': data['capacity_af'],
                'Percent_Capacity': percent_capacity,
                'Spill_Event': 1 if np.random.random() < 0.001 and day_of_year in range(100, 140) else 0
            })
    
    return pd.DataFrame(reservoir_data)

def generate_water_deliveries():
    """Generate water delivery data for CUP & CWP"""
    customers = [
        'Alpine', 'American Fork', 'Cedar Hills', 'Highland', 'Lehi',
        'Pleasant Grove', 'Provo', 'Saratoga Springs', 'Spanish Fork',
        'Jordan Valley Water Conservancy District', 'Utah County',
        'Wasatch County', 'Summit County'
    ]
    
    # Based on CUWCD 2024 data
    base_deliveries = {
        'Alpine': 2500, 'American Fork': 8500, 'Cedar Hills': 1200,
        'Highland': 1800, 'Lehi': 12000, 'Pleasant Grove': 6800,
        'Provo': 15000, 'Saratoga Springs': 4500, 'Spanish Fork': 3200,
        'Jordan Valley Water Conservancy District': 37690,
        'Utah County': 8500, 'Wasatch County': 4200, 'Summit County': 2800
    }
    
    months = pd.date_range(start='2024-01-01', end='2024-12-31', freq='MS')
    
    delivery_data = []
    
    for month in months:
        for customer in customers:
            base = base_deliveries[customer]
            
            # Seasonal variation - higher in summer
            month_num = month.month
            if 5 <= month_num <= 9:  # Summer months
                seasonal_factor = 1.3 + 0.2 * np.sin((month_num - 5) * np.pi / 4)
            else:
                seasonal_factor = 0.7 + 0.3 * np.sin(month_num * np.pi / 6)
            
            delivery = base * seasonal_factor / 12 + np.random.normal(0, base * 0.1)
            delivery = max(0, delivery)
            
            delivery_data.append({
                'Month': month,
                'Customer': customer,
                'Delivery_AF': delivery,
                'Customer_Type': 'Municipal' if 'County' not in customer and 'District' not in customer else 'Wholesale'
            })
    
    return pd.DataFrame(delivery_data)

def generate_hydropower_data():
    """Generate hydropower generation data"""
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    
    # Based on CUWCD 2024 data: Olmsted ~2,222 MWh, Jordanelle ~1,977 MWh
    plants = {
        'Olmsted': {'base_mwh': 6.1, 'capacity_mw': 15},  # Daily average
        'Jordanelle': {'base_mwh': 5.4, 'capacity_mw': 12}
    }
    
    power_data = []
    
    for date in dates:
        for plant, data in plants.items():
            # Seasonal variation - higher generation in spring/summer
            day_of_year = date.timetuple().tm_yday
            
            if 60 <= day_of_year <= 180:  # Spring/summer
                seasonal_factor = 1.0 + 0.3 * np.sin((day_of_year - 60) * np.pi / 120)
            else:
                seasonal_factor = 0.6 + 0.2 * np.sin(day_of_year * np.pi / 180)
            
            generation = data['base_mwh'] * seasonal_factor + np.random.normal(0, 1.5)
            generation = max(0, min(generation, data['capacity_mw'] * 24))  # Max daily capacity
            
            power_data.append({
                'Date': date,
                'Plant': plant,
                'Generation_MWh': generation,
                'Capacity_Factor': (generation / (data['capacity_mw'] * 24)) * 100
            })
    
    return pd.DataFrame(power_data)

def generate_conservation_data():
    """Generate conservation program participation data"""
    programs = {
        'Turf_Removal': {'participants': 609, 'area_sqft': 612621, 'water_saved_af': 45.2},
        'Smart_Controllers': {'participants': 1493, 'rebate_amount': 150, 'water_saved_af': 12.8},
        'High_Efficiency_Toilets': {'participants': 313, 'rebate_amount': 100, 'water_saved_af': 8.5},
        'Drip_Irrigation': {'participants': 95, 'area_sqft': 95161, 'water_saved_af': 6.2}
    }
    
    conservation_data = []
    
    for program, data in programs.items():
        for i in range(data['participants']):
            # Simulate individual participant data
            if 'area_sqft' in data:
                area = np.random.normal(data['area_sqft'] / data['participants'], 
                                      data['area_sqft'] / data['participants'] * 0.3)
                area = max(100, area)  # Minimum area
                
                conservation_data.append({
                    'Program': program,
                    'Participant_ID': f"{program}_{i+1:04d}",
                    'Area_SqFt': area,
                    'Water_Saved_AF': area * 0.000074,  # Conversion factor
                    'Rebate_Amount': data.get('rebate_amount', 0)
                })
            else:
                conservation_data.append({
                    'Program': program,
                    'Participant_ID': f"{program}_{i+1:04d}",
                    'Area_SqFt': 0,
                    'Water_Saved_AF': data['water_saved_af'] / data['participants'],
                    'Rebate_Amount': data.get('rebate_amount', 0)
                })
    
    return pd.DataFrame(conservation_data)

def generate_gpcd_data():
    """Generate GPCD (Gallons Per Capita Per Day) data"""
    counties = [
        'Utah County', 'Salt Lake County', 'Davis County', 'Weber County',
        'Cache County', 'Washington County', 'Iron County', 'Summit County'
    ]
    
    # Based on Utah statewide data: 223 GPCD in 2019, down from 241 in 2018
    base_gpcd = {
        'Utah County': 215, 'Salt Lake County': 220, 'Davis County': 210,
        'Weber County': 225, 'Cache County': 230, 'Washington County': 240,
        'Iron County': 250, 'Summit County': 280
    }
    
    years = range(2018, 2025)
    gpcd_data = []
    
    for year in years:
        for county in counties:
            # Trend downward over time (conservation efforts)
            trend_factor = 1 - (year - 2018) * 0.02  # 2% reduction per year
            gpcd = base_gpcd[county] * trend_factor + np.random.normal(0, 5)
            gpcd = max(150, gpcd)  # Minimum reasonable GPCD
            
            gpcd_data.append({
                'Year': year,
                'County': county,
                'GPCD': gpcd,
                'Population': np.random.normal(500000, 100000) if county == 'Utah County' 
                            else np.random.normal(200000, 50000)
            })
    
    return pd.DataFrame(gpcd_data)

if __name__ == "__main__":
    print("Generating Utah Water Conservation datasets...")
    
    # Generate all datasets
    snowpack_df = generate_snowpack_data()
    reservoir_df = generate_reservoir_data()
    deliveries_df = generate_water_deliveries()
    hydropower_df = generate_hydropower_data()
    conservation_df = generate_conservation_data()
    gpcd_df = generate_gpcd_data()
    
    # Save to CSV files
    snowpack_df.to_csv('snowpack_data.csv', index=False)
    reservoir_df.to_csv('reservoir_data.csv', index=False)
    deliveries_df.to_csv('water_deliveries.csv', index=False)
    hydropower_df.to_csv('hydropower_data.csv', index=False)
    conservation_df.to_csv('conservation_programs.csv', index=False)
    gpcd_df.to_csv('gpcd_trends.csv', index=False)
    
    print("✅ All datasets generated successfully!")
    print(f"📊 Snowpack data: {len(snowpack_df)} records")
    print(f"🏔️ Reservoir data: {len(reservoir_df)} records")
    print(f"💧 Water deliveries: {len(deliveries_df)} records")
    print(f"⚡ Hydropower data: {len(hydropower_df)} records")
    print(f"🌱 Conservation data: {len(conservation_df)} records")
    print(f"📈 GPCD trends: {len(gpcd_df)} records")
