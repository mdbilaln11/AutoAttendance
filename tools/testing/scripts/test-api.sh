#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${BASE_URL:-http://localhost:8000}"
VIDEO_PATH="${1:-}"

echo "Checking API health at ${BASE_URL}/health"
curl --fail --silent --show-error "${BASE_URL}/health"
echo

if [[ -z "${VIDEO_PATH}" ]]; then
  echo "Skipping video upload because no video path was provided."
  echo "Example: ./test-api.sh /path/to/classroom-video.mp4"
  exit 0
fi

if [[ ! -f "${VIDEO_PATH}" ]]; then
  echo "Video file not found: ${VIDEO_PATH}" >&2
  exit 1
fi

echo "Uploading attendance preview video: ${VIDEO_PATH}"
curl --fail --silent --show-error \
  -X POST "${BASE_URL}/api/v1/attendance/preview" \
  -F "department=Computer Science" \
  -F "year=3" \
  -F "section=A" \
  -F "subject=Artificial Intelligence" \
  -F "video=@${VIDEO_PATH}"
echo
