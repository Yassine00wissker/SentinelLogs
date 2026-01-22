const API_BASE = "http://localhost:8000";

export async function getSummary() {
    const res = await fetch(`${API_BASE}/dashboard/summary`)
    return res.json();
}

export async function getDashboard() {
    const res = await fetch(`${API_BASE}/dashboard`);
    return res.json()
}