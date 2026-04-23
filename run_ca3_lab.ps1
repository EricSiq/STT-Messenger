# STT Messenger  Edition Launcher
# Methodology: Architecture-first, Zero-deployment-friction.

Write-Host "--- STT Messenger Secure Lab ---" -ForegroundColor Green
Write-Host "Cleaning environment..." -ForegroundColor Gray

# 1. Kill any existing port 8000 process (Zombie Cleanup)
$portProcess = Get-NetTCPConnection -LocalPort 8000 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess -First 1
if ($portProcess) {
    Write-Host "Stopping existing backend (PID: $portProcess)..." -ForegroundColor Yellow
    Stop-Process -Id $portProcess -Force
    Start-Sleep -Seconds 1
}

# 2. Open the UI immediately
$frontendPath = "file://" + (Get-Item "frontend/index.html").FullName
Write-Host "Launching UI: $frontendPath" -ForegroundColor Cyan
Start-Process $frontendPath

# 3. Start the Backend
Write-Host "Starting Secure Backend..." -ForegroundColor Green
cd backend
python -m uvicorn main:app --host 127.0.0.1 --port 8000
