param([int]$Workers = 3, [int]$Dpi = 180, [switch]$Force)
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path $PSScriptRoot -Parent
$pythonPath = Join-Path $projectRoot '.venv-pdf/Scripts/python.exe'
if (-not (Test-Path -LiteralPath $pythonPath)) {
    python -m venv (Join-Path $projectRoot '.venv-pdf')
    if ($LASTEXITCODE -ne 0) { throw 'Falha ao criar ambiente Python' }
}
& $pythonPath -m pip install -r (Join-Path $PSScriptRoot 'requirements-pdf.txt')
if ($LASTEXITCODE -ne 0) { throw 'Falha ao instalar dependências' }
$pipelineArgs = @((Join-Path $PSScriptRoot 'pdf_to_markdown.py'), '--workers', $Workers, '--dpi', $Dpi)
if ($Force) { $pipelineArgs += '--force' }
& $pythonPath @pipelineArgs
if ($LASTEXITCODE -ne 0) { throw 'Conversão incompleta: consulte output/pdf/report.json' }
& $pythonPath (Join-Path $PSScriptRoot 'validate_pdf_markdown.py')
if ($LASTEXITCODE -ne 0) { throw 'Falha na validação: consulte output/pdf/validation.json' }
