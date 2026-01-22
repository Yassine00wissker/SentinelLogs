import SummaryCard from "../components/SummaryCard";
import { getSummary } from "../lib/api";

export default async function Summary() {
  const summary = await getSummary();

  return (
    <div className="p-6 grid grid-cols-1 md:grid-cols-4 gap-4">
      <SummaryCard title="Status" value={summary.status} color="green" />
      <SummaryCard title="Total Logs" value={summary.total_logs} color="blue" />
      <SummaryCard title="Error Rate" value={(summary.error_rate * 100).toFixed(1) + "%"} color="red" />
      <SummaryCard title="Anomalies" value={summary.anomalies_detected} color="yellow" />
    </div>

  );
}
