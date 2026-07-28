const form = document.querySelector('#attendanceForm');
const apiBaseUrl = document.querySelector('#apiBaseUrl');
const apiStatus = document.querySelector('#apiStatus');
const rawResponse = document.querySelector('#rawResponse');
const lastUpdated = document.querySelector('#lastUpdated');
const presentList = document.querySelector('#presentList');
const absentList = document.querySelector('#absentList');
const unknownList = document.querySelector('#unknownList');
const cameraPreview = document.querySelector('#cameraPreview');
const videoFile = document.querySelector('#videoFile');
let stream;

function endpoint(path) {
  return `${apiBaseUrl.value.replace(/\/$/, '')}${path}`;
}

function renderList(node, rows, formatter) {
  node.innerHTML = '';
  if (!rows.length) {
    node.innerHTML = '<li class="muted">None</li>';
    return;
  }
  rows.forEach((row) => {
    const li = document.createElement('li');
    li.textContent = formatter(row);
    node.appendChild(li);
  });
}

function renderPreview(payload) {
  rawResponse.textContent = JSON.stringify(payload, null, 2);
  renderList(presentList, payload.present ?? [], (row) => `${row.name ?? row.student_id ?? 'Student'} · ${(row.confidence * 100).toFixed(1)}% · ${row.face_track_id}`);
  renderList(absentList, payload.absent_student_ids ?? [], (id) => id);
  renderList(unknownList, payload.unknown ?? [], (row) => `${row.status} · ${(row.confidence * 100).toFixed(1)}% · ${row.face_track_id}`);
  lastUpdated.textContent = new Date().toLocaleString();
}

async function checkApi() {
  apiStatus.textContent = 'Checking...';
  apiStatus.className = 'status';
  try {
    const response = await fetch(endpoint('/health'));
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    apiStatus.textContent = 'API online';
    apiStatus.classList.add('ok');
  } catch (error) {
    apiStatus.textContent = `API offline: ${error.message}`;
    apiStatus.classList.add('fail');
  }
}

document.querySelector('#checkApi').addEventListener('click', checkApi);

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  rawResponse.textContent = 'Uploading video...';
  const data = new FormData(form);
  try {
    const response = await fetch(endpoint('/api/v1/attendance/preview'), { method: 'POST', body: data });
    const payload = await response.json();
    if (!response.ok) throw new Error(JSON.stringify(payload));
    renderPreview(payload);
  } catch (error) {
    rawResponse.textContent = `Request failed: ${error.message}`;
  }
});

document.querySelector('#startCamera').addEventListener('click', async () => {
  stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
  cameraPreview.srcObject = stream;
  document.querySelector('#record').disabled = false;
});

document.querySelector('#record').addEventListener('click', () => {
  const recorder = new MediaRecorder(stream, { mimeType: 'video/webm' });
  const chunks = [];
  recorder.ondataavailable = (event) => chunks.push(event.data);
  recorder.onstop = () => {
    const file = new File(chunks, `attendance-${Date.now()}.webm`, { type: 'video/webm' });
    const transfer = new DataTransfer();
    transfer.items.add(file);
    videoFile.files = transfer.files;
  };
  recorder.start();
  setTimeout(() => recorder.stop(), 10000);
});

checkApi();
