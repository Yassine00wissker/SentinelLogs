import Summary from "./components/Summary";
import LogsChart from "./components/LogsChart";
import AnomaliesTable from "./components/AnomaliesTable";
import { getDashboard } from "./lib/api";



export default async function Home() {

  const data = await getDashboard()
  const metrics = data.metrics;
  const anomalies = data.anomalies;

  const chartData = Object.entries(metrics.logs_per_minute).map(
  ([time, count]) => ({ time, count })
);
  return (
    <div className="space-y-6">
      <Summary />
      <LogsChart data={chartData} />
      <AnomaliesTable anomalies={anomalies} />
    </div>

  );
}
