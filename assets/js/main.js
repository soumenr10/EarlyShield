"use strict";

const AppState = {
  currentLang: "en",
  alertCount: 7,
  isOffline: false,
  sensorData: {},
  maps: {},
  charts: {},
  layers: null,
  currentBase: "map",
  mapOverlays: null
};

const TRANSLATIONS = {
  en: { nav_home: "Home", nav_dashboard: "Dashboard", nav_map: "GIS Map", nav_alerts: "Alerts", nav_report: "Field Report", nav_analytics: "Analytics", nav_weather: "Weather", nav_sensors: "Sensors", nav_response: "Response" },
  hi: { nav_home: "होम", nav_dashboard: "डैशबोर्ड", nav_map: "GIS मानचित्र", nav_alerts: "अलर्ट", nav_report: "फ़ील्ड रिपोर्ट", nav_analytics: "विश्लेषण", nav_weather: "मौसम", nav_sensors: "सेंसर", nav_response: "प्रतिक्रिया" },
  as: { nav_home: "মূল পৃষ্ঠা", nav_dashboard: "ড্যাশবোৰ্ড", nav_map: "মানচিত্ৰ", nav_alerts: "সতৰ্কতা", nav_report: "ফিল্ড ৰিপোৰ্ট", nav_analytics: "বিশ্লেষণ", nav_weather: "বতৰ", nav_sensors: "চেন্সৰ", nav_response: "সঁহাৰি" },
  bn: { nav_home: "হোম", nav_dashboard: "ড্যাশবোর্ড", nav_map: "GIS মানচিত্র", nav_alerts: "সতর্কতা", nav_report: "ফিল্ড রিপোর্ট", nav_analytics: "বিশ্লেষণ", nav_weather: "আবহাওয়া", nav_sensors: "সেন্সর", nav_response: "সাড়া" },
  mni: { nav_home: "Home", nav_dashboard: "Dashboard", nav_map: "Map", nav_alerts: "Alert", nav_report: "Field Report", nav_analytics: "Analytics", nav_weather: "Weather", nav_sensors: "Sensors", nav_response: "Response" }
};

const NER_LOCATIONS = [
  { name: "Tawang, Arunachal Pradesh", lat: 27.586, lng: 91.865, risk: "critical", probability: 89, rainfall: 142, soilMoisture: 94, slope: 72 },
  { name: "Papum Pare, Arunachal Pradesh", lat: 27.083, lng: 93.611, risk: "critical", probability: 85, rainfall: 135, soilMoisture: 91, slope: 68 },
  { name: "Cherrapunji, Meghalaya", lat: 25.288, lng: 91.701, risk: "high", probability: 76, rainfall: 187, soilMoisture: 88, slope: 45 },
  { name: "Ribhoi, Meghalaya", lat: 25.7, lng: 91.9, risk: "high", probability: 71, rainfall: 165, soilMoisture: 85, slope: 52 },
  { name: "Tamenglong, Manipur", lat: 24.97, lng: 93.5, risk: "high", probability: 69, rainfall: 128, soilMoisture: 82, slope: 61 },
  { name: "Senapati, Manipur", lat: 25.266, lng: 94.033, risk: "medium", probability: 58, rainfall: 112, soilMoisture: 76, slope: 48 },
  { name: "Zunheboto, Nagaland", lat: 25.91, lng: 94.55, risk: "medium", probability: 52, rainfall: 98, soilMoisture: 72, slope: 55 },
  { name: "Haflong, Assam", lat: 25.168, lng: 93.015, risk: "medium", probability: 47, rainfall: 89, soilMoisture: 68, slope: 38 },
  { name: "Lunglei, Mizoram", lat: 22.886, lng: 92.735, risk: "low", probability: 32, rainfall: 76, soilMoisture: 61, slope: 42 },
  { name: "Kohima, Nagaland", lat: 25.674, lng: 94.11, risk: "low", probability: 28, rainfall: 68, soilMoisture: 55, slope: 35 },
  { name: "Imphal, Manipur", lat: 24.817, lng: 93.936, risk: "low", probability: 21, rainfall: 52, soilMoisture: 48, slope: 22 },
  { name: "Agartala, Tripura", lat: 23.831, lng: 91.286, risk: "low", probability: 19, rainfall: 45, soilMoisture: 42, slope: 18 }
];

const RISK_COLORS = { critical: "#c0392b", high: "#f47920", medium: "#d4ac0d", low: "#1a7a3e" };

const ALERT_DATA = [
  { level: "critical", icon: "🚨", title: "CRITICAL: Imminent Landslide Risk", location: "Tawang District, Arunachal Pradesh", time: "2 minutes ago", type: "AI Prediction", description: "AI model predicts 89% probability of landslide in next 6 hours. Soil moisture at 94%, rainfall 142mm/hr. NH-13 likely to be affected.", district: "Tawang", affected: "~3,200 people" },
  { level: "critical", icon: "🌧️", title: "Extreme Rainfall Warning", location: "Papum Pare, Arunachal Pradesh", time: "11 minutes ago", type: "IMD Alert", description: "Red rainfall alert issued by IMD. 135mm/hr recorded. Multiple slope failure points identified via satellite imagery.", district: "Papum Pare", affected: "~5,800 people" },
  { level: "high", icon: "⚠️", title: "HIGH: Slope Instability Detected", location: "Cherrapunji, East Khasi Hills, Meghalaya", time: "24 minutes ago", type: "Sensor Alert", description: "Inclinometer readings show 3.2 degree slope movement. Ground cracks spotted by field officer. NH-6 at risk.", district: "East Khasi Hills", affected: "~1,450 people" },
  { level: "high", icon: "⛈️", title: "Debris Flow Risk - NH-44", location: "Senapati District, Manipur", time: "1 hour ago", type: "Satellite Analysis", description: "Sentinel-2 imagery shows 40% increase in saturated soil area near NH-44 km 34. Debris flow possible in 12-18 hrs.", district: "Senapati", affected: "~890 people" },
  { level: "medium", icon: "📡", title: "Sensor Threshold Exceeded", location: "Haflong, Assam", time: "2 hours ago", type: "Sensor Network", description: "Piezometer readings crossed 85% threshold. Soil moisture sensors elevated. Monitoring increased to 15-min intervals.", district: "Dima Hasao", affected: "~400 people" }
];

const SENSOR_NODES = [
  { id: "SN-001", name: "Tawang Ridge Station", district: "Tawang, AP", status: "warning", moisture: 94, rainfall: 142, inclination: 3.2, battery: 72 },
  { id: "SN-002", name: "Cherrapunji Valley", district: "East Khasi Hills, ML", status: "online", moisture: 88, rainfall: 187, inclination: 1.1, battery: 85 },
  { id: "SN-003", name: "Tamenglong Summit", district: "Tamenglong, MN", status: "online", moisture: 82, rainfall: 128, inclination: 2.4, battery: 64 },
  { id: "SN-004", name: "Haflong Hillside", district: "Dima Hasao, AS", status: "online", moisture: 68, rainfall: 89, inclination: 0.8, battery: 91 },
  { id: "SN-005", name: "Kohima East Slope", district: "Kohima, NL", status: "offline", moisture: 55, rainfall: 68, inclination: 0.4, battery: 12 },
  { id: "SN-006", name: "Lunglei Forest Node", district: "Lunglei, MZ", status: "online", moisture: 61, rainfall: 76, inclination: 0.6, battery: 78 }
];

const WEATHER_FORECAST = [
  { day: "Today", icon: "⛈️", mm: 142, risk: "high", pct: 95 },
  { day: "Mon", icon: "🌧️", mm: 118, risk: "high", pct: 82 },
  { day: "Tue", icon: "⛈️", mm: 78, risk: "med", pct: 61 },
  { day: "Wed", icon: "🌧️", mm: 95, risk: "high", pct: 74 },
  { day: "Thu", icon: "⛈️", mm: 42, risk: "low", pct: 35 },
  { day: "Fri", icon: "⛈️", mm: 18, risk: "low", pct: 20 },
  { day: "Sat", icon: "⛈️", mm: 55, risk: "med", pct: 48 }
];

document.addEventListener("DOMContentLoaded", () => {
  console.log("Early Shield: Initializing...");

  const initializers = [
    initNavbar, initTicker, initHeroMap, initMainMap, initAlerts,
    initSensors, initCharts, initWeather, initFieldReport,
    initResponseTimeline, initSOSButton, initMobileMenu,
    initScrollAnimations, initOfflineDetection, initLangModal, initTabs
  ];

  initializers.forEach(fn => {
    try {
      fn();
    } catch (e) {
      console.error(`Error initializing ${fn.name}:`, e);
    }
  });

  setTimeout(() => {
    document.querySelectorAll(".risk-meter-fill[data-width]").forEach(el => {
      el.style.width = el.dataset.width + "%";
    });
  }, 600);

  setInterval(updateSensorData, 8000);
  setInterval(cycleAlertCount, 30000);
});

function initNavbar() {
  const navbar = document.getElementById("navbar");
  const links = document.querySelectorAll(".nav-link");
  if (!navbar || !links.length) return;

  window.addEventListener("scroll", () => {
    navbar.classList.toggle("scrolled", window.scrollY > 20);
    const sections = document.querySelectorAll("section[id]");
    let current = "";
    sections.forEach(s => {
      if (window.scrollY >= s.offsetTop - 120) current = s.id;
    });
    links.forEach(l => l.classList.toggle("active", l.getAttribute("href") === "#" + current));
  });

  links.forEach(link => {
    link.addEventListener("click", (e) => {
      const href = link.getAttribute("href");
      if (href && href.startsWith("#")) {
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) target.scrollIntoView({ behavior: "smooth", block: "start" });
        document.querySelector(".mobile-menu")?.classList.remove("open");
      }
    });
  });
}

function initMobileMenu() {
  const hamburger = document.querySelector(".nav-hamburger");
  const menu = document.querySelector(".mobile-menu");
  if (!hamburger || !menu) return;
  hamburger.addEventListener("click", () => menu.classList.toggle("open"));
  menu.querySelectorAll(".mobile-nav-link").forEach(link => link.addEventListener("click", () => menu.classList.remove("open")));
}

function initTicker() {
  const messages = [
    { color: "#e74c3c", text: "CRITICAL: Tawang District - 89% landslide probability in 6 hrs. Evacuate NH-13 villages immediately." },
    { color: "#f39c12", text: "HIGH ALERT: Cherrapunji - Slope instability detected. 3.2 degree tilt. Field teams deployed." },
    { color: "#f39c12", text: "HIGH: Papum Pare - Soil saturation at 94%. Flash flood and landslide risk elevated." },
    { color: "#3498db", text: "SENSOR UPDATE: 847 IoT nodes active across NER. Real-time slope monitoring operational." },
    { color: "#27ae60", text: "SYSTEM OK: AI model updated with latest satellite data. Prediction accuracy: 85.3%" },
    { color: "#e74c3c", text: "ALERT: Tamenglong district debris flow risk elevated to HIGH. NDRF team on standby." },
    { color: "#3498db", text: "UPDATE: 28 medium-risk zones under continuous monitoring. Last satellite scan: 15 min ago." }
  ];
  const doubled = [...messages, ...messages];
  const track = document.querySelector(".ticker-content");
  if (!track) return;
  track.innerHTML = doubled.map(m => `<span class="ticker-item"><span class="ticker-dot" style="background:${m.color}"></span>${m.text}</span>`).join("");
}

function gisStreetTiles() {
  return L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", { attribution: "&copy; OpenStreetMap contributors", maxZoom: 19 });
}

function gisSatelliteTiles() {
  return L.tileLayer("https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}", { attribution: "Tiles &copy; Esri &mdash; World Imagery", maxZoom: 19 });
}

function embedFallback(el, satellite) {
  const bbox = "88.0,22.0,97.5,29.5";
  const layer = satellite ? "cyclosm" : "mapnik";
  el.innerHTML = '<iframe class="map-fallback" title="NER GIS Map" loading="lazy" src="https://www.openstreetmap.org/export/embed.html?bbox=' + bbox + '&amp;layer=' + layer + '"></iframe>';
}

function keepMapSized(map, el) {
  const refresh = () => map.invalidateSize();
  setTimeout(refresh, 200);
  setTimeout(refresh, 800);
  window.addEventListener("resize", refresh);
  if ("IntersectionObserver" in window) {
    new IntersectionObserver(entries => {
      if (entries.some(e => e.isIntersecting)) refresh();
    }, { threshold: 0.05 }).observe(el);
  }
}

function initHeroMap() {
  const el = document.getElementById("hero-map");
  if (!el) return;
  if (typeof L === "undefined") {
    embedFallback(el, true);
    return;
  }
  try {
    const map = L.map("hero-map", { center: [26.2, 93.7], zoom: 6, zoomControl: false, attributionControl: false, dragging: true, scrollWheelZoom: false });
    AppState.maps.hero = map;
    gisSatelliteTiles().addTo(map);
    NER_LOCATIONS.forEach(loc => addRiskMarker(map, loc, false));
    keepMapSized(map, el);
  } catch (e) {
    console.error("Hero Map Init Error:", e);
    embedFallback(el, true);
  }
}

function initMainMap() {
  const el = document.getElementById("main-map");
  if (!el) return;

  // 1. Setup Buttons (independent of Leaflet)
  document.querySelectorAll("#map-section .view-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll("#map-section .view-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      const next = btn.dataset.view;
      const currentMap = AppState.maps.main;
      if (currentMap && AppState.layers && AppState.layers[AppState.currentBase]) {
        currentMap.removeLayer(AppState.layers[AppState.currentBase]);
      }
      if (currentMap && AppState.layers && (AppState.layers[next] || AppState.layers.map)) {
        (AppState.layers[next] || AppState.layers.map).addTo(currentMap);
      }
      AppState.currentBase = next;
      if (currentMap) currentMap.invalidateSize();
    });
  });

  document.querySelectorAll("#map-section .map-controls .map-filter-btn").forEach(btn => {
    btn.addEventListener("click", function() {
      document.querySelectorAll("#map-section .map-controls .map-filter-btn").forEach(b => b.classList.remove("active"));
      this.classList.add("active");
      applyMapFilter(this.dataset.filter);
      showToast("info", "Map Filter", "Showing: " + this.textContent, 2500);
    });
  });

  // 2. Leaflet Init
  if (typeof L === "undefined") {
    embedFallback(el, false);
    return;
  }

  try {
    const map = L.map("main-map", { center: [26.2, 93.7], zoom: 6, zoomControl: true, scrollWheelZoom: true });
    AppState.maps.main = map;
    const layers = { map: gisStreetTiles(), satellite: gisSatelliteTiles() };
    layers.map.addTo(map);
    AppState.layers = layers;
    AppState.currentBase = "map";
    AppState.mapOverlays = { markers: L.layerGroup(), heat: L.layerGroup(), sensors: L.layerGroup(), roads: L.layerGroup(), villages: L.layerGroup() };
    Object.values(AppState.mapOverlays).forEach(g => g.addTo(map));

    NER_LOCATIONS.forEach(loc => {
      const marker = addRiskMarker(map, loc, true, AppState.mapOverlays.markers);
      if (marker) marker._risk = loc.risk;
      L.circle([loc.lat, loc.lng], { color: RISK_COLORS[loc.risk], fillColor: RISK_COLORS[loc.risk], fillOpacity: 0.12, weight: 1, radius: loc.probability * 900 }).addTo(AppState.mapOverlays.heat);
    });

    const sensorCoords = [ { lat: 27.586, lng: 91.865 }, { lat: 25.288, lng: 91.701 }, { lat: 24.97, lng: 93.5 }, { lat: 25.168, lng: 93.015 }, { lat: 25.674, lng: 94.11 }, { lat: 22.886, lng: 92.735 } ];
    SENSOR_NODES.forEach((s, i) => {
      const c = sensorCoords[i];
      if (!c) return;
      const icon = L.divIcon({ html: '<div style="width:12px;height:12px;background:#2563eb;border:2px solid #fff;border-radius:2px;box-shadow:0 0 6px #2563eb"></div>', className: "", iconSize: [12, 12], iconAnchor: [6, 6] });
      L.marker([c.lat, c.lng], { icon }).bindPopup("<strong>" + s.name + "</strong><br/>" + s.id + " · " + s.status).addTo(AppState.mapOverlays.sensors);
    });

    const highways = [ { name: "NH-13 Tawang corridor", pts: [ [27.586, 91.865], [27.35, 92.4], [27.083, 93.611] ] }, { name: "NH-44 Senapati–Imphal", pts: [ [25.266, 94.033], [24.817, 93.936] ] }, { name: "NH-6 Khasi Hills", pts: [ [25.288, 91.701], [25.57, 91.88], [25.7, 91.9] ] } ];
    highways.forEach(h => {
      L.polyline(h.pts, { color: "#0f172a", weight: 3, opacity: 0.7, dashArray: "8 6" }).bindPopup(h.name).addTo(AppState.mapOverlays.roads);
    });

    NER_LOCATIONS.forEach(loc => {
      const icon = L.divIcon({ html: '<div style="font-size:11px;background:#fff;border:1px solid #cbd5e1;border-radius:4px;padding:1px 5px;white-space:nowrap;box-shadow:0 1px 3px rgba(0,0,0,.15)">' + loc.name.split(",")[0] + "</div>", className: "", iconSize: [80, 18], iconAnchor: [40, -8] });
      L.marker([loc.lat, loc.lng], { icon, interactive: false }).addTo(AppState.mapOverlays.villages);
    });

    const baseMaps = { "Street Map": layers.map, "Satellite": layers.satellite };
    const overlayMaps = { "Risk Zones": AppState.mapOverlays.markers, "Heatmap": AppState.mapOverlays.heat, "Sensors": AppState.mapOverlays.sensors, "Roads": AppState.mapOverlays.roads, "Villages": AppState.mapOverlays.villages };
    L.control.layers(baseMaps, overlayMaps, { collapsed: false }).addTo(map);
    keepMapSized(map, el);
  } catch (e) {
    console.error("Map Init Error:", e);
    embedFallback(el, false);
  }
}

function applyMapFilter(filter) {
  const o = AppState.mapOverlays;
  if (!o || !AppState.maps.main) return;
  const map = AppState.maps.main;
  const show = (g, on) => {
    if (on) {
      if (!map.hasLayer(g)) g.addTo(map);
    } else if (map.hasLayer(g)) {
      map.removeLayer(g);
    }
  };
  show(o.sensors, filter === "all" || filter === "sensors");
  show(o.roads, filter === "all" || filter === "roads");
  show(o.villages, filter === "all" || filter === "villages");
  show(o.markers, filter !== "sensors");
  show(o.heat, filter === "all" || filter === "critical");
  o.markers.eachLayer(m => {
    if (m._icon) m._icon.style.display = (filter === "critical" && m._risk !== "critical") ? "none" : "";
  });
  o.heat.clearLayers();
  NER_LOCATIONS.filter(loc => filter !== "critical" || loc.risk === "critical").forEach(loc => {
    L.circle([loc.lat, loc.lng], { color: RISK_COLORS[loc.risk], fillColor: RISK_COLORS[loc.risk], fillOpacity: 0.12, weight: 1, radius: loc.probability * 900 }).addTo(o.heat);
  });
}

function addRiskMarker(map, loc, interactive, layer) {
  const color = RISK_COLORS[loc.risk];
  const size = loc.risk === "critical" ? 20 : loc.risk === "high" ? 17 : 14;
  const icon = L.divIcon({ html: `<div style="width:${size}px;height:${size}px;background:${color};border-radius:50%;border:3px solid white;box-shadow:0 0 ${loc.risk === "critical" ? 12 : 6}px ${color};"></div>`, className: "", iconSize: [size, size], iconAnchor: [size / 2, size / 2] });
  const marker = L.marker([loc.lat, loc.lng], { icon });
  if (interactive) {
    marker.bindPopup(createPopupContent(loc), { maxWidth: 280 });
    marker.on("click", () => updateSidePanel(loc));
  }
  (layer || map).addLayer(marker);
  return marker;
}

function createPopupContent(loc) {
  const riskLabel = { critical: "CRITICAL", high: "HIGH", medium: "MEDIUM", low: "LOW" };
  const color = RISK_COLORS[loc.risk];
  return `<div style="padding:8px;color:#0f172a;"><div style="display:flex;align-items:center;gap:8px;margin-bottom:10px"><div style="width:10px;height:10px;background:${color};border-radius:50%"></div><strong>${loc.name}</strong></div><div style="display:inline-block;padding:3px 10px;background:${color}33;border:1px solid ${color}66;border-radius:12px;font-size:.72rem;font-weight:700;color:${color};margin-bottom:10px">${riskLabel[loc.risk]} RISK</div><table style="width:100%;font-size:.8rem;border-collapse:collapse"><tr><td style="color:#94a3b8;padding:3px 0">AI Probability</td><td style="font-weight:700;text-align:right">${loc.probability}%</td></tr><tr><td style="color:#94a3b8;padding:3px 0">Rainfall</td><td style="font-weight:700;text-align:right">${loc.rainfall} mm/hr</td></tr><tr><td style="color:#94a3b8;padding:3px 0">Soil Moisture</td><td style="font-weight:700;text-align:right">${loc.soilMoisture}%</td></tr><tr><td style="color:#94a3b8;padding:3px 0">Slope</td><td style="font-weight:700;text-align:right">${loc.slope}°</td></tr></table><button onclick="triggerAlert('${loc.name}')" style="width:100%;margin-top:10px;padding:8px;background:#e74c3c;color:white;border:none;border-radius:6px;cursor:pointer;font-weight:600;font-size:.82rem">🚨 Send Alert</button></div>`;
}

function updateSidePanel(loc) {
  const panel = document.getElementById("map-side-panel");
  if (!panel) return;
  const color = RISK_COLORS[loc.risk];
  panel.innerHTML = `<h4 style="margin-bottom:12px;display:flex;align-items:center;gap:8px"><div style="width:10px;height:10px;background:${color};border-radius:50%"></div>${loc.name}</h4><div style="display:grid;gap:8px">${[ ["AI Probability", loc.probability + "%", color], ["Rainfall", loc.rainfall + " mm/hr", "#3498db"], ["Soil Moisture", loc.soilMoisture + "%", "#9b59b6"], ["Slope Angle", loc.slope + "°", "#f39c12"] ].map(([k, v, c]) => `<div style="display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid #e2e8f0"><span style="font-size:.82rem;color:#475569">${k}</span><span style="font-weight:700;color:${c}">${v}</span></div>`).join("")}</div><div style="margin-top:16px"><div style="display:flex;justify-content:space-between;font-size:.8rem;margin-bottom:4px"><span>Risk Level</span><span style="color:${color};font-weight:700">${loc.probability}%</span></div><div style="height:6px;background:var(--border);border-radius:3px;overflow:hidden"><div style="width:${loc.probability}%;height:100%;background:${color};border-radius:3px;transition:width 1s ease"></div></div></div><div style="margin-top:16px;display:flex;gap:8px"><button onclick="triggerAlert('${loc.name}')" class="btn btn-danger btn-sm" style="flex:1">🚨 Alert</button><button onclick="showToast('info','[WATCH] Watchlist','Location added to watchlist',3000)" class="btn btn-outline btn-sm" style="flex:1">[WATCH] Watch</button></div>`;
}

function initAlerts() {
  const container = document.getElementById("alert-list");
  if (!container) return;
  container.innerHTML = ALERT_DATA.map((a, i) => createAlertCard(a, i)).join("");
  document.querySelectorAll(".alert-filter-btn").forEach(btn => {
    btn.addEventListener("click", function() {
      document.querySelectorAll(".alert-filter-btn").forEach(b => b.classList.remove("active"));
      this.classList.add("active");
      const filter = this.dataset.filter;
      container.querySelectorAll(".alert-card").forEach(card => {
        card.style.display = (filter === "all" || card.dataset.level === filter) ? "flex" : "none";
      });
    });
  });
}

function createAlertCard(a, index) {
  const bc = { critical: "badge-danger", high: "badge-warning", medium: "badge-info", low: "badge-success" };
  const rc = { critical: "critical", high: "high", medium: "medium", low: "low" };
  return `<div class="alert-card ${rc[a.level]}" data-level="${a.level}" style="animation-delay:${index * .1}s"><div class="alert-icon">${a.icon}</div><div class="alert-body"><div class="alert-title">${a.title}<span class="badge ${bc[a.level]}">${a.level.toUpperCase()}</span><span class="badge badge-primary">${a.type}</span></div><p style="font-size:.88rem;margin:6px 0 0">${a.description}</p><div class="alert-meta"><span>📍 ${a.location}</span><span> ${a.time}</span><span> ${a.affected}</span></div></div><div class="alert-actions"><button class="btn btn-danger btn-sm" onclick="acknowledgeAlert(this,'${a.district}')">🚨 Alert District</button><button class="btn btn-outline btn-sm" onclick="showToast('info','ℹ️ Details','Opening full incident report...',3000)">View Details</button></div></div>`;
}

window.acknowledgeAlert = function(btn, district) {
  btn.textContent = "✅ Sent";
  btn.disabled = true;
  btn.classList.remove("btn-danger");
  btn.classList.add("btn-success");
  showToast("success", "✅ Alert Dispatched", "Emergency alert sent to " + district + " district administration, NDRF, and local police.", 5000);
};

window.triggerAlert = function(name) {
  showToast("danger", "🚨 Alert Triggered", "Emergency broadcast initiated for " + name + ". SMS + App notifications sent.", 6000);
};

function initSensors() {
  const container = document.getElementById("sensor-grid");
  if (!container) return;
  container.innerHTML = SENSOR_NODES.map(createSensorCard).join("");
  setTimeout(() => {
    SENSOR_NODES.forEach(s => initSensorMiniChart(s.id));
  }, 300);
}

function createSensorCard(s) {
  const sc = { online: "#27ae60", offline: "#e74c3c", warning: "#f39c12" };
  const mc = s.moisture > 85 ? "#e74c3c" : s.moisture > 70 ? "#f39c12" : "#27ae60";
  return `<div class="card" id="sensor-${s.id}"><div class="sensor-header"><div><div style="font-weight:700;font-size:.95rem">${s.name}</div><div class="sensor-location">📍 ${s.district}</div></div><div class="sensor-status"><div class="status-dot ${s.status}"></div><span style="text-transform:uppercase;font-size:.72rem;font-weight:600;color:${sc[s.status]}">${s.status}</span></div></div><div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:8px"><div><div class="sensor-unit">Soil Moisture</div><div style="font-size:1.6rem;font-weight:800;color:${mc}" id="moisture-${s.id}">${s.moisture}%</div><div class="gauge-bar"><div class="gauge-fill" style="width:${s.moisture}%;background:${mc}"></div></div></div><div><div class="sensor-unit">Rainfall</div><div style="font-size:1.6rem;font-weight:800;color:#3498db" id="rain-${s.id}">${s.rainfall} mm</div><div class="gauge-bar"><div class="gauge-fill" style="width:${Math.min(s.rainfall / 2, 100)}%;background:#3498db"></div></div></div></div><div style="margin-top:12px;display:flex;justify-content:space-between;font-size:.78rem;color:var(--text-muted)"><span>Tilt: <strong style="color:var(--text-primary)">${s.inclination}°</strong></span><span>Battery: <strong style="color:${s.battery < 20 ? "#e74c3c" : "var(--text-primary)"}">${s.battery}%</strong></span><span>ID: ${s.id}</span></div><div class="sensor-chart" style="margin-top:8px"><canvas id="chart-${s.id}"></canvas></div></div>`;
}

function initSensorMiniChart(id) {
  const canvas = document.getElementById("chart-" + id);
  if (!canvas || typeof Chart === "undefined") return;
  const data = Array.from({ length: 20 }, () => Math.random() * 40 + 50);
  const color = id === "SN-001" ? "#e74c3c" : "#3498db";
  AppState.charts["sensor-" + id] = new Chart(canvas, {
    type: "line",
    data: { labels: data.map((_, i) => i), datasets: [{ data, borderColor: color, backgroundColor: color + "22", borderWidth: 1.5, fill: true, tension: 0.4, pointRadius: 0 }] },
    options: { responsive: true, maintainAspectRatio: false, animation: false, plugins: { legend: { display: false }, tooltip: { enabled: false } }, scales: { x: { display: false }, y: { display: false } } }
  });
}

function updateSensorData() {
  SENSOR_NODES.forEach(s => {
    if (s.status === "offline") return;
    const delta = (Math.random() - .45) * 3;
    s.moisture = Math.max(20, Math.min(99, s.moisture + delta));
    s.rainfall = Math.max(0, s.rainfall + (Math.random() - .4) * 8);
    const el = document.getElementById("moisture-" + s.id);
    const rain = document.getElementById("rain-" + s.id);
    if (el) el.textContent = s.moisture.toFixed(0) + "%";
    if (rain) rain.textContent = s.rainfall.toFixed(0) + " mm";
    const chart = AppState.charts["sensor-" + s.id];
    if (chart) {
      chart.data.datasets[0].data.push(s.moisture);
      chart.data.datasets[0].data.shift();
      chart.update("none");
    }
  });
}

function initCharts() {
  initRiskTrendChart();
  initRainfallChart();
  initMLPredictionChart();
  initZoneDistributionChart();
}

function chartDefaults() {
  return { responsive: true, maintainAspectRatio: false, plugins: { legend: { labels: { color: "#444444", font: { size: 11 } } }, tooltip: { backgroundColor: "#003366", titleColor: "#ffffff", bodyColor: "#d8e8f4", borderColor: "#f47920", borderWidth: 1 } }, scales: { x: { grid: { color: "#efefef" }, ticks: { color: "#777777", font: { size: 10 } } }, y: { grid: { color: "#efefef" }, ticks: { color: "#777777", font: { size: 10 } } } } };
}

function initRiskTrendChart() {
  const canvas = document.getElementById("risk-trend-chart");
  if (!canvas || typeof Chart === "undefined") return;
  AppState.charts.riskTrend = new Chart(canvas, {
    type: "line",
    data: { labels: ["Aug 23", "Aug 24", "Aug 25", "Aug 26", "Aug 27", "Aug 28", "Today"], datasets: [{ label: "Critical Zones", data: [2, 3, 2, 4, 3, 5, 6], borderColor: "#e74c3c", backgroundColor: "#e74c3c22", fill: true, tension: 0.4, borderWidth: 2 }, { label: "High Risk Zones", data: [5, 6, 7, 6, 8, 9, 8], borderColor: "#f39c12", backgroundColor: "#f39c1222", fill: true, tension: 0.4, borderWidth: 2 }, { label: "Medium Risk", data: [12, 14, 13, 15, 16, 14, 15], borderColor: "#3498db", backgroundColor: "#3498db22", fill: true, tension: 0.4, borderWidth: 2 }] },
    options: chartDefaults()
  });
}

function initRainfallChart() {
  const canvas = document.getElementById("rainfall-chart");
  if (!canvas || typeof Chart === "undefined") return;
  AppState.charts.rainfall = new Chart(canvas, {
    type: "bar",
    data: { labels: ["Tawang", "Cherrapunji", "Papum Pare", "Tamenglong", "Senapati", "Haflong", "Kohima"], datasets: [{ label: "Rainfall (mm/hr)", data: [142, 187, 135, 128, 112, 89, 68], backgroundColor: "#3498dbcc", borderRadius: 4 }, { label: "Critical Threshold", data: [100, 100, 100, 100, 100, 100, 100], type: "line", borderColor: "#e74c3c", borderDash: [5, 5], pointRadius: 0, borderWidth: 2, fill: false }] },
    options: chartDefaults()
  });
}

function initMLPredictionChart() {
  const canvas = document.getElementById("ml-chart");
  if (!canvas || typeof Chart === "undefined") return;
  AppState.charts.ml = new Chart(canvas, {
    type: "radar",
    data: { labels: ["Rainfall", "Soil Moisture", "Slope", "Vegetation Loss", "Historical Risk", "Seismic Activity"], datasets: [{ label: "Tawang (89%)", data: [95, 94, 72, 78, 85, 45], borderColor: "#e74c3c", backgroundColor: "#e74c3c22", borderWidth: 2, pointBackgroundColor: "#e74c3c" }, { label: "Cherrapunji (76%)", data: [90, 88, 45, 65, 72, 30], borderColor: "#f39c12", backgroundColor: "#f39c1222", borderWidth: 2, pointBackgroundColor: "#f39c12" }, { label: "Haflong (47%)", data: [65, 68, 38, 42, 55, 20], borderColor: "#3498db", backgroundColor: "#3498db22", borderWidth: 2, pointBackgroundColor: "#3498db" }] },
    options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { labels: { color: "#444444", font: { size: 11 } } } }, scales: { r: { grid: { color: "#2a4560" }, angleLines: { color: "#2a4560" }, pointLabels: { color: "#444444", font: { size: 11 } }, ticks: { color: "#94a3b8", backdropColor: "#ffffff" }, min: 0, max: 100 } } }
  });
}

function initZoneDistributionChart() {
  const canvas = document.getElementById("zone-chart");
  if (!canvas || typeof Chart === "undefined") return;
  AppState.charts.zone = new Chart(canvas, {
    type: "doughnut",
    data: { labels: ["Critical", "High", "Medium", "Low", "Safe"], datasets: [{ data: [6, 14, 28, 38, 76], backgroundColor: ["#c0392b", "#f47920", "#d4ac0d", "#1a7a3e", "#145e30"], borderWidth: 0, hoverOffset: 8 }] },
    options: { responsive: true, maintainAspectRatio: false, cutout: "70%", plugins: { legend: { position: "right", labels: { color: "#444444", font: { size: 11 }, padding: 12 } }, tooltip: { callbacks: { label: (c) => ` ${c.label}: ${c.raw} zones` } } } }
  });
}

function initWeather() {
  const forecastEl = document.getElementById("forecast-list");
  if (!forecastEl) return;
  forecastEl.innerHTML = WEATHER_FORECAST.map(f => `<div class="forecast-row"><span class="forecast-day">${f.day}</span><span class="forecast-icon">${f.icon}</span><div class="forecast-bar"><div class="forecast-bar-fill" style="width:${f.pct}%"></div></div><span class="forecast-mm">${f.mm}mm</span><span class="forecast-risk risk-${f.risk}">${f.risk.toUpperCase()}</span></div>`).join("");
  animateCounter("current-rainfall", 142, " mm/hr", 1500);
  animateCounter("current-humidity", 94, "%", 1200);
}

function animateCounter(id, target, suffix, duration) {
  const el = document.getElementById(id);
  if (!el) return;
  let start = 0;
  const step = target / (duration / 16);
  const timer = setInterval(() => {
    start = Math.min(start + step, target);
    el.textContent = Math.round(start) + suffix;
    if (start >= target) clearInterval(timer);
  }, 16);
}

function initFieldReport() {
  const geoBtn = document.getElementById("get-location-btn");
  const geoDisplay = document.getElementById("geo-display");
  if (geoBtn) {
    geoBtn.addEventListener("click", () => {
      if (navigator.geolocation) {
        geoBtn.textContent = " Getting...";
        geoBtn.disabled = true;
        navigator.geolocation.getCurrentPosition(pos => {
          const { latitude, longitude } = pos.coords;
          const li = document.getElementById("lat-input");
          const ln = document.getElementById("lng-input");
          if (li) li.value = latitude.toFixed(6);
          if (ln) ln.value = longitude.toFixed(6);
          if (geoDisplay) {
            geoDisplay.style.display = "flex";
            const gc = geoDisplay.querySelector(".geo-coords");
            if (gc) gc.textContent = latitude.toFixed(4) + "°N, " + longitude.toFixed(4) + "°E";
          }
          geoBtn.textContent = "✅ Location Set";
          showToast("success", "📍 Location Captured", "GPS coordinates attached.", 3000);
        }, () => {
          const li = document.getElementById("lat-input");
          const ln = document.getElementById("lng-input");
          if (li) li.value = "25.5709";
          if (ln) ln.value = "91.8817";
          if (geoDisplay) {
            geoDisplay.style.display = "flex";
            const gc = geoDisplay.querySelector(".geo-coords");
            if (gc) gc.textContent = "25.5709°N, 91.8817°E (demo)";
          }
          geoBtn.textContent = "✅ Demo Location";
          showToast("warning", "⚠️ GPS Unavailable", "Using demo location.", 4000);
        }, { timeout: 5000 });
      }
    });
  }
}

function handleFileUpload(files) {
  if (!files || !files.length) return;
  const names = Array.from(files).map(f => f.name).join(", ");
  showToast("success", "📁 Files Selected", files.length + " file(s): " + names, 3000);
  const uz = document.getElementById("upload-zone");
  if (uz) uz.innerHTML = `<div class="upload-icon">✅</div><p style="color:#27ae60;font-weight:700">${files.length} file(s) ready</p><p style="font-size:.8rem;color:var(--text-muted)">${names}</p>`;
}

function initResponseTimeline() {
  document.querySelectorAll(".timeline-item").forEach((item, i) => {
    item.style.opacity = "0";
    setTimeout(() => {
      item.style.transition = "opacity 0.5s ease";
      item.style.opacity = "1";
    }, i * 200);
  });
}

function showToast(type, title, msg, duration = 5000) {
  const container = document.getElementById("toast-container");
  if (!container) return;
  const icons = { danger: "🚨", warning: "⚠️", success: "✅", info: "ℹ️" };
  const toast = document.createElement("div");
  toast.className = "toast " + type;
  toast.innerHTML = `<span class="toast-icon">${icons[type] || "ℹ️"}</span><div class="toast-body"><div class="title">${title}</div><div class="msg">${msg}</div></div><button class="toast-close" onclick="this.parentElement.remove()"></button>`;
  container.appendChild(toast);
  setTimeout(() => toast.remove(), duration + 500);
}

window.showToast = showToast;

function initSOSButton() {
  const btn = document.querySelector(".sos-btn");
  if (!btn) return;
  btn.addEventListener("click", () => {
    if (confirm("🚨 SEND SOS ALERT?\\n\\nThis will immediately notify:\\n• NDRF Control Room\\n• District Disaster Management\\n• State Emergency Operations\\n• Local Police\\n\\nProceed?")) {
      showToast("danger", "🚨 SOS DISPATCHED", "Emergency alert sent to all agencies. Help is on the way!", 10000);
      btn.textContent = "✅ SENT";
      btn.style.background = "#27ae60";
      setTimeout(() => {
        btn.textContent = "SOS";
        btn.style.background = "";
      }, 15000);
    }
  });
}

function initOfflineDetection() {
  const banner = document.querySelector(".offline-banner");
  window.addEventListener("offline", () => {
    AppState.isOffline = true;
    if (banner) banner.style.display = "block";
    showToast("warning", "📡 Offline Mode", "Network unavailable. Data cached locally.", 10000);
  });
  window.addEventListener("online", () => {
    AppState.isOffline = false;
    if (banner) banner.style.display = "none";
    showToast("success", "📡 Reconnected", "Connection restored. Syncing data...", 5000);
  });
}

function initScrollAnimations() {
  const mapObserver = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        try {
          if (AppState.maps && AppState.maps.main) AppState.maps.main.invalidateSize();
        } catch (e) {}
        if (AppState.maps.hero) AppState.maps.hero.invalidateSize();
      }
    });
  }, { threshold: 0.1 });
  const mapSection = document.getElementById("map-section");
  if (mapSection) mapObserver.observe(mapSection);
  const heroSection = document.getElementById("hero");
  if (heroSection) mapObserver.observe(heroSection);

  const observer = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add("visible");
        observer.unobserve(e.target);
      }
    });
  }, { threshold: 0.1 });
  document.querySelectorAll(".fade-in").forEach(el => observer.observe(el));

  const statObs = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.querySelectorAll("[data-count]").forEach(el => animateCounterEl(el, parseInt(el.dataset.count), 1500));
        statObs.unobserve(e.target);
      }
    });
  }, { threshold: 0.5 });
  document.querySelectorAll(".hero-stats").forEach(el => statObs.observe(el));
}

function animateCounterEl(el, target, duration) {
  let start = 0;
  const suffix = el.dataset.suffix || "";
  const step = target / (duration / 16);
  const timer = setInterval(() => {
    start = Math.min(start + step, target);
    el.textContent = Math.round(start) + suffix;
    if (start >= target) clearInterval(timer);
  }, 16);
}

function initLangModal() {
  const overlay = document.getElementById("lang-modal");
  document.querySelectorAll("[data-lang-open]").forEach(btn => btn.addEventListener("click", () => overlay?.classList.add("active")));
  document.querySelectorAll("[data-lang-close]").forEach(btn => btn.addEventListener("click", () => overlay?.classList.remove("active")));
  overlay?.addEventListener("click", e => {
    if (e.target === overlay) overlay.classList.remove("active");
  });
  document.querySelectorAll(".lang-btn").forEach(btn => {
    btn.addEventListener("click", function() {
      document.querySelectorAll(".lang-btn").forEach(b => b.classList.remove("selected"));
      this.classList.add("selected");
    });
  });
  document.getElementById("apply-lang")?.addEventListener("click", () => {
    const selected = document.querySelector(".lang-btn.selected");
    if (selected) {
      applyLanguage(selected.dataset.lang);
      overlay?.classList.remove("active");
      showToast("success", "[LANG] Language Changed", "Interface updated.", 3000);
    }
  });
}

function applyLanguage(lang) {
  AppState.currentLang = lang;
  const t = TRANSLATIONS[lang] || TRANSLATIONS.en;
  document.querySelectorAll("[data-i18n]").forEach(el => {
    const key = el.dataset.i18n;
    if (t[key]) el.textContent = t[key];
  });
}

function initTabs() {
  document.querySelectorAll(".tabs").forEach(tabGroup => {
    tabGroup.querySelectorAll(".tab-btn").forEach(btn => {
      btn.addEventListener("click", function() {
        const parent = this.closest(".tab-section") || document;
        const targetId = this.dataset.tab;
        tabGroup.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
        this.classList.add("active");
        parent.querySelectorAll(".tab-content").forEach(c => c.classList.toggle("active", c.id === targetId));
      });
    });
  });
}

function cycleAlertCount() {
  const el = document.getElementById("alert-count");
  if (el) {
    AppState.alertCount = Math.floor(Math.random() * 5) + 5;
    el.textContent = AppState.alertCount;
  }
}

setTimeout(() => {
  showToast("danger", "🚨 CRITICAL ALERT", "Tawang District: 89% landslide probability. Immediate action required!", 8000);
}, 2000);
setTimeout(() => {
  showToast("warning", "⚠️ HIGH RISK", "Cherrapunji: Slope instability detected. Field teams deployed.", 7000);
}, 5500);
setTimeout(() => {
  showToast("success", "✅ System Status", "AI Model updated. 12 new high-risk zones mapped via satellite.", 5000);
}, 9000);
