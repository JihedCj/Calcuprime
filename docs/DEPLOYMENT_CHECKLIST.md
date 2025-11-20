# CalcuPrime Deployment Checklist for Hostinger

## Pre-Deployment Tasks

### 1. File Preparation
- [ ] All files tested locally
- [ ] Images optimized (use TinyPNG or similar)
- [ ] CSS and JS minified (optional but recommended)
- [ ] All links working (no broken links)
- [ ] All calculators tested and functional
- [ ] Mobile responsiveness verified
- [ ] Cross-browser testing completed

### 2. Content Updates
- [ ] Replace all "calcuprime.com" with your actual domain
- [ ] Update contact email addresses
- [ ] Add your social media links
- [ ] Verify all calculator descriptions
- [ ] Proofread all content

### 3. SEO Preparation
- [ ] Sitemap.xml updated with all pages
- [ ] Robots.txt configured
- [ ] Meta descriptions written for all pages
- [ ] Title tags optimized (50-60 characters)
- [ ] Alt text added to all images
- [ ] Canonical URLs set correctly

---

## Hostinger Deployment Steps

### Step 1: Domain Setup
- [ ] Log in to Hostinger control panel
- [ ] Navigate to Domains section
- [ ] Verify domain is active and pointed to hosting
- [ ] Note: DNS propagation can take 24-48 hours

### Step 2: SSL Certificate (HTTPS)
- [ ] Go to SSL section in Hostinger panel
- [ ] Install free Let's Encrypt SSL certificate
- [ ] Enable Force HTTPS redirect
- [ ] Verify SSL is active (look for padlock icon)

### Step 3: FTP Connection

**Connection Details:**
```
Host: ftp.yourdomain.com
Username: [from Hostinger]
Password: [from Hostinger]
Port: 21
```

**Using FileZilla:**
1. [ ] Open FileZilla
2. [ ] Enter FTP credentials
3. [ ] Click "Quickconnect"
4. [ ] Navigate to `/public_html` directory on remote

### Step 4: File Upload

**Upload these files to `/public_html`:**
- [ ] index.html (homepage)
- [ ] robots.txt
- [ ] sitemap.xml
- [ ] .htaccess (create this file - see below)
- [ ] favicon.ico (create one at favicon.io)

**Upload these folders:**
- [ ] css/ (with style.css)
- [ ] js/ (with main.js)
- [ ] calculators/ (all calculator HTML files)
- [ ] assets/ (images, icons)
- [ ] category/ (category pages - create these)
- [ ] docs/ (optional)

### Step 5: Create .htaccess File

In Hostinger File Manager or via FTP, create `.htaccess` in `/public_html`:

```apache
# Force HTTPS
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

# Remove .html extension
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^([^\.]+)$ $1.html [NC,L]

# Enable compression
<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/html
    AddOutputFilterByType DEFLATE text/plain
    AddOutputFilterByType DEFLATE text/xml
    AddOutputFilterByType DEFLATE text/css
    AddOutputFilterByType DEFLATE text/javascript
    AddOutputFilterByType DEFLATE application/javascript
    AddOutputFilterByType DEFLATE application/x-javascript
</IfModule>

# Browser Caching
<IfModule mod_expires.c>
    ExpiresActive On
    
    # Images
    ExpiresByType image/jpg "access plus 1 year"
    ExpiresByType image/jpeg "access plus 1 year"
    ExpiresByType image/gif "access plus 1 year"
    ExpiresByType image/png "access plus 1 year"
    ExpiresByType image/webp "access plus 1 year"
    ExpiresByType image/svg+xml "access plus 1 year"
    ExpiresByType image/x-icon "access plus 1 year"
    
    # CSS and JavaScript
    ExpiresByType text/css "access plus 1 month"
    ExpiresByType application/javascript "access plus 1 month"
    ExpiresByType text/javascript "access plus 1 month"
    
    # HTML
    ExpiresByType text/html "access plus 1 hour"
</IfModule>

# Security Headers
<IfModule mod_headers.c>
    Header set X-Content-Type-Options "nosniff"
    Header set X-Frame-Options "SAMEORIGIN"
    Header set X-XSS-Protection "1; mode=block"
</IfModule>

# Custom Error Pages (optional)
ErrorDocument 404 /404.html
ErrorDocument 403 /403.html
ErrorDocument 500 /500.html
```

### Step 6: Verify Deployment
- [ ] Visit https://yourdomain.com in browser
- [ ] Check homepage loads correctly
- [ ] Test navigation menu
- [ ] Click through to calculator pages
- [ ] Test at least 3 calculators
- [ ] Check mobile view (use Chrome DevTools)
- [ ] Verify all images load
- [ ] Test search functionality

---

## Google Services Setup

### Google Search Console

1. **Verify Ownership**
   - [ ] Go to search.google.com/search-console
   - [ ] Add property (use domain property type)
   - [ ] Choose verification method:
     - **Option A**: HTML file upload (recommended)
       - Download verification file
       - Upload to `/public_html`
       - Click verify
     - **Option B**: DNS verification
       - Add TXT record in Hostinger DNS
       - Wait for propagation
       - Click verify

2. **Submit Sitemap**
   - [ ] Go to Sitemaps section
   - [ ] Enter: `https://yourdomain.com/sitemap.xml`
   - [ ] Click Submit
   - [ ] Wait for Google to process (can take days)

3. **Request Indexing**
   - [ ] Go to URL Inspection
   - [ ] Enter homepage URL
   - [ ] Click "Request Indexing"
   - [ ] Repeat for important calculator pages

### Google Analytics

1. **Create Account**
   - [ ] Go to analytics.google.com
   - [ ] Create account and property
   - [ ] Get Tracking ID (G-XXXXXXXXXX)

2. **Add Tracking Code**
   Add this to `<head>` of ALL pages:
   ```html
   <!-- Google Analytics -->
   <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
   <script>
     window.dataLayer = window.dataLayer || [];
     function gtag(){dataLayer.push(arguments);}
     gtag('js', new Date());
     gtag('config', 'G-XXXXXXXXXX');
   </script>
   ```

3. **Verify Installation**
   - [ ] Visit your site
   - [ ] Check Analytics Real-Time reports
   - [ ] Confirm you see active user

### Google AdSense (After 20+ Pages)

1. **Apply**
   - [ ] Go to google.com/adsense
   - [ ] Submit application
   - [ ] Add AdSense code to `<head>`
   - [ ] Wait for approval (1-2 weeks)

2. **Set Up Ads** (after approval)
   - [ ] Create ad units
   - [ ] Add ad code to pages
   - [ ] Recommended placements:
     - Header banner (728x90)
     - Sidebar (300x250)
     - Below calculator (responsive)
     - In-content between sections

---

## Post-Deployment Tasks

### Week 1
- [ ] Monitor Google Search Console for crawl errors
- [ ] Check Google Analytics daily
- [ ] Fix any broken links
- [ ] Test all calculators from different devices
- [ ] Share on social media

### Week 2
- [ ] Start building backlinks
- [ ] Create 5 more calculators
- [ ] Write blog post about your calculators
- [ ] Submit to calculator directories
- [ ] Engage in relevant forums

### Week 3-4
- [ ] Analyze traffic sources
- [ ] Identify top-performing calculators
- [ ] Optimize underperforming pages
- [ ] Create more calculators in popular categories
- [ ] Build more backlinks

### Month 2
- [ ] Reach 50 total calculators
- [ ] Optimize ad placements
- [ ] A/B test different designs
- [ ] Create email newsletter
- [ ] Start guest posting

---

## Performance Optimization Checklist

### Speed Optimization
- [ ] Enable Gzip compression (.htaccess)
- [ ] Leverage browser caching (.htaccess)
- [ ] Optimize images (WebP format if possible)
- [ ] Minify CSS and JavaScript
- [ ] Use CDN for static assets (optional)
- [ ] Enable lazy loading for images
- [ ] Remove unused CSS/JS

### Mobile Optimization
- [ ] Test on multiple devices (iPhone, Android)
- [ ] Ensure buttons are large enough (44x44px min)
- [ ] Check text is readable (16px minimum)
- [ ] Verify no horizontal scrolling
- [ ] Test form inputs on mobile
- [ ] Check calculator usability on small screens

### SEO Optimization
- [ ] Each page has unique title tag
- [ ] Each page has unique meta description
- [ ] Proper heading hierarchy (H1 → H2 → H3)
- [ ] Internal linking between calculators
- [ ] Add breadcrumb navigation
- [ ] Include FAQ schema markup
- [ ] Add author and date to content

---

## Testing Checklist

### Functional Testing
- [ ] All calculators produce correct results
- [ ] Input validation works properly
- [ ] Error messages display correctly
- [ ] Results update in real-time
- [ ] Print function works
- [ ] Share buttons work (if implemented)

### Cross-Browser Testing
Test on:
- [ ] Chrome (Desktop & Mobile)
- [ ] Firefox (Desktop & Mobile)
- [ ] Safari (Desktop & Mobile)
- [ ] Edge (Desktop)

### Performance Testing
- [ ] Google PageSpeed Insights score > 90
- [ ] GTmetrix grade A
- [ ] Mobile PageSpeed > 85
- [ ] Load time < 2 seconds
- [ ] First Contentful Paint < 1.5s

### SEO Testing
- [ ] All pages indexed in Google
- [ ] No 404 errors in Search Console
- [ ] Sitemap processed without errors
- [ ] Mobile-friendly test passes
- [ ] Rich results test passes (if using schema)

---

## Common Issues & Solutions

### Issue: Site not loading
- Check DNS settings in Hostinger
- Verify domain is pointed correctly
- Wait 24-48 hours for DNS propagation
- Clear browser cache

### Issue: HTTPS not working
- Install SSL certificate in Hostinger
- Add HTTPS redirect in .htaccess
- Clear browser cache
- Check for mixed content warnings

### Issue: Calculators not working
- Check JavaScript console for errors
- Verify all JS files uploaded correctly
- Check file paths are correct
- Test in incognito mode

### Issue: Images not loading
- Verify images uploaded to correct folder
- Check file paths in HTML
- Ensure image filenames match exactly (case-sensitive)
- Optimize large images

### Issue: Not appearing in Google
- Submit sitemap in Search Console
- Request indexing for important pages
- Build quality backlinks
- Ensure robots.txt isn't blocking
- Give it time (can take weeks)

---

## Support Resources

### Hostinger Support
- Knowledge Base: hostinger.com/tutorials
- Live Chat: Available 24/7
- Ticket System: Through hPanel

### Google Resources
- Search Console Help: support.google.com/webmasters
- Analytics Help: support.google.com/analytics
- AdSense Help: support.google.com/adsense

### Web Development
- MDN Web Docs: developer.mozilla.org
- Stack Overflow: stackoverflow.com
- Web.dev: web.dev

---

## Launch Checklist Summary

**Before Going Live:**
- [x] Files prepared and tested
- [ ] Domain configured
- [ ] SSL enabled
- [ ] All files uploaded
- [ ] .htaccess created
- [ ] Site verified and working

**After Going Live:**
- [ ] Google Search Console set up
- [ ] Google Analytics installed
- [ ] Sitemap submitted
- [ ] Social media announced
- [ ] Begin SEO work

**First Month Goals:**
- [ ] 20 calculators live
- [ ] 100+ daily visitors
- [ ] 5+ backlinks
- [ ] AdSense application submitted

---

**Good luck with your launch! 🚀**

Remember: Building traffic takes time. Focus on creating quality calculators, writing excellent content, and building legitimate backlinks. Success will follow.

For detailed development guidance, refer to: `docs/DEVELOPMENT_GUIDE.md`
