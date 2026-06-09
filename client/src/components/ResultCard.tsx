import { useState, type FC } from "react";

type ResultCardProps = {
    item: {
        title: string;
        summary: string;
    };
};


const ResultCard: FC<ResultCardProps> = ({ item }) => {
    const [isOpen, setIsOpen] = useState(false);

    return (
        <article className="p-4 rounded-lg border border-slate-100 bg-white shadow-sm hover:shadow-md transition-shadow">
            <header className="flex items-start justify-between gap-2">
                <h3 className="text-sm font-semibold text-slate-800">{item.title}</h3>
            </header>

            <p className="mt-2 text-sm text-slate-600 line-clamp-4">{item.summary?.slice(0, 100) + ' ...'}</p>

            <footer className="mt-3 flex items-center justify-between text-xs text-slate-500">
                <button onClick={() => setIsOpen(true)} className="text-indigo-600 hover:underline">View</button>
            </footer>
            {isOpen && (
                <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50">
                    <div className="w-full max-w-md rounded-lg bg-white p-6 shadow-lg">
                        <h2 className="mb-4 text-xl font-bold">{item.title}</h2>

                        <p className="mb-6 text-gray-600">
                            {item.summary}
                        </p>

                        <div className="flex justify-end gap-2">
                            <button
                                onClick={() => setIsOpen(false)}
                                className="rounded border px-4 py-2"
                            >
                                Close
                            </button>
                        </div>
                    </div>
                </div>
            )}
        </article>
    );
};

export default ResultCard;