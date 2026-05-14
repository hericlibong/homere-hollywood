param(
  [int]$Port = 8000
)

$ErrorActionPreference = "Stop"
$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path

$Types = @{
  ".html" = "text/html; charset=utf-8"
  ".css" = "text/css; charset=utf-8"
  ".js" = "text/javascript; charset=utf-8"
  ".json" = "application/json; charset=utf-8"
  ".svg" = "image/svg+xml"
  ".png" = "image/png"
  ".jpg" = "image/jpeg"
  ".jpeg" = "image/jpeg"
  ".webp" = "image/webp"
}

function Get-ResponseBytes([int]$Status, [string]$StatusText, [byte[]]$Body, [string]$ContentType) {
  $header = "HTTP/1.1 $Status $StatusText`r`nContent-Type: $ContentType`r`nContent-Length: $($Body.Length)`r`nCache-Control: no-store`r`nConnection: close`r`n`r`n"
  $headerBytes = [System.Text.Encoding]::ASCII.GetBytes($header)
  $response = New-Object byte[] ($headerBytes.Length + $Body.Length)
  [System.Buffer]::BlockCopy($headerBytes, 0, $response, 0, $headerBytes.Length)
  [System.Buffer]::BlockCopy($Body, 0, $response, $headerBytes.Length, $Body.Length)
  return $response
}

function Send-Response($Stream, [int]$Status, [string]$StatusText, [string]$Text) {
  $body = [System.Text.Encoding]::UTF8.GetBytes($Text)
  $bytes = Get-ResponseBytes $Status $StatusText $body "text/plain; charset=utf-8"
  $Stream.Write($bytes, 0, $bytes.Length)
}

$Listener = [System.Net.Sockets.TcpListener]::new([System.Net.IPAddress]::Loopback, $Port)
$Listener.Start()
Write-Host "Homere Hollywood webapp: http://localhost:$Port/webapp/"

try {
  while ($true) {
    $Client = $Listener.AcceptTcpClient()
    try {
      $Stream = $Client.GetStream()
      $Buffer = New-Object byte[] 8192
      $Read = $Stream.Read($Buffer, 0, $Buffer.Length)
      if ($Read -le 0) {
        $Client.Close()
        continue
      }

      $Request = [System.Text.Encoding]::ASCII.GetString($Buffer, 0, $Read)
      $FirstLine = ($Request -split "`r?`n")[0]
      $Parts = $FirstLine -split " "
      if ($Parts.Length -lt 2 -or $Parts[0] -ne "GET") {
        Send-Response $Stream 405 "Method Not Allowed" "Method not allowed"
        $Client.Close()
        continue
      }

      $RequestPath = [System.Uri]::UnescapeDataString(($Parts[1] -split "\?")[0])
      if ($RequestPath -eq "/") {
        $RequestPath = "/webapp/index.html"
      }

      $Relative = $RequestPath.TrimStart("/") -replace "/", [System.IO.Path]::DirectorySeparatorChar
      $FilePath = [System.IO.Path]::GetFullPath((Join-Path $Root $Relative))

      if (-not $FilePath.StartsWith($Root, [System.StringComparison]::OrdinalIgnoreCase)) {
        Send-Response $Stream 403 "Forbidden" "Forbidden"
        $Client.Close()
        continue
      }

      if ((Test-Path -LiteralPath $FilePath -PathType Container)) {
        $FilePath = Join-Path $FilePath "index.html"
      }

      if (-not (Test-Path -LiteralPath $FilePath -PathType Leaf)) {
        Send-Response $Stream 404 "Not Found" "Not found"
        $Client.Close()
        continue
      }

      $Body = [System.IO.File]::ReadAllBytes($FilePath)
      $Ext = [System.IO.Path]::GetExtension($FilePath).ToLowerInvariant()
      $ContentType = if ($Types.ContainsKey($Ext)) { $Types[$Ext] } else { "application/octet-stream" }
      $Response = Get-ResponseBytes 200 "OK" $Body $ContentType
      $Stream.Write($Response, 0, $Response.Length)
    }
    catch {
      try {
        Send-Response $Stream 500 "Server Error" "Server error"
      }
      catch {}
    }
    finally {
      $Client.Close()
    }
  }
}
finally {
  $Listener.Stop()
}
