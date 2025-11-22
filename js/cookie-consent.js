/**
 * CalcuPrime Cookie Consent Manager
 * GDPR/CCPA Compliant Cookie Consent System
 */

const COOKIE_CONSENT_KEY = 'calcuprime_cookie_consent';
const COOKIE_CONSENT_DATE_KEY = 'calcuprime_cookie_consent_date';

function showCookieConsent() {
    const consent = localStorage.getItem(COOKIE_CONSENT_KEY);
    const consentDate = localStorage.getItem(COOKIE_CONSENT_DATE_KEY);

    // Show banner if no consent or consent older than 365 days
    if (!consent || !consentDate) {
        const banner = document.getElementById('cookieConsent');
        if (banner) banner.classList.add('show');
    } else {
        const daysSinceConsent = (Date.now() - parseInt(consentDate)) / (1000 * 60 * 60 * 24);
        if (daysSinceConsent > 365) {
            const banner = document.getElementById('cookieConsent');
            if (banner) banner.classList.add('show');
        }
    }
}

function acceptCookies() {
    localStorage.setItem(COOKIE_CONSENT_KEY, 'accepted');
    localStorage.setItem(COOKIE_CONSENT_DATE_KEY, Date.now().toString());
    const banner = document.getElementById('cookieConsent');
    if (banner) banner.classList.remove('show');

    // Enable analytics and ads
    enableAnalytics();
    enableAds();

    console.log('✓ Cookies accepted - Analytics and Ads enabled');
}

function rejectCookies() {
    localStorage.setItem(COOKIE_CONSENT_KEY, 'rejected');
    localStorage.setItem(COOKIE_CONSENT_DATE_KEY, Date.now().toString());
    const banner = document.getElementById('cookieConsent');
    if (banner) banner.classList.remove('show');

    // Disable analytics and ads
    disableAnalytics();
    disableAds();

    console.log('✗ Cookies rejected - Only essential cookies enabled');
}

function enableAnalytics() {
    // Enable Google Analytics if user accepted
    if (window.GA_MEASUREMENT_ID) {
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', window.GA_MEASUREMENT_ID);
        console.log('Google Analytics enabled');
    }
}

function disableAnalytics() {
    // Disable Google Analytics tracking
    if (window.GA_MEASUREMENT_ID) {
        window['ga-disable-' + window.GA_MEASUREMENT_ID] = true;
        console.log('Google Analytics disabled');
    }
}

function enableAds() {
    // Enable Google AdSense if user accepted
    console.log('AdSense enabled (when integrated)');
    // TODO: Add AdSense initialization code when approved
}

function disableAds() {
    // Disable ads if user rejected
    console.log('AdSense disabled');
}

function getCookieConsent() {
    return localStorage.getItem(COOKIE_CONSENT_KEY);
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    const consent = getCookieConsent();

    if (consent === 'accepted') {
        enableAnalytics();
        enableAds();
    } else if (consent === 'rejected') {
        disableAnalytics();
        disableAds();
    }

    // Show banner if needed (after short delay for better UX)
    setTimeout(showCookieConsent, 500);
});
