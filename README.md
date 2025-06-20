# town-service-combinations-generator-python-script-seo-for-local-business
Script Generates Town + Service Landing Page Combinations for Local Businesses - #LOCALSEO #PYTHON #LANDINGPAGE #GENERATOR

# Static Landing Page Generator

A Python script that automatically generates SEO-optimized landing pages for service-based businesses across multiple locations. Perfect for landscaping companies, home services, contractors, and other local businesses looking to improve their local SEO presence.

## 🎯 What This Does

This script creates individual HTML landing pages for every combination of:
- **Services** you offer (e.g., "Lawn Care", "Tree Removal")  
- **Towns/Cities** you serve (e.g., "Springfield", "Riverside")

For example, with 3 services and 3 towns, you'll get **9 optimized pages** like:
- `springfield-lawn-care.html`
- `springfield-tree-removal.html`
- `riverside-lawn-care.html`
- etc.

## ✨ Features

- **SEO Optimized**: Each page has unique titles, meta descriptions, and content
- **Mobile Responsive**: Clean, professional design that works on all devices
- **Fast Loading**: Lightweight HTML/CSS with optimized images
- **Cross-linking**: Pages link to related services in other towns
- **Professional Design**: Hero sections, image galleries, and clear CTAs
- **Easy Customization**: Simple configuration at the top of the script

## 🚀 Quick Start

### 1. Clone or Download

```bash
git clone https://github.com/vinaeoua/town-service-combinations-generator-python-script-seo-for-local-business.git
cd static-page-generator
```

### 2. Customize Your Information

Edit the configuration section at the top of `generate_pages.py`:

```python
# Your towns/cities
towns = ["Your Town 1", "Your Town 2", "Your Town 3"]

# Your services  
services = ["Your Service 1", "Your Service 2", "Your Service 3"]

# Company details
COMPANY_NAME = "Your Company Name"
COMPANY_PHONE = "+1234567890"
HERO_IMAGE_URL = "https://your-hero-image-url.com/image.jpg"

# Project images
PROJECT_IMAGES = [
    "https://your-project-1-image.com/image.jpg",
    "https://your-project-2-image.com/image.jpg", 
    "https://your-project-3-image.com/image.jpg",
    "https://your-project-4-image.com/image.jpg"
]
```

### 3. Run the Script

```bash
python generate_pages.py
```

### 4. Upload to Your Website

The script creates a `static_pages` folder with all your HTML files. Upload these to your web server!

## 📁 File Structure

```
your-project/
├── generate_pages.py          # Main script
├── README.md                  # This file
└── static_pages/             # Generated files (created after running)
    ├── springfield-lawn-care.html
    ├── springfield-tree-removal.html
    ├── riverside-lawn-care.html
    └── ...
```

## 🛠️ Customization Options

### Adding More Towns/Services

Simply add items to the lists:

```python
towns = ["Town 1", "Town 2", "Town 3", "Town 4", "Town 5"]
services = ["Service 1", "Service 2", "Service 3", "Service 4"]
```

### Changing the Design

Edit the CSS in the `html_template` section. The template includes:
- Responsive grid layouts
- Professional color scheme  
- Hover effects and transitions
- Mobile-first design

### Custom Navigation

Modify the navigation links in the template:

```html
<nav>
    <a href="/">Home</a>
    <a href="/about">About Us</a>
    <a href="/services">Services</a>
    <a href="/gallery">Gallery</a>
    <a href="/contact">Contact</a>
</nav>
```

### Adding Analytics

Add your tracking codes in the `<head>` section:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

## 📊 SEO Benefits

Each generated page includes:
- **Unique Title Tags**: "Town Service | Your Company"
- **Meta Descriptions**: Optimized for local search
- **Local Keywords**: Town and service combinations
- **Internal Linking**: Cross-links between related pages
- **Structured Content**: H1, H2 tags properly organized
- **Image Alt Text**: Descriptive alt attributes

## 🎨 Use Cases

Perfect for:
- **Landscaping Companies**: Lawn care, hardscaping, design services
- **Home Services**: Plumbing, electrical, HVAC across multiple areas  
- **Contractors**: Roofing, renovation, construction services
- **Cleaning Services**: Residential, commercial, specialized cleaning
- **Any Local Business**: Serving multiple towns with various services

## 🔧 Requirements

- Python 3.6 or higher
- No external dependencies required!

## 📈 Pro Tips

1. **Image Optimization**: Use WebP format and compress images for faster loading
2. **Content Variation**: Consider adding unique content for each town/service combo
3. **Schema Markup**: Add structured data for better search results
4. **Local Citations**: Include address and hours for each location
5. **Regular Updates**: Refresh content and images periodically

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests!

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

Having issues? 
1. Check that your Python version is 3.6+
2. Ensure all URLs in the configuration are valid
3. Verify write permissions in the project directory
4. Check the console output for any error messages

---

**Made with ❤️ for local businesses looking to improve their online presence**
