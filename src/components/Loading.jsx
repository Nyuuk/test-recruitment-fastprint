const Load = () => {
  return (
    <div className="fixed inset-0 flex items-center justify-center z-50 backdrop-filter backdrop-blur-sm backdrop-opacity-50">
      <div className="flex items-center space-x-2 text-black">
        <svg
          className="animate-spin h-6 w-6 text-black"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
        >
          <circle
            className="opacity-25"
            cx="12"
            cy="12"
            r="10"
            stroke="currentColor"
            strokeWidth="4"
          ></circle>
          <path
            className="opacity-75"
            fill="currentColor"
            d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647zM20 12c0-3.042-1.135-5.824-3-7.938l-3 2.647A7.962 7.962 0 0120 12h4zm-2 5.291l3 2.647A7.963 7.963 0 0024 12h-4a7.962 7.962 0 01-2 5.291zM12 20c3.042 0 5.824-1.135 7.938-3l-2.647-3A7.963 7.963 0 0012 20zm-2-5.291l-3 2.647A7.962 7.962 0 004 12h4a7.963 7.963 0 012-5.291zM12 4c-3.042 0-5.824 1.135-7.938 3l2.647 3A7.963 7.963 0 0012 4zm2 5.291A7.962 7.962 0 0016 12h4c0-3.042-1.135-5.824-3-7.938l-3 2.647z"
          ></path>
        </svg>
        <span>Loading...</span>
      </div>
    </div>
  );
};

export default Load;
