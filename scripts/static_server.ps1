param(
    [int]$Port = 8010,
    [string]$Root = (Get-Location).Path
)

$server = [System.Net.Sockets.TcpListener]::new([System.Net.IPAddress]::Parse("127.0.0.1"), $Port)
$server.Start()

$contentTypes = @{
    ".html" = "text/html; charset=utf-8"
    ".css" = "text/css; charset=utf-8"
    ".js" = "application/javascript; charset=utf-8"
    ".json" = "application/json; charset=utf-8"
    ".csv" = "text/csv; charset=utf-8"
    ".png" = "image/png"
    ".jpg" = "image/jpeg"
    ".jpeg" = "image/jpeg"
    ".svg" = "image/svg+xml"
}

function Send-Response($stream, [int]$statusCode, [string]$statusText, [byte[]]$body, [string]$contentType) {
    $header = "HTTP/1.1 $statusCode $statusText`r`nContent-Type: $contentType`r`nContent-Length: $($body.Length)`r`nConnection: close`r`n`r`n"
    $headerBytes = [Text.Encoding]::ASCII.GetBytes($header)
    $stream.Write($headerBytes, 0, $headerBytes.Length)
    if ($body.Length -gt 0) {
        $stream.Write($body, 0, $body.Length)
    }
}

try {
    while ($true) {
        $client = $server.AcceptTcpClient()
        try {
            $stream = $client.GetStream()
            $buffer = New-Object byte[] 4096
            $read = $stream.Read($buffer, 0, $buffer.Length)
            if ($read -le 0) {
                $client.Close()
                continue
            }

            $request = [Text.Encoding]::ASCII.GetString($buffer, 0, $read)
            $firstLine = ($request -split "`r?`n")[0]
            $parts = $firstLine -split " "
            if ($parts.Length -lt 2 -or $parts[0] -ne "GET") {
                Send-Response $stream 405 "Method Not Allowed" ([Text.Encoding]::UTF8.GetBytes("Method not allowed")) "text/plain; charset=utf-8"
                $client.Close()
                continue
            }

            $requestPath = [Uri]::UnescapeDataString(($parts[1] -split "\?")[0].TrimStart("/"))
            if ([string]::IsNullOrWhiteSpace($requestPath)) {
                $requestPath = "webapp/index.html"
            }

        $relativePath = $requestPath -replace "/", [System.IO.Path]::DirectorySeparatorChar
        $fullPath = [System.IO.Path]::GetFullPath([System.IO.Path]::Combine($Root, $relativePath))
        $rootPath = [System.IO.Path]::GetFullPath($Root)

            if (-not $fullPath.StartsWith($rootPath, [StringComparison]::OrdinalIgnoreCase)) {
                Send-Response $stream 403 "Forbidden" ([Text.Encoding]::UTF8.GetBytes("Forbidden")) "text/plain; charset=utf-8"
                $client.Close()
                continue
            }

        if ([System.IO.Directory]::Exists($fullPath)) {
            $fullPath = [System.IO.Path]::Combine($fullPath, "index.html")
        }

        if (-not [System.IO.File]::Exists($fullPath)) {
            Send-Response $stream 404 "Not Found" ([Text.Encoding]::UTF8.GetBytes("Not found")) "text/plain; charset=utf-8"
            $client.Close()
            continue
        }

        $extension = [System.IO.Path]::GetExtension($fullPath).ToLowerInvariant()
            $contentType = $contentTypes[$extension]
            if (-not $contentType) {
                $contentType = "application/octet-stream"
            }

        Send-Response $stream 200 "OK" ([System.IO.File]::ReadAllBytes($fullPath)) $contentType
        }
        finally {
            $client.Close()
        }
    }
}
finally {
    $server.Stop()
}
