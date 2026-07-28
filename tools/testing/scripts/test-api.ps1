param(
  [string]$BaseUrl = "http://localhost:8000",
  [string]$VideoPath = ""
)

Write-Host "Checking API health at $BaseUrl/health"
$health = Invoke-RestMethod -Uri "$BaseUrl/health" -Method Get
$health | ConvertTo-Json

if ($VideoPath -eq "") {
  Write-Host "Skipping video upload because -VideoPath was not provided."
  Write-Host "Example: .\test-api.ps1 -VideoPath C:\path\to\classroom-video.mp4"
  exit 0
}

if (!(Test-Path $VideoPath)) {
  throw "Video file not found: $VideoPath"
}

$Form = @{
  department = "Computer Science"
  year = "3"
  section = "A"
  subject = "Artificial Intelligence"
  video = Get-Item $VideoPath
}

Write-Host "Uploading attendance preview video: $VideoPath"
$response = Invoke-RestMethod -Uri "$BaseUrl/api/v1/attendance/preview" -Method Post -Form $Form
$response | ConvertTo-Json -Depth 10
