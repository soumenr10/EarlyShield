# LandSafe NER - Full HTML Builder Script
import os

out = open(r'd:/sih2026/landslide-warning-system/index.html', 'w', encoding='utf-8')

def w(s):
    out.write(s + '\n')

# HEAD
w('<!DOCTYPE html>')
w('<html lang="en">')
w('<head>')
w('<meta charset="UTF-8"/>')
w('<meta name="viewport" content="width=device-width, initial-scale=1.0"/>')
w('<meta name="description" content="AI-Based Landslide Early Warning System for North Eastern Region of India"/>')
w('<title>LandSafe NER - AI Landslide Early Warning System</title>')
w('<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>')
w('<link rel="stylesheet" href="assets/css/style.css"/>')
w('</head>')
w('<body>')

# OFFLINE BANNER
w('<div class="offline-banner">You are offline. Cached data shown. Will sync when reconnected.</div>')

# NAVBAR
w('''<nav id="navbar">
<div class="nav-container">
  <a href="#hero" class="nav-logo">
    <div class="nav-logo-icon" style="font-size:1.4rem;display:flex;align-items:center;justify-content:center;">&#9968;</div>
    <div class="nav-logo-text"><strong>LandSafe NER</strong><span>AI Early Warning System</span></div>
  </a>
  <div class="nav-links">
    <a href="#hero" class="nav-link active" data-i18n="nav_home">Home</a>
    <a href="#dashboard" class="nav-link" data-i18n="nav_dashboard">Dashboard</a>
    <a href="#map-section" class="nav-link" data-i18n="nav_map">GIS Map</a>
    <a href="#alerts" class="nav-link" data-i18n="nav_alerts">Alerts</a>
    <a href="#analytics" class="nav-link" data-i18n="nav_analytics">Analytics</a>
    <a href="#weather" class="nav-link" data-i18n="nav_weather">Weather</a>
    <a href="#sensors" class="nav-link" data-i18n="nav_sensors">Sensors</a>
    <a href="#field-report" class="nav-link" data-i18n="nav_report">Field Report</a>
    <a href="#response" class="nav-link" data-i18n="nav_response">Response</a>
  </div>
  <div class="nav-actions">
    <div class="alert-indicator" title="Active Alerts" id="alert-bell">&#128276;<div class="alert-dot"></div></div>
    <button class="lang-selector" data-lang-open title="Language">&#127760; EN</button>
    <button class="btn btn-danger btn-sm" id="nav-sos">&#128680; SOS</button>
  </div>
  <div class="nav-hamburger" id="hamburger"><span></span><span></span><span></span></div>
</div>
</nav>''')

# TICKER
w('<div class="live-ticker"><div class="container"><div class="ticker-inner"><div class="ticker-label">&#128308; LIVE ALERTS</div><div class="ticker-track"><div class="ticker-content"></div></div></div></div></div>')

# MOBILE MENU
w('''<div class="mobile-menu" id="mobile-menu">
<div class="mobile-nav-links">
  <a href="#hero" class="mobile-nav-link">&#127968; Home</a>
  <a href="#dashboard" class="mobile-nav-link">&#128202; Dashboard</a>
  <a href="#map-section" class="mobile-nav-link">&#128506; GIS Map</a>
  <a href="#alerts" class="mobile-nav-link">&#128680; Alerts</a>
  <a href="#analytics" class="mobile-nav-link">&#128200; Analytics</a>
  <a href="#weather" class="mobile-nav-link">&#127783; Weather</a>
  <a href="#sensors" class="mobile-nav-link">&#128225; Sensors</a>
  <a href="#field-report" class="mobile-nav-link">&#128203; Field Report</a>
  <a href="#response" class="mobile-nav-link">&#128641; Response</a>
</div>
<div style="display:flex;flex-direction:column;gap:12px;margin-top:24px;">
  <button class="btn btn-danger" id="mob-sos-btn">&#128680; SOS Alert</button>
  <button class="btn btn-outline" data-lang-open>&#127760; Change Language</button>
</div>
</div>''')

out.close()
print('Part 1 written (header, nav, ticker, mobile menu)')
