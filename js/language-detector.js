/**
 * CalcuPrime Language Detection and Switcher
 * Automatically detects user's browser language and redirects to appropriate version
 */

(function() {
    'use strict';

    // Language configuration
    const SUPPORTED_LANGUAGES = {
        'en': {
            code: 'en',
            name: 'English',
            flag: '🇺🇸',
            path: '/'
        },
        'es': {
            code: 'es',
            name: 'Español',
            flag: '🇪🇸',
            path: '/es/'
        }
    };

    const DEFAULT_LANGUAGE = 'en';
    const LANGUAGE_STORAGE_KEY = 'calcuprime_language';

    /**
     * Get user's preferred language from browser
     */
    function getBrowserLanguage() {
        const browserLang = navigator.language || navigator.userLanguage;
        const langCode = browserLang.split('-')[0].toLowerCase();
        return SUPPORTED_LANGUAGES[langCode] ? langCode : DEFAULT_LANGUAGE;
    }

    /**
     * Get current language from URL path
     */
    function getCurrentLanguage() {
        const path = window.location.pathname;
        if (path.startsWith('/es/') || path === '/es') {
            return 'es';
        }
        return 'en';
    }

    /**
     * Get stored language preference
     */
    function getStoredLanguage() {
        try {
            return localStorage.getItem(LANGUAGE_STORAGE_KEY);
        } catch (e) {
            return null;
        }
    }

    /**
     * Store language preference
     */
    function setStoredLanguage(lang) {
        try {
            localStorage.setItem(LANGUAGE_STORAGE_KEY, lang);
        } catch (e) {
            // LocalStorage not available
        }
    }

    /**
     * Get the equivalent page URL in target language
     */
    function getTranslatedURL(targetLang) {
        const currentPath = window.location.pathname;
        const currentLang = getCurrentLanguage();

        // Already on correct language
        if (currentLang === targetLang) {
            return null;
        }

        let newPath;

        if (targetLang === 'en') {
            // Remove /es/ prefix
            newPath = currentPath.replace(/^\/es\//, '/').replace(/^\/es$/, '/');
        } else if (targetLang === 'es') {
            // Add /es/ prefix
            if (currentPath === '/' || currentPath === '/index.html') {
                newPath = '/es/index.html';
            } else {
                newPath = '/es' + currentPath;
            }
        }

        return newPath + window.location.search + window.location.hash;
    }

    /**
     * Redirect to translated page
     */
    function redirectToLanguage(targetLang) {
        const translatedURL = getTranslatedURL(targetLang);
        if (translatedURL) {
            window.location.href = translatedURL;
        }
    }

    /**
     * Auto-detect and redirect on first visit
     * Only runs on homepage
     */
    function autoDetectLanguage() {
        // Only run on homepage
        const path = window.location.pathname;
        const isHomepage = path === '/' || path === '/index.html';

        if (!isHomepage) {
            return;
        }

        // Check if user has already set a preference
        const storedLang = getStoredLanguage();
        if (storedLang) {
            return; // User has made a choice, respect it
        }

        // Check if this is a redirect from language detection
        const urlParams = new URLSearchParams(window.location.search);
        if (urlParams.has('lang_detected')) {
            return; // Already redirected once
        }

        // Detect browser language
        const browserLang = getBrowserLanguage();
        const currentLang = getCurrentLanguage();

        // Redirect if browser language doesn't match current page
        if (browserLang !== currentLang) {
            setStoredLanguage(browserLang);
            const targetURL = getTranslatedURL(browserLang);
            if (targetURL) {
                // Add parameter to prevent redirect loop
                window.location.href = targetURL + '?lang_detected=1';
            }
        }
    }

    /**
     * Create language switcher UI
     */
    function createLanguageSwitcher() {
        const currentLang = getCurrentLanguage();

        // Create switcher HTML
        const switcherHTML = `
            <div class="language-switcher" id="languageSwitcher">
                <button class="language-btn" id="languageBtn" aria-label="Change language">
                    <span class="language-flag">${SUPPORTED_LANGUAGES[currentLang].flag}</span>
                    <span class="language-code">${currentLang.toUpperCase()}</span>
                    <svg width="12" height="12" viewBox="0 0 12 12" fill="currentColor">
                        <path d="M6 8L2 4h8z"/>
                    </svg>
                </button>
                <div class="language-menu" id="languageMenu">
                    ${Object.entries(SUPPORTED_LANGUAGES).map(([code, lang]) => `
                        <button class="language-option ${code === currentLang ? 'active' : ''}"
                                data-lang="${code}"
                                onclick="CalcuPrimeLanguage.switchLanguage('${code}')">
                            <span class="language-flag">${lang.flag}</span>
                            <span class="language-name">${lang.name}</span>
                            ${code === currentLang ? '<span class="checkmark">✓</span>' : ''}
                        </button>
                    `).join('')}
                </div>
            </div>
        `;

        // Add CSS
        const style = document.createElement('style');
        style.textContent = `
            .language-switcher {
                position: relative;
                display: inline-block;
            }

            .language-btn {
                display: flex;
                align-items: center;
                gap: 0.375rem;
                padding: 0.5rem 0.75rem;
                background: white;
                border: 1px solid #e5e7eb;
                border-radius: 0.5rem;
                cursor: pointer;
                font-size: 0.875rem;
                font-weight: 500;
                color: #1f2937;
                transition: all 0.2s ease;
            }

            .language-btn:hover {
                border-color: #2563eb;
                box-shadow: 0 2px 8px rgba(37, 99, 235, 0.1);
            }

            .language-flag {
                font-size: 1.25rem;
                line-height: 1;
            }

            .language-code {
                font-family: monospace;
            }

            .language-menu {
                position: absolute;
                top: calc(100% + 0.5rem);
                right: 0;
                background: white;
                border: 1px solid #e5e7eb;
                border-radius: 0.5rem;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
                min-width: 160px;
                opacity: 0;
                visibility: hidden;
                transform: translateY(-10px);
                transition: all 0.2s ease;
                z-index: 1000;
            }

            .language-menu.active {
                opacity: 1;
                visibility: visible;
                transform: translateY(0);
            }

            .language-option {
                display: flex;
                align-items: center;
                gap: 0.75rem;
                width: 100%;
                padding: 0.75rem 1rem;
                background: none;
                border: none;
                cursor: pointer;
                font-size: 0.875rem;
                color: #1f2937;
                transition: background 0.2s ease;
                text-align: left;
            }

            .language-option:first-child {
                border-radius: 0.5rem 0.5rem 0 0;
            }

            .language-option:last-child {
                border-radius: 0 0 0.5rem 0.5rem;
            }

            .language-option:hover {
                background: #f3f4f6;
            }

            .language-option.active {
                background: #eff6ff;
                color: #2563eb;
                font-weight: 600;
            }

            .language-name {
                flex: 1;
            }

            .checkmark {
                color: #2563eb;
                font-weight: bold;
            }

            @media (max-width: 768px) {
                .language-switcher {
                    margin-left: auto;
                }
            }
        `;
        document.head.appendChild(style);

        // Find header actions and insert switcher
        const headerActions = document.querySelector('.header-actions');
        if (headerActions) {
            headerActions.insertAdjacentHTML('afterbegin', switcherHTML);

            // Add click event to toggle menu
            const btn = document.getElementById('languageBtn');
            const menu = document.getElementById('languageMenu');

            if (btn && menu) {
                btn.addEventListener('click', (e) => {
                    e.stopPropagation();
                    menu.classList.toggle('active');
                });

                // Close menu when clicking outside
                document.addEventListener('click', () => {
                    menu.classList.remove('active');
                });
            }
        }
    }

    /**
     * Switch to selected language
     */
    function switchLanguage(targetLang) {
        if (!SUPPORTED_LANGUAGES[targetLang]) {
            return;
        }

        // Store preference
        setStoredLanguage(targetLang);

        // Redirect to translated page
        redirectToLanguage(targetLang);
    }

    /**
     * Initialize language detection and switcher
     */
    function init() {
        // Auto-detect language on homepage
        autoDetectLanguage();

        // Create language switcher UI
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', createLanguageSwitcher);
        } else {
            createLanguageSwitcher();
        }
    }

    // Export public API
    window.CalcuPrimeLanguage = {
        switchLanguage: switchLanguage,
        getCurrentLanguage: getCurrentLanguage,
        getSupportedLanguages: () => SUPPORTED_LANGUAGES
    };

    // Initialize
    init();
})();
