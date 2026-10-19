import re

html_path = r"C:\tmp\00-Mycat\Engineering\Automotive_Engineering_Presentation.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Slide 6 (CAD Evolution) to show the image
old_s6_bottom = '<div class="card" style="flex: 1; border-left: 6px solid var(--primary);">'
new_s6_bottom = '''<div style="display: flex; gap: 12px; flex: 1; align-items: stretch;">
          <div style="flex: 1.2; border-radius: 8px; overflow: hidden; border: 1px solid #1E293B; background: #000; display: flex; align-items: center; justify-content: center;">
            <img src="assets/cad_design_evolution.jpg" alt="CAD Design Evolution Across 4 Eras" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
          <div class="card" style="flex: 1; border-left: 6px solid var(--primary);">'''
content = content.replace(old_s6_bottom, new_s6_bottom, 1)

# 2. Update Slide 16 (Master Flowchart) to show the visual flowchart prominently
old_s16_content = '''      <div class="slide-content">
        <div class="grid-6" style="height: 180px;">'''
new_s16_content = '''      <div class="slide-content">
        <div style="width: 100%; height: 280px; border-radius: 8px; overflow: hidden; border: 1px solid var(--primary); background: #050E1D; display: flex; align-items: center; justify-content: center; margin-bottom: 8px;">
          <img src="assets/automotive_flowchart_diagram.jpg" alt="Automotive Vehicle Development Flowchart" style="width: 100%; height: 100%; object-fit: contain;">
        </div>
        <div class="grid-6" style="height: 120px;">'''
content = content.replace(old_s16_content, new_s16_content, 1)

# 3. Update Slide 22 (GD&T Metrology) to show the metrology image
old_s22_card3 = '''          <div class="card">
            <div class="card-stripe" style="background: var(--teal);"></div>
            <div class="card-title">GEOMETRIC CONTROLS IN BIW</div>'''
new_s22_card3 = '''          <div class="card" style="padding: 6px; display: flex; flex-direction: column;">
            <div style="flex: 1; border-radius: 6px; overflow: hidden; border: 1px solid #1E3A8A; margin-bottom: 8px; background: #000;">
              <img src="assets/dimensional_gdt_metrology.jpg" alt="Automotive GD&T Metrology & RPS" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
            <div style="padding: 4px 6px;">
              <div style="font-size: 11px; font-weight: 700; color: var(--teal);">RPS & GD&T LASER METROLOGY</div>
              <div style="font-size: 9.5px; color: #94A3B8;">3-2-1 Datums, CMM optical scanning, and gap/flush tolerances.</div>
            </div>
          </div>
          <div class="card" style="display: none;">
            <div class="card-title">GEOMETRIC CONTROLS IN BIW</div>'''
content = content.replace(old_s22_card3, new_s22_card3, 1)

# 4. Update Slide 25 (Crash & EV Safety) to show the BIW crash safety image
old_s25_card3 = '''          <div class="card">
            <div class="card-stripe" style="background: var(--teal);"></div>
            <div class="card-title">MEB EV BATTERY PROTECTION</div>'''
new_s25_card3 = '''          <div class="card" style="padding: 6px; display: flex; flex-direction: column;">
            <div style="flex: 1; border-radius: 6px; overflow: hidden; border: 1px solid #1E3A8A; margin-bottom: 8px; background: #000;">
              <img src="assets/biw_crash_safety.jpg" alt="BIW Crash Load Paths & EV Battery Protection" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
            <div style="padding: 4px 6px;">
              <div style="font-size: 11px; font-weight: 700; color: var(--primary-light);">BIW CRASH LOAD PATHS & EV BATTERY</div>
              <div style="font-size: 9.5px; color: #94A3B8;">3-tier front load paths, 22MnB5 boron steel, and extruded sills.</div>
            </div>
          </div>
          <div class="card" style="display: none;">
            <div class="card-title">MEB EV BATTERY PROTECTION</div>'''
content = content.replace(old_s25_card3, new_s25_card3, 1)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully injected visual image elements into Automotive_Engineering_Presentation.html")
