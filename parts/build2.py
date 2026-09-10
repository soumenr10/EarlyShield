import os

out = open(r'd:/sih2026/landslide-warning-system/index.html', 'a', encoding='utf-8')

def w(s):
    out.write(s + '\n')

# HERO SECTION
w('''
<section id="hero">
<div class="hero-bg"></div>
<div class="hero-grid-overlay"></div>
<div class="container">
  <div class="grid-2" style="align-items:center;gap:60px;padding:40px 0;">
    <div class="hero-content">
      <div class="hero-badge"><span class="dot"></span> REAL-TIME MONITORING ACTIVE &bull; NER 2026</div>
      <h1 class="hero-title" data-i18n="hero_title">AI-Powered <span class="highlight">Landslide</span><br/>Early Warning System</h1>
      <p class="hero-description">Real-time monitoring, predictive analytics and automated alerts for disaster preparedness across the <strong style="color:var(--text-primary)">8 states of North Eastern India</strong>.</p>
      <div class="hero-cta">
        <a href="#dashboard" class="btn btn-primary btn-lg">&#128202; View Dashboard</a>
        <a href="#map-section" class="btn btn-outline btn-lg">&#128506; Open GIS Map</a>
        <a href="#field-report" class="btn btn-warning btn-lg">&#128203; File Report</a>
      </div>
      <div class="hero-stats">
        <div class="hero-stat"><span class="number" data-count="162" data-suffix="">162</span><span class="label">Districts Monitored</span></div>
        <div class="hero-stat"><span class="number" data-count="48" data-suffix="">48</span><span class="label">Active Sensors</span></div>
        <div class="hero-stat"><span class="number" data-count="94" data-suffix="%">94%</span><span class="label">AI Accuracy</span></div>
      </div>
    </div>
    <div class="hero-visual fade-in">
      <div class="hero-map-preview">
        <div id="hero-map"></div>
        <div class="map-overlay-card">
          <div class="title" style="color:var(--text-primary);margin-bottom:6px;">&#128308; Active Alerts</div>
          <div style="font-size:.78rem;display:flex;flex-direction:column;gap:3px;">
            <div><span style="color:#e74c3c;font-weight:700;">&#9679; 6</span> Critical zones</div>
            <div><span style="color:#f39c12;font-weight:700;">&#9679; 14</span> High risk zones</div>
            <div><span style="color:#27ae60;font-weight:700;">&#9679; 76</span> Safe zones</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</section>
''')

# RISK BAND
w('''
<div class="risk-band">
<div class="container">
  <div class="risk-band-inner">
    <div class="risk-item"><div class="risk-circle high">6</div><div class="risk-info"><div class="label">Critical Zones</div><div class="value" style="color:#e74c3c;">CRITICAL</div></div></div>
    <div class="risk-divider"></div>
    <div class="risk-item"><div class="risk-circle medium">14</div><div class="risk-info"><div class="label">High Risk Zones</div><div class="value" style="color:#f39c12;">HIGH ALERT</div></div></div>
    <div class="risk-divider"></div>
    <div class="risk-item"><div class="risk-circle monitoring">28</div><div class="risk-info"><div class="label">Under Watch</div><div class="value" style="color:#60a5fa;">MONITORING</div></div></div>
    <div class="risk-divider"></div>
    <div class="risk-item"><div class="risk-circle low">76</div><div class="risk-info"><div class="label">Safe Zones</div><div class="value" style="color:#27ae60;">SAFE</div></div></div>
    <div class="risk-divider"></div>
    <div class="risk-item"><div style="font-size:1.5rem;">&#129302;</div><div class="risk-info"><div class="label">AI Model</div><div class="value" style="color:#60a5fa;">v4.2 LIVE</div></div></div>
    <div class="last-updated" id="last-updated-time">Last updated: --:--:-- IST</div>
  </div>
</div>
</div>
''')

out.close()
print('Part 2 done: hero + risk band')
