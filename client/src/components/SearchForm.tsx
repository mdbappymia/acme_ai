/* eslint-disable @typescript-eslint/no-explicit-any */
import { useState, type FC } from 'react';
import { HiMagnifyingGlass } from "react-icons/hi2";
import { ImSpinner9 } from "react-icons/im";
type SearchFormProps = {
    onSearch: (query: string) => void;
    loading: boolean;
};


const SearchForm: FC<SearchFormProps> = ({ onSearch, loading }) => {
    const [query, setQuery] = useState("");

    const handleSubmit = (e: any) => {
        e.preventDefault();

        if (!query.trim()) return;

        onSearch(query);
    };

    return (
        <form onSubmit={handleSubmit} className="flex flex-col sm:flex-row gap-3 items-center">
            <div className="flex-1 w-full">
                <label className="sr-only">Search</label>
                <div className="relative">
                    <input
                        value={query}
                        onChange={(e) => setQuery(e.target.value)}
                        placeholder="Search legal documents"
                        className="w-full rounded-xl border border-slate-200 px-4 py-3 pr-12 shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-300"
                    />

                </div>
            </div>

            <div className="shrink-0">
                <button
                    type="submit"
                    disabled={loading}
                    className="inline-flex items-center gap-2 bg-linear-to-r from-indigo-600 to-sky-500 text-white px-5 py-3 rounded-xl shadow-md hover:brightness-105 disabled:opacity-60"
                >
                    {loading ? (
                        <ImSpinner9 className="animate-spin" />
                    ) : (
                        <HiMagnifyingGlass />
                    )}
                    <span className="font-medium">{loading ? 'Searching...' : 'Search'}</span>
                </button>
            </div>
        </form>
    );
};

export default SearchForm;
