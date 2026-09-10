import os
out = open(r'd:/sih2026/landslide-warning-system/index.html', 'a', encoding='utf-8')
def w(s): out.write(s + '\n')

# GIS MAP SECTION
w('''
<section id="map-section" class="section" style="padding-top:40px;">
<div class="container">
  <div class="section-label">&#128506; GIS Mapping</div>
  <h2 class="section-title">Interactive Risk Heatmap</h2>
  <p class="section-subtitle">Real-time visualization of landslide-prone areas, vulnerable infrastructure, and active monitoring zones</p>
  <div class="map-sidebar fade-in">
    <div class="map-container">
      <div class="map-toolbar">
        <div class="map-controls">
          <button class="map-filter-btn active" data-filter="all">All Risks</button>
          <button class="map-filter-btn" data-filter="critical">Critical</button>
          <button class="map-filter-btn" data-filter="sensors">Sensors</button>
          <button class="map-filter-btn" data-filter="roads">Roads</button>
          <button class="map-filter-btn" data-filter="villages">Villages</button>
        </div>
        <div class="view-toggle">
          <button class="view-btn active" data-view="map">Map</button>
          <button class="view-btn" data-view="satellite">Satellite</button>
        </div>
      </div>
      <div id="main-map"></div>
      <div class="map-legend">
        <div class="legend-item"><div class="legend-dot critical"></div>Critical (&gt;80%)</div>
        <div class="legend-item"><div class="legend-dot high"></div>High (60-80%)</div>
        <div class="legend-item"><div class="legend-dot medium"></div>Medium (40-60%)</div>
        <div class="legend-item"><div class="legend-dot safe"></div>Low (&lt;40%)</div>
        <div style="margin-left:auto;font-size:.78rem;color:var(--text-muted);">Click marker for details</div>
      </div>
    </div>
    <div>
      <div class="card" style="margin-bottom:16px;">
        <h4 style="margin-bottom:16px;">&#128205; Location Details</h4>
        <div id="map-side-panel">
          <div style="text-align:center;padding:20px;color:var(--text-muted);">
            <div style="font-size:2rem;margin-bottom:8px;">&#128506;</div>
            <p style="font-size:.88rem;">Click any map marker to view detailed risk information</p>
          </div>
        </div>
      </div>
      <div class="card">
        <h4 style="margin-bottom:14px;">&#128202; Zone Summary</h4>
        <div style="display:flex;flex-direction:column;gap:10px;">
          <div style="display:flex;justify-content:space-between;align-items:center;"><span style="font-size:.85rem;display:flex;align-items:center;gap:6px;"><span style="color:#e74c3c;">&#9679;</span> Critical</span><div style="flex:1;margin:0 12px;"><div class="risk-meter-bar"><div style="width:5%;height:100%;border-radius:3px;background:#e74c3c;"></div></div></div><span style="font-size:.85rem;font-weight:700;color:#e74c3c;">6</span></div>
          <div style="display:flex;justify-content:space-between;align-items:center;"><span style="font-size:.85rem;display:flex;align-items:center;gap:6px;"><span style="color:#f39c12;">&#9679;</span> High</span><div style="flex:1;margin:0 12px;"><div class="risk-meter-bar"><div style="width:11%;height:100%;border-radius:3px;background:#f39c12;"></div></div></div><span style="font-size:.85rem;font-weight:700;color:#f39c12;">14</span></div>
          <div style="display:flex;justify-content:space-between;align-items:center;"><span style="font-size:.85rem;display:flex;align-items:center;gap:6px;"><span style="color:#f1c40f;">&#9679;</span> Medium</span><div style="flex:1;margin:0 12px;"><div class="risk-meter-bar"><div style="width:22%;height:100%;border-radius:3px;background:#f1c40f;"></div></div></div><span style="font-size:.85rem;font-weight:700;color:#f1c40f;">28</span></div>
          <div style="display:flex;justify-content:space-between;align-items:center;"><span style="font-size:.85rem;display:flex;align-items:center;gap:6px;"><span style="color:#27ae60;">&#9679;</span> Safe</span><div style="flex:1;margin:0 12px;"><div class="risk-meter-bar"><div style="width:62%;height:100%;border-radius:3px;background:#27ae60;"></div></div></div><span style="font-size:.85rem;font-weight:700;color:#27ae60;">76</span></div>
        </div>
        <div style="margin-top:16px;padding-top:16px;border-top:1px solid var(--border);">
          <button class="btn btn-primary" style="width:100%;" onclick="showToast('info','Export','GIS data export initiated in GeoJSON format',3000)">&#128229; Export GIS Data</button>
        </div>
      </div>
    </div>
  </div>
</div>
</section>
''')

# ALERTS SECTION
w('''
<section id="alerts" class="section" style="padding-top:40px;">
<div class="container">
  <div class="flex-between" style="margin-bottom:8px;flex-wrap:wrap;gap:12px;">
    <div>
      <div class="section-label">&#128680; Alert Management</div>
      <h2 style="font-size:2rem;">Active Alerts &amp; Warnings</h2>
    </div>
    <div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap;">
      <div style="display:flex;gap:6px;">
        <button class="map-filter-btn alert-filter-btn active" data-filter="all">All</button>
        <button class="map-filter-btn alert-filter-btn" data-filter="critical">Critical</button>
        <button class="map-filter-btn alert-filter-btn" data-filter="high">High</button>
        <button class="map-filter-btn alert-filter-btn" data-filter="medium">Medium</button>
      </div>
      <button class="btn btn-danger" onclick="showToast('danger','BROADCAST','Emergency broadcast sent to all 8 NER states. 1,847 SMS alerts dispatched.',8000)">&#128226; Broadcast All</button>
    </div>
  </div>
  <p class="section-subtitle" style="text-align:left;margin-bottom:24px;">AI-generated alerts ranked by urgency. <span id="alert-count" style="color:#e74c3c;font-weight:700;">7</span> active alerts across NER.</p>
  <div id="alert-list"></div>
</div>
</section>
''')

# ANALYTICS SECTION
w('''
<section id="analytics" class="section" style="padding-top:40px;">
<div class="container">
  <div class="section-label">&#128200; AI/ML Analytics</div>
  <h2 class="section-title">Predictive Analytics Engine</h2>
  <p class="section-subtitle">Machine learning models analyzing rainfall patterns, soil conditions, terrain data and historical records</p>
  <div class="grid-2 fade-in" style="margin-bottom:24px;">
    <div class="card"><h4 style="margin-bottom:16px;">Risk Zone Trend (7 Days)</h4><div class="chart-card"><canvas id="risk-trend-chart"></canvas></div></div>
    <div class="card"><h4 style="margin-bottom:16px;">District Rainfall vs Critical Threshold</h4><div class="chart-card"><canvas id="rainfall-chart"></canvas></div></div>
  </div>
  <div class="grid-2 fade-in">
    <div class="card"><h4 style="margin-bottom:16px;">AI Multi-factor Risk Analysis</h4><div class="chart-card"><canvas id="ml-chart"></canvas></div></div>
    <div class="card"><h4 style="margin-bottom:16px;">Zone Risk Distribution</h4><div class="chart-card"><canvas id="zone-chart"></canvas></div></div>
  </div>
  <div class="card fade-in" style="margin-top:24px;">
    <div class="flex-between" style="margin-bottom:20px;flex-wrap:wrap;gap:12px;">
      <h4>&#129302; AI/ML Model Pipeline</h4>
      <span class="badge badge-success">Models Live</span>
    </div>
    <div class="grid-3">
      <div style="padding:16px;background:var(--bg-dark);border:1px solid var(--border);border-radius:var(--radius-sm);">
        <div style="font-size:1.5rem;margin-bottom:8px;">&#127810;</div>
        <div style="font-weight:700;margin-bottom:4px;">Random Forest</div>
        <div style="font-size:.82rem;color:var(--text-muted);margin-bottom:10px;">Terrain + Soil Classification</div>
        <div style="display:flex;justify-content:space-between;font-size:.8rem;"><span>Accuracy</span><span style="color:#4ade80;font-weight:700;">91.2%</span></div>
        <div class="risk-meter-bar" style="margin-top:4px;"><div style="width:91%;height:100%;border-radius:3px;background:#27ae60;"></div></div>
      </div>
      <div style="padding:16px;background:var(--bg-dark);border:1px solid var(--border);border-radius:var(--radius-sm);">
        <div style="font-size:1.5rem;margin-bottom:8px;">&#129504;</div>
        <div style="font-weight:700;margin-bottom:4px;">LSTM Neural Net</div>
        <div style="font-size:.82rem;color:var(--text-muted);margin-bottom:10px;">Rainfall Time-Series Forecasting</div>
        <div style="display:flex;justify-content:space-between;font-size:.8rem;"><span>Accuracy</span><span style="color:#60a5fa;font-weight:700;">93.7%</span></div>
        <div class="risk-meter-bar" style="margin-top:4px;"><div style="width:93%;height:100%;border-radius:3px;background:#3498db;"></div></div>
      </div>
      <div style="padding:16px;background:var(--bg-dark);border:1px solid var(--border);border-radius:var(--radius-sm);">
        <div style="font-size:1.5rem;margin-bottom:8px;">&#9889;</div>
        <div style="font-weight:700;margin-bottom:4px;">XGBoost Ensemble</div>
        <div style="font-size:.82rem;color:var(--text-muted);margin-bottom:10px;">Multi-variable Risk Scoring</div>
        <div style="display:flex;justify-content:space-between;font-size:.8rem;"><span>Accuracy</span><span style="color:#a78bfa;font-weight:700;">94.1%</span></div>
        <div class="risk-meter-bar" style="margin-top:4px;"><div style="width:94%;height:100%;border-radius:3px;background:#9b59b6;"></div></div>
      </div>
    </div>
    <div style="margin-top:20px;padding:16px;background:rgba(37,99,168,.08);border:1px solid rgba(37,99,168,.2);border-radius:var(--radius-sm);">
      <div style="font-size:.85rem;font-weight:700;margin-bottom:8px;color:#60a5fa;">Data Sources Integrated:</div>
      <div style="display:flex;gap:8px;flex-wrap:wrap;">
        <span class="chip">Sentinel-2 Imagery</span>
        <span class="chip">IMD Weather API</span>
        <span class="chip">IoT Sensor Network</span>
        <span class="chip">SRTM DEM Terrain</span>
        <span class="chip">Historical Records 1980-2025</span>
        <span class="chip">NDVI Vegetation Index</span>
        <span class="chip">MODIS Soil Moisture</span>
        <span class="chip">Seismic Data NGRI</span>
      </div>
    </div>
  </div>
</div>
</section>
''')

out.close()
print('Map + Alerts + Analytics written')
