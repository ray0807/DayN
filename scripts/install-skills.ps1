param(
    [string]$Destination,
    [string[]]$Names,
    [switch]$Overwrite
)
$ErrorActionPreference = 'Stop'
$sourceRoot = [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../skills'))
if (-not $Destination) {
    $codexBase = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path ([Environment]::GetFolderPath('UserProfile')) '.codex' }
    $Destination = Join-Path $codexBase 'skills'
}
$targetRoot = [System.IO.Path]::GetFullPath($Destination)
$folders = @(Get-ChildItem -LiteralPath $sourceRoot -Directory | Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName 'SKILL.md') })
if ($Names) {
    foreach ($name in $Names) {
        if ($name -notmatch '^[a-z0-9]+(-[a-z0-9]+)*$' -or $name -notin $folders.Name) { throw "Unknown skill: $name" }
    }
    $folders = @($folders | Where-Object { $_.Name -in $Names })
}
$plan = @()
foreach ($folder in $folders) {
    $target = [System.IO.Path]::GetFullPath((Join-Path $targetRoot $folder.Name))
    if (-not $target.StartsWith($targetRoot.TrimEnd('\') + '\', [StringComparison]::OrdinalIgnoreCase)) { throw 'Target escapes destination.' }
    foreach ($file in Get-ChildItem -LiteralPath $folder.FullName -Recurse -File) {
        $relative = $file.FullName.Substring($folder.FullName.Length).TrimStart('\')
        $targetFile = Join-Path $target $relative
        if ((Test-Path -LiteralPath $targetFile) -and -not $Overwrite) {
            if ((Get-FileHash -LiteralPath $file.FullName).Hash -ne (Get-FileHash -LiteralPath $targetFile).Hash) {
                throw "Existing file differs: $targetFile. Use -Overwrite only if you intend to update it."
            }
        }
        $plan += [pscustomobject]@{ Source = $file.FullName; Target = $targetFile }
    }
}
foreach ($item in $plan) {
    New-Item -ItemType Directory -Path ([System.IO.Path]::GetDirectoryName($item.Target)) -Force | Out-Null
    Copy-Item -LiteralPath $item.Source -Destination $item.Target -Force
}
Write-Output "Installed $($folders.Count) skills into $targetRoot"
