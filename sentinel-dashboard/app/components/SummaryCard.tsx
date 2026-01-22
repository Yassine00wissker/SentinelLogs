type summary = {
    title : string;
    value : string | number;
    color : string ;
}

export default function SummaryCard({title ,value, color} : summary) {
    return (
    <div className={`rounded-xl p-4 shadow bg-${color}-100`}>
      <h3 className="text-sm text-gray-600">{title}</h3>
      <p className="text-2xl font-bold">{value}</p>
    </div>
  );
}