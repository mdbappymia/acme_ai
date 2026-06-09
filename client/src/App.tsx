/* eslint-disable @typescript-eslint/no-explicit-any */
/* eslint-disable @typescript-eslint/no-unused-vars */
import { useState } from "react";
import { IoDocumentText } from "react-icons/io5";
import SearchForm from "./components/SearchForm";
import ResultCard from "./components/ResultCard";
import axios from "axios";

function App() {
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState<any[]>([]);
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  const searchLegalDocs = async (query: string) => {
    const response = await axios.post("http://localhost:8000/generate", { query });
    return response.data;
  };

  const handleSearch = async (query: string) => {
    try {
      setLoading(true);
      setError("");

      const data = await searchLegalDocs(query);

      setMessage(data?.summary || "");
      setResults(data?.sources || []);
    } catch (err: any) {
      setError("Failed to fetch documents.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-start justify-center py-12 px-6 app-bg">
      <div className="w-full max-w-4xl">
        <header className="mb-8 flex items-center gap-4">
          <div className="w-12 h-12 rounded-xl bg-linear-to-br from-indigo-700 to-sky-500 flex items-center justify-center text-white shadow-lg">
            <IoDocumentText />
          </div>

          <div>
            <h1 className="text-2xl font-semibold text-slate-800">Legal Document Search</h1>
            <p className="text-sm text-slate-500">Search your documents</p>
          </div>
        </header>

        <main className="glass-card rounded-2xl shadow-xl p-6">
          <SearchForm onSearch={handleSearch} loading={loading} />

          {error && (
            <div className="mt-4 text-red-700 bg-red-50 border border-red-100 p-3 rounded-md">{error}</div>
          )}

          {message && (
            <div className="mt-4 p-4 rounded-md bg-linear-to-r from-white to-slate-50 border border-slate-100">
              <h2 className="font-medium text-slate-700 mb-2">Summary</h2>
              <p className="text-slate-600">{message}</p>
            </div>
          )}

          <section className="mt-6 grid grid-cols-1 sm:grid-cols-2 gap-4 max-h-96 overflow-y-auto scrollbar-thumb-purple-100">
            {results.map((item, index) => (
              <ResultCard key={index} item={item} />
            ))}
          </section>
        </main>
      </div>
    </div>
  );
}

export default App;