type Anomaly = {
    type: string;
    severity: "low" | "medium" | "high" | string;
    value: number | string;
};
type AnomaliesTableProps = {
    anomalies: Anomaly[];
};
export default function AnomaliesTable({ anomalies }: AnomaliesTableProps) {
    return (
        <div className="bg-white rounded-xl shadow p-4">
            <h3 className="font-semibold mb-3">Anomalies</h3>
            <table className="w-full text-sm">
                <thead>
                    <tr className="text-left border-b">
                        <th>Type</th>
                        <th>Severity</th>
                        <th>Value</th>
                    </tr>
                </thead>
                <tbody>
                    {anomalies.map((a, i) => (
                        <tr key={i} className="border-b">
                            <td>{a.type}</td>
                            <td className="font-bold">{a.severity}</td>
                            <td>{a.value}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}
