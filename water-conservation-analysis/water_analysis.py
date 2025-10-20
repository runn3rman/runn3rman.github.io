"""
Utah Water Conservation Analysis Dashboard
Comprehensive data analysis and visualization for CUWCD 2024 data
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class WaterConservationAnalyzer:
    def __init__(self):
        self.snowpack_data = None
        self.reservoir_data = None
        self.deliveries_data = None
        self.hydropower_data = None
        self.conservation_data = None
        self.gpcd_data = None
        
    def load_data(self):
        """Load all datasets"""
        try:
            self.snowpack_data = pd.read_csv('snowpack_data.csv', parse_dates=['Date'])
            self.reservoir_data = pd.read_csv('reservoir_data.csv', parse_dates=['Date'])
            self.deliveries_data = pd.read_csv('water_deliveries.csv', parse_dates=['Month'])
            self.hydropower_data = pd.read_csv('hydropower_data.csv', parse_dates=['Date'])
            self.conservation_data = pd.read_csv('conservation_programs.csv')
            self.gpcd_data = pd.read_csv('gpcd_trends.csv')
            print("✅ All datasets loaded successfully!")
        except FileNotFoundError as e:
            print(f"❌ Error loading data: {e}")
            print("Please run data_generator.py first to create the datasets.")
    
    def analyze_snowpack_trends(self):
        """Analyze snowpack trends and create visualizations"""
        if self.snowpack_data is None:
            return
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Utah Snowpack Analysis 2024', fontsize=16, fontweight='bold')
        
        # 1. Daily SWE trends
        axes[0,0].plot(self.snowpack_data['Date'], self.snowpack_data['Jordan_SWE_inches'], 
                      label='Jordan River Basin', linewidth=2, color='#2563eb')
        axes[0,0].plot(self.snowpack_data['Date'], self.snowpack_data['Green_SWE_inches'], 
                      label='Lower Green River Basin', linewidth=2, color='#7c3aed')
        axes[0,0].set_title('Snow Water Equivalent (SWE) Trends')
        axes[0,0].set_ylabel('SWE (inches)')
        axes[0,0].legend()
        axes[0,0].grid(True, alpha=0.3)
        
        # 2. Percent of median comparison
        axes[0,1].plot(self.snowpack_data['Date'], self.snowpack_data['Jordan_Percent_Median'], 
                      label='Jordan River Basin (135% avg)', linewidth=2, color='#2563eb')
        axes[0,1].plot(self.snowpack_data['Date'], self.snowpack_data['Green_Percent_Median'], 
                      label='Lower Green River Basin (131% avg)', linewidth=2, color='#7c3aed')
        axes[0,1].axhline(y=100, color='red', linestyle='--', alpha=0.7, label='30-year Median')
        axes[0,1].set_title('Percent of 30-Year Median')
        axes[0,1].set_ylabel('Percent (%)')
        axes[0,1].legend()
        axes[0,1].grid(True, alpha=0.3)
        
        # 3. Peak snowpack analysis
        jordan_peak = self.snowpack_data['Jordan_SWE_inches'].max()
        green_peak = self.snowpack_data['Green_SWE_inches'].max()
        
        basins = ['Jordan River', 'Lower Green River']
        peaks = [jordan_peak, green_peak]
        colors = ['#2563eb', '#7c3aed']
        
        bars = axes[1,0].bar(basins, peaks, color=colors, alpha=0.8)
        axes[1,0].set_title('Peak Snowpack 2024')
        axes[1,0].set_ylabel('Peak SWE (inches)')
        
        # Add value labels on bars
        for bar, peak in zip(bars, peaks):
            axes[1,0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                          f'{peak:.1f}"', ha='center', va='bottom', fontweight='bold')
        
        # 4. Seasonal distribution
        self.snowpack_data['Month'] = self.snowpack_data['Date'].dt.month
        monthly_avg = self.snowpack_data.groupby('Month')[['Jordan_SWE_inches', 'Green_SWE_inches']].mean()
        
        x = np.arange(len(monthly_avg.index))
        width = 0.35
        
        axes[1,1].bar(x - width/2, monthly_avg['Jordan_SWE_inches'], width, 
                     label='Jordan River', color='#2563eb', alpha=0.8)
        axes[1,1].bar(x + width/2, monthly_avg['Green_SWE_inches'], width, 
                     label='Lower Green River', color='#7c3aed', alpha=0.8)
        
        axes[1,1].set_title('Average Monthly SWE Distribution')
        axes[1,1].set_ylabel('Average SWE (inches)')
        axes[1,1].set_xlabel('Month')
        axes[1,1].set_xticks(x)
        axes[1,1].set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
        axes[1,1].legend()
        axes[1,1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('snowpack_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Summary statistics
        print("\n📊 SNOWPACK ANALYSIS SUMMARY")
        print("=" * 50)
        print(f"Jordan River Basin - Peak SWE: {jordan_peak:.1f} inches")
        print(f"Lower Green River Basin - Peak SWE: {green_peak:.1f} inches")
        print(f"Jordan River - Average % of Median: {self.snowpack_data['Jordan_Percent_Median'].mean():.1f}%")
        print(f"Lower Green River - Average % of Median: {self.snowpack_data['Green_Percent_Median'].mean():.1f}%")
    
    def analyze_reservoir_operations(self):
        """Analyze reservoir levels and operations"""
        if self.reservoir_data is None:
            return
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Utah Reservoir Operations Analysis 2024', fontsize=16, fontweight='bold')
        
        # 1. Reservoir capacity trends
        for reservoir in self.reservoir_data['Reservoir'].unique():
            data = self.reservoir_data[self.reservoir_data['Reservoir'] == reservoir]
            axes[0,0].plot(data['Date'], data['Percent_Capacity'], 
                          label=reservoir, linewidth=2, marker='o', markersize=3)
        
        axes[0,0].set_title('Reservoir Capacity Over Time')
        axes[0,0].set_ylabel('Percent of Capacity (%)')
        axes[0,0].legend()
        axes[0,0].grid(True, alpha=0.3)
        axes[0,0].axhline(y=100, color='red', linestyle='--', alpha=0.7, label='Full Capacity')
        
        # 2. Current storage levels
        current_data = self.reservoir_data.groupby('Reservoir').last()
        colors = ['#2563eb', '#7c3aed', '#fbbf24']
        
        bars = axes[0,1].bar(current_data.index, current_data['Percent_Capacity'], 
                            color=colors, alpha=0.8)
        axes[0,1].set_title('Current Reservoir Levels (End of 2024)')
        axes[0,1].set_ylabel('Percent of Capacity (%)')
        axes[0,1].set_ylim(0, 105)
        
        # Add value labels
        for bar, value in zip(bars, current_data['Percent_Capacity']):
            axes[0,1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                          f'{value:.1f}%', ha='center', va='bottom', fontweight='bold')
        
        # 3. Storage capacity comparison
        capacity_data = self.reservoir_data.groupby('Reservoir')['Capacity_AF'].first()
        storage_data = self.reservoir_data.groupby('Reservoir')['Storage_AF'].mean()
        
        x = np.arange(len(capacity_data.index))
        width = 0.35
        
        axes[1,0].bar(x - width/2, capacity_data.values, width, 
                     label='Total Capacity', color='lightblue', alpha=0.7)
        axes[1,0].bar(x + width/2, storage_data.values, width, 
                     label='Average Storage', color='darkblue', alpha=0.8)
        
        axes[1,0].set_title('Reservoir Capacity vs Average Storage')
        axes[1,0].set_ylabel('Storage (Acre-Feet)')
        axes[1,0].set_xticks(x)
        axes[1,0].set_xticklabels(capacity_data.index, rotation=45)
        axes[1,0].legend()
        axes[1,0].grid(True, alpha=0.3)
        
        # 4. Spill events analysis
        spill_data = self.reservoir_data.groupby(['Reservoir', 'Date']).agg({
            'Spill_Event': 'sum'
        }).reset_index()
        spill_summary = spill_data.groupby('Reservoir')['Spill_Event'].sum()
        
        if spill_summary.sum() > 0:
            axes[1,1].bar(spill_summary.index, spill_summary.values, 
                         color=['#ff6b6b', '#4ecdc4', '#45b7d1'], alpha=0.8)
            axes[1,1].set_title('Spill Events by Reservoir')
            axes[1,1].set_ylabel('Number of Spill Events')
        else:
            axes[1,1].text(0.5, 0.5, 'No Spill Events\nin 2024', 
                          ha='center', va='center', transform=axes[1,1].transAxes,
                          fontsize=14, fontweight='bold')
            axes[1,1].set_title('Spill Events by Reservoir')
        
        plt.tight_layout()
        plt.savefig('reservoir_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Summary statistics
        print("\n🏔️ RESERVOIR ANALYSIS SUMMARY")
        print("=" * 50)
        for reservoir in self.reservoir_data['Reservoir'].unique():
            data = self.reservoir_data[self.reservoir_data['Reservoir'] == reservoir]
            avg_capacity = data['Percent_Capacity'].mean()
            max_capacity = data['Percent_Capacity'].max()
            print(f"{reservoir}: Avg {avg_capacity:.1f}%, Peak {max_capacity:.1f}%")
    
    def analyze_water_deliveries(self):
        """Analyze water delivery patterns"""
        if self.deliveries_data is None:
            return
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Water Delivery Analysis 2024', fontsize=16, fontweight='bold')
        
        # 1. Monthly delivery trends
        monthly_deliveries = self.deliveries_data.groupby('Month')['Delivery_AF'].sum()
        axes[0,0].plot(monthly_deliveries.index, monthly_deliveries.values, 
                      linewidth=3, marker='o', markersize=6, color='#2563eb')
        axes[0,0].set_title('Total Monthly Water Deliveries')
        axes[0,0].set_ylabel('Delivery (Acre-Feet)')
        axes[0,0].grid(True, alpha=0.3)
        
        # 2. Top customers by delivery volume
        customer_totals = self.deliveries_data.groupby('Customer')['Delivery_AF'].sum().sort_values(ascending=True)
        top_customers = customer_totals.tail(10)
        
        bars = axes[0,1].barh(range(len(top_customers)), top_customers.values, 
                             color='#7c3aed', alpha=0.8)
        axes[0,1].set_yticks(range(len(top_customers)))
        axes[0,1].set_yticklabels(top_customers.index)
        axes[0,1].set_title('Top 10 Customers by Annual Delivery')
        axes[0,1].set_xlabel('Annual Delivery (Acre-Feet)')
        
        # Add value labels
        for i, (bar, value) in enumerate(zip(bars, top_customers.values)):
            axes[0,1].text(bar.get_width() + 100, bar.get_y() + bar.get_height()/2,
                          f'{value:,.0f}', ha='left', va='center', fontweight='bold')
        
        # 3. Customer type analysis
        type_analysis = self.deliveries_data.groupby('Customer_Type')['Delivery_AF'].sum()
        colors = ['#fbbf24', '#2563eb']
        
        wedges, texts, autotexts = axes[1,0].pie(type_analysis.values, labels=type_analysis.index,
                                                autopct='%1.1f%%', colors=colors, startangle=90)
        axes[1,0].set_title('Deliveries by Customer Type')
        
        # 4. Seasonal delivery patterns by customer type
        seasonal_data = self.deliveries_data.groupby(['Month', 'Customer_Type'])['Delivery_AF'].sum().unstack()
        seasonal_data.plot(kind='bar', ax=axes[1,1], color=['#fbbf24', '#2563eb'], alpha=0.8)
        axes[1,1].set_title('Seasonal Delivery Patterns by Customer Type')
        axes[1,1].set_ylabel('Delivery (Acre-Feet)')
        axes[1,1].set_xlabel('Month')
        axes[1,1].legend(title='Customer Type')
        axes[1,1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('water_deliveries_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Summary statistics
        print("\n💧 WATER DELIVERY ANALYSIS SUMMARY")
        print("=" * 50)
        total_deliveries = self.deliveries_data['Delivery_AF'].sum()
        print(f"Total Annual Deliveries: {total_deliveries:,.0f} Acre-Feet")
        print(f"Average Monthly Delivery: {total_deliveries/12:,.0f} Acre-Feet")
        print(f"Peak Month: {monthly_deliveries.idxmax().strftime('%B')} ({monthly_deliveries.max():,.0f} AF)")
        print(f"Top Customer: {customer_totals.index[-1]} ({customer_totals.iloc[-1]:,.0f} AF)")
    
    def analyze_conservation_programs(self):
        """Analyze conservation program effectiveness"""
        if self.conservation_data is None:
            return
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Water Conservation Programs Analysis 2024', fontsize=16, fontweight='bold')
        
        # 1. Program participation
        program_stats = self.conservation_data.groupby('Program').agg({
            'Participant_ID': 'count',
            'Water_Saved_AF': 'sum',
            'Area_SqFt': 'sum'
        }).reset_index()
        
        bars = axes[0,0].bar(program_stats['Program'], program_stats['Participant_ID'], 
                            color=['#2563eb', '#7c3aed', '#fbbf24', '#4ecdc4'], alpha=0.8)
        axes[0,0].set_title('Program Participation')
        axes[0,0].set_ylabel('Number of Participants')
        axes[0,0].tick_params(axis='x', rotation=45)
        
        # Add value labels
        for bar, value in zip(bars, program_stats['Participant_ID']):
            axes[0,0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 10,
                          f'{value}', ha='center', va='bottom', fontweight='bold')
        
        # 2. Water savings by program
        bars = axes[0,1].bar(program_stats['Program'], program_stats['Water_Saved_AF'], 
                            color=['#2563eb', '#7c3aed', '#fbbf24', '#4ecdc4'], alpha=0.8)
        axes[0,1].set_title('Water Savings by Program')
        axes[0,1].set_ylabel('Water Saved (Acre-Feet)')
        axes[0,1].tick_params(axis='x', rotation=45)
        
        # Add value labels
        for bar, value in zip(bars, program_stats['Water_Saved_AF']):
            axes[0,1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                          f'{value:.1f}', ha='center', va='bottom', fontweight='bold')
        
        # 3. Cost-effectiveness analysis
        program_stats['Cost_Per_AF'] = program_stats['Water_Saved_AF'] / program_stats['Participant_ID']
        program_stats['Rebate_Per_AF'] = (program_stats['Participant_ID'] * 100) / program_stats['Water_Saved_AF']
        
        bars = axes[1,0].bar(program_stats['Program'], program_stats['Cost_Per_AF'], 
                            color=['#2563eb', '#7c3aed', '#fbbf24', '#4ecdc4'], alpha=0.8)
        axes[1,0].set_title('Water Savings per Participant')
        axes[1,0].set_ylabel('AF per Participant')
        axes[1,0].tick_params(axis='x', rotation=45)
        
        # 4. Area converted analysis
        area_programs = program_stats[program_stats['Area_SqFt'] > 0]
        if not area_programs.empty:
            bars = axes[1,1].bar(area_programs['Program'], area_programs['Area_SqFt'], 
                                color=['#2563eb', '#4ecdc4'], alpha=0.8)
            axes[1,1].set_title('Area Converted by Program')
            axes[1,1].set_ylabel('Area (Square Feet)')
            axes[1,1].tick_params(axis='x', rotation=45)
            
            # Add value labels
            for bar, value in zip(bars, area_programs['Area_SqFt']):
                axes[1,1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1000,
                              f'{value:,.0f}', ha='center', va='bottom', fontweight='bold')
        else:
            axes[1,1].text(0.5, 0.5, 'No Area Data\nAvailable', 
                          ha='center', va='center', transform=axes[1,1].transAxes,
                          fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        plt.savefig('conservation_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Summary statistics
        print("\n🌱 CONSERVATION PROGRAMS SUMMARY")
        print("=" * 50)
        total_participants = program_stats['Participant_ID'].sum()
        total_water_saved = program_stats['Water_Saved_AF'].sum()
        total_area = program_stats['Area_SqFt'].sum()
        
        print(f"Total Participants: {total_participants:,}")
        print(f"Total Water Saved: {total_water_saved:.1f} Acre-Feet")
        print(f"Total Area Converted: {total_area:,.0f} Square Feet")
        print(f"Average Water Saved per Participant: {total_water_saved/total_participants:.2f} AF")
    
    def analyze_gpcd_trends(self):
        """Analyze GPCD trends and conservation progress"""
        if self.gpcd_data is None:
            return
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('GPCD Trends and Conservation Progress', fontsize=16, fontweight='bold')
        
        # 1. GPCD trends by county
        for county in self.gpcd_data['County'].unique():
            county_data = self.gpcd_data[self.gpcd_data['County'] == county]
            axes[0,0].plot(county_data['Year'], county_data['GPCD'], 
                          label=county, linewidth=2, marker='o', markersize=4)
        
        axes[0,0].set_title('GPCD Trends by County (2018-2024)')
        axes[0,0].set_ylabel('Gallons Per Capita Per Day')
        axes[0,0].set_xlabel('Year')
        axes[0,0].legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        axes[0,0].grid(True, alpha=0.3)
        
        # 2. Utah County focus
        utah_county_data = self.gpcd_data[self.gpcd_data['County'] == 'Utah County']
        axes[0,1].plot(utah_county_data['Year'], utah_county_data['GPCD'], 
                      linewidth=3, marker='o', markersize=8, color='#2563eb')
        axes[0,1].set_title('Utah County GPCD Trend')
        axes[0,1].set_ylabel('GPCD')
        axes[0,1].set_xlabel('Year')
        axes[0,1].grid(True, alpha=0.3)
        
        # Add trend line
        z = np.polyfit(utah_county_data['Year'], utah_county_data['GPCD'], 1)
        p = np.poly1d(z)
        axes[0,1].plot(utah_county_data['Year'], p(utah_county_data['Year']), 
                      "r--", alpha=0.8, linewidth=2, label=f'Trend: {z[0]:.1f} GPCD/year')
        axes[0,1].legend()
        
        # 3. Current GPCD comparison
        current_gpcd = self.gpcd_data[self.gpcd_data['Year'] == 2024].sort_values('GPCD')
        colors = ['#2563eb' if county == 'Utah County' else '#7c3aed' 
                 for county in current_gpcd['County']]
        
        bars = axes[1,0].barh(range(len(current_gpcd)), current_gpcd['GPCD'], color=colors, alpha=0.8)
        axes[1,0].set_yticks(range(len(current_gpcd)))
        axes[1,0].set_yticklabels(current_gpcd['County'])
        axes[1,0].set_title('2024 GPCD by County')
        axes[1,0].set_xlabel('GPCD')
        
        # Add value labels
        for i, (bar, value) in enumerate(zip(bars, current_gpcd['GPCD'])):
            axes[1,0].text(bar.get_width() + 2, bar.get_y() + bar.get_height()/2,
                          f'{value:.0f}', ha='left', va='center', fontweight='bold')
        
        # 4. Conservation progress
        progress_data = self.gpcd_data.groupby('Year')['GPCD'].mean()
        progress_pct = ((progress_data.iloc[0] - progress_data.iloc[-1]) / progress_data.iloc[0]) * 100
        
        axes[1,1].plot(progress_data.index, progress_data.values, 
                      linewidth=3, marker='o', markersize=8, color='#4ecdc4')
        axes[1,1].set_title(f'Statewide GPCD Progress\n({progress_pct:.1f}% Reduction)')
        axes[1,1].set_ylabel('Average GPCD')
        axes[1,1].set_xlabel('Year')
        axes[1,1].grid(True, alpha=0.3)
        
        # Add progress annotation
        axes[1,1].annotate(f'{progress_pct:.1f}% Reduction\n2018-2024', 
                          xy=(2021, progress_data.iloc[2]), 
                          xytext=(2019, progress_data.iloc[0] - 5),
                          arrowprops=dict(arrowstyle='->', color='red', lw=2),
                          fontsize=12, fontweight='bold', color='red')
        
        plt.tight_layout()
        plt.savefig('gpcd_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Summary statistics
        print("\n📈 GPCD TRENDS SUMMARY")
        print("=" * 50)
        utah_county_2024 = utah_county_data[utah_county_data['Year'] == 2024]['GPCD'].iloc[0]
        utah_county_2018 = utah_county_data[utah_county_data['Year'] == 2018]['GPCD'].iloc[0]
        utah_reduction = ((utah_county_2018 - utah_county_2024) / utah_county_2018) * 100
        
        print(f"Utah County 2024 GPCD: {utah_county_2024:.0f}")
        print(f"Utah County 2018 GPCD: {utah_county_2018:.0f}")
        print(f"Utah County Reduction: {utah_reduction:.1f}%")
        print(f"Statewide Average 2024: {progress_data.iloc[-1]:.0f} GPCD")
        print(f"Statewide Progress: {progress_pct:.1f}% reduction since 2018")
    
    def create_interactive_dashboard(self):
        """Create an interactive Plotly dashboard"""
        if any(data is None for data in [self.snowpack_data, self.reservoir_data, 
                                        self.deliveries_data, self.conservation_data]):
            print("❌ Please load all datasets first")
            return
        
        # Create subplots
        fig = make_subplots(
            rows=3, cols=2,
            subplot_titles=('Snowpack Trends', 'Reservoir Levels', 
                          'Water Deliveries', 'Conservation Programs',
                          'GPCD Trends', 'Hydropower Generation'),
            specs=[[{"secondary_y": False}, {"secondary_y": False}],
                   [{"secondary_y": False}, {"secondary_y": False}],
                   [{"secondary_y": False}, {"secondary_y": False}]]
        )
        
        # 1. Snowpack trends
        fig.add_trace(
            go.Scatter(x=self.snowpack_data['Date'], y=self.snowpack_data['Jordan_SWE_inches'],
                      name='Jordan River SWE', line=dict(color='#2563eb')),
            row=1, col=1
        )
        fig.add_trace(
            go.Scatter(x=self.snowpack_data['Date'], y=self.snowpack_data['Green_SWE_inches'],
                      name='Lower Green River SWE', line=dict(color='#7c3aed')),
            row=1, col=1
        )
        
        # 2. Reservoir levels
        for reservoir in self.reservoir_data['Reservoir'].unique():
            data = self.reservoir_data[self.reservoir_data['Reservoir'] == reservoir]
            fig.add_trace(
                go.Scatter(x=data['Date'], y=data['Percent_Capacity'],
                          name=f'{reservoir} Capacity', line=dict(width=2)),
                row=1, col=2
            )
        
        # 3. Water deliveries
        monthly_deliveries = self.deliveries_data.groupby('Month')['Delivery_AF'].sum()
        fig.add_trace(
            go.Bar(x=monthly_deliveries.index, y=monthly_deliveries.values,
                   name='Monthly Deliveries', marker_color='#fbbf24'),
            row=2, col=1
        )
        
        # 4. Conservation programs
        program_stats = self.conservation_data.groupby('Program')['Water_Saved_AF'].sum()
        fig.add_trace(
            go.Bar(x=program_stats.index, y=program_stats.values,
                   name='Water Saved by Program', marker_color='#4ecdc4'),
            row=2, col=2
        )
        
        # 5. GPCD trends
        utah_county_data = self.gpcd_data[self.gpcd_data['County'] == 'Utah County']
        fig.add_trace(
            go.Scatter(x=utah_county_data['Year'], y=utah_county_data['GPCD'],
                      name='Utah County GPCD', line=dict(color='#2563eb', width=3)),
            row=3, col=1
        )
        
        # 6. Hydropower generation
        for plant in self.hydropower_data['Plant'].unique():
            data = self.hydropower_data[self.hydropower_data['Plant'] == plant]
            monthly_power = data.groupby(data['Date'].dt.to_period('M'))['Generation_MWh'].sum()
            fig.add_trace(
                go.Scatter(x=monthly_power.index.astype(str), y=monthly_power.values,
                          name=f'{plant} Generation', line=dict(width=2)),
                row=3, col=2
            )
        
        # Update layout
        fig.update_layout(
            title_text="Utah Water Conservation Dashboard 2024",
            title_x=0.5,
            height=1200,
            showlegend=True,
            template="plotly_white"
        )
        
        # Save and show
        fig.write_html("water_conservation_dashboard.html")
        fig.show()
        
        print("✅ Interactive dashboard created: water_conservation_dashboard.html")
    
    def generate_executive_summary(self):
        """Generate an executive summary report"""
        if any(data is None for data in [self.snowpack_data, self.reservoir_data, 
                                        self.deliveries_data, self.conservation_data, self.gpcd_data]):
            print("❌ Please load all datasets first")
            return
        
        print("\n" + "="*80)
        print("UTAH WATER CONSERVATION ANALYSIS - EXECUTIVE SUMMARY 2024")
        print("="*80)
        
        # Snowpack summary
        jordan_avg = self.snowpack_data['Jordan_Percent_Median'].mean()
        green_avg = self.snowpack_data['Green_Percent_Median'].mean()
        print(f"\n❄️  SNOWPACK PERFORMANCE:")
        print(f"   • Jordan River Basin: {jordan_avg:.1f}% of 30-year median")
        print(f"   • Lower Green River Basin: {green_avg:.1f}% of 30-year median")
        print(f"   • Both basins exceeded normal levels, indicating strong water supply")
        
        # Reservoir summary
        reservoir_summary = self.reservoir_data.groupby('Reservoir')['Percent_Capacity'].mean()
        print(f"\n🏔️  RESERVOIR STATUS:")
        for reservoir, capacity in reservoir_summary.items():
            print(f"   • {reservoir}: {capacity:.1f}% average capacity")
        
        # Delivery summary
        total_deliveries = self.deliveries_data['Delivery_AF'].sum()
        print(f"\n💧  WATER DELIVERIES:")
        print(f"   • Total annual deliveries: {total_deliveries:,.0f} acre-feet")
        print(f"   • Average monthly delivery: {total_deliveries/12:,.0f} acre-feet")
        
        # Conservation summary
        total_water_saved = self.conservation_data['Water_Saved_AF'].sum()
        total_participants = self.conservation_data['Participant_ID'].nunique()
        print(f"\n🌱  CONSERVATION PROGRAMS:")
        print(f"   • Total participants: {total_participants:,}")
        print(f"   • Total water saved: {total_water_saved:.1f} acre-feet")
        print(f"   • Average savings per participant: {total_water_saved/total_participants:.2f} AF")
        
        # GPCD summary
        utah_county_2024 = self.gpcd_data[(self.gpcd_data['County'] == 'Utah County') & 
                                         (self.gpcd_data['Year'] == 2024)]['GPCD'].iloc[0]
        utah_county_2018 = self.gpcd_data[(self.gpcd_data['County'] == 'Utah County') & 
                                         (self.gpcd_data['Year'] == 2018)]['GPCD'].iloc[0]
        reduction = ((utah_county_2018 - utah_county_2024) / utah_county_2018) * 100
        
        print(f"\n📈  CONSERVATION PROGRESS:")
        print(f"   • Utah County GPCD 2024: {utah_county_2024:.0f}")
        print(f"   • Reduction since 2018: {reduction:.1f}%")
        print(f"   • Demonstrates effective conservation efforts")
        
        print(f"\n🎯  KEY INSIGHTS:")
        print(f"   • Strong snowpack performance supports water security")
        print(f"   • Reservoir levels remain healthy across all facilities")
        print(f"   • Conservation programs show measurable water savings")
        print(f"   • GPCD trends indicate successful conservation education")
        print(f"   • System optimization opportunities exist for efficiency gains")
        
        print("\n" + "="*80)

def main():
    """Main analysis function"""
    print("🚀 Starting Utah Water Conservation Analysis...")
    
    # Initialize analyzer
    analyzer = WaterConservationAnalyzer()
    
    # Load data
    analyzer.load_data()
    
    if all(data is not None for data in [analyzer.snowpack_data, analyzer.reservoir_data, 
                                        analyzer.deliveries_data, analyzer.conservation_data, 
                                        analyzer.gpcd_data]):
        
        # Run all analyses
        print("\n📊 Running comprehensive analysis...")
        analyzer.analyze_snowpack_trends()
        analyzer.analyze_reservoir_operations()
        analyzer.analyze_water_deliveries()
        analyzer.analyze_conservation_programs()
        analyzer.analyze_gpcd_trends()
        
        # Create interactive dashboard
        print("\n🎨 Creating interactive dashboard...")
        analyzer.create_interactive_dashboard()
        
        # Generate executive summary
        analyzer.generate_executive_summary()
        
        print("\n✅ Analysis complete! Check the generated files:")
        print("   • snowpack_analysis.png")
        print("   • reservoir_analysis.png") 
        print("   • water_deliveries_analysis.png")
        print("   • conservation_analysis.png")
        print("   • gpcd_analysis.png")
        print("   • water_conservation_dashboard.html")
        
    else:
        print("❌ Please run data_generator.py first to create the datasets")

if __name__ == "__main__":
    main()
