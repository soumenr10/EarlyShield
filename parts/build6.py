import os
out = open(r'd:/sih2026/landslide-warning-system/index.html', 'a', encoding='utf-8')
def w(s): out.write(s + '\n')

# FIELD REPORT SECTION
w('''
<section id="field-report" class="section" style="padding-top:40px;background:rgba(37,99,168,.03);">
<div class="container">
  <div class="section-label">&#128203; Field Reporting</div>
  <h2 class="section-title">Geo-Tagged Field Report</h2>
  <p class="section-subtitle">Citizens and field officials can upload geo-tagged photos/videos of cracks, slope movement, or blocked roads</p>
  <div class="grid-2 fade-in" style="align-items:start;">
    <div class="report-form">
      <form id="field-report-form">
        <div class="form-row">
          <div class="form-group"><label class="form-label">Reporter Name <span>*</span></label><input type="text" class="form-control" placeholder="Your full name" required/></div>
          <div class="form-group"><label class="form-label">Contact Number <span>*</span></label><input type="tel" class="form-control" placeholder="+91 XXXXX XXXXX" required/></div>
        </div>
        <div class="form-row">
          <div class="form-group">
            <label class="form-label">State <span>*</span></label>
            <select class="form-control form-select" required>
              <option value="">Select State</option>
              <option>Arunachal Pradesh</option><option>Assam</option><option>Manipur</option>
              <option>Meghalaya</option><option>Mizoram</option><option>Nagaland</option>
              <option>Sikkim</option><option>Tripura</option>
            </select>
          </div>
          <div class="form-group"><label class="form-label">District <span>*</span></label><input type="text" class="form-control" placeholder="Enter district name" required/></div>
        </div>
        <div class="form-group">
          <label class="form-label">Incident Type <span>*</span></label>
          <select class="form-control form-select" required>
            <option value="">Select incident type</option>
            <option>Active Landslide</option><option>Ground Cracks</option><option>Slope Movement</option>
            <option>Blocked Road</option><option>Debris Flow</option><option>Flood + Landslide</option>
            <option>Soil Erosion</option><option>Building Damage</option><option>Other</option>
          </select>
        </div>
        <div class="form-group">
          <label class="form-label">Severity Level <span>*</span></label>
          <select class="form-control form-select" required>
            <option value="">Select severity</option>
            <option>Critical - Immediate Danger</option><option>High - Urgent Action Needed</option>
            <option>Medium - Monitoring Required</option><option>Low - Precautionary</option>
          </select>
        </div>
        <div class="form-group">
          <label class="form-label">Description <span>*</span></label>
          <textarea class="form-control" placeholder="Describe what you observed - size of cracks, distance of landslide, estimated area affected, number of people at risk..." required></textarea>
        </div>
        <div class="form-group">
          <label class="form-label">GPS Coordinates</label>
          <div style="display:flex;gap:10px;margin-bottom:10px;">
            <input type="text" id="lat-input" class="form-control" placeholder="Latitude" style="flex:1"/>
            <input type="text" id="lng-input" class="form-control" placeholder="Longitude" style="flex:1"/>
            <button type="button" class="btn btn-success" id="get-location-btn">&#128205; Get GPS</button>
          </div>
          <div class="geo-info" id="geo-display" style="display:none;">
            <span>&#128205;</span><span>Location: <strong class="geo-coords"></strong></span>
          </div>
        </div>
        <div class="form-group">
          <label class="form-label">Upload Photos/Videos</label>
          <div class="upload-zone" id="upload-zone">
            <div class="upload-icon">&#128248;</div>
            <p>Drag and drop photos/videos or click to browse</p>
            <p style="font-size:.8rem;color:var(--text-muted);">Supports: JPG, PNG, MP4, MOV - Max 50MB per file</p>
          </div>
          <input type="file" id="file-input" style="display:none;" multiple accept="image/*,video/*"/>
        </div>
        <div style="margin-bottom:20px;">
          <label style="display:flex;align-items:center;gap:10px;cursor:pointer;">
            <input type="checkbox" required style="width:18px;height:18px;accent-color:var(--primary-light)"/>
            <span style="font-size:.88rem;color:var(--text-secondary);">I confirm this is an accurate field observation. False reports may attract legal action under NDMA guidelines.</span>
          </label>
        </div>
        <button type="submit" class="btn btn-danger btn-lg" style="width:100%;">&#128228; Submit Field Report</button>
      </form>
    </div>
    <div>
      <div class="card" style="margin-bottom:16px;">
        <h4 style="margin-bottom:16px;">Reporting Guidelines</h4>
        <div style="display:flex;flex-direction:column;gap:12px;">
          <div style="display:flex;gap:12px;"><span style="font-size:1.2rem;flex-shrink:0;">1</span><div><strong>Ensure your safety first</strong><br/><span style="font-size:.82rem;color:var(--text-muted);">Do not approach unstable slopes or active landslides</span></div></div>
          <div style="display:flex;gap:12px;"><span style="font-size:1.2rem;flex-shrink:0;">2</span><div><strong>Enable GPS location</strong><br/><span style="font-size:.82rem;color:var(--text-muted);">Accurate coordinates help emergency response teams</span></div></div>
          <div style="display:flex;gap:12px;"><span style="font-size:1.2rem;flex-shrink:0;">3</span><div><strong>Upload clear visuals</strong><br/><span style="font-size:.82rem;color:var(--text-muted);">Photos/videos of cracks, movement, blocked roads</span></div></div>
          <div style="display:flex;gap:12px;"><span style="font-size:1.2rem;flex-shrink:0;">4</span><div><strong>Works offline too</strong><br/><span style="font-size:.82rem;color:var(--text-muted);">Data cached locally and synced when connected</span></div></div>
          <div style="display:flex;gap:12px;"><span style="font-size:1.2rem;flex-shrink:0;">5</span><div><strong>Reviewed by AI + Officials</strong><br/><span style="font-size:.82rem;color:var(--text-muted);">Reports trigger automated alerts within 2 minutes</span></div></div>
        </div>
        <div style="margin-top:16px;padding:12px;background:rgba(39,174,96,.08);border:1px solid rgba(39,174,96,.2);border-radius:var(--radius-sm);font-size:.82rem;color:#27ae60;">
          SMS: Send REPORT to 14567 | Available in 8 NE languages
        </div>
      </div>
      <div class="card">
        <h4 style="margin-bottom:16px;">Recent Field Reports</h4>
        <div style="display:flex;flex-direction:column;gap:12px;">
          <div style="padding:12px;background:var(--bg-dark);border-radius:var(--radius-sm);border-left:3px solid #e74c3c;">
            <div style="display:flex;justify-content:space-between;margin-bottom:4px;"><strong style="font-size:.88rem;">Active Landslide - NH-13</strong><span class="badge badge-danger" style="font-size:.68rem;">CRITICAL</span></div>
            <div style="font-size:.78rem;color:var(--text-muted);">Tawang, AP - 18 mins ago - Range Forest Officer</div>
            <div style="font-size:.82rem;margin-top:4px;">Large debris slide ~200m wide blocking NH-13. 50+ vehicles stranded.</div>
          </div>
          <div style="padding:12px;background:var(--bg-dark);border-radius:var(--radius-sm);border-left:3px solid #f39c12;">
            <div style="display:flex;justify-content:space-between;margin-bottom:4px;"><strong style="font-size:.88rem;">Ground Cracks Observed</strong><span class="badge badge-warning" style="font-size:.68rem;">HIGH</span></div>
            <div style="font-size:.78rem;color:var(--text-muted);">Ribhoi, Meghalaya - 1.2 hrs ago - Village Head</div>
            <div style="font-size:.82rem;margin-top:4px;">Multiple 5-8cm cracks in hillside. Trees tilting. 40 households at risk.</div>
          </div>
          <div style="padding:12px;background:var(--bg-dark);border-radius:var(--radius-sm);border-left:3px solid #3498db;">
            <div style="display:flex;justify-content:space-between;margin-bottom:4px;"><strong style="font-size:.88rem;">Road Erosion Reported</strong><span class="badge badge-info" style="font-size:.68rem;">MEDIUM</span></div>
            <div style="font-size:.78rem;color:var(--text-muted);">Haflong, Assam - 3 hrs ago - NHAI Engineer</div>
            <div style="font-size:.82rem;margin-top:4px;">Side slope erosion 15m section on NH-37 km 82. Immediate repair needed.</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</section>
''')

out.close()
print('Field Report written')
