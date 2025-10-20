# Utah Water Conservation Analysis

A comprehensive data analysis and visualization project showcasing water conservation analytics for the Central Utah Water Conservancy District (CUWCD) 2024 Annual Report.

## 🎯 Project Overview

This project demonstrates advanced data analysis skills through the examination of Utah's water resources, including:

- **Snowpack Analysis**: Jordan & Lower Green River Basin snow water equivalent trends
- **Reservoir Operations**: Storage levels and capacity management for major Utah reservoirs
- **Water Deliveries**: CUP & CWP delivery patterns and customer analysis
- **Conservation Programs**: Effectiveness of water-saving initiatives and rebate programs
- **GPCD Trends**: Gallons per capita per day trends showing conservation progress
- **Hydropower Generation**: Renewable energy production from water infrastructure

## 📊 Datasets Included

### 1. Snowpack Data
- Daily Snow Water Equivalent (SWE) measurements
- Percent of 30-year median comparisons
- Jordan River Basin (135% of median in 2024)
- Lower Green River Basin (131% of median in 2024)

### 2. Reservoir Data
- Storage levels and capacity percentages
- Fill/spill volume tracking
- Major reservoirs: Strawberry, Jordanelle, Utah Lake
- Real-time operational data

### 3. Water Deliveries
- Monthly delivery volumes by customer
- Municipal vs. wholesale customer analysis
- CUP & CWP system performance
- Seasonal delivery patterns

### 4. Conservation Programs
- Turf removal program participation (609 participants, 612,621 sq ft)
- Smart irrigation controller rebates (1,493 units)
- High-efficiency toilet rebates (313 units)
- Drip irrigation conversions (95,161 sq ft)

### 5. GPCD Trends
- County-level water use metrics
- Conservation progress tracking (2018-2024)
- Utah County focus analysis
- Statewide comparison data

### 6. Hydropower Generation
- Daily generation from Olmsted and Jordanelle facilities
- Capacity factor analysis
- Renewable energy production tracking

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Required packages (see requirements.txt)

### Installation

1. **Clone or download the project files**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Generate sample datasets:**
   ```bash
   python data_generator.py
   ```

4. **Run the analysis:**
   ```bash
   python water_analysis.py
   ```

## 📈 Analysis Features

### Static Visualizations
- **Snowpack Trends**: Seasonal patterns and peak analysis
- **Reservoir Operations**: Capacity trends and spill event tracking
- **Water Deliveries**: Customer analysis and seasonal patterns
- **Conservation Programs**: Participation and effectiveness metrics
- **GPCD Trends**: Conservation progress and county comparisons

### Interactive Dashboard
- **Plotly-based dashboard** with multiple interactive charts
- **Real-time data exploration** capabilities
- **Exportable HTML report** for presentations

### Key Insights Generated
- Snowpack performance above historical averages
- Reservoir capacity optimization opportunities
- Conservation program ROI analysis
- Water use efficiency trends
- System optimization recommendations

## 🎨 Visualization Examples

### 1. Snowpack Analysis
- Daily SWE trends with seasonal patterns
- Percent of median comparisons
- Peak snowpack identification
- Monthly distribution analysis

### 2. Reservoir Operations
- Capacity trends over time
- Current storage levels
- Spill event analysis
- Storage efficiency metrics

### 3. Conservation Impact
- Program participation rates
- Water savings quantification
- Cost-effectiveness analysis
- Area conversion tracking

### 4. GPCD Progress
- County-level trends
- Conservation success metrics
- Benchmark comparisons
- Progress visualization

## 📋 Technical Skills Demonstrated

### Data Analysis
- **Pandas**: Data manipulation and analysis
- **NumPy**: Statistical calculations
- **SciPy**: Advanced statistical analysis
- **Scikit-learn**: Machine learning applications

### Visualization
- **Matplotlib**: Static plot creation
- **Seaborn**: Statistical visualizations
- **Plotly**: Interactive dashboards
- **Custom styling**: Professional presentation

### Data Engineering
- **Data generation**: Realistic synthetic datasets
- **Data cleaning**: Quality assurance processes
- **Feature engineering**: Derived metrics and KPIs
- **Data validation**: Consistency checks

### Business Intelligence
- **KPI development**: Key performance indicators
- **Trend analysis**: Time series analysis
- **Comparative analysis**: Benchmark comparisons
- **Executive reporting**: Summary dashboards

## 🎯 Business Value

### For Water Conservation Companies
- **Performance Metrics**: Quantifiable conservation results
- **ROI Analysis**: Program effectiveness measurement
- **Trend Identification**: Long-term pattern recognition
- **Optimization Opportunities**: System efficiency improvements

### For Stakeholders
- **Transparency**: Clear data visualization
- **Accountability**: Measurable outcomes
- **Decision Support**: Data-driven insights
- **Progress Tracking**: Conservation goal monitoring

## 📁 File Structure

```
water-conservation-analysis/
├── data_generator.py          # Dataset creation
├── water_analysis.py          # Main analysis script
├── requirements.txt           # Python dependencies
├── README.md                 # Project documentation
├── snowpack_data.csv         # Generated snowpack data
├── reservoir_data.csv        # Generated reservoir data
├── water_deliveries.csv      # Generated delivery data
├── hydropower_data.csv       # Generated power data
├── conservation_programs.csv # Generated conservation data
├── gpcd_trends.csv          # Generated GPCD data
└── output/                  # Generated visualizations
    ├── snowpack_analysis.png
    ├── reservoir_analysis.png
    ├── water_deliveries_analysis.png
    ├── conservation_analysis.png
    ├── gpcd_analysis.png
    └── water_conservation_dashboard.html
```

## 🔧 Customization

### Adding New Datasets
1. Modify `data_generator.py` to include new data sources
2. Update `water_analysis.py` to include new analysis methods
3. Add corresponding visualization functions

### Modifying Visualizations
- Update color schemes in the analysis functions
- Modify chart types and layouts
- Add new interactive features to the dashboard

### Extending Analysis
- Add machine learning predictions
- Include more sophisticated statistical analysis
- Implement real-time data connections

## 📊 Sample Output

The analysis generates:
- **5 static visualization files** (PNG format)
- **1 interactive dashboard** (HTML format)
- **Console output** with summary statistics
- **Executive summary** with key insights

## 🎓 Learning Outcomes

This project demonstrates:
- **Data Science Pipeline**: End-to-end analysis workflow
- **Water Resource Management**: Domain-specific knowledge
- **Visualization Best Practices**: Professional presentation
- **Business Communication**: Executive-level reporting
- **Technical Documentation**: Clear code organization

## 🤝 Contributing

Feel free to:
- Add new analysis methods
- Improve visualizations
- Enhance data generation
- Extend documentation

## 📞 Contact

For questions about this analysis or to discuss water conservation data science opportunities, please reach out through the portfolio contact form.

---

**Note**: This project uses synthetic data based on publicly available CUWCD 2024 Annual Report information. For production use, connect to actual data sources through the referenced APIs and data portals.
