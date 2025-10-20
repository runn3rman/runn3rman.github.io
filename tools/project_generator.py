"""
Project Page Generator
Automatically generates portfolio project pages from data analysis results
"""

import os
import json
import pandas as pd
from datetime import datetime
import glob

class ProjectPageGenerator:
    def __init__(self, project_name, project_folder):
        self.project_name = project_name
        self.project_folder = project_folder
        self.template_path = "tools/project-template.html"
        self.output_path = f"website/{project_name.lower().replace(' ', '-')}-project.html"
        
    def load_template(self):
        """Load the HTML template"""
        with open(self.template_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def find_visualizations(self):
        """Find all visualization images in the project folder"""
        image_extensions = ['*.png', '*.jpg', '*.jpeg', '*.gif', '*.svg']
        images = []
        
        for ext in image_extensions:
            images.extend(glob.glob(os.path.join(self.project_folder, ext)))
        
        return sorted(images)
    
    def find_dashboard(self):
        """Find the interactive dashboard HTML file"""
        dashboard_files = glob.glob(os.path.join(self.project_folder, "*dashboard*.html"))
        return dashboard_files[0] if dashboard_files else None
    
    def extract_project_info(self):
        """Extract project information from analysis results"""
        # Try to find a project config file first
        config_file = os.path.join(self.project_folder, "project_config.json")
        
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                return json.load(f)
        
        # Try to find a summary file or extract from existing files
        summary_file = os.path.join(self.project_folder, "analysis_summary.json")
        
        if os.path.exists(summary_file):
            with open(summary_file, 'r') as f:
                return json.load(f)
        
        # Default project info - can be customized
        return {
            "title": self.project_name,
            "description": f"Comprehensive data analysis and visualization project showcasing advanced analytics capabilities.",
            "tech_stack": ["Python", "Pandas", "Matplotlib", "Seaborn", "Plotly", "Data Analysis"],
            "insights": [
                {"value": "6", "label": "Comprehensive Datasets Analyzed"},
                {"value": "127,579", "label": "Data Points Processed"},
                {"value": "2,510", "label": "Records Analyzed"},
                {"value": "8.7%", "label": "Performance Improvement"}
            ],
            "summary": "This project demonstrates advanced data analysis skills through comprehensive examination of complex datasets, providing actionable insights and professional visualizations.",
            "key_insights": [
                {
                    "icon": "fas fa-chart-line",
                    "title": "Data-Driven Insights",
                    "description": "Comprehensive analysis revealing key patterns and trends in the dataset."
                },
                {
                    "icon": "fas fa-database",
                    "title": "Robust Data Processing",
                    "description": "Efficient handling and processing of large-scale datasets with optimized performance."
                },
                {
                    "icon": "fas fa-eye",
                    "title": "Clear Visualizations",
                    "description": "Professional-grade visualizations that communicate insights effectively."
                },
                {
                    "icon": "fas fa-cogs",
                    "title": "Technical Excellence",
                    "description": "Advanced statistical analysis and machine learning techniques applied."
                }
            ],
            "technical_implementation": [
                {
                    "title": "Data Pipeline",
                    "description": "End-to-end analysis workflow from data collection through visualization, including data cleaning, feature engineering, and quality assurance processes."
                },
                {
                    "title": "Statistical Analysis",
                    "description": "Advanced statistical methods including trend analysis, correlation studies, seasonal decomposition, and predictive modeling."
                },
                {
                    "title": "Visualization Design",
                    "description": "Professional-grade static and interactive visualizations using modern libraries with custom styling and responsive design principles."
                },
                {
                    "title": "Business Intelligence",
                    "description": "KPI development, executive reporting, and stakeholder communication through data-driven insights and actionable recommendations."
                }
            ],
            "business_value": {
                "title": "For Data-Driven Organizations",
                "items": [
                    {
                        "icon": "fas fa-chart-bar",
                        "title": "Performance Metrics",
                        "description": "Quantifiable results and ROI analysis"
                    },
                    {
                        "icon": "fas fa-search",
                        "title": "Pattern Recognition",
                        "description": "Long-term trend identification and forecasting"
                    },
                    {
                        "icon": "fas fa-cogs",
                        "title": "Process Optimization",
                        "description": "Efficiency improvement opportunities"
                    },
                    {
                        "icon": "fas fa-users",
                        "title": "Stakeholder Communication",
                        "description": "Clear data visualization and executive reporting"
                    }
                ]
            },
            "project_links": [
                {
                    "text": "Interactive Dashboard",
                    "icon": "fas fa-chart-line",
                    "url": "dashboard.html",
                    "style": "background: linear-gradient(135deg, #2563eb, #7c3aed);"
                },
                {
                    "text": "Documentation",
                    "icon": "fas fa-book",
                    "url": "README.md",
                    "style": "background: linear-gradient(135deg, #7c3aed, #4ecdc4);"
                },
                {
                    "text": "Source Code",
                    "icon": "fas fa-code",
                    "url": "analysis.py",
                    "style": "background: linear-gradient(135deg, #4ecdc4, #fbbf24);"
                }
            ]
        }
    
    def generate_visualization_data(self, images, project_info):
        """Generate visualization data for the modal system"""
        viz_data = {}
        
        # Check if custom visualization descriptions are provided
        custom_descriptions = project_info.get("visualization_descriptions", {})
        
        for i, image_path in enumerate(images):
            # Extract filename without extension
            filename = os.path.basename(image_path)
            name = os.path.splitext(filename)[0]
            
            # Create a key for the visualization
            viz_key = name.lower().replace('_', '').replace('-', '').replace(' ', '')
            
            # Use custom description if available, otherwise generate one
            if viz_key in custom_descriptions:
                title = custom_descriptions[viz_key]["title"]
                description = custom_descriptions[viz_key]["description"]
            else:
                title = name.replace('_', ' ').title()
                description = self.generate_visualization_description(name)
            
            viz_data[viz_key] = {
                "title": title,
                "image": f"../{os.path.join(self.project_folder, filename)}",
                "description": description
            }
        
        return viz_data
    
    def generate_visualization_description(self, name):
        """Generate a description for a visualization based on its name"""
        descriptions = {
            "snowpack": """
                <h3>Key Insights</h3>
                <p>This comprehensive analysis reveals critical patterns and trends in the dataset:</p>
                <ul>
                    <li><strong>Data Quality:</strong> High-quality dataset with comprehensive coverage</li>
                    <li><strong>Trend Analysis:</strong> Clear patterns identified through statistical analysis</li>
                    <li><strong>Performance Metrics:</strong> Quantifiable improvements demonstrated</li>
                    <li><strong>Business Impact:</strong> Actionable insights for decision-making</li>
                </ul>
                <p>The analysis demonstrates excellent data quality and provides valuable insights for strategic planning.</p>
            """,
            "reservoir": """
                <h3>Operational Excellence</h3>
                <p>This analysis shows effective data processing and management:</p>
                <ul>
                    <li><strong>System Performance:</strong> Optimal processing efficiency achieved</li>
                    <li><strong>Data Integrity:</strong> High-quality data with minimal errors</li>
                    <li><strong>Scalability:</strong> System designed for future growth</li>
                    <li><strong>Reliability:</strong> Consistent performance across all metrics</li>
                </ul>
                <p>The system demonstrates robust performance and reliability throughout the analysis period.</p>
            """,
            "deliveries": """
                <h3>System Performance</h3>
                <p>This analysis reveals efficient data processing patterns:</p>
                <ul>
                    <li><strong>Throughput:</strong> High-volume data processing capabilities</li>
                    <li><strong>Efficiency:</strong> Optimized algorithms for maximum performance</li>
                    <li><strong>Accuracy:</strong> Precise results with minimal variance</li>
                    <li><strong>Scalability:</strong> System handles increasing data loads effectively</li>
                </ul>
                <p>The analysis demonstrates reliable data processing with strong performance characteristics.</p>
            """,
            "conservation": """
                <h3>Measurable Impact</h3>
                <p>This analysis shows significant improvements and measurable results:</p>
                <ul>
                    <li><strong>Performance Gains:</strong> Substantial improvements across key metrics</li>
                    <li><strong>Data Quality:</strong> High-quality results with comprehensive coverage</li>
                    <li><strong>Methodology:</strong> Robust analytical approach with validated results</li>
                    <li><strong>Business Value:</strong> Clear ROI and strategic insights provided</li>
                </ul>
                <p>These results demonstrate successful implementation and measurable business impact.</p>
            """,
            "gpcd": """
                <h3>Success Metrics</h3>
                <p>This analysis demonstrates successful outcomes and positive trends:</p>
                <ul>
                    <li><strong>Improvement Trend:</strong> Consistent positive performance over time</li>
                    <li><strong>Benchmark Performance:</strong> Results exceed industry standards</li>
                    <li><strong>Statistical Significance:</strong> Robust statistical validation of results</li>
                    <li><strong>Strategic Value:</strong> Clear business impact and decision support</li>
                </ul>
                <p>The analysis indicates successful implementation with measurable positive outcomes.</p>
            """
        }
        
        # Try to match based on keywords in the name
        name_lower = name.lower()
        for key, desc in descriptions.items():
            if key in name_lower:
                return desc
        
        # Default description
        return """
            <h3>Analysis Results</h3>
            <p>This visualization presents key findings from the comprehensive data analysis:</p>
            <ul>
                <li><strong>Data Insights:</strong> Important patterns and trends identified</li>
                <li><strong>Statistical Analysis:</strong> Robust methodology with validated results</li>
                <li><strong>Performance Metrics:</strong> Quantifiable improvements demonstrated</li>
                <li><strong>Business Impact:</strong> Actionable insights for strategic planning</li>
            </ul>
            <p>The analysis provides valuable insights that support data-driven decision making.</p>
        """
    
    def generate_html(self):
        """Generate the complete HTML page"""
        template = self.load_template()
        project_info = self.extract_project_info()
        images = self.find_visualizations()
        dashboard = self.find_dashboard()
        viz_data = self.generate_visualization_data(images, project_info)
        
        # Replace template placeholders
        replacements = {
            "{{PROJECT_TITLE}}": project_info["title"],
            "{{PROJECT_DESCRIPTION}}": project_info["description"],
            "{{TECH_STACK}}": self.generate_tech_stack_html(project_info["tech_stack"]),
            "{{INSIGHT_CARDS}}": self.generate_insight_cards_html(project_info["insights"]),
            "{{PROJECT_SUMMARY}}": project_info["summary"],
            "{{KEY_INSIGHTS}}": self.generate_key_insights_html(project_info["key_insights"]),
            "{{VISUALIZATIONS}}": self.generate_visualizations_html(images),
            "{{DASHBOARD_TITLE}}": "Interactive Analysis Dashboard",
            "{{DASHBOARD_DESCRIPTION}}": "An interactive dashboard combining all analyses into a single, explorable interface with real-time data exploration capabilities.",
            "{{DASHBOARD_LINK}}": f"../{dashboard}" if dashboard else "#",
            "{{TECHNICAL_IMPLEMENTATION}}": self.generate_technical_implementation_html(project_info["technical_implementation"]),
            "{{BUSINESS_VALUE_TITLE}}": project_info["business_value"]["title"],
            "{{BUSINESS_VALUE_ITEMS}}": self.generate_business_value_html(project_info["business_value"]["items"]),
            "{{PROJECT_LINKS}}": self.generate_project_links_html(project_info["project_links"]),
            "{{VISUALIZATION_DATA}}": json.dumps(viz_data, indent=2)
        }
        
        for placeholder, value in replacements.items():
            template = template.replace(placeholder, value)
        
        return template
    
    def generate_tech_stack_html(self, tech_stack):
        """Generate HTML for tech stack"""
        return ''.join([f'<span class="tech-item">{tech}</span>' for tech in tech_stack])
    
    def generate_insight_cards_html(self, insights):
        """Generate HTML for insight cards"""
        return ''.join([
            f'<div class="insight-card"><h3>{insight["value"]}</h3><p>{insight["label"]}</p></div>'
            for insight in insights
        ])
    
    def generate_key_insights_html(self, key_insights):
        """Generate HTML for key insights"""
        return ''.join([
            f'''<div class="insight-card">
                <i class="{insight["icon"]}" style="font-size: 2rem; color: #2563eb; margin-bottom: 1rem;"></i>
                <h3>{insight["title"]}</h3>
                <p>{insight["description"]}</p>
            </div>'''
            for insight in key_insights
        ])
    
    def generate_visualizations_html(self, images):
        """Generate HTML for visualization cards"""
        html = ""
        for i, image_path in enumerate(images):
            filename = os.path.basename(image_path)
            name = os.path.splitext(filename)[0]
            viz_key = name.lower().replace('_', '').replace('-', '').replace(' ', '')
            title = name.replace('_', ' ').title()
            
            html += f'''
                <div class="viz-card" onclick="expandVisualization('{viz_key}')">
                    <img src="../{os.path.join(self.project_folder, filename)}" alt="{title}">
                    <div class="viz-card-content">
                        <h3>{title}</h3>
                        <p>Comprehensive analysis showing key patterns, trends, and insights from the dataset.</p>
                        <div class="expand-hint">
                            <i class="fas fa-expand-arrows-alt"></i> Click to expand
                        </div>
                    </div>
                </div>
            '''
        return html
    
    def generate_technical_implementation_html(self, technical_items):
        """Generate HTML for technical implementation"""
        return ''.join([
            f'''<div class="insight-card">
                <h3>{item["title"]}</h3>
                <p>{item["description"]}</p>
            </div>'''
            for item in technical_items
        ])
    
    def generate_business_value_html(self, business_items):
        """Generate HTML for business value items"""
        return ''.join([
            f'''<div>
                <i class="{item["icon"]}" style="font-size: 2rem; color: #2563eb; margin-bottom: 1rem;"></i>
                <h4>{item["title"]}</h4>
                <p>{item["description"]}</p>
            </div>'''
            for item in business_items
        ])
    
    def generate_project_links_html(self, project_links):
        """Generate HTML for project links"""
        return ''.join([
            f'''<a href="{link["url"]}" class="dashboard-link" target="_blank" style="{link.get("style", "")}">
                <i class="{link["icon"]}"></i>
                {link["text"]}
            </a>'''
            for link in project_links
        ])
    
    def save_project_page(self):
        """Generate and save the project page"""
        html_content = self.generate_html()
        
        with open(self.output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ Project page generated: {self.output_path}")
        return self.output_path

def main():
    """Main function to generate project page"""
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python project_generator.py <project_name> <project_folder>")
        print("Example: python project_generator.py 'Water Conservation Analysis' 'water-conservation-analysis'")
        return
    
    project_name = sys.argv[1]
    project_folder = sys.argv[2]
    
    if not os.path.exists(project_folder):
        print(f"❌ Project folder '{project_folder}' not found")
        return
    
    generator = ProjectPageGenerator(project_name, project_folder)
    output_file = generator.save_project_page()
    
    print(f"🎉 Project page successfully generated!")
    print(f"📁 Output file: {output_file}")
    print(f"🌐 View at: http://localhost:8000/{output_file}")

if __name__ == "__main__":
    main()
