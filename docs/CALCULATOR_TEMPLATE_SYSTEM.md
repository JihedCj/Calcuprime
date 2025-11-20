# Calculator Template System

## Overview
This document provides templates and automation tools for rapidly creating new calculators for CalcuPrime.

## Quick Start: Python Generator Script

Use this script to generate calculators quickly:

```python
#!/usr/bin/env python3
"""
CalcuPrime Calculator Generator
Generates fully functional calculator HTML files from specifications
"""

import os
from datetime import datetime

def generate_calculator(spec):
    """
    Generate a calculator HTML file from specification

    spec = {
        "filename": "my-calculator",
        "title": "My Calculator",
        "description": "Calculate something useful",
        "meta_description": "SEO-optimized description",
        "keywords": "keyword1, keyword2, keyword3",
        "category": "finance",  # finance, health, math, converters, everyday, chemistry
        "inputs": [
            {"id": "input1", "label": "First Value", "type": "number", "default": "100", "min": "0", "max": "1000", "step": "1"},
            {"id": "input2", "label": "Second Value", "type": "number", "default": "50"}
        ],
        "results": [
            {"id": "result1", "label": "Result", "color": "#10b981"},
            {"id": "result2", "label": "Details"}
        ],
        "calculation_js": "// Your JavaScript calculation logic here",
        "content_sections": [
            {"title": "How to Use", "content": "Step by step instructions..."},
            {"title": "Understanding Results", "content": "Explanation of results..."}
        ]
    }
    """

    template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{spec['meta_description']}">
    <meta name="keywords" content="{spec['keywords']}">
    <meta name="author" content="CalcuPrime">
    <title>{spec['title']} | CalcuPrime</title>
    <link rel="stylesheet" href="../css/style.css">
    <link rel="canonical" href="https://calcuprime.com/calculators/{spec['filename']}.html">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <header class="header">
        <nav class="nav container">
            <a href="../index.html" class="logo">
                <span class="logo-icon">⚡</span>
                <span class="logo-text">CalcuPrime</span>
            </a>
            <button class="mobile-menu-toggle" id="mobileMenuToggle" aria-label="Toggle menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <ul class="nav-menu" id="navMenu">
                <li><a href="../index.html#finance">Finance</a></li>
                <li><a href="../index.html#health">Health</a></li>
                <li><a href="../index.html#converters">Converters</a></li>
                <li><a href="../index.html#math">Math</a></li>
            </ul>
        </nav>
    </header>

    <main class="calculator-container">
        <div class="calculator-header">
            <h1 class="calculator-title">{spec['title']}</h1>
            <p class="calculator-description">{spec['description']}</p>
        </div>

        <div class="calculator-wrapper">
            <div class="calculator-inputs">
                <h3>Calculator Inputs</h3>
"""

    # Generate input fields
    for input_field in spec['inputs']:
        attrs = f"id=\"{input_field['id']}\" class=\"form-input\""
        if 'default' in input_field:
            attrs += f" value=\"{input_field['default']}\""
        if 'min' in input_field:
            attrs += f" min=\"{input_field['min']}\""
        if 'max' in input_field:
            attrs += f" max=\"{input_field['max']}\""
        if 'step' in input_field:
            attrs += f" step=\"{input_field['step']}\""

        template += f"""                <div class="form-group">
                    <label for="{input_field['id']}" class="form-label">{input_field['label']}</label>
                    <input type="{input_field.get('type', 'number')}" {attrs}>
                </div>
"""

    template += """                <button onclick="calculate()" class="btn-calculate">Calculate</button>
            </div>

            <div class="calculator-results">
                <h3>Results</h3>
"""

    # Generate result fields
    for result in spec['results']:
        color = result.get('color', '#10b981')
        template += f"""                <div class="result-item">
                    <div class="result-label">{result['label']}</div>
                    <div class="result-value" id="{result['id']}" style="font-size: 2rem; color: {color};">-</div>
                </div>
"""

    template += """            </div>
        </div>

        <div class="content-section">
"""

    # Generate content sections
    for section in spec.get('content_sections', []):
        template += f"""            <h2>{section['title']}</h2>
            <p>{section['content']}</p>
"""

    template += f"""        </div>
    </main>

    <footer class="footer">
        <div class="container">
            <div class="footer-bottom">
                <p>&copy; {datetime.now().year} CalcuPrime. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script src="../js/main.js"></script>
    <script>
        function calculate() {{
            {spec['calculation_js']}
        }}

        document.querySelectorAll('.form-input').forEach(input => {{
            input.addEventListener('input', calculate);
        }});

        window.addEventListener('load', calculate);
    </script>
</body>
</html>"""

    return template


# Example usage:
if __name__ == "__main__":
    example_spec = {
        "filename": "simple-interest-calculator",
        "title": "Simple Interest Calculator",
        "description": "Calculate simple interest on loans or investments",
        "meta_description": "Free simple interest calculator - Calculate interest on principal amount over time. Simple and accurate interest calculations.",
        "keywords": "simple interest, interest calculator, principal, interest rate, time period",
        "category": "finance",
        "inputs": [
            {"id": "principal", "label": "Principal Amount ($)", "type": "number", "default": "1000", "min": "0"},
            {"id": "rate", "label": "Interest Rate (% per year)", "type": "number", "default": "5", "min": "0", "max": "100", "step": "0.1"},
            {"id": "time", "label": "Time Period (years)", "type": "number", "default": "1", "min": "0", "max": "50"}
        ],
        "results": [
            {"id": "interest", "label": "Interest Earned", "color": "#10b981"},
            {"id": "total", "label": "Total Amount", "color": "#3b82f6"}
        ],
        "calculation_js": """
            const principal = parseFloat(document.getElementById('principal').value);
            const rate = parseFloat(document.getElementById('rate').value) / 100;
            const time = parseFloat(document.getElementById('time').value);

            const interest = principal * rate * time;
            const total = principal + interest;

            document.getElementById('interest').textContent = '$' + interest.toFixed(2);
            document.getElementById('total').textContent = '$' + total.toFixed(2);
        """,
        "content_sections": [
            {
                "title": "Simple Interest Formula",
                "content": "Simple Interest = Principal × Rate × Time. This formula calculates interest only on the principal amount, not on accumulated interest."
            },
            {
                "title": "When to Use Simple Interest",
                "content": "Simple interest is used for short-term loans, car loans, and some personal loans. It's simpler than compound interest but results in less growth for investments."
            }
        ]
    }

    html = generate_calculator(example_spec)

    # Save to file
    output_dir = "../calculators"
    os.makedirs(output_dir, exist_ok=True)
    with open(f"{output_dir}/{example_spec['filename']}.html", 'w') as f:
        f.write(html)

    print(f"Generated: {example_spec['filename']}.html")
```

## Manual HTML Template

For manual creation, use this base template:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="[SEO DESCRIPTION]">
    <meta name="keywords" content="[KEYWORDS]">
    <title>[CALCULATOR NAME] | CalcuPrime</title>
    <link rel="stylesheet" href="../css/style.css">
    <link rel="canonical" href="https://calcuprime.com/calculators/[filename].html">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <header class="header">
        <nav class="nav container">
            <a href="../index.html" class="logo">
                <span class="logo-icon">⚡</span>
                <span class="logo-text">CalcuPrime</span>
            </a>
            <ul class="nav-menu">
                <li><a href="../index.html#finance">Finance</a></li>
                <li><a href="../index.html#health">Health</a></li>
            </ul>
        </nav>
    </header>

    <main class="calculator-container">
        <div class="calculator-header">
            <h1 class="calculator-title">[TITLE]</h1>
            <p class="calculator-description">[DESCRIPTION]</p>
        </div>

        <div class="calculator-wrapper">
            <div class="calculator-inputs">
                <h3>Inputs</h3>
                <!-- Add input fields here -->
                <button onclick="calculate()" class="btn-calculate">Calculate</button>
            </div>

            <div class="calculator-results">
                <h3>Results</h3>
                <!-- Add result displays here -->
            </div>
        </div>

        <div class="content-section">
            <!-- Add SEO content here (1000+ words recommended) -->
        </div>
    </main>

    <footer class="footer">
        <div class="container">
            <div class="footer-bottom">
                <p>&copy; 2024 CalcuPrime. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script src="../js/main.js"></script>
    <script>
        function calculate() {
            // Add calculation logic here
        }

        document.querySelectorAll('.form-input').forEach(input => {
            input.addEventListener('input', calculate);
        });

        window.addEventListener('load', calculate);
    </script>
</body>
</html>
```

## Best Practices

### SEO Optimization
- **Title**: Keep under 60 characters, include primary keyword
- **Meta Description**: 150-160 characters, compelling call-to-action
- **Keywords**: 5-10 relevant keywords, comma-separated
- **Content**: Minimum 1000 words of unique, helpful content
- **Headings**: Use H2, H3 hierarchy properly
- **Internal Links**: Link to 3-5 related calculators

### User Experience
- **Auto-calculate**: Update results on input change
- **Input Validation**: Check for valid inputs before calculating
- **Mobile-friendly**: Test on various screen sizes
- **Fast**: Keep calculations instant (< 100ms)
- **Clear Labels**: Descriptive field labels and result descriptions

### Calculator Logic
- **Accuracy**: Use appropriate precision (usually 2 decimal places for money)
- **Error Handling**: Alert users for invalid inputs
- **Default Values**: Pre-fill with realistic example values
- **Format Numbers**: Use comma separators for large numbers

### Testing Checklist
- [ ] All inputs work correctly
- [ ] Calculation is accurate
- [ ] Mobile responsive
- [ ] SEO meta tags present
- [ ] Links work
- [ ] JavaScript console has no errors
- [ ] Loads in under 2 seconds

## Updating Sitemap

After creating calculators, add to `sitemap.xml`:

```xml
<url>
    <loc>https://calcuprime.com/calculators/[filename].html</loc>
    <lastmod>YYYY-MM-DD</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
</url>
```

## Calculator Categories

### Finance (High Revenue Potential)
- Prioritize these for AdSense revenue
- Typical search volume: 10K-1M monthly
- Focus on loans, investments, mortgages, taxes

### Health (High Traffic)
- Second highest traffic category
- Strong mobile usage
- Focus on BMI, calories, pregnancy, fitness

### Converters (Easy to Create, Steady Traffic)
- Simple logic, quick to build
- Consistent search traffic
- Low competition

### Math (Educational Traffic)
- Good for student demographics
- Lower revenue but steady traffic
- Easy to create and maintain

### Everyday (Practical Tools)
- Age, date, tip, discount calculators
- High engagement, frequent use
- Good for return visitors

### Chemistry (Niche, Lower Volume)
- Specialized audience
- Academic/professional use
- Lower competition
