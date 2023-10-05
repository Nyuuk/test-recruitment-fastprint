const ViewAllData = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        fetch('http://localhost:5000/data')
            .then(res => res.json())
            .then(data => setData(data))
            .catch(err => {
                console.log(err);
            })
    })
  return (
    <>
      <div className="bg-gray-100 py-6 h-screen">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center mb-4">
            <h2 className="text-2xl font-semibold text-gray-800">
              Daftar Data
            </h2>
            <button className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-full">
              Tambah Data
            </button>
          </div>
          {/* <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4"> */}
          <div className="bg-white shadow-md rounded-md overflow-x-auto">
            <table className="min-w-full divide-y divide-gray-200">
                <thead className="sticky">
                    <th className="px-6 py-3 bg-gray-50 text-left text-xs leading-4 font-medium text-gray-500 uppercase tracking-wider">Nama</th>
                    <th className="px-6 py-3 bg-gray-50 text-left text-xs leading-4 font-medium text-gray-500 uppercase tracking-wider">Harga</th>
                    <th className="px-6 py-3 bg-gray-50 text-left text-xs leading-4 font-medium text-gray-500 uppercase tracking-wider">Kategori</th>
                    <th className="px-6 py-3 bg-gray-50 text-left text-xs leading-4 font-medium text-gray-500 uppercase tracking-wider">Status</th>
                    <th className="px-6 py-3 bg-gray-50 text-left text-xs leading-4 font-medium text-gray-500 uppercase tracking-wider">Action</th>
                </thead>
                <tbody className="bg-white divide-y divide-gray-200">
                    <tr>
                        <td className="px-6 py-4 whitespace-no-wrap">Data 1</td>
                        <td className="px-6 py-4 whitespace-no-wrap">Data 2</td>
                        <td className="px-6 py-4 whitespace-no-wrap">Data 3</td>
                        <td className="px-6 py-4 whitespace-no-wrap">Data 4</td>
                        <td className="px-6 py-4 whitespace-no-wrap flex flex-row">
                            <button className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-1 px-4 rounded-full mr-2">Edit</button>
                            <button className="bg-red-500 hover:bg-red-600 text-white font-bold py-1 px-4 rounded-full">Hapus</button>
                        </td>
                    </tr>
                </tbody>
            </table>
          </div>
        </div>
      </div>
    </>
  );
};

export default ViewAllData;
