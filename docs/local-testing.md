# Local Testing Guide

This guide explains how to test your portfolio website locally before deploying to GitHub Pages.

## 📁 Project Structure

The portfolio is now organized into the following structure:
- `website/` - Main portfolio website files
- `tools/` - Development tools and templates  
- `docs/` - Documentation files
- `water-conservation-analysis/` - Data analysis project

## Quick Start (Python - Currently Running)
```bash
# Server is already running at:
http://localhost:8000

# Main portfolio:
http://localhost:8000/website/

# Individual project pages:
http://localhost:8000/website/water-conservation-project.html
```

## Alternative Methods

### Method 1: Python HTTP Server
```bash
# Navigate to your project directory
cd "/Users/grantgardner/Personal Projects/runn3rman.github.io"

# Start Python HTTP server
python3 -m http.server 8000

# Or if you have Python 2
python -m SimpleHTTPServer 8000

# Access at: http://localhost:8000
```

### Method 2: Node.js HTTP Server
```bash
# Install http-server globally (one-time setup)
npm install -g http-server

# Navigate to your project directory
cd "/Users/grantgardner/Personal Projects/runn3rman.github.io"

# Start the server
http-server -p 8000

# Access at: http://localhost:8000
```

### Method 3: PHP Built-in Server
```bash
# Navigate to your project directory
cd "/Users/grantgardner/Personal Projects/runn3rman.github.io"

# Start PHP server
php -S localhost:8000

# Access at: http://localhost:8000
```

### Method 4: Live Server (VS Code Extension)
1. Install "Live Server" extension in VS Code
2. Right-click on `index.html`
3. Select "Open with Live Server"
4. Automatically opens in browser with live reload

## Testing Features

### What to Test:
- [ ] Typing animation in hero section
- [ ] Navigation menu (desktop and mobile)
- [ ] Smooth scrolling between sections
- [ ] Hover effects on cards and buttons
- [ ] Contact form validation
- [ ] Responsive design on different screen sizes
- [ ] Profile picture display
- [ ] Experience timeline animations
- [ ] Project cards hover effects

### Browser Testing:
- [ ] Chrome
- [ ] Firefox
- [ ] Safari
- [ ] Edge

### Mobile Testing:
- [ ] iPhone Safari
- [ ] Android Chrome
- [ ] Tablet view

## Troubleshooting

### If the server doesn't start:
```bash
# Check if port 8000 is in use
lsof -i :8000

# Use a different port
python3 -m http.server 8080
# Then access: http://localhost:8080
```

### If images don't load:
- Check file paths are correct
- Ensure Assets folder exists
- Verify image file permissions

### If animations don't work:
- Check browser console for JavaScript errors
- Ensure all CSS and JS files are loading
- Test in different browsers

## Stopping the Server
Press `Ctrl + C` in the terminal to stop the server.
