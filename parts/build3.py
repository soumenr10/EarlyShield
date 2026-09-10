import os
out = open(r'd:/sih2026/landslide-warning-system/index.html', 'a', encoding='utf-8')
def w(s): out.write(s + '\n')

# DASHBOARD
w('''
<section id="dashboard" class="section">
<div class="container">
  <div class="section-label">&#128202; Real-Time Dashboard</div>
  <h2 class="section-title">Situation Overview</h2>
  <p class="section-subtitle">Live data from sensors, satellites, and AI predictive models across NER districts</p>
  <div class="grid-4 fade-in" style="margin-bottom:24px;">
    <div class="card card-danger">
      <div class="stat-card"><div class="stat-icon red">&#128680;</div><div class="stat-body">
        <div class="number" style="color:#e74c3c;">6</div>
        <div class="label">Critical Risk Zones</div>
        <div class="change change-up">&#8593; 2 from yesterday</div>
      </div></div>
      <div class="risk-meter"><div class="risk-meter-bar"><div class="risk-meter-fill" data-width="89" style="background:#e74c3c;"></div></div>
      <div style="display:flex;justify-content:space-between;font-size:.72rem;color:var(--text-muted);margin-top:4px;"><span>Risk Index</span><span style="color:#e74c3c;font-weight:700;">89/100</span></div></div>
    </div>
    <div class="card card-warning">
      <div class="stat-card"><div class="stat-icon orange">&#9888;</div><div class="stat-body">
        <div class="number" style="color:#f39c12;">187</div>
        <div class="label">Peak Rainfall mm/hr</div>
        <div class="change change-up">&#8593; 42mm from 6hr ago</div>
      </div></div>
      <div class="risk-meter"><div class="risk-meter-bar"><div class="risk-meter-fill" data-width="75" style="background:#f39c12;"></div></div>
      <div style="display:flex;justify-content:space-between;font-size:.72rem;color:var(--text-muted);margin-top:4px;"><span>Cherrapunji Station</span><span style="color:#f39c12;font-weight:700;">75%</span></div></div>
    </div>
    <div class="card">
      <div class="stat-card"><div class="stat-icon blue">&#128225;</div><div class="stat-body">
        <div class="number" style="color:#60a5fa;">48</div>
        <div class="label">Active Sensor Nodes</div>
        <div class="change" style="color:#f39c12;">&#9888; 1 offline (Kohima)</div>
      </div></div>
      <div style="display:flex;gap:6px;margin-top:12px;flex-wrap:wrap;">
        <span class="badge badge-success">43 Online</span>
        <span class="badge badge-warning">4 Warning</span>
        <span class="badge badge-danger">1 Offline</span>
      </div>
    </div>
    <div class="card">
      <div class="stat-card"><div class="stat-icon purple">&#129302;</div><div class="stat-body">
        <div class="number" style="color:#a78bfa;">94%</div>
        <div class="label">AI Model Accuracy</div>
        <div class="change change-down">&#8593; 2.3% this month</div>
      </div></div>
      <div style="margin-top:12px;font-size:.78rem;color:var(--text-muted);">
        <div style="display:flex;justify-content:space-between;margin-bottom:4px;"><span>RandomForest</span><span style="color:#a78bfa;">91%</span></div>
        <div style="display:flex;justify-content:space-between;margin-bottom:4px;"><span>LSTM Neural Net</span><span style="color:#a78bfa;">93%</span></div>
        <div style="display:flex;justify-content:space-between;"><span>XGBoost Ensemble</span><span style="color:#a78bfa;">94%</span></div>
      </div>
    </div>
  </div>
  <div class="grid-4 fade-in" style="margin-bottom:24px;">
    <div class="card"><div class="stat-card"><div class="stat-icon teal">&#127968;</div><div class="stat-body"><div class="number" style="color:#2dd4bf;">23,840</div><div class="label">People in Risk Zones</div><div class="change change-up">&#8593; 1,200 since morning</div></div></div></div>
    <div class="card"><div class="stat-card"><div class="stat-icon red">&#128739;</div><div class="stat-body"><div class="number" style="color:#e74c3c;">12</div><div class="label">Roads at Risk</div><div class="change change-up">&#8593; 3 new (NH-13, NH-44, NH-6)</div></div></div></div>
    <div class="card"><div class="stat-card"><div class="stat-icon green">&#128241;</div><div class="stat-body"><div class="number" style="color:#4ade80;">1,847</div><div class="label">SMS Alerts Sent Today</div><div class="change change-down">98.6% delivered</div></div></div></div>
    <div class="card"><div class="stat-card"><div class="stat-icon orange">&#128641;</div><div class="stat-body"><div class="number" style="color:#fb923c;">7</div><div class="label">NDRF Teams Deployed</div><div class="change" style="color:#60a5fa;">3 on standby</div></div></div></div>
  </div>
  <div class="card full-width fade-in">
    <div class="flex-between" style="margin-bottom:20px;flex-wrap:wrap;gap:12px;">
      <h4>&#128739; Road Connectivity Status &mdash; Critical NH Routes</h4>
      <span class="badge badge-warning">12 Routes at Risk</span>
    </div>
    <div class="table-wrap">
      <table class="data-table">
        <thead><tr><th>Route</th><th>Section</th><th>Status</th><th>Risk</th><th>Rainfall</th><th>Alternate</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td><strong>NH-13</strong></td><td>Km 34-67 (Tawang)</td><td><span class="badge badge-danger">AT RISK</span></td><td><span style="color:#e74c3c;font-weight:700;">CRITICAL</span></td><td>142 mm/hr</td><td>Via Tenga Valley (+3.5hr)</td><td><button class="btn btn-danger btn-sm" onclick="showToast('danger','NH-13 Alert','Emergency advisory issued for NH-13.',5000)">Alert</button></td></tr>
          <tr><td><strong>NH-27</strong></td><td>Papum Pare section</td><td><span class="badge badge-danger">AT RISK</span></td><td><span style="color:#e74c3c;font-weight:700;">CRITICAL</span></td><td>135 mm/hr</td><td>Via Rono Hills</td><td><button class="btn btn-danger btn-sm" onclick="showToast('danger','NH-27 Alert','Emergency advisory issued for NH-27.',5000)">Alert</button></td></tr>
          <tr><td><strong>NH-6</strong></td><td>Km 12-28 (Cherrapunji)</td><td><span class="badge badge-warning">WARNING</span></td><td><span style="color:#f39c12;font-weight:700;">HIGH</span></td><td>187 mm/hr</td><td>Via Shillong Bypass</td><td><button class="btn btn-warning btn-sm" onclick="showToast('warning','NH-6 Warning','Warning advisory issued for NH-6.',4000)">Alert</button></td></tr>
          <tr><td><strong>NH-44</strong></td><td>Senapati Km 34</td><td><span class="badge badge-warning">WARNING</span></td><td><span style="color:#f39c12;font-weight:700;">HIGH</span></td><td>112 mm/hr</td><td>Via Imphal Bypass</td><td><button class="btn btn-warning btn-sm" onclick="showToast('warning','NH-44 Warning','Warning issued for NH-44.',4000)">Alert</button></td></tr>
          <tr><td><strong>NH-37</strong></td><td>Haflong bypass</td><td><span class="badge badge-info">WATCH</span></td><td><span style="color:#60a5fa;font-weight:700;">MEDIUM</span></td><td>89 mm/hr</td><td>NH-54 alternate</td><td><button class="btn btn-outline btn-sm" onclick="showToast('info','NH-37 Watch','NH-37 added to watch list.',3000)">Watch</button></td></tr>
          <tr><td><strong>NH-102</strong></td><td>Nagaland section</td><td><span class="badge badge-success">OPEN</span></td><td><span style="color:#27ae60;font-weight:700;">LOW</span></td><td>68 mm/hr</td><td>Not required</td><td><button class="btn btn-ghost btn-sm">Monitor</button></td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
</section>
''')
out.close()
print('Dashboard written')
