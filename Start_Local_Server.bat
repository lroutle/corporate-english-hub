@echo off
echo Starting Local HTTP Server on port 8088...
start "" "http://localhost:8088/index.html"
python -m http.server 8088
