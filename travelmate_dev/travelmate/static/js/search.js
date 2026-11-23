// React Search Component
const root = ReactDOM.createRoot(document.getElementById('react-search'));


function SearchBar() {
    const [search, setSearch] = React.useState('');
    const [results, setResults] = React.useState([]);
    const [loading, setLoading] = React.useState(false);


    const handleSearch = React.useCallback(async (value) => {
        setSearch(value);
       
        if (value.trim() === '') {
            setResults([]);
            return;
        }


        setLoading(true);
       
        try {
            // Fetch from API
            const response = await fetch(`/api/destinations/`);
            const data = await response.json();
           
            if (data.success) {
                const filtered = data.data.filter(d =>
                    d.name.toLowerCase().includes(value.toLowerCase()) ||
                    d.country.toLowerCase().includes(value.toLowerCase())
                );
                setResults(filtered);
            }
        } catch (error) {
            console.error('Search error:', error);
        } finally {
            setLoading(false);
        }
    }, []);


    return (
        <div className="mb-4">
            <div className="input-group input-group-lg">
                <span className="input-group-text bg-primary text-white border-0">
                    <i className="fas fa-search"></i>
                </span>
                <input
                    className="form-control border-start-0"
                    placeholder="Search by destination or country..."
                    value={search}
                    onChange={(e) => handleSearch(e.target.value)}
                    style={{
                        borderRadius: '0 5px 5px 0',
                        border: '1px solid #ddd',
                        borderLeft: 'none'
                    }}
                />
            </div>
           
            {loading && (
                <div className="mt-3 p-3 bg-white border rounded text-center">
                    <div className="spinner-border spinner-border-sm text-primary" role="status">
                        <span className="visually-hidden">Loading...</span>
                    </div>
                    <p className="text-muted mt-2">Searching...</p>
                </div>
            )}
           
            {results.length > 0 && !loading && (
                <div className="mt-3 p-3 bg-white border rounded shadow-sm">
                    <p className="text-muted mb-3">
                        <i className="fas fa-check-circle text-success"></i> Found {results.length} result(s)
                    </p>
                    <div className="row">
                        {results.map((destination) => (
                            <div key={destination.id} className="col-md-6 mb-2">
                                <div className="p-2 border rounded bg-light">
                                    <p className="mb-1 fw-bold">{destination.name}</p>
                                    <p className="mb-0 small text-muted">
                                        <i className="fas fa-map-marker-alt"></i> {destination.country}
                                    </p>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            )}
           
            {search.trim() !== '' && results.length === 0 && !loading && (
                <div className="mt-3 p-3 bg-white border rounded text-center">
                    <p className="text-muted mb-0">
                        <i className="fas fa-search"></i> No destinations found matching "{search}"
                    </p>
                </div>
            )}
        </div>
    );
}


root.render(<SearchBar />);