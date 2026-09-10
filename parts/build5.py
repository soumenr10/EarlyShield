import os
out = open(r'd:/sih2026/landslide-warning-system/index.html', 'a', encoding='utf-8')
def w(s): out.write(s + '\n')

# WEATHER SECTION
w('''
<section id="weather" class="section" style="padding-top:40px;">
<div class="container">
  <div class="section-label">&#127783; Weather Intelligence</div>
  <h2 class="section-title">IMD Weather Integration</h2>
  <p class="section-subtitle">Real-time weather data and 7-day rainfall forecast with landslide risk correlation</p>
  <div class="grid-3 fade-in">
    <div class="card" style="grid-column:span 1;">
      <div style="text-align:center;margin-bottom:16px;">
        <span style="font-size:3rem;display:block;margin-bottom:12px;">&#9928;</span>
        <div style="font-size:2.5rem;font-weight:800;">24&deg;C</div>
        <div style="color:var(--text-muted);font-size:.9rem;margin-top:4px;">Heavy Thunderstorm &mdash; Tawang, AP</div>
        <div style="margin-top:8px;"><span class="badge badge-danger">RED ALERT</span></div>
      </div>
      <div class="weather-grid">
        <div class="weather-stat"><div class="key">Rainfall</div><div class="val text-info" id="current-rainfall">-- mm/hr</div></div>
        <div class="weather-stat"><div class="key">Humidity</div><div class="val text-info" id="current-humidity">-- %</div></div>
        <div class="weather-stat"><div class="key">Wind Speed</div><div class="val">47 km/h</div></div>
        <div class="weather-stat"><div class="key">Visibility</div><div class="val">0.8 km</div></div>
        <div class="weather-stat"><div class="key">Pressure</div><div class="val">982 hPa</div></div>
        <div class="weather-stat"><div class="key">Cloud Cover</div><div class="val">98%</div></div>
      </div>
      <div style="margin-top:16px;padding:10px;background:rgba(231,76,60,.08);border:1px solid rgba(231,76,60,.2);border-radius:var(--radius-sm);font-size:.8rem;color:#e74c3c;">
        IMD Red Alert: Extremely heavy rainfall forecast for AP and Meghalaya next 24 hours.
      </div>
    </div>
    <div class="card" style="grid-column:span 2;">
      <div class="flex-between" style="margin-bottom:16px;">
        <h4>7-Day Rainfall &amp; Risk Forecast</h4>
        <span class="badge badge-info">IMD Data</span>
      </div>
      <div id="forecast-list"></div>
      <div style="margin-top:16px;padding:12px;background:rgba(22,160,133,.08);border:1px solid rgba(22,160,133,.2);border-radius:var(--radius-sm);">
        <div style="font-size:.82rem;font-weight:700;color:#2dd4bf;margin-bottom:6px;">AI Risk Forecast Insight:</div>
        <div style="font-size:.82rem;color:var(--text-muted);">Cumulative rainfall over next 72 hours likely to exceed soil saturation thresholds in Tawang, Cherrapunji, and Tamenglong. AI model recommends pre-emptive evacuation of low-lying villages within 500m of slopes.</div>
      </div>
    </div>
  </div>
  <div class="card fade-in" style="margin-top:24px;">
    <h4 style="margin-bottom:16px;">Weather Station Network</h4>
    <div class="table-wrap">
      <table class="data-table">
        <thead><tr><th>Station</th><th>District</th><th>Temp</th><th>Rainfall mm/hr</th><th>Humidity</th><th>Wind</th><th>Alert Level</th></tr></thead>
        <tbody>
          <tr><td>Tawang AWS</td><td>Tawang, AP</td><td>18&deg;C</td><td style="color:#e74c3c;font-weight:700;">142</td><td>96%</td><td>47 km/h</td><td><span class="badge badge-danger">RED</span></td></tr>
          <tr><td>Cherrapunji AWS</td><td>E. Khasi, ML</td><td>22&deg;C</td><td style="color:#e74c3c;font-weight:700;">187</td><td>99%</td><td>38 km/h</td><td><span class="badge badge-danger">RED</span></td></tr>
          <tr><td>Naharlagun AWS</td><td>Papum Pare, AP</td><td>25&deg;C</td><td style="color:#f39c12;font-weight:700;">135</td><td>94%</td><td>32 km/h</td><td><span class="badge badge-danger">RED</span></td></tr>
          <tr><td>Senapati AWS</td><td>Senapati, MN</td><td>23&deg;C</td><td style="color:#f39c12;font-weight:700;">112</td><td>91%</td><td>28 km/h</td><td><span class="badge badge-warning">ORANGE</span></td></tr>
          <tr><td>Haflong AWS</td><td>Dima Hasao, AS</td><td>26&deg;C</td><td style="color:#f39c12;font-weight:700;">89</td><td>87%</td><td>22 km/h</td><td><span class="badge badge-warning">ORANGE</span></td></tr>
          <tr><td>Kohima AWS</td><td>Kohima, NL</td><td>21&deg;C</td><td>68</td><td>82%</td><td>18 km/h</td><td><span class="badge badge-info">YELLOW</span></td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
</section>
''')

# SENSORS SECTION
w('''
<section id="sensors" class="section" style="padding-top:40px;background:rgba(22,160,133,.03);">
<div class="container">
  <div class="section-label">&#128225; IoT Sensor Network</div>
  <h2 class="section-title">Real-Time Sensor Dashboard</h2>
  <p class="section-subtitle">Live data from soil moisture sensors, inclinometers, piezometers, and rain gauges across NER</p>
  <div class="grid-3 fade-in" id="sensor-grid"></div>
  <div class="card fade-in" style="margin-top:24px;">
    <div class="flex-between" style="margin-bottom:16px;flex-wrap:wrap;gap:12px;">
      <h4>Sensor Network Overview</h4>
      <div style="display:flex;gap:10px;"><span class="badge badge-success">43 Online</span><span class="badge badge-warning">4 Warning</span><span class="badge badge-danger">1 Offline</span></div>
    </div>
    <div class="grid-4">
      <div style="text-align:center;padding:16px;background:var(--bg-dark);border-radius:var(--radius-sm);border:1px solid var(--border);"><div style="font-size:2rem;margin-bottom:6px;">&#128167;</div><div style="font-weight:700;font-size:1.2rem;color:#3498db;">32</div><div style="font-size:.78rem;color:var(--text-muted);">Soil Moisture Sensors</div></div>
      <div style="text-align:center;padding:16px;background:var(--bg-dark);border-radius:var(--radius-sm);border:1px solid var(--border);"><div style="font-size:2rem;margin-bottom:6px;">&#128208;</div><div style="font-weight:700;font-size:1.2rem;color:#f39c12;">18</div><div style="font-size:.78rem;color:var(--text-muted);">Inclinometers</div></div>
      <div style="text-align:center;padding:16px;background:var(--bg-dark);border-radius:var(--radius-sm);border:1px solid var(--border);"><div style="font-size:2rem;margin-bottom:6px;">&#127783;</div><div style="font-weight:700;font-size:1.2rem;color:#9b59b6;">24</div><div style="font-size:.78rem;color:var(--text-muted);">Rain Gauges</div></div>
      <div style="text-align:center;padding:16px;background:var(--bg-dark);border-radius:var(--radius-sm);border:1px solid var(--border);"><div style="font-size:2rem;margin-bottom:6px;">&#128207;</div><div style="font-weight:700;font-size:1.2rem;color:#2dd4bf;">12</div><div style="font-size:.78rem;color:var(--text-muted);">Piezometers</div></div>
    </div>
  </div>
</div>
</section>
''')

out.close()
print('Weather + Sensors written')
