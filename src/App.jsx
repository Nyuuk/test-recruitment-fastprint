import './App.css'
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import ViewAllData from './pages/AllData/ViewAllData';

const router = createBrowserRouter([
  {
    path: "/",
    element: <ViewAllData />,
  },
]);

function App() {

  return (
    <RouterProvider router={router} />
  )
}

export default App
