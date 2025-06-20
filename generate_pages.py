import os

# Configuration - Edit these lists with your own data
towns = ["Springfield", "Riverside", "Madison"]

services = ["Lawn Care", "Tree Removal", "Garden Design"]

# Company information - Edit these with your details
COMPANY_NAME = "Your Landscape Company"
COMPANY_PHONE = "+1234567890"
HERO_IMAGE_URL = "https://via.placeholder.com/1200x400/4CAF50/white?text=Your+Company+Hero+Image"

# Sample project images - Replace with your own
PROJECT_IMAGES = [
    "https://via.placeholder.com/250x200/4CAF50/white?text=Project+1",
    "https://via.placeholder.com/250x200/4CAF50/white?text=Project+2", 
    "https://via.placeholder.com/250x200/4CAF50/white?text=Project+3",
    "https://via.placeholder.com/250x200/4CAF50/white?text=Project+4"
]

# Output folder
output_folder = "static_pages"
os.makedirs(output_folder, exist_ok=True)

# HTML template
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{town} {service} | {company_name}</title>
    <meta name="description" content="Professional {service} services in {town}. Contact {company_name} for a free consultation and transform your outdoor space today!">

    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            line-height: 1.6;
        }}
        header {{
            background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('{hero_image}') center center / cover no-repeat;
            height: 300px;
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.7);
        }}
        header h1 {{
            font-size: 2.5rem;
            text-align: center;
            margin: 0;
        }}
        nav {{
            background-color: #333;
            padding: 15px 20px;
            text-align: center;
        }}
        nav a {{
            color: white;
            margin: 0 20px;
            text-decoration: none;
            font-size: 18px;
            font-weight: 500;
        }}
        nav a:hover {{
            color: #4CAF50;
            text-decoration: underline;
        }}
        .content {{
            padding: 60px 20px;
            text-align: center;
            max-width: 800px;
            margin: 0 auto;
        }}
        .content h2 {{
            color: #333;
            margin-bottom: 20px;
        }}
        .content p {{
            font-size: 18px;
            color: #666;
            margin-bottom: 30px;
        }}
        .cta-button {{
            display: inline-block;
            background-color: #4CAF50;
            color: white;
            padding: 15px 30px;
            font-size: 20px;
            font-weight: bold;
            text-decoration: none;
            border-radius: 5px;
            margin: 10px;
            transition: background-color 0.3s;
        }}
        .cta-button:hover {{
            background-color: #45a049;
        }}
        .cta-button.secondary {{
            background-color: #2196F3;
        }}
        .cta-button.secondary:hover {{
            background-color: #1976D2;
        }}
        .gallery {{
            padding: 60px 20px;
            text-align: center;
            background-color: #f9f9f9;
        }}
        .gallery h2 {{
            color: #333;
            margin-bottom: 40px;
        }}
        .gallery-row {{
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
            max-width: 1000px;
            margin: 0 auto;
        }}
        .gallery img {{
            width: 100%;
            max-width: 230px;
            height: 180px;
            object-fit: cover;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s;
        }}
        .gallery img:hover {{
            transform: scale(1.05);
        }}
        .town-selection {{
            padding: 40px 20px;
            text-align: center;
            background-color: #fff;
            max-width: 800px;
            margin: 0 auto;
        }}
        .town-selection h3 {{
            color: #333;
            margin-bottom: 20px;
        }}
        .town-list {{
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 15px;
            list-style: none;
            padding: 0;
            margin: 0;
        }}
        .town-list li {{
            background-color: #f0f0f0;
            border-radius: 5px;
            padding: 8px 15px;
        }}
        .town-list a {{
            color: #2196F3;
            text-decoration: none;
            font-weight: 500;
        }}
        .town-list a:hover {{
            color: #1976D2;
            text-decoration: underline;
        }}
        footer {{
            margin-top: 50px;
            text-align: center;
            padding: 30px 20px;
            background-color: #333;
            color: #ccc;
        }}
        @media (max-width: 768px) {{
            header h1 {{
                font-size: 2rem;
            }}
            nav a {{
                margin: 0 10px;
                font-size: 16px;
            }}
            .content {{
                padding: 40px 15px;
            }}
            .gallery-row {{
                gap: 15px;
            }}
        }}
    </style>
</head>
<body>
    <header>
        <h1>{town} {service} Experts</h1>
    </header>
    
    <nav>
        <a href="/">Home</a>
        <a href="/about">About Us</a>
        <a href="/services">Services</a>
        <a href="/gallery">Gallery</a>
        <a href="/contact">Contact</a>
    </nav>
    
    <div class="content">
        <h2>Professional {service} in {town}</h2>
        <p>Transform your outdoor space in {town} with our expert {service} services. We bring years of experience and quality craftsmanship to every project.</p>
        <a href="tel:{phone}" class="cta-button">Call Now: {phone}</a>
        <a href="/contact" class="cta-button secondary">Get Free Quote</a>
    </div>
    
    <div class="gallery">
        <h2>Our Recent Projects</h2>
        <div class="gallery-row">
            <img src="{project_img1}" alt="{service} Project 1 in {town}">
            <img src="{project_img2}" alt="{service} Project 2 in {town}">
            <img src="{project_img3}" alt="{service} Project 3 in {town}">
            <img src="{project_img4}" alt="{service} Project 4 in {town}">
        </div>
    </div>
    
    <div class="town-selection">
        <h3>We also serve other areas for {service}:</h3>
        <ul class="town-list">
            {related_links}
        </ul>
    </div>
    
    <footer>
        <p>&copy; 2025 {company_name}. All rights reserved.</p>
        <p>Professional landscaping and outdoor services</p>
    </footer>
</body>
</html>"""

def generate_pages():
    """Generate HTML pages for all town-service combinations"""
    total_pages = len(towns) * len(services)
    print(f"Generating {total_pages} pages...")
    
    for town in towns:
        for service in services:
            # Generate related town links (excluding current town)
            related_links = "\n            ".join([
                f'<li><a href="{other_town.lower().replace(" ", "-")}-{service.lower().replace(" ", "-")}.html">{other_town}</a></li>'
                for other_town in towns if other_town != town
            ])
            
            # Create filename
            file_name = f"{town.lower().replace(' ', '-')}-{service.lower().replace(' ', '-')}.html"
            file_path = os.path.join(output_folder, file_name)
            
            # Generate HTML content
            html_content = html_template.format(
                town=town,
                service=service,
                company_name=COMPANY_NAME,
                phone=COMPANY_PHONE,
                hero_image=HERO_IMAGE_URL,
                project_img1=PROJECT_IMAGES[0],
                project_img2=PROJECT_IMAGES[1],
                project_img3=PROJECT_IMAGES[2],
                project_img4=PROJECT_IMAGES[3],
                related_links=related_links
            )
            
            # Write file
            with open(file_path, "w", encoding='utf-8') as file:
                file.write(html_content)
    
    print(f"✅ Successfully generated {total_pages} HTML pages in '{output_folder}' folder")
    print(f"📁 Files created: {[f'{town.lower().replace(" ", "-")}-{service.lower().replace(" ", "-")}.html' for town in towns for service in services]}")

if __name__ == "__main__":
    generate_pages()
