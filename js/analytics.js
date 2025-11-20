/**
 * CalcuPrime Analytics & Advertising Configuration
 *
 * This file contains placeholder code for Google Analytics and Google AdSense.
 * Replace the placeholder IDs with your actual tracking IDs before deployment.
 */

// ============================================================================
// GOOGLE ANALYTICS 4 (GA4)
// ============================================================================
// Instructions:
// 1. Create a Google Analytics 4 property at https://analytics.google.com
// 2. Get your Measurement ID (format: G-XXXXXXXXXX)
// 3. Replace 'G-XXXXXXXXXX' below with your actual Measurement ID
// 4. Add this script tag to your HTML <head>:
//    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
//    <script src="js/analytics.js"></script>

window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());

// Replace G-XXXXXXXXXX with your actual Google Analytics Measurement ID
gtag('config', 'G-XXXXXXXXXX', {
    'anonymize_ip': true, // Anonymize IP for GDPR compliance
    'cookie_flags': 'SameSite=None;Secure', // Cookie configuration
    'page_path': window.location.pathname
});

// ============================================================================
// EVENT TRACKING
// ============================================================================
// Custom event tracking for calculator usage
function trackCalculatorUse(calculatorName) {
    if (typeof gtag !== 'undefined') {
        gtag('event', 'calculator_use', {
            'calculator_name': calculatorName,
            'page_location': window.location.href
        });
    }
}

// Track form submissions
function trackFormSubmit(formName) {
    if (typeof gtag !== 'undefined') {
        gtag('event', 'form_submit', {
            'form_name': formName
        });
    }
}

// Track converter usage
function trackConverterUse(converterName) {
    if (typeof gtag !== 'undefined') {
        gtag('event', 'converter_use', {
            'converter_name': converterName,
            'page_location': window.location.href
        });
    }
}

// ============================================================================
// GOOGLE ADSENSE
// ============================================================================
// Instructions:
// 1. Sign up for Google AdSense at https://www.google.com/adsense
// 2. Get your AdSense Publisher ID (format: ca-pub-XXXXXXXXXXXXXXXX)
// 3. Replace the ID in ads.txt file with your actual Publisher ID
// 4. Add this script tag to your HTML <head>:
//    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXXXXXXXX" crossorigin="anonymous"></script>
// 5. Insert ad units in your HTML using the format below

/**
 * Ad Unit Placement Guidelines:
 *
 * 1. Header/Top Banner: 728x90 (Leaderboard) or 320x50 (Mobile)
 * 2. Sidebar: 300x250 (Medium Rectangle) or 300x600 (Half Page)
 * 3. In-content: 336x280 (Large Rectangle) or 300x250 (Medium Rectangle)
 * 4. Footer: 728x90 (Leaderboard)
 *
 * Example AdSense code (replace data-ad-client and data-ad-slot):
 *
 * <ins class="adsbygoogle"
 *      style="display:block"
 *      data-ad-client="ca-pub-XXXXXXXXXXXXXXXX"
 *      data-ad-slot="1234567890"
 *      data-ad-format="auto"
 *      data-full-width-responsive="true"></ins>
 * <script>
 *      (adsbygoogle = window.adsbygoogle || []).push({});
 * </script>
 */

// ============================================================================
// AD BLOCKER DETECTION (Optional)
// ============================================================================
function detectAdBlocker() {
    const adTest = document.createElement('div');
    adTest.innerHTML = '&nbsp;';
    adTest.className = 'adsbox';
    adTest.style.position = 'absolute';
    adTest.style.left = '-9999px';
    document.body.appendChild(adTest);

    setTimeout(function() {
        if (adTest.offsetHeight === 0) {
            console.log('Ad blocker detected');
            // Optionally display a message to users about supporting the site
        }
        document.body.removeChild(adTest);
    }, 100);
}

// Run ad blocker detection on page load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', detectAdBlocker);
} else {
    detectAdBlocker();
}

// ============================================================================
// COOKIE CONSENT (GDPR Compliance)
// ============================================================================
// Check if user has consented to cookies
function checkCookieConsent() {
    return localStorage.getItem('cookieConsent') === 'accepted';
}

// Load tracking scripts only if consent is given
function loadTrackingScripts() {
    if (checkCookieConsent()) {
        // Analytics and AdSense are loaded via HTML script tags
        console.log('Tracking scripts enabled');
    } else {
        console.log('Tracking scripts disabled - no consent');
    }
}

// Set cookie consent
function setCookieConsent(accepted) {
    if (accepted) {
        localStorage.setItem('cookieConsent', 'accepted');
        loadTrackingScripts();
        // Reload page to activate tracking
        window.location.reload();
    } else {
        localStorage.setItem('cookieConsent', 'declined');
    }
}

// Initialize on page load
loadTrackingScripts();

// ============================================================================
// EXPORT FUNCTIONS
// ============================================================================
// Make functions available globally
window.CalcuPrimeAnalytics = {
    trackCalculatorUse: trackCalculatorUse,
    trackFormSubmit: trackFormSubmit,
    trackConverterUse: trackConverterUse,
    setCookieConsent: setCookieConsent,
    checkCookieConsent: checkCookieConsent
};
