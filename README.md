# Grant Gardner - Portfolio Website

A modern, responsive portfolio website built with HTML, CSS, and JavaScript, hosted on GitHub Pages.

## 🚀 Live Demo

Visit the live website: [runn3rman.github.io](https://runn3rman.github.io)

## ✨ Features

- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Modern UI/UX**: Clean, professional design with smooth animations
- **Interactive Elements**: 
  - Smooth scrolling navigation
  - Mobile-friendly hamburger menu
  - Contact form with validation
  - Scroll-triggered animations
  - Back-to-top button
- **Project Showcase**: Highlight your best work with detailed project cards
- **Skills Section**: Display your technical expertise
- **Contact Form**: Easy way for visitors to get in touch
- **Social Links**: Connect your professional profiles

## 🛠️ Technologies Used

- **HTML5**: Semantic markup and structure
- **CSS3**: Modern styling with Flexbox and Grid
- **JavaScript (ES6+)**: Interactive functionality and animations
- **Font Awesome**: Icons for enhanced visual appeal
- **Google Fonts**: Inter font family for typography

## 📁 Project Structure

```
runn3rman.github.io/
├── index.html              # Redirect to main website
├── website/                # Main portfolio website
│   ├── index.html          # Main portfolio page
│   ├── styles.css          # CSS styles and responsive design
│   ├── script.js           # JavaScript functionality
│   ├── Assets/             # Images and media files
│   │   └── Good-profile-pic.jpg
│   └── *-project.html      # Individual project pages
├── tools/                  # Development tools
│   ├── project_generator.py    # Auto-generate project pages
│   └── project-template.html   # Template for project pages
├── docs/                   # Documentation
│   ├── local-testing.md    # Local development guide
│   └── PROJECT_GENERATION_README.md
├── water-conservation-analysis/  # Data analysis project
│   ├── data_generator.py
│   ├── water_analysis.py
│   ├── requirements.txt
│   ├── README.md
│   ├── project_config.json
│   └── *.png              # Generated visualizations
└── README.md              # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- A GitHub account
- Basic knowledge of HTML, CSS, and JavaScript (for customization)

### Setup Instructions

1. **Fork or Clone this Repository**
   ```bash
   git clone https://github.com/runn3rman/runn3rman.github.io.git
   cd runn3rman.github.io
   ```

2. **Customize Your Information**
   
   Edit the following files to personalize your portfolio:

   **index.html** - Update personal information:
   - Replace "Grant Gardner" with your name
   - Update the hero section description
   - Modify the about section with your story
   - Add your actual projects in the projects section
   - Update contact information (email, phone, location)
   - Add your social media links

   **styles.css** - Customize colors and styling:
   - Change the color scheme by modifying CSS variables
   - Adjust fonts, spacing, and layout as needed
   - Update the gradient backgrounds

3. **Add Your Projects**
   
   In the projects section of `index.html`, replace the example projects with your own:
   ```html
   <div class="project-card">
       <div class="project-image">
           <i class="fas fa-laptop-code"></i> <!-- Change icon -->
       </div>
       <div class="project-content">
           <h3>Your Project Name</h3>
           <p>Project description...</p>
           <div class="project-tech">
               <span>Technology 1</span>
               <span>Technology 2</span>
           </div>
           <div class="project-links">
               <a href="your-github-repo" class="project-link">
                   <i class="fab fa-github"></i> Code
               </a>
               <a href="your-live-demo" class="project-link">
                   <i class="fas fa-external-link-alt"></i> Live Demo
               </a>
           </div>
       </div>
   </div>
   ```

4. **Update Contact Information**
   
   Replace the placeholder contact details with your actual information:
   - Email address
   - Phone number
   - Location
   - Social media profiles

5. **Deploy to GitHub Pages**
   
   Since this is a GitHub Pages repository, your site will automatically deploy when you push changes to the main branch.

   ```bash
   git add .
   git commit -m "Update portfolio with personal information"
   git push origin main
   ```

   Your site will be available at `https://yourusername.github.io` within a few minutes.

## 🎨 Customization Guide

### Changing Colors

The main color scheme is defined in `styles.css`. Key colors to modify:
- Primary blue: `#2563eb`
- Secondary purple: `#7c3aed`
- Accent yellow: `#fbbf24`
- Text colors: `#1f2937`, `#4b5563`, `#6b7280`

### Adding New Sections

1. Add the HTML structure in `index.html`
2. Add corresponding CSS styles in `styles.css`
3. Update the navigation menu
4. Add scroll reveal animations in `script.js`

### Modifying Animations

Animations are controlled in `script.js`. You can:
- Adjust scroll reveal timing
- Modify hover effects
- Change typing animation speed
- Customize form validation messages

## 📱 Mobile Responsiveness

The website is fully responsive and includes:
- Mobile-first CSS design
- Hamburger menu for mobile navigation
- Touch-friendly buttons and links
- Optimized typography for different screen sizes
- Flexible grid layouts

## 🔧 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Feel free to fork this project and customize it for your own portfolio. If you make improvements that could benefit others, pull requests are welcome!

## 📞 Support

If you have any questions or need help customizing your portfolio, feel free to:
- Open an issue on GitHub
- Contact me through the portfolio contact form
- Reach out on social media

---

**Happy coding! 🚀**