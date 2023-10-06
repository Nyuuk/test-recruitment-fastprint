import { useEffect, useState } from "react";
import ActionModal from "../../components/Modal";
import Load from "../../components/Loading";

const ViewAllData = () => {
  const [datas, setDatas] = useState({ code: 0, data: [] });
  const [modalDelete, setModalDelete] = useState({ status: false, id: null });
  const [isLoading, setIsLoading] = useState(false);

  const handleDelete = () => {
    setIsLoading(true);
    setModalDelete({ status: false, id: modalDelete.id });
    fetch(`http://localhost:5000/api/products/${modalDelete.id}`, {
      method: "DELETE",
    })
      .then((res) => {
        setIsLoading(false);
        if (res.status === 200) {
          setModalDelete({ status: false, id: null });
          fetch("http://localhost:5000/api/products/getall")
            .then((res) => res.json())
            .then((data) => setDatas(data))
            .catch((err) => console.log(err));
        }
      })
      .catch((err) => console.log(err));
  };

  const refreshData = () => {
    setIsLoading(true);
    fetch("http://localhost:5000/api/refresh_data")
      .then((res) => {
        setIsLoading(false)
        if (res.status === 200) {
          fetch("http://localhost:5000/api/products/getall")
            .then((res) => res.json())
            .then((data) => setDatas(data))
            .catch((err) => console.log(err));
        }
      })
      .catch((err) => {
        console.log(err)
        setIsLoading(false);
      });
  }

  useEffect(() => {
    setIsLoading(true)
    fetch("http://localhost:5000/api/products/getall")
      .then((res) => res.json())
      .then((data) => {
        setIsLoading(false);
        setDatas(data)
      })
      .catch((err) => {
        console.log(err)
        setIsLoading(false);
      });
  }, []);

  useEffect(() => {
    console.log(datas);
  }, [datas]);

  return (
    <>
      {isLoading && <Load />}
      {modalDelete.status && (
        <ActionModal
          funcSetModal={[handleDelete, setModalDelete]}
          messages={{
            title: "Action Delete",
            content: "Are you sure want to delete this data?",
            button: "Delete",
            type: "FETCH_DELETE",
            url: `http://localhost:5000/api/products/${modalDelete.id}`,
            idData: modalDelete.id,
          }}
        />
      )}
      <div className="bg-gray-100 py-6 h-full">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center mb-4">
            <h2 className="text-2xl font-semibold text-gray-800">
              Daftar Data
            </h2>
            <div className="flex flex-row gap-2 flex-row-reverse">
              <button className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-full">
                Tambah Data
              </button>
              <button className=" text-blue-500 hover:text-blue-800 font-bold py-2 px-4" onClick={() => refreshData()}>
                Refresh Data
              </button>
            </div>
          </div>
          {/* <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4"> */}
          <div className="bg-white shadow-md rounded-md overflow-x-auto">
            <table className="min-w-full divide-y divide-gray-200">
              <thead className="sticky">
                <tr>
                  <th className="px-6 py-3 bg-gray-50 text-left text-xs leading-4 font-medium text-gray-500 uppercase tracking-wider">
                    Num
                  </th>
                  <th className="px-6 py-3 bg-gray-50 text-left text-xs leading-4 font-medium text-gray-500 uppercase tracking-wider">
                    Nama
                  </th>
                  <th className="px-6 py-3 bg-gray-50 text-left text-xs leading-4 font-medium text-gray-500 uppercase tracking-wider">
                    Harga
                  </th>
                  <th className="px-6 py-3 bg-gray-50 text-left text-xs leading-4 font-medium text-gray-500 uppercase tracking-wider">
                    Kategori
                  </th>
                  <th className="px-6 py-3 bg-gray-50 text-left text-xs leading-4 font-medium text-gray-500 uppercase tracking-wider">
                    Status
                  </th>
                  <th className="px-6 py-3 bg-gray-50 text-left text-xs leading-4 font-medium text-gray-500 uppercase tracking-wider">
                    Action
                  </th>
                </tr>
              </thead>
              <tbody className="bg-white divide-y divide-gray-200">
                {Object.keys(datas).length > 0 &&
                  datas.data.map((data, i) => {
                    return (
                      <tr key={i}>
                        <td className="px-6 py-4 whitespace-no-wrap text-sm leading-5 font-medium">
                          {i + 1}
                        </td>
                        <td className="px-6 py-4 whitespace-no-wrap text-sm leading-5 font-medium">
                          {data.nama_produk}
                        </td>
                        <td className="px-6 py-4 whitespace-no-wrap text-sm leading-5 font-medium">
                          {data.harga}
                        </td>
                        <td className="px-6 py-4 whitespace-no-wrap text-sm leading-5 font-medium">
                          {data.kategori_id}
                        </td>
                        <td className="px-6 py-4 whitespace-no-wrap text-sm leading-5 font-medium">
                          {data.status_id}
                        </td>
                        <td className="px-6 py-4 align-middle text-sm leading-5 font-medium">
                          <div className="flex md:flex-row flex-col gap-1">
                            <button className="bg-blue-500 hover:bg-blue-600 text-white font-bold md:py-1.5 py-2 px-4 rounded-lg">
                              Edit
                            </button>
                            <button
                              className="bg-red-500 hover:bg-red-600 text-white font-bold md:py-1.5 py-2 px-4 rounded-lg"
                              onClick={() =>
                                setModalDelete({
                                  status: true,
                                  id: data.id_produk,
                                })
                              }
                            >
                              Hapus
                            </button>
                          </div>
                        </td>
                      </tr>
                    );
                  })}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </>
  );
};

export default ViewAllData;
