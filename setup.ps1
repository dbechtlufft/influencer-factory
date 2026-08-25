# Setup reprodutível do influencer-factory (PowerShell 5.1-safe).
# Clona o MoneyPrinterTurbo pinado, cria o venv, instala deps e baixa os
# materiais de domínio público listados em materials.json.

$ErrorActionPreference = "Stop"
$root = $PSScriptRoot
$mpt = Join-Path $root "MoneyPrinterTurbo"
$mptRepo = "https://github.com/harry0703/MoneyPrinterTurbo"
# Revisão validada no e2e de 2026-08-25; bump consciente, não automático.
$mptPin = "68ce652372e62748c191f7b8a95da66162b3d3bf"

# 1. Vendorar o MPT na revisão pinada
if (-not (Test-Path $mpt)) {
    git clone $mptRepo $mpt
}
git -C $mpt fetch --depth 1 origin $mptPin
git -C $mpt checkout $mptPin

# 2. venv + dependências
$venvPython = Join-Path $root ".venv\Scripts\python.exe"
if (-not (Test-Path $venvPython)) {
    python -m venv (Join-Path $root ".venv")
}
& $venvPython -m pip install --quiet -r (Join-Path $mpt "requirements.txt")

# 3. Materiais (NASA Image and Video Library, domínio público, sem API key)
$ffmpeg = & $venvPython -c "import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())"
$dest = Join-Path $mpt "storage\local_videos"
New-Item -ItemType Directory -Force $dest | Out-Null
$manifest = Get-Content (Join-Path $root "materials.json") -Raw -Encoding UTF8 | ConvertFrom-Json

foreach ($m in $manifest.materials) {
    $out = Join-Path $dest $m.file
    if (Test-Path $out) {
        Write-Output "ja existe: $($m.file)"
        continue
    }
    $asset = Invoke-RestMethod "https://images-api.nasa.gov/asset/$([uri]::EscapeDataString($m.nasa_id))"
    $hrefs = $asset.collection.items.href
    $pick = $null
    foreach ($pattern in @('~medium.mp4', '~small.mp4', '~mobile.mp4')) {
        $pick = $hrefs | Where-Object { $_ -like "*$pattern" } | Select-Object -First 1
        if ($pick) { break }
    }
    if (-not $pick) { throw "sem rendition mp4 para $($m.nasa_id)" }

    $raw = "$out.download"
    Invoke-WebRequest -Uri ($pick -replace ' ', '%20') -OutFile $raw -UserAgent "influencer-factory-setup/0.1"
    if ($m.trim) {
        & $ffmpeg -y -ss $m.trim.start_seconds -i $raw -t $m.trim.duration_seconds -c copy $out -loglevel error
        Remove-Item $raw -Confirm:$false
    } else {
        Move-Item $raw $out
    }
    $mb = [Math]::Round((Get-Item $out).Length / 1MB, 1)
    Write-Output "OK $($m.file) ($mb MB)"
}

Write-Output "setup completo. E2E: .venv\Scripts\python run_e2e.py"
