import os
out = open(r'd:/sih2026/landslide-warning-system/index.html', 'a', encoding='utf-8')
def w(s): out.write(s + '\n')

# RESPONSE SECTION
w('''
<section id="response" class="section" style="padding-top:40px;">
<div class="container">
  <div class="section-label">&#128641; Emergency Response</div>
  <h2 class="section-title">Response Coordination</h2>
  <p class="section-subtitle">Automated emergency response prioritisation and coordination with NDRF, SDRF, and district authorities</p>
  <div class="grid-2 fade-in">
    <div class="card">
      <h4 style="margin-bottom:20px;">Active Response Timeline - Tawang Incident</h4>
      <div class="response-timeline">
        <div class="timeline-item done"><div class="timeline-time">19:12 IST - Aug 29, 2026</div><div class="timeline-title">AI Alert Generated</div><div class="timeline-desc">System detected 89% probability. Automated alert triggered.</div></div>
        <div class="timeline-item done"><div class="timeline-time">19:14 IST</div><div class="timeline-title">SMS Alerts Dispatched</div><div class="timeline-desc">3,200+ residents notified via SMS, app push, and IVR calls.</div></div>
        <div class="timeline-item done"><div class="timeline-time">19:17 IST</div><div class="timeline-title">District Administration Notified</div><div class="timeline-desc">DC Tawang and DDMA received official alert. EOC activated.</div></div>
        <div class="timeline-item done"><div class="timeline-time">19:25 IST</div><div class="timeline-title">NDRF Team Mobilised</div><div class="timeline-desc">Team 7 (Guwahati) - 45 personnel en route to Tawang.</div></div>
        <div class="timeline-item active"><div class="timeline-time">19:40 IST - IN PROGRESS</div><div class="timeline-title">Helicopter Survey Underway</div><div class="timeline-desc">IAF Mi-17 helicopter conducting aerial assessment of affected zones.</div></div>
        <div class="timeline-item pending"><div class="timeline-time">ETA: 20:30 IST</div><div class="timeline-title">Evacuation to Begin</div><div class="timeline-desc">12 villages within 500m of critical slopes to be evacuated.</div></div>
        <div class="timeline-item pending"><div class="timeline-time">ETA: 21:00 IST</div><div class="timeline-title">Medical Teams Deploy</div><div class="timeline-desc">3 medical teams with emergency supplies heading to relief camps.</div></div>
      </div>
    </div>
    <div>
      <div class="card" style="margin-bottom:16px;">
        <h4 style="margin-bottom:16px;">Emergency Contacts</h4>
        <div class="contact-card"><div class="contact-avatar" style="background:rgba(231,76,60,.15);">&#128680;</div><div class="contact-info"><div class="name">NDRF Control Room</div><div class="role">National Disaster Response Force - 24/7</div></div><div class="contact-actions"><a href="tel:9711077372" class="btn btn-success btn-sm">&#128222; Call</a></div></div>
        <div class="contact-card"><div class="contact-avatar" style="background:rgba(243,156,18,.15);">&#127963;</div><div class="contact-info"><div class="name">SDMA NER Helpline</div><div class="role">State Disaster Management Authority</div></div><div class="contact-actions"><a href="tel:1070" class="btn btn-success btn-sm">&#128222; 1070</a></div></div>
        <div class="contact-card"><div class="contact-avatar" style="background:rgba(39,174,96,.15);">&#128682;</div><div class="contact-info"><div class="name">National Emergency</div><div class="role">Police - Fire - Ambulance - Disaster</div></div><div class="contact-actions"><a href="tel:112" class="btn btn-danger btn-sm">&#128222; 112</a></div></div>
        <div class="contact-card"><div class="contact-avatar" style="background:rgba(37,99,168,.15);">&#127968;</div><div class="contact-info"><div class="name">IMD Flood Warning Centre</div><div class="role">Guwahati Meteorological Centre</div></div><div class="contact-actions"><a href="tel:03612731030" class="btn btn-outline btn-sm">&#128222; Call</a></div></div>
      </div>
      <div class="card">
        <h4 style="margin-bottom:16px;">Emergency Prioritisation Matrix</h4>
        <div style="display:flex;flex-direction:column;gap:10px;">
          <div style="padding:12px;background:rgba(231,76,60,.08);border:1px solid rgba(231,76,60,.2);border-radius:var(--radius-sm);"><div style="display:flex;justify-content:space-between;margin-bottom:6px;"><strong style="color:#e74c3c;">P1 - CRITICAL</strong><span class="badge badge-danger">6 Zones</span></div><div style="font-size:.82rem;color:var(--text-muted);">Immediate evacuation. NDRF + helicopters. Road closures enforced.</div></div>
          <div style="padding:12px;background:rgba(243,156,18,.08);border:1px solid rgba(243,156,18,.2);border-radius:var(--radius-sm);"><div style="display:flex;justify-content:space-between;margin-bottom:6px;"><strong style="color:#f39c12;">P2 - HIGH</strong><span class="badge badge-warning">14 Zones</span></div><div style="font-size:.82rem;color:var(--text-muted);">Prepositioning of SDRF teams. Community alerts. Route diversions.</div></div>
          <div style="padding:12px;background:rgba(37,99,168,.08);border:1px solid rgba(37,99,168,.2);border-radius:var(--radius-sm);"><div style="display:flex;justify-content:space-between;margin-bottom:6px;"><strong style="color:#60a5fa;">P3 - WATCH</strong><span class="badge badge-info">28 Zones</span></div><div style="font-size:.82rem;color:var(--text-muted);">Enhanced monitoring. Local teams on standby. Community awareness.</div></div>
        </div>
        <div style="margin-top:16px;display:flex;gap:10px;flex-wrap:wrap;">
          <button class="btn btn-danger" style="flex:1;" onclick="showToast('danger','BROADCAST','Emergency broadcast sent to all 8 NER states.',8000)">Mass Alert All States</button>
          <button class="btn btn-outline" style="flex:1;" onclick="showToast('info','Report','Generating situation report for NDMA...',3000)">Generate SitRep</button>
        </div>
      </div>
    </div>
  </div>
</div>
</section>
''')

# FOOTER
w('''
<footer>
<div class="container">
  <div class="footer-grid">
    <div class="footer-brand">
      <div class="nav-logo" style="margin-bottom:12px;">
        <div class="nav-logo-icon" style="animation:none;font-size:1.4rem;display:flex;align-items:center;justify-content:center;">&#9968;</div>
        <div class="nav-logo-text"><strong style="font-size:1.1rem;">LandSafe NER</strong><span>AI Early Warning System</span></div>
      </div>
      <p>AI-powered landslide early warning and monitoring platform for the North Eastern Region of India. Developed for Smart India Hackathon 2026.</p>
      <div style="display:flex;gap:10px;margin-top:16px;flex-wrap:wrap;">
        <span class="partner-logo">NDMA</span><span class="partner-logo">IMD</span><span class="partner-logo">ISRO</span><span class="partner-logo">GSI</span><span class="partner-logo">NIC</span>
      </div>
    </div>
    <div class="footer-col">
      <h5>Platform</h5>
      <ul>
        <li><a href="#dashboard">Dashboard</a></li>
        <li><a href="#map-section">GIS Map</a></li>
        <li><a href="#alerts">Alerts</a></li>
        <li><a href="#analytics">Analytics</a></li>
        <li><a href="#field-report">Field Report</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h5>Resources</h5>
      <ul>
        <li><a href="#">User Manual</a></li>
        <li><a href="#">API Documentation</a></li>
        <li><a href="#">Sensor Network</a></li>
        <li><a href="#">Satellite Feed</a></li>
        <li><a href="#">Historical Data</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h5>Emergency</h5>
      <ul>
        <li><a href="tel:112">112 - National Emergency</a></li>
        <li><a href="tel:1070">1070 - SDMA Helpline</a></li>
        <li><a href="tel:9711077372">NDRF Control Room</a></li>
        <li><a href="#">Download App</a></li>
        <li><a href="#">Contact Support</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <p>2026 LandSafe NER | Smart India Hackathon 2026 | Built for disaster resilience</p>
    <p>Data: IMD - ISRO Bhuvan - GSI - NDMA - Sentinel-2 - OpenStreetMap</p>
  </div>
</div>
</footer>
''')

# LANGUAGE MODAL
w('''
<div class="modal-overlay" id="lang-modal">
<div class="modal">
  <div class="flex-between" style="margin-bottom:20px;">
    <h3 style="margin:0;">Select Language</h3>
    <button data-lang-close style="background:none;border:none;color:var(--text-muted);font-size:1.3rem;cursor:pointer;">X</button>
  </div>
  <div class="lang-grid">
    <button class="lang-btn selected" data-lang="en"><span class="native">English</span><small>English</small></button>
    <button class="lang-btn" data-lang="hi"><span class="native">&#2361;&#2367;&#2306;&#2342;&#2368;</span><small>Hindi</small></button>
    <button class="lang-btn" data-lang="as"><span class="native">&#2437;&#2488;&#2478;&#2496;&#2479;&#2492;&#2494;</span><small>Assamese</small></button>
    <button class="lang-btn" data-lang="bn"><span class="native">&#2476;&#2494;&#2434;&#2482;&#2494;</span><small>Bengali</small></button>
    <button class="lang-btn" data-lang="mni"><span class="native">Meitei</span><small>Manipur</small></button>
    <button class="lang-btn" data-lang="en"><span class="native">Khasi</span><small>Meghalaya</small></button>
    <button class="lang-btn" data-lang="en"><span class="native">Mizo</span><small>Mizoram</small></button>
    <button class="lang-btn" data-lang="en"><span class="native">Nagamese</span><small>Nagaland</small></button>
    <button class="lang-btn" data-lang="en"><span class="native">Nepali</span><small>Sikkim</small></button>
  </div>
  <div style="padding:12px;background:rgba(37,99,168,.08);border-radius:var(--radius-sm);font-size:.82rem;color:var(--text-muted);margin-bottom:16px;">
    Emergency alerts are automatically sent in the local language of each district.
  </div>
  <div style="display:flex;gap:10px;">
    <button class="btn btn-primary" id="apply-lang" style="flex:1;">Apply Language</button>
    <button class="btn btn-ghost" data-lang-close>Cancel</button>
  </div>
</div>
</div>
''')

# TOAST + SOS + SCRIPTS
w('''
<div class="toast-container" id="toast-container"></div>
<button class="sos-btn" title="Send SOS Emergency Alert">SOS</button>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<script src="assets/js/main.js"></script>
<script>
  function updateClock(){
    var now=new Date();
    var t=document.getElementById("last-updated-time");
    if(t){
      var h=String(now.getHours()).padStart(2,"0");
      var m=String(now.getMinutes()).padStart(2,"0");
      var s=String(now.getSeconds()).padStart(2,"0");
      t.textContent="Last updated: "+h+":"+m+":"+s+" IST";
    }
  }
  setInterval(updateClock,1000);
  updateClock();
  document.getElementById("hamburger").addEventListener("click",function(){
    document.getElementById("mobile-menu").classList.toggle("open");
  });
  document.getElementById("nav-sos").addEventListener("click",function(){
    document.querySelector(".sos-btn").click();
  });
  document.getElementById("alert-bell").addEventListener("click",function(){
    document.getElementById("alert-list").scrollIntoView({behavior:"smooth"});
  });
  document.getElementById("mob-sos-btn") && document.getElementById("mob-sos-btn").addEventListener("click",function(){
    document.getElementById("mobile-menu").classList.remove("open");
    document.querySelector(".sos-btn").click();
  });
</script>
</body>
</html>
''')

out.close()
print('Response + Footer + Scripts written. HTML complete!')
