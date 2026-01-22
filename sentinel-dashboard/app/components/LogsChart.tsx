"use client";

import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    Tooltip,
    ResponsiveContainer,
} from "recharts";

type LogData = {
    time: string;
    count: number;
};

type LogsChartProps = {
    data: LogData[];
};

export default function LogsChart({ data }: LogsChartProps) {
    return (
        <div className="bg-white rounded-xl shadow p-4">
            <h3 className="mb-2 font-semibold">Logs per Minute</h3>

            {/* chart container MUST have height */}
            <div className="w-full h-[250px]">
                <ResponsiveContainer width="100%" height="100%">
                    <LineChart data={data}>
                        <XAxis dataKey="time" />
                        <YAxis />
                        <Tooltip />
                        <Line type="monotone" dataKey="count" />
                    </LineChart>
                </ResponsiveContainer>
            </div>
        </div>
    );
}
