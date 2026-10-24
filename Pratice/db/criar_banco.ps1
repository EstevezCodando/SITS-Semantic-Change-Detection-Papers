# Cria o banco mudanca_mascara no PostgreSQL 18 local e carrega mascara_cobertura.sql.
# O psql pede a senha do usuário postgres no próprio terminal (duas vezes).
param(
    [string]$Banco = 'mudanca_mascara',
    [int]$Porta = 5432,
    [string]$Usuario = 'postgres'
)
$psql = 'C:\Program Files\PostgreSQL\18\bin\psql.exe'
$sql  = Join-Path $PSScriptRoot 'mascara_cobertura.sql'

& $psql -h localhost -p $Porta -U $Usuario -d postgres -v ON_ERROR_STOP=1 -c "CREATE DATABASE $Banco"
if ($LASTEXITCODE -ne 0) { Write-Error 'Falha ao criar o banco (já existe?)'; exit 1 }

& $psql -h localhost -p $Porta -U $Usuario -d $Banco -v ON_ERROR_STOP=1 -q -f $sql
if ($LASTEXITCODE -ne 0) { Write-Error 'Falha ao carregar o SQL; nada foi gravado no esquema'; exit 1 }

& $psql -h localhost -p $Porta -U $Usuario -d $Banco -c "SELECT fonte, count(*) AS imagens FROM mascara.imagem GROUP BY fonte ORDER BY 1"
