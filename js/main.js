// ===========================
// Mobile Menu Toggle
// ===========================
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuToggle = document.getElementById('mobileMenuToggle');
    const navMenu = document.getElementById('navMenu');
    
    if (mobileMenuToggle) {
        mobileMenuToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
        });
    }
    
    // Close mobile menu when clicking outside
    document.addEventListener('click', function(event) {
        if (!event.target.closest('.nav') && navMenu.classList.contains('active')) {
            navMenu.classList.remove('active');
        }
    });
});

// ===========================
// Search Modal Functionality
// ===========================
const searchBtn = document.getElementById('searchBtn');
const searchModal = document.getElementById('searchModal');
const searchClose = document.getElementById('searchClose');
const searchInput = document.getElementById('searchInput');
const searchResults = document.getElementById('searchResults');

// Calculator database for search
const calculators = [
    { name: 'Mortgage Calculator', url: 'calculators/mortgage-calculator.html', category: 'Finance', keywords: 'mortgage loan home payment interest' },
    { name: 'BMI Calculator', url: 'calculators/bmi-calculator.html', category: 'Health', keywords: 'bmi body mass index weight health' },
    { name: 'Percentage Calculator', url: 'calculators/percentage-calculator.html', category: 'Math', keywords: 'percentage percent calculation' },
    { name: 'Calorie Calculator', url: 'calculators/calorie-calculator.html', category: 'Health', keywords: 'calorie diet weight loss tdee' },
    { name: 'Loan Calculator', url: 'calculators/loan-calculator.html', category: 'Finance', keywords: 'loan payment interest rate' },
    { name: 'Investment Calculator', url: 'calculators/investment-calculator.html', category: 'Finance', keywords: 'investment returns stocks compound' },
    { name: 'Compound Interest Calculator', url: 'calculators/compound-interest-calculator.html', category: 'Finance', keywords: 'compound interest savings investment' },
    { name: 'Retirement Calculator', url: 'calculators/retirement-calculator.html', category: 'Finance', keywords: 'retirement savings pension 401k' },
    { name: 'Pregnancy Calculator', url: 'calculators/pregnancy-calculator.html', category: 'Health', keywords: 'pregnancy due date conception' },
    { name: 'Ideal Weight Calculator', url: 'calculators/ideal-weight-calculator.html', category: 'Health', keywords: 'ideal weight height bmi' },
    { name: 'Length Converter', url: 'calculators/length-converter.html', category: 'Converter', keywords: 'length distance meter feet inch' },
    { name: 'Weight Converter', url: 'calculators/weight-converter.html', category: 'Converter', keywords: 'weight mass kg pound ounce' },
    { name: 'Temperature Converter', url: 'calculators/temperature-converter.html', category: 'Converter', keywords: 'temperature celsius fahrenheit kelvin' },
    { name: 'Currency Converter', url: 'calculators/currency-converter.html', category: 'Converter', keywords: 'currency exchange rate money' }
];

if (searchBtn) {
    searchBtn.addEventListener('click', function() {
        searchModal.classList.add('active');
        searchInput.focus();
    });
}

if (searchClose) {
    searchClose.addEventListener('click', function() {
        searchModal.classList.remove('active');
        searchInput.value = '';
        searchResults.innerHTML = '';
    });
}

// Close modal on outside click
if (searchModal) {
    searchModal.addEventListener('click', function(e) {
        if (e.target === searchModal) {
            searchModal.classList.remove('active');
            searchInput.value = '';
            searchResults.innerHTML = '';
        }
    });
}

// Search functionality
if (searchInput) {
    searchInput.addEventListener('input', function(e) {
        const query = e.target.value.toLowerCase().trim();
        
        if (query.length < 2) {
            searchResults.innerHTML = '';
            return;
        }
        
        const results = calculators.filter(calc => 
            calc.name.toLowerCase().includes(query) ||
            calc.keywords.toLowerCase().includes(query) ||
            calc.category.toLowerCase().includes(query)
        );
        
        displaySearchResults(results);
    });
}

function displaySearchResults(results) {
    if (results.length === 0) {
        searchResults.innerHTML = '<div style="padding: 20px; text-align: center; color: #6b7280;">No calculators found</div>';
        return;
    }
    
    const html = results.map(calc => `
        <a href="${calc.url}" style="display: block; padding: 15px; border-bottom: 1px solid #e5e7eb; text-decoration: none; color: inherit; transition: background 0.2s;">
            <div style="font-weight: 600; color: #1f2937; margin-bottom: 5px;">${calc.name}</div>
            <div style="font-size: 0.875rem; color: #6b7280;">${calc.category}</div>
        </a>
    `).join('');
    
    searchResults.innerHTML = html;
    
    // Add hover effect
    searchResults.querySelectorAll('a').forEach(link => {
        link.addEventListener('mouseenter', function() {
            this.style.background = '#f3f4f6';
        });
        link.addEventListener('mouseleave', function() {
            this.style.background = 'transparent';
        });
    });
}

// Hero search functionality
const heroSearch = document.getElementById('heroSearch');
if (heroSearch) {
    heroSearch.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            const query = e.target.value.toLowerCase().trim();
            if (query.length >= 2) {
                const results = calculators.filter(calc => 
                    calc.name.toLowerCase().includes(query) ||
                    calc.keywords.toLowerCase().includes(query)
                );
                
                if (results.length > 0) {
                    window.location.href = results[0].url;
                }
            }
        }
    });
}

// ===========================
// Smooth Scroll for Anchor Links
// ===========================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// ===========================
// Form Validation Helper
// ===========================
function validateNumber(value, min = null, max = null) {
    const num = parseFloat(value);
    
    if (isNaN(num)) {
        return { valid: false, message: 'Please enter a valid number' };
    }
    
    if (min !== null && num < min) {
        return { valid: false, message: `Value must be at least ${min}` };
    }
    
    if (max !== null && num > max) {
        return { valid: false, message: `Value must be at most ${max}` };
    }
    
    return { valid: true, value: num };
}

// ===========================
// Number Formatting Utilities
// ===========================
function formatNumber(num, decimals = 2) {
    return num.toLocaleString('en-US', {
        minimumFractionDigits: decimals,
        maximumFractionDigits: decimals
    });
}

function formatCurrency(num, currency = 'USD') {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: currency,
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    }).format(num);
}

function formatPercentage(num, decimals = 2) {
    return num.toFixed(decimals) + '%';
}

// ===========================
// Show Result Animation
// ===========================
function showResult(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        element.style.opacity = '0';
        element.style.transform = 'translateY(10px)';
        
        setTimeout(() => {
            element.style.transition = 'all 0.3s ease';
            element.style.opacity = '1';
            element.style.transform = 'translateY(0)';
        }, 50);
    }
}

// ===========================
// Error Display Helper
// ===========================
function showError(inputId, message) {
    const input = document.getElementById(inputId);
    if (!input) return;
    
    // Remove existing error
    const existingError = input.parentElement.querySelector('.error-message');
    if (existingError) {
        existingError.remove();
    }
    
    // Add error styling
    input.style.borderColor = '#ef4444';
    
    // Create error message
    const errorDiv = document.createElement('div');
    errorDiv.className = 'error-message';
    errorDiv.style.color = '#ef4444';
    errorDiv.style.fontSize = '0.875rem';
    errorDiv.style.marginTop = '0.25rem';
    errorDiv.textContent = message;
    
    input.parentElement.appendChild(errorDiv);
}

function clearError(inputId) {
    const input = document.getElementById(inputId);
    if (!input) return;
    
    input.style.borderColor = '#e5e7eb';
    
    const errorMessage = input.parentElement.querySelector('.error-message');
    if (errorMessage) {
        errorMessage.remove();
    }
}

// ===========================
// Local Storage Helpers
// ===========================
function saveCalculation(calculatorName, data) {
    const key = `calcuprime_${calculatorName}`;
    localStorage.setItem(key, JSON.stringify(data));
}

function loadCalculation(calculatorName) {
    const key = `calcuprime_${calculatorName}`;
    const data = localStorage.getItem(key);
    return data ? JSON.parse(data) : null;
}

// ===========================
// Print/Export Functionality
// ===========================
function printResults() {
    window.print();
}

function exportToCSV(data, filename) {
    const csv = Object.entries(data)
        .map(([key, value]) => `${key},${value}`)
        .join('\n');
    
    const blob = new Blob([csv], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.click();
    window.URL.revokeObjectURL(url);
}

// ===========================
// Analytics Helper (Placeholder)
// ===========================
function trackCalculation(calculatorName, action) {
    // Placeholder for Google Analytics or similar
    if (typeof gtag !== 'undefined') {
        gtag('event', action, {
            'event_category': 'Calculator',
            'event_label': calculatorName
        });
    }
}

// ===========================
// Copy to Clipboard
// ===========================
function copyToClipboard(text) {
    if (navigator.clipboard) {
        navigator.clipboard.writeText(text).then(() => {
            showNotification('Copied to clipboard!');
        });
    } else {
        // Fallback for older browsers
        const textarea = document.createElement('textarea');
        textarea.value = text;
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand('copy');
        document.body.removeChild(textarea);
        showNotification('Copied to clipboard!');
    }
}

function showNotification(message) {
    const notification = document.createElement('div');
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: #10b981;
        color: white;
        padding: 15px 25px;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        z-index: 10000;
        animation: slideIn 0.3s ease;
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// Add animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(400px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// ===========================
// Page Load Performance
// ===========================
window.addEventListener('load', function() {
    // Track page load time
    const loadTime = window.performance.timing.domContentLoadedEventEnd - window.performance.timing.navigationStart;
    console.log('Page loaded in ' + loadTime + 'ms');
});
